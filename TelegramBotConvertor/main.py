import telebot
from config import keys, TOKEN
from extensions import MyException, Convertor

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start','help'])
def start_help(message: telebot.types.Message):
    text = 'Чтобы перевести валюту введите следующее:\n' \
           '<валюту которую хотите перевести> <валюту в которую хотите перевести>\n' \
           '<количество переводимой валюты>'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def value(message: telebot.types.Message):
    text = 'Валюты: '
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise MyException(f'Много параметров! ')
        q, base, amount = values
        quote = q.lower()
        total = Convertor.convert(quote, base, amount)
    except MyException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}!')
    except Exception as e:
        bot.reply_to(message, f'Не обработалась команда.\n {e}!')
    else:
        text = f'Цена {amount} {quote} в {base} - {float(total)*float(amount)}'
        bot.send_message(message.chat.id, text)



bot.polling(none_stop=True)
