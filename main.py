import requests
import json

data = requests.get('https://services5.arcgis.com/VS6HdKS0VfIhv8Ct/arcgis/rest/services/'
                    'COVID19_Indonesia_per_Provinsi/FeatureServer/0/query?where=1%3D1&out'
                    'Fields=*&outSR=4326&f=json')
data_json = data.json()

features = (data_json['features'])

for i in features:
    k_provinsi = i['attributes']['Kode_Provi']
    n_provinsi = i['attributes']['Provinsi']
    positif = i['attributes']['Kasus_Posi']
    sembuh = i['attributes']['Kasus_Semb']
    meninggal = i['attributes']['Kasus_Meni']
    print('''
Provinsi = {}
    '''.format(n_provinsi))

