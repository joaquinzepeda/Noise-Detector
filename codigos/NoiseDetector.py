# -- coding: utf-8 --
#!/usr/bin/env python3
import requests

#importamos las librerias para conectar con el arduino Uno
import serial
import time
import urllib.request
from numpy import log10

CHAT_ID = '1134817572'

def enviar_mensaje(msj,CHAT_ID='1134817572'):
    
    TOKEN_BOT = '5389751808:AAE6UrYPJ06H1a_AitZyLtHfTBUwMtq8MRQ'
    requests.post('https://api.telegram.org/bot'+TOKEN_BOT+'/sendMessage',
              data={'chat_id': CHAT_ID, 'text': msj})
    

arduino = serial.Serial('/dev/ttyUSB0',9600, timeout = 1)

# Funcion que recibe el numero de muestras a los cuales
# se les saca el promedio y el numero de data perdida aceptada

def sound_detector(umbral=60,n_mean=150,m_error=20):
    
    suma = 0
    promedio = 0
    sound = 0
    #read from arduino

    n=0 #numero de muestras 
    m=0 #numero de data no recibida
    
    time.sleep(1)
    

    while 1:
        
        try:
            sound_str  = arduino.readline();
            #sound = sound_str.decode("utf-8").strip().split()[4]
            print("read input "+sound_str.decode("utf-8").strip() + " from arduino")

        except:
            print("no data returned")
            m+=1
        if m==m_error:
            break
            
        try:
            suma+=int(sound_str.decode("utf-8").strip())
            n+=1
        except:
            print('error en la muestra')
            m+=1

        
        if suma!=0 and suma%10==0:
            print(suma)
        if n==n_mean:
            promedio = suma/n_mean
            db = np.log10(promedio)
            b = urllib.request.urlopen('https://api.thingspeak.com/update?api_key=LXFUK4CHFK6OBI9H&field1='+str(db))
            suma=0
            n=0
            time.sleep(0.2)
        if db>np.log10(umbral): 
            enviar_mensaje('Has superado el limite de ruido permitido, por favor baja el volumen.')
            print("data enviada")
            time.sleep(0.2)

        
        

if _name_ == "_main_":
    print('Inicio detección de ruido')
    sound_detector(60,100,20)
    print('programa terminado')