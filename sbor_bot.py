import telebot
token = '6064109770:AAFNlk6PBCIXnhqBBJiKuxlHKXoFiWAqtAM'
bot = telebot.TeleBot(token)
telegatag = "@tap0checkldg,@M_Temo ,@pass2hoff, @E671G, @drsovets, @mevd01"
telegatagside = "Кто-то меня звал чтобы я объявил сбор? Просьба послать инициатора нахуй."
seregatag = "@slightly_lazy, ебните стулом вашего брата"
sidetag = "@drsovets, @pass2hoff. Можете дать обратную связь?"
egortag =  "@pass2hoff, ну ты как обычно - долбаебина. ХЫЫЫЫЫЫ"
@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '@сбор':
 
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