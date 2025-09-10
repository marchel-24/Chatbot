import discord
import os
import re
import random
from dotenv import load_dotenv
from recipe_bot import recipes   # <-- Import recipes here
import logging
from logging.handlers import RotatingFileHandler

# Create logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configure the logger
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
log_handler = RotatingFileHandler(
    'logs/bot.log', 
    maxBytes=1024*1024, # 1 MB
    backupCount=5
)
log_handler.setFormatter(log_formatter)

logger = logging.getLogger('recipe_bot')
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

# Configuration
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

reflections = {
    "i": "you", "am": "are", "was": "were", "my": "your",
    "mine": "yours", "me": "you", "i've": "you have", "i have": "you have"
}

# Functions
def reflect_pronouns(text):
    words = re.findall(r"[\w']+|[.,!?;]", text.lower())
    reflected_words = [reflections.get(word, word) for word in words]
    return " ".join(reflected_words).capitalize()

def find_recipe(message):
    for recipe in recipes:
        if recipe["pattern"].search(message):
            return recipe
    return None

def find_recipe_by_name(message):
    for recipe in recipes:
        if recipe["name"].lower() in message.lower():
            return recipe
    return None

def process_message(message):
    # Greetings
    if re.search(r"\b(hi|hello|hey|good morning|good evening)\b", message, re.IGNORECASE):
        return "Hello there! 👋 Tell me what ingredients you have, and I’ll suggest a recipe."

    # Help
    if re.search(r"\b(help|how to use|instructions)\b", message, re.IGNORECASE):
        return ("You can tell me what ingredients you have, like: "
                "`I have chicken, rice, and broccoli` 🍗🍚🥦\n"
                "Or, just mention a recipe name like `Pasta` and I’ll give you instructions!")

    # Random Recipe
    if re.search(r"\b(surprise me|random|i don't know|anything)\b", message, re.IGNORECASE):
        random_recipe = random.choice(recipes)
        return (f"Here’s a random idea for you 🎲: **{random_recipe['name']}**!\n"
                f"{random_recipe['response']}")

    # Ingredient-based
    found_recipe = find_recipe(message)
    if found_recipe:
        return found_recipe["response"]

    # Menu search
    found_by_name = find_recipe_by_name(message)
    if found_by_name:
        return f"Here’s the recipe for **{found_by_name['name']}**:\n{found_by_name['response']}"

    # Reflective fallback
    if re.search(r"\bi\b.*\bhave\b", message, re.IGNORECASE):
        reflected_input = reflect_pronouns(message)
        return (f"{reflected_input}, but I'm not sure what to make with that combination. "
                "Can you add another main ingredient like a protein or a vegetable?")

    # Generic fallback
    return ("Sorry, I couldn't find a recipe with those ingredients or menu name. "
            "Try listing what you have, like 'I have chicken, rice, and broccoli'.")

# Discord Integration
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord! Ready to find some recipes! 🍳')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        try:
            logger.info(f"Received mention from '{message.author}' in channel '{message.channel}'. Message: '{message.content}'")
            cleaned_message = re.sub(f'<@!?{client.user.id}>', '', message.content).strip()

            if not cleaned_message:
                await message.channel.send("Hello! Tell me what ingredients you have. For example: `@RecipeBot I have chicken, rice, and carrots`")
                return

            response = process_message(cleaned_message)
            logger.info(f"Sending response to '{message.channel}': {response}")
            await message.channel.send(response)

        except Exception as e:
            print(f"An error occurred: {e}")
            logger.exception("An unhandled error occurred in on_message")
            await message.channel.send("Oops! Something went wrong in the kitchen. Please try again.")

def run_bot():
    if TOKEN:
        logger.info("Starting bot...")
        client.run(TOKEN)
    else:
        print("ERROR: DISCORD_TOKEN not found. Please set it in your .env file.")
        logger.error("FATAL: DISCORD_TOKEN not found. Please set it in your .env file.")

if __name__ == "__main__":
    run_bot()
