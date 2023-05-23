import telebot
token = '6064109770:AAFNlk6PBCIXnhqBBJiKuxlHKXoFiWAqtAM'
bot = telebot.TeleBot(token)
telegatag = "@tap0checkldg, @pass2hoff, @E671G, @drsovets"

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '@сбор':
        bot.send_message(message.chat.id, telegatag)

bot.polling(none_stop=True, interval=0)