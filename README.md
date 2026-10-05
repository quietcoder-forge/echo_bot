Echo Bot

A simple Telegram echo bot built with Python and aiogram.

This project is a small learning project for understanding the basic structure of an asynchronous Telegram bot:

Telegram → Dispatcher → Router → Handler

Features

/start sends a startup message.

/help shows a short help message.

Any text message is echoed back by the bot.

Requirements

Python 3.10+

aiogram

Installation

Clone the repository:

git clone https://github.com/your-username/your-repository.git
cd your-repository

Install aiogram:

pip install aiogram

Configuration

Open main.py and add your Telegram bot token:

BOT_TOKEN = "YOUR_BOT_TOKEN"

Get the token from BotFather on Telegram.

For a real project, do not commit your bot token to GitHub. Use an environment variable or a .env file instead.

Run

python main.py

Then open your bot in Telegram and send:

/start

or:

/help

You can also send any text and the bot will echo it back.

Project Structure

echo-bot/
├── main.py
└── README.md

How It Works

The bot uses four basic pieces:

Dispatcher

dp = Dispatcher()

The Dispatcher is the main entry point that receives updates from Telegram.

Router

router = Router()

The Router contains the handler for incoming messages.

Handler

@router.message()
async def handle_message(message: Message) -> None:

The handler receives a Message object and decides how to respond.

Connect the Router

dp.include_router(router)

This connects the Router to the Dispatcher.

Start Polling

await dp.start_polling(bot)

This starts receiving updates from Telegram.

Learning Goal

This project is intentionally small. It focuses on the fundamentals of aiogram, async/await, Dispatcher, Router, and Handlers before moving on to more advanced bot features.

License

This project is for learning and educational purposes.
