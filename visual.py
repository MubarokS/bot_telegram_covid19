import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

response = requests.get('https://services5.arcgis.com/VS6HdKS0VfIhv8Ct/arcgis/rest/services/'
                        'COVID19_Indonesia_per_Provinsi/FeatureServer/0/query?where=1%3D1&outFields'
                        '=*&outSR=4326&f=json')
data_json = response.json()
features = (data_json['features'])
tabel =[]
for i in features:
    baris = []
    baris.append(i['attributes']['Provinsi'])
    baris.append(i['attributes']['Kasus_Posi'])
    tabel.append(baris)
hasil = pd.DataFrame(tabel, columns=['nama_prov', 'positif'])
print(hasil)

sns.catplot(x='nama_prov', y='positif', kind='bar', data=hasil[:10], height=4, aspect=3)
plt.xticks(rotation=0)
plt.show()
plt.savefig('sumatera.png')
sns.catplot(x='nama_prov', y='positif', kind='bar', data=hasil[10:16], height=4, aspect=3,n_boot=1000)
plt.xticks(rotation=0)
plt.savefig('jawa.png')
sns.catplot(x='nama_prov', y='positif', kind='bar', data=hasil[16:19], height=4, aspect=3,n_boot=1000)
plt.xticks(rotation=0)
plt.savefig('kepulauan_sunda.png')
sns.catplot(x='nama_prov', y='positif', kind='bar', data=hasil[19:24], height=4, aspect=3,n_boot=1000)
plt.xticks(rotation=0)
plt.savefig('kalimantan.png')
sns.catplot(x='nama_prov', y='positif', kind='bar', data=hasil[24:30], height=4, aspect=3,n_boot=1000)
plt.xticks(rotation=0)
plt.savefig('sulawesi.png')
sns.catplot(x='nama_prov', y='positif', kind='bar', data=hasil[30:34], height=4, aspect=3,n_boot=1000)
plt.xticks(rotation=0)
plt.savefig('papua.png')