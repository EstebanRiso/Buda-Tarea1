import unittest
from Spread import *




class TestValores(unittest.TestCase):
    #testeando si todos conectan
    def test_is_connected(self):

        base='http://localhost:5000/api/v2/'
        mercados=returnAllMercados()
        spread=0.4
        urls_spreads=list()
        urls_polling=list()

        for data in mercados:
            urls_spreads.append(base+'spreads/'+data)
            string=base+'polling/spread/'+data+'/'+str(spread)
            urls_polling.append(string)

        for url in urls_spreads:
            try:
                respuesta = requests.get(url)
                # Verifica que la solicitud fue exitosa (código 200)
                self.assertEqual(respuesta.status_code, 200)
            except ConnectionError:
                self.fail(f"La conexión a {url} falló, puede que haber problemas o que no hayas iniciado la instancia de flask")
        
        for url in urls_polling:
            try:
                respuesta = requests.get(url)
                # Verifica que la solicitud fue exitosa (código 200)
                response=respuesta.json() 
                response=response['comparacion']
                response=response['spread_comparado']
                self.test_equal_less_more_status(response,spread)
                self.assertEqual(respuesta.status_code, 200)
            except ConnectionError:
                self.fail(f"La conexión a {url} falló, puede que haber problemas o que no hayas iniciado la instancia de flask")




    def test_is_negative(self):
        spreads=returnAllSpreads()
        for data in spreads:
            if(self.assertGreaterEqual(data, 0.0)==True):
                print("error, hay un spread negativo")
        
    def test_spread_string(self):
        spread='holamundo'
        base='http://localhost:5000/api/v2/'
        url=base+'polling/spread/BTC-COP/'+spread
        response= requests.get(url)
        self.assertEqual(response.status_code, 404)

    

    def test_equal_less_more_status(self,to_compare,spread):
        
        is_equal=False
        is_less=False
        is_more=False

        
        is_equal=self.assertEqual(to_compare,spread)
        is_more=self.assertLess(to_compare,spread)
        is_less=self.assertGreater(to_compare,spread)
        
        print('es igual?: '+is_equal+'\n')
        print('es mayor?: '+is_more+'\n')
        print('es menor?: '+is_less+'\n')


if __name__ == '__main__':
    unittest.main()

