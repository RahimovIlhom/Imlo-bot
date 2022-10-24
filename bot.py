import logging

from aiogram import Bot, Dispatcher, executor, types
from checkWord import checkWord
from transliterate import to_latin, to_cyrillic

API_TOKEN = '5605668276:AAHYNjRKsc25KR_UPXEbfRz1n0IkhxQkPJY'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_start(message: types.Message):
    """
    '/start' buyruq kelganda javob beruvchi funksiya
    """
    await message.reply("Assalomu alaykum. 'Imlo Uz (bexato yozamiz)' botimizga xush kelibsiz!")

@dp.message_handler(commands=['help'])
async def sent_help(message: types.Message):
    """
    '/help' buyruq kelganda javob beruvchi funksiya
    """
    await message.reply("Botimizdan qanday foydalanish mumkin.\n"
                        "Siz biror bir so'z jo'nating.\n"
                        "Bu bot sizga xato yoki to'g'ri ekanligini tekshirib beradi.")


@dp.message_handler()
async def checkImlo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    word = message.text
    if(word.isascii()):
        words = to_cyrillic(word).split()
        repetitions = len(words)
        for i in range(repetitions):
            result = checkWord(words[i])
            if result['avairable']:
                response = f"✅ {to_latin(result['matches']).capitalize()}"
            else:
                response = f"❌ {to_latin(words[i]).capitalize()}\n"
                for match in result['matches']:
                    response += f"✅ {to_latin(match).capitalize()}\n"
            await message.answer(response)


    else:
        words = message.text.split()
        repetitions = len(words)
        for i in range(repetitions):
            result = checkWord(words[i])
            if result['avairable']:
                response = f"✅ {words[i].capitalize()}"
            else:
                response = f"❌ {words[i].capitalize()}\n"
                for text in result['matches']:
                    response += f"✅ {text.capitalize()}\n"
            await message.answer(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)