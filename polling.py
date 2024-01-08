import time
import requests
import os





def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def is_connected(url):
    request=requests.get(url)
    if(request.status_code==200):
         return True
    else:
         return False
     

def polling(market_id,spread):
    url='http://localhost:5000/api/v2/polling/spread/'+market_id+'/'+spread
    print(url)
    conection=is_connected(url)
    
    print("la conexión es: "+str(conection))

    if(conection==True):
        while True:
            request=requests.get(url)
            request=request.json()
            print(request)
            time.sleep(2)
        
    
    elif conection==False:
        print("error, api no inicializada o tiene problemas")

def pollingAll(spread):
    url='http://localhost:5000/api/v2/polling/spread/all/'+spread
    conection=is_connected(url)

    if(conection==True):
        while True:
            request=requests.get(url)
            request=request.json()
            print(request)
            time.sleep(2)
            

    elif conection==False:
        print("error, api no inicializada o tiene problemas")


def hud_uno():

    while True:
        print("Indique que tipo de polling requiere:\n")
        print("1.Polling de solo un mercado\n2.Polling de todos los mercados")
        entrada=input()
        entrada=int(entrada)
        limpiar_pantalla()
        if(entrada==1):
                hud_dos()
        elif(entrada==2):
                hud_tres()
        else:
            print("error, entrada no concuerda")
            time.sleep(1)
            limpiar_pantalla()
    

def hud_dos():
    print("Indique mercado\n")
    market_id=input()
    print("Indique spread\n")
    spread=input()
    time.sleep(1)
    limpiar_pantalla()
    polling(market_id,spread)


def hud_tres():
     print("Indique spread")
     spread=input()
     time.sleep(1)
     limpiar_pantalla()
     pollingAll(spread)
     



def main():

    hud_uno()
   
    

main()