import requests
import json

api_token = '7edc0ac54fcf4ab8ee6e932108c870166e986556'
api_url_base = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token='


response = requests.get(api_url_base + api_token)
json_res = response.json()

numero_casas = str(json_res['numero_casas'])
token = str(json_res['token'])
cifrado = str(json_res['cifrado'])
decifrado = str(json_res['decifrado'])
resumo_criptografico = str(json_res['resumo_criptografico'])

print("numero_casas: ", numero_casas)
print("token    : ",token)
print("cifrado  : ",cifrado)
print("decifrado: ",decifrado)
print("resumo_criptografico: ", resumo_criptografico)

print(" ")


from caesarcipher import CaesarCipher

cipher = CaesarCipher(str(cifrado),offset=int(numero_casas))
decifrado = cipher.decoded

print("numero_casas: ", numero_casas)
print("token    : ",token)
print("cifrado  : ",cifrado)
print("decifrado: ",decifrado)

import hashlib

resumo_criptografico = hashlib.sha1(str(decifrado).encode('utf-8')).hexdigest()
print("resumo_criptografico",resumo_criptografico)
print(" ")

class cjc():

	def __init__(self, numero_casas, token, cifrado, decifrado,resumo_criptografico):
		self.numero_casas = numero_casas
		self.token = token
		self.cifrado = cifrado
		self.decifrado = decifrado
		self.resumo_criptografico = resumo_criptografico


criptografia_JC = cjc(numero_casas, token, cifrado, decifrado,resumo_criptografico)

json_reports = json.dumps(criptografia_JC.__dict__)

print("json_reports",json_reports)


api_url_request ='https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token='

answer = {'answer': open('answer.json','rb')}
submit = requests.post(api_url_request + api_token, files=answer)


#from flask_restful import Resource, Api
#from flask_cors import CORS

#app = Flask(__name__)
#api = Api(app)
#CORS(app)
#
#
#api_url_request ='https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token='
#
#{
#    "numero_casas": 5,
#    "token": "7edc0ac54fcf4ab8ee6e932108c870166e986556",
#    "cifrado": "bmjs ns itzgy, qjfaj ny tzy. otxmzf gqthm",
#    "decifrado": "when in doubt, leave it out. joshua bloch",
#    "resumo_criptografico": "3217accf836703467f2af0f195edc3d0fcb5a9dd"
#}

# here we create new data_file.json file with write mode using file i/o operation 
#with open('json_file.json', "w") as file_write:
# write json data into file
#json.dump(person_data, file_write)
