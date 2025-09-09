# 🍳 Quick Recipe Finder Bot  

A **rule-based Discord chatbot** that helps you find **simple recipes** based on the ingredients you already have.  

---

## 👨‍💻 Our Team  
- **Marchel Rianra Glendrikho Simanjuntak** (22/494013/TK/54157)  
- **Brian Tirafi Aufauzan** (22/497916/TK/54592)  

---

## 🌍 Background: Why This Bot?  

We’ve all been there—**hungry, tired, and staring at random ingredients in the fridge**.  
Recipe websites? Too many steps. Cooking shows? Too complicated.  
This often leads to **decision fatigue** or even wasted food.  

✨ *Quick Recipe Finder Bot* is here to help! It instantly gives you **simple meal ideas** based on the ingredients you already have—cutting through complexity and helping you cook smarter.  

---

## 🚀 Features  

✅ **Ingredient-Based Suggestions** – Finds recipes that match what you list.  
✅ **Regex-Powered** – Smart ingredient matching.  
✅ **Pronoun Reflection** – Natural chat experience (e.g., "I have..." → "You have...").  
✅ **Simple & Fast** – Get meal ideas in seconds.  
✅ **Discord Integration** – Add it easily to your server.  

---

## ⚙️ Setup & Installation  

### 1️ Prerequisites  
- Python **3.8 or newer**  
- A [Discord Bot Token](https://discord.com/developers/applications)  

### 2️ Clone the Repository  

```bash
git clone https://github.com/marchel-24/Chatbot
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
### 5. Run the Bot
Once the dependencies are installed and the .env file is configured, you can start the bot.
```Bash

python your_bot_file.py
```

## Unit Test
Unit test can be found in ./tests folder. To run the program, can use with this command

```Bash
python -m unittest discover tests
```

## Demo



![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![Discord](https://img.shields.io/badge/Discord-Bot-7289DA?logo=discord&logoColor=white)  
