import telebot
bot = telebot.TeleBot('1764041870:AAGICoNVrAQ5TYudCCcVJ6EDgXmhBH5awT4')

@bot.message_handler(commands=['start'])
def start(message):
     bot.reply_to(message,
               '- Ketik /covid  untuk menampilkan data persebaran di tiap provinsi \n'
               '- Tambahkan nama provinsi di belakang perintah /covid untuk menampilkan data persebaran di provinsi tertentu \n'
               '- Tambahkan kalimat `zona merah`,`zona kuning`,`zona hijau` untuk menampilkan provinsi menurut zona \n'
               '- Ketik /grafik untuk menampilkan garfik persebaran di tiap pulau'
                    )
print('boot running')
bot.polling()