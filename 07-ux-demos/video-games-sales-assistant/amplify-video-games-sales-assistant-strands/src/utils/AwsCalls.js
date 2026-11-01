import { DynamoDBClient, QueryCommand } from "@aws-sdk/client-dynamodb";
import { createAwsClient } from "./AwsAuth";
import { extractBetweenTags, removeCharFromStartAndEnd, handleFormatter } from "./Utils.js";
import {
  QUESTION_ANSWERS_TABLE_NAME,
  CHART_ENDPOINT_URL,
  CHART_PROMPT
} from "../env.js";

/**
 * Query data from DynamoDB
 *
 * @param {string} id - The ID to query
 * @returns {Promise<Object>} - The query response
 */
export const getQueryResults = async (queryUuid = "") => {
  let queryResults = [];
  try {
    const dynamodb = await createAwsClient(DynamoDBClient);

    const input = {
      TableName: QUESTION_ANSWERS_TABLE_NAME,
      KeyConditionExpression: "id = :queryUuid",
      ExpressionAttributeValues: {
        ":queryUuid": {
          S: queryUuid,
        },
      },
      ConsistentRead: true,
    };

    console.log("------- Get Query Results -------");
    console.log(input);

    const command = new QueryCommand(input);
    const response = await dynamodb.send(command);

    if (response.hasOwnProperty("Items")) {
      for (let i = 0; i < response.Items.length; i++) {
        queryResults.push({
          query: response.Items[i].sql_query.S,
          query_results: JSON.parse(response.Items[i].data.S).result,
          query_description: response.Items[i].sql_query_description.S,
        });
      }
    }

    return queryResults;
  } catch (error) {
    console.error("Error querying DynamoDB:", error);
    throw error;
  }
};

/**
 * Generates a chart based on answer and data
 * @param {Object} answer - Answer object containing text
 * @returns {Object} Chart configuration or rationale for no chart
 */
export const generateChart = async (
  answer
) => {
  let query_results = "";
  for (let i = 0; i < answer.queryResults.length; i++) {
    query_results += JSON.stringify(answer.queryResults[i].query_results) + "\n";
  }

  // Prepare the prompt
  let new_chart_prompt = CHART_PROMPT.replace(
    /<<answer>>/i,
    answer.text
  ).replace(/<<data_sources>>/i, query_results);

  const payload = { prompt: new_chart_prompt };

  try {
    // Send the request to the agent backend, which calls the OpenAI model
    console.log("------- Request chart -------");
    console.log(payload);

    const headers = { "Content-Type": "application/json" };
    try {
      const { fetchAuthSession } = await import("aws-amplify/auth");
      const session = await fetchAuthSession();
      const authToken = session.tokens?.idToken?.toString();
      if (authToken) {
        headers["Authorization"] = `Bearer ${authToken}`;
      }
    } catch (authError) {
      console.warn("Could not get auth token:", authError);
    }

    const apiResponse = await fetch(CHART_ENDPOINT_URL, {
      method: "POST",
      headers,
      body: JSON.stringify(payload),
    });
    if (!apiResponse.ok) {
      throw new Error(`HTTP error! Status: ${apiResponse.status}`);
    }
    const responseBody = (await apiResponse.json()).text;

    console.log("------- Response chart generation -------");
    console.log(responseBody);

    // Process the response
    const has_chart = parseInt(extractBetweenTags(responseBody, "has_chart"));

    if (has_chart) {
      const chartConfig = JSON.parse(
        extractBetweenTags(responseBody, "chart_configuration")
      );
      const chart = {
        chart_type: removeCharFromStartAndEnd(
          extractBetweenTags(responseBody, "chart_type"),
          "\n"
        ),
        chart_configuration: handleFormatter(chartConfig),
        caption: removeCharFromStartAndEnd(
          extractBetweenTags(responseBody, "caption"),
          "\n"
        ),
      };

      console.log("------- Final chart generation -------");
      console.log(chart);

      return chart;
    } else {
      return {
        rationale: removeCharFromStartAndEnd(
          extractBetweenTags(responseBody, "rationale"),
          "\n"
        ),
      };
    }
  } catch (error) {
    console.error("Chart generation failed:", error);
    return {
      rationale: "Error generating or parsing chart data.",
    };
  }
};


