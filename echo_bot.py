import asyncio

from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message

BOT_TOKEN = ""

dp = Dispatcher()
router = Router()


@router.message()
async def handle_message(message: Message) -> None:
    if message.text == "/start":
        await message.answer("Bot is now started.")
    elif message.text == "/help":
        await message.answer("This is an echo bot.")
    else:
        await message.answer(message.text or "I can only echo text messages.")


async def main() -> None:
    bot = Bot(token=BOT_TOKEN)

    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
