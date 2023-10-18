import telebot
from collections import defaultdict

token = '6064109770:AAFNlk6PBCIXnhqBBJiKuxlHKXoFiWAqtAM'
bot = telebot.TeleBot(token)


def start_message(message):
    bot.send_message(message.chat.id, text="Я новая версия бота, здрасте")


telegatag = "@tap0checkldg, @M_Temo, @pass2hoff, @E671G, @drsovets"
telegatagside = "Кто-то меня звал чтобы я объявил сбор? Просьба послать инициатора нахуй."

telegatag_count = len(telegatag.split(','))
telegatag_call_dict = defaultdict(list)


@bot.message_handler(content_types=['text'])
def startup(message):
    readycheck = telebot.types.InlineKeyboardMarkup()
    readycheck.add(telebot.types.InlineKeyboardButton(text='🔥🔥🔥Готов сосать🔥🔥🔥', callback_data='ready'))

    if message.text == '@сбор':
        global nametager
        nametager = message.from_user.username
        bot.send_message(message.chat.id, telegatag)
        msg = bot.send_message(message.chat.id,
                               text='🤖Вас приветсутвет сбор бот🤖 \n 🤡' + nametager + ' инициировал сбор🤡 не поленитесь ткнуть кнопку 🏆',
                               reply_markup=readycheck)
        return nametager


@bot.callback_query_handler(func=lambda call: True)
def readyanswer(call):
    nametag = call.from_user.username
    message: telebot.types.Message = call.message
    if call.data == 'ready':
        if nametag in telegatag_call_dict[message.message_id]:
            telegatag_call_dict[message.message_id].append(nametag)
        else:
            telegatag_call_dict[message.message_id].append(nametag)
            bot.send_message(call.message.chat.id, '✅ ' + '@' + nametag)
        if telegatag_call_dict[message.message_id] == telegatag_count:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=message.message_id,
                                  text=message.text, reply_markup=None)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
