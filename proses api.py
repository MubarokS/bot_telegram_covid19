import json

file = open('sample2.json')
parsing_data = json.load(file)

f_name = parsing_data['firstName']
l_name = parsing_data['lastName']
gender = parsing_data['gender']
age = parsing_data['age']
s_adress = parsing_data['address']['streetAddress']
city = parsing_data['address']['city']
state = parsing_data['address']['state']
phone = parsing_data['phoneNumbers'][0]['number']

print(
    'Nama =',f_name,l_name,'\n'
    'Gender =',gender,'\n'
    'Umur =',age,'\n'
    'Alamat =',s_adress,city,state,'\n'
    'No HP =', phone
)