import telebot
token = '6064109770:AAFNlk6PBCIXnhqBBJiKuxlHKXoFiWAqtAM'
bot = telebot.TeleBot(token)
def start_message(message):
    bot.send_message(message.chat.id, text = "Я новая версия бота, здрасте")

telegatag = "@tap0checkldg, @M_Temo, @pass2hoff, @E671G, @drsovets"
telegatagside = "Кто-то меня звал чтобы я объявил сбор? Просьба послать инициатора нахуй."
seregatag = "@slightly_lazy, ебните стулом вашего брата"
sidetag = "@drsovets, @pass2hoff. Можете дать обратную связь?"
egortag =  "@pass2hoff, ну ты как обычно - долбаебина. ХЫЫЫЫЫЫ"
@bot.message_handler(content_types=['text'])
def starup(message):
    readycheck = telebot.types.InlineKeyboardMarkup()
    readycheck.add(telebot.types.InlineKeyboardButton(text = '🔥🔥🔥Готов сосать🔥🔥🔥', callback_data = 'ready'))
    
    if message.text == '@сбор':
        global nametager
        nametager = message.from_user.username
        bot.send_message(message.chat.id, telegatag)
        msg = bot.send_message(message.chat.id, text ='🤖Вас приветсутвет сбор бот🤖 \n 🤡' + nametager + ' инициировал сбор🤡 не поленитесь ткнуть кнопку 🏆', reply_markup = readycheck)
        return nametager
               

@bot.callback_query_handler(func=lambda call: True)
def readyanswer(call):
    nametag = call.from_user.username
    if call.data == 'ready':
        msg = bot.send_message(call.message.chat.id, '✅ ' + nametag + ' нажал реди ✅\n '+ '💩💩@' + nametager + ' вы как инициатор сбора посланы нахуй💩💩')

def get_text_messages(message):
    if message.text == '@сбор_олд':
        bot.send_message(message.chat.id, telegatag)
        bot.send_message(message.chat.id, telegatagside)
        bot.send_photo(message.chat.id, 'https://kartinkin.net/uploads/posts/2022-12/1670561397_1-kartinkin-net-p-pudzh-kartinka-oboi-1.png')
    elif message.text == '@гуру':
        bot.send_message(message.chat.id, seregatag)
    elif message.text == '@ебланы':
        bot.send_message(message.chat.id, sidetag)
    elif message.text == '@пастух':
        bot.send_message(message.chat.id, egortag)

bot.polling(none_stop=True, interval=0)