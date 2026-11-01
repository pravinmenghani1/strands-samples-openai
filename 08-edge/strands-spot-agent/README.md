# Spot Robot Agent Control

An AI-powered control system for Boston Dynamics Spot robots using the Strands framework. Uses OpenAI models (default `gpt-5-mini`) through Strands.

## Overview

This project enables natural language control of Spot robots through an AI agent. Simply tell the robot what to do in plain English, and the LLM interprets your intent and executes the appropriate robot commands.

**Example commands:**

- "Connect to the robot and stand up"
- "Move forward for 2 seconds, then turn left"
- "Take a picture with the front camera"
- "Dock with the charging station"
- "Check battery status"

## How It Works

1. You speak to the agent in natural language
2. Your configured LLM interprets your request
3. The agent calls the appropriate robot control tools
4. The Boston Dynamics SDK sends commands to the physical robot

## Requirements

- Python 3.10+
- Boston Dynamics Spot robot with SDK access
- Set `OPENAI_API_KEY` in your environment (optionally `OPENAI_MODEL_ID`, default `gpt-5-mini`)

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

1. Copy the example environment file:

```bash
cp example.env .env
```

2. Edit `.env` with your settings:

```bash
# OpenAI
OPENAI_API_KEY=your-key
# OPENAI_MODEL_ID=gpt-5-mini  # optional, this is the default

# Robot connection
ROBOT_HOSTNAME="192.168.80.3"
ROBOT_USERNAME="admin"
ROBOT_PASSWORD="your-password"
```

3. Alternatively, export `OPENAI_API_KEY` in your shell instead of putting it in `.env`.

## Usage

Run the interactive agent:

```bash
python agent.py
```

The agent provides an interactive prompt where you can issue natural language commands.

## Available Robot Commands

| Category   | Commands                                                                                                                      |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Connection | `connect_to_robot`, `robot_force_take_lease`                                                                                  |
| Movement   | `robot_stand`, `robot_sit`, `robot_stop`                                                                                      |
| Navigation | `robot_move_forward`, `robot_move_backward`, `robot_strafe_left`, `robot_strafe_right`, `robot_turn_left`, `robot_turn_right` |
| Docking    | `robot_dock`, `robot_undock`, `robot_get_dock_status`                                                                         |
| Status     | `robot_get_status`, `robot_toggle_power`                                                                                      |
| Camera     | `robot_take_image`                                                                                                            |
| Recovery   | `robot_self_right`, `robot_battery_change_pose`                                                                               |

## Architecture

- `agent.py` - Main agent interface using Strands framework
- `spot_mcp_server.py` - Robot control tools exposed as Strands tools

## Safety

The system includes built-in safety limits:

- Maximum movement duration: 10 seconds
- Maximum movement speed: 1.5 m/s
- Maximum angular speed: 2.0 rad/s

Always maintain visual contact with the robot and ensure adequate clearance during operation.

## Acknowledgments

- [Strands Agents](https://github.com/strands-agents) - Agent framework
- [Boston Dynamics SDK](https://github.com/boston-dynamics/spot-sdk) - Robot control

