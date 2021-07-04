import telebot
import requests
import json

bot = telebot.TeleBot('1830101644:AAE4R-rjWAXzKcaK1Zjc33USibMPDwoE4L8')

@bot.message_handler(commands=['covid'])

def covid(message):
    texts = message.text
    provinsi = texts[7:]
    page = requests.get('https://services5.arcgis.com/VS6HdKS0VfIhv8Ct/arcgis'
                       '/rest/services/COVID19_Indonesia_per_Provinsi/Feature'
                       'Server/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')
    page_json = page.json()
    features = page_json['features']
    for i in features:
        k_provinsi = i['attributes']['Kode_Provi']
        n_provinsi = i['attributes']['Provinsi']
        positif = i['attributes']['Kasus_Posi']
        sembuh = i['attributes']['Kasus_Semb']
        meninggal = i['attributes']['Kasus_Meni']
        data = ('''
        Provinsi = {}
        Positif = {}
        Sembuh = {}
        Meninggal= {}
        Dirawat = {}
        '''.format(n_provinsi, pos, sem, men, dirawat))
        if provinsi.upper() in prov.upper():
            bot.reply_to(message, data)
        else:
            pass
    if provinsi.upper() in n_provinsi.upper():
         bot.reply_to(message, data)
    else:
         pass
print('bot running')
bot.polling()