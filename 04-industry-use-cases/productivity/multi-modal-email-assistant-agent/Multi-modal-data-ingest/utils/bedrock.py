import boto3
from langchain_aws import BedrockEmbeddings

# from langchain.memory import ConversationBufferMemory, ReadOnlySharedMemory
from botocore.config import Config
from botocore.exceptions import ClientError

bedrock_agent_runtime_client = boto3.client("bedrock-agent-runtime")


def get_embedding(
    model_id: str = "amazon.titan-embed-text-v2:0", aws_region: str = "us-west-2"
):
    config = Config(
        retries=dict(
            max_attempts=10,
            total_max_attempts=25,
        )
    )
    bedrock_client = boto3.client(
        "bedrock-runtime", config=config, region_name=aws_region
    )

    return BedrockEmbeddings(
        client=bedrock_client, region_name=aws_region, model_id=model_id
    )


def check_and_delete_iam_policy(policy_name):
    # Create an IAM client
    iam = boto3.client("iam")

    try:
        # Try to get the policy
        response = iam.get_policy(PolicyArn=f"arn:aws:iam::aws:policy/{policy_name}")

        # If we reach here, the policy exists
        print(f"Policy '{policy_name}' exists. Attempting to delete...")

        # First, we need to detach the policy from all entities
        detach_policy(iam, response["Policy"]["Arn"])

        # Now we can delete the policy
        iam.delete_policy(PolicyArn=response["Policy"]["Arn"])
        print(f"Policy '{policy_name}' has been deleted successfully.")

    except ClientError as e:
        if e.response["Error"]["Code"] == "NoSuchEntity":
            print(f"Policy '{policy_name}' does not exist.")
        else:
            print(f"An error occurred: {e}")


def detach_policy(iam, policy_arn):
    # Detach from users
    for user in iam.list_entities_for_policy(PolicyArn=policy_arn, EntityFilter="User")[
        "PolicyUsers"
    ]:
        iam.detach_user_policy(UserName=user["UserName"], PolicyArn=policy_arn)

    # Detach from groups
    for group in iam.list_entities_for_policy(
        PolicyArn=policy_arn, EntityFilter="Group"
    )["PolicyGroups"]:
        iam.detach_group_policy(GroupName=group["GroupName"], PolicyArn=policy_arn)

    # Detach from roles
    for role in iam.list_entities_for_policy(PolicyArn=policy_arn, EntityFilter="Role")[
        "PolicyRoles"
    ]:
        iam.detach_role_policy(RoleName=role["RoleName"], PolicyArn=policy_arn)


def check_table_exists(table_name):
    # Create a DynamoDB client
    dynamodb = boto3.client("dynamodb")

    try:
        # Try to describe the table
        response = dynamodb.describe_table(TableName=table_name)
        return True
    except:
        return False


def check_lambda_function_exists(function_name):
    # Create a Lambda client
    lambda_client = boto3.client("lambda")
    try:
        # Try to get the function configuration
        lambda_client.get_function(FunctionName=function_name)
        return True
    except:
        return False
