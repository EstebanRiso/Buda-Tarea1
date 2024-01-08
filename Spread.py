
import requests
import time
import json 






def SpreadMercado(market_id,singular):

    if singular==True:
        string='{ "spread":'
    else:
        string=''
    

    api_ticker=f'https://www.buda.com/api/v2/markets/{market_id}/ticker'
    response = requests.get(api_ticker)
    response = response.json()
    response= response['ticker']
    ask=float(response['min_ask'][0])
    bid=float(response['max_bid'][0])
    
    spread=ask-bid


    string=string+'{"market_id":"'+str(market_id)+'","spread":'+str(spread)
    string=string+'}'

    if singular==True:
        string=string+'}' 
    

    return string



def SpreadMercados():
    
    api_markets = 'https://www.buda.com/api/v2/markets'
    api_markets = requests.get(api_markets)
    api_markets = api_markets.json()
    api_markets = api_markets['markets']
    
    json_string='{ "spreads":['
    
    mercados=list()
    
    for data in api_markets:
        mercados.append(data['id'])

    ultimo_elemento=mercados[-1]

    for market_id in mercados:
        
        json_string=json_string+SpreadMercado(market_id,singular=False)
        if market_id is not ultimo_elemento:
            json_string=json_string+','


    json_string=json_string+']}'

    return json_string


def SpreadCompare(spread,market_id,singular):
    api_spread=f'http://localhost:5000/api/v2/spreads/{market_id}'
    api_spread = requests.get(api_spread)
    api_spread = api_spread.json()
    api_spread = api_spread['spread']
    
    api_spread=api_spread['spread']
    print("api spread es: "+str(api_spread))
    print("spread es: "+str(spread))
    
    if(singular==True):
        string='{ "comparacion":'
    else:
        string=''
    
    string=string+'{"market_id":"'+str(market_id)+'",'

    string=string+'"spread_comparado":"'+str(api_spread)+'",'

    if(spread > api_spread):
        string=string+'"status": "mayor"'

    if(spread == api_spread):
        string=string+'"status": "igual"'
  

    if(spread < api_spread):
        string=string+'"status": "menor"'

    
    string=string+'}'
    
    if singular==True:
        string=string+'}' 


    return string


def SpreadCompareAll(spread):
    api_spreads=f'http://localhost:5000/api/v2/spreads/all'
    api_spreads = requests.get(api_spreads)
    api_spreads = api_spreads.json()
    api_spreads = api_spreads['spreads']
    json_string='{ "comparaciones":['

    mercados=list()
    
    for data in api_spreads:
        mercados.append(data['market_id'])

    ultimo_elemento=mercados[-1]

    for market_id in mercados:
        
        json_string=json_string+SpreadCompare(spread,market_id,singular=False)
        if market_id is not ultimo_elemento:
            json_string=json_string+','

    json_string=json_string+']}'

    return json_string



def returnAllSpreads():
    api_spreads=f'http://localhost:5000/api/v2/spreads/all'
    api_spreads = requests.get(api_spreads)
    api_spreads = api_spreads.json()
    api_spreads = api_spreads['spreads']

    spreads=list()
    
    for data in api_spreads:
        spreads.append(data['spread'])

    return spreads

def returnAllMercados():
    api_markets = 'https://www.buda.com/api/v2/markets'
    api_markets = requests.get(api_markets)
    api_markets = api_markets.json()
    api_markets = api_markets['markets']
    
    mercados=list()
    
    for data in api_markets:
        mercados.append(data['id'])

    return mercados