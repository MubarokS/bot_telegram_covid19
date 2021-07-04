import telebot
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

api_token = '1720239439:AAGGZwqZJuqWsq-97DJZXfwQBmuCdUXRAoc'
bot = telebot.TeleBot(api_token)

@bot.message_handler(commands=['start'])
def start(message):
     bot.reply_to(message,
               '- Ketik /covid  untuk menampilkan data persebaran di tiap provinsi \n'
               '- Tambahkan nama provinsi di belakang perintah /covid untuk menampilkan data persebaran di provinsi tertentu \n'
               '- Tambahkan kalimat `zona merah`,`zona kuning`,`zona hijau` untuk menampilkan provinsi menurut zona \n'
               '- Ketik /grafik untuk menampilkan garfik persebaran di tiap pulau')

@bot.message_handler(commands=['covid'])
def covid(message):
   texts = message.text
   provinsi = texts[7:]
   zona = texts[7:]
   page = requests.get('https://services5.arcgis.com/VS6HdKS0VfIhv8Ct'
                       '/arcgis/rest/services/COVID19_Indonesia_per_Provinsi'
                       '/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')
   page_json = page.json()
   features = page_json['features']

   for i in features:
      n_provinsi = i['attributes']['Provinsi']
      positif =  i['attributes']['Kasus_Posi']
      sembuh = i['attributes']['Kasus_Semb']
      meninggal = i['attributes']['Kasus_Meni']
      data = ('''
Provinsi = {}
Positif = {}
Sembuh = {}
Meninggal = {}
'''.format(n_provinsi, positif, sembuh, meninggal))
      if provinsi.lower() in n_provinsi.lower():
         bot.reply_to(message, data)
      elif zona.lower()=='zona merah' and positif>100000 :
         bot.reply_to(message, data)
      elif zona.lower()=='zona kuning' and 100000>positif>50000:
         bot.reply_to(message, data)
      elif zona.lower()=='zona hijau' and positif<50000:
         bot.reply_to(message, data)
      else:
         pass

#VISUALISASI
@bot.message_handler(commands=['grafik'])
def grafik(message):
   page = requests.get('https://services5.arcgis.com/VS6HdKS0VfIhv8Ct'
                       '/arcgis/rest/services/COVID19_Indonesia_per_Provinsi'
                       '/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')
   data_json = page.json()
   features = (data_json['features'])
   x = []
   for i in features:
      row = []
      row.append(i['attributes']['Provinsi'])
      row.append(i['attributes']['Kasus_Posi'])
      x.append(row)
   hasil = pd.DataFrame(x, columns=['prov','pos'])

   sns.catplot(x='prov', y='pos', kind='bar', data=hasil[:10], height=4, aspect=3, n_boot=1000)
   plt.xticks(rotation=0)
   plt.savefig('sumatera.png')
   sns.catplot(x='prov', y='pos', kind='bar', data=hasil[10:16], height=4, aspect=3, n_boot=1000)
   plt.xticks(rotation=0)
   plt.savefig('jawa.png')
   sns.catplot(x='prov', y='pos', kind='bar', data=hasil[16:19], height=4, aspect=3, n_boot=1000)
   plt.xticks(rotation=0)
   plt.savefig('kepulauan_sunda.png')
   sns.catplot(x='prov', y='pos', kind='bar', data=hasil[19:24], height=4, aspect=3, n_boot=1000)
   plt.xticks(rotation=0)
   plt.savefig('kalimantan.png')
   sns.catplot(x='prov', y='pos', kind='bar', data=hasil[24:30], height=4, aspect=3, n_boot=1000)
   plt.xticks(rotation=0)
   plt.savefig('sulawesi.png')
   sns.catplot(x='prov', y='pos', kind='bar', data=hasil[30:34], height=4, aspect=3, n_boot=1000)
   plt.xticks(rotation=0)
   plt.savefig('papua.png')

   chatid = message.chat.id
   bot.send_photo(chatid,open('sumatera.png','rb'))
   bot.send_photo(chatid, open('jawa.png','rb'))
   bot.send_photo(chatid, open('kepulauan_sunda.png','rb'))
   bot.send_photo(chatid, open('kalimantan.png','rb'))
   bot.send_photo(chatid, open('sulawesi.png', 'rb'))
   bot.send_photo(chatid, open('papua.png', 'rb'))
print('bot running')
bot.polling()