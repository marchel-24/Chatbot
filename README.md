# Quick Recipe Finder Bot

A rule-based Discord chatbot that helps users find simple recipes based on the ingredients they have on hand.

## Background: The Problem This Bot Solves

In a world full of complex recipe websites and cooking shows, deciding what to make for dinner can lead to "analysis paralysis." Many people have a few ingredients in their fridge but lack the inspiration to combine them into a simple meal.

The *Quick Recipe Finder Bot* solves this by providing immediate, simple recipe suggestions. It cuts through the noise of detailed, multi-step recipes and empowers users to quickly create a meal with what they already have, reducing food waste and decision fatigue.

## Features

-   *Ingredient-Based Suggestions*: Finds recipes by matching the ingredients you list.
-   *Regex-Powered*: Uses regular expressions for flexible and powerful matching.
-   *Pronoun Reflection*: Engages in simple, natural conversation (e.g., "I have..." -> "You have...").
-   *Simple & Fast*: Designed to give you a meal idea in seconds.
-   *Discord Integration*: Easy to add to any Discord server.

## Setup and Installation

Follow these steps to get the bot running on your own server.

### 1. Prerequisites

-   Python 3.8 or newer
-   A Discord Bot Token. You can create a bot and get a token from the [Discord Developer Portal](https://discord.com/developers/applications).

### 2. Clone the Repository

```bash
git clone [https://github.com/marchel-24/Chatbot](https://github.com/marchel-24/Chatbot)
cd quick-recipe-bot
```

### 3. Configuration
The bot uses a .env file to securely store your Discord bot token.

- Create a file named .env in the root of the project folder.

- Add your Discord bot token to this file in the following format, replacing your_token_here with your actual token:

```bash
DISCORD_TOKEN=your_token_here
```
For reference, an example .env.example file is included in the repository.

### 4. Install Dependencies
Install the required Python libraries using pip.

```Bash

pip install -r requirements.txt

```
5. Run the Bot
Once the dependencies are installed and the .env file is configured, you can start the bot.
```Bash

python your_bot_file.py
```