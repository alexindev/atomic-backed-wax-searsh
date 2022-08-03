import requests
from time import sleep
from datetime import datetime
from fake_useragent import UserAgent


ua = UserAgent()
print('скрипт запущен')

def main():
    try:
        while True:
            headers = {'user-ahent':f'{ua.random}'}
            url = 'https://wax.api.atomicassets.io/atomicmarket/v1/sales'
            resp = requests.get(url, headers=headers).json()
            now = datetime.now() 
            current_time = now.strftime("%H:%M:%S")
            for token in resp['data']:
                bt = token['assets'][0]['backed_tokens']
                token_synbol = token['listing_symbol']
                price = int(token['price']['amount'])* 0.00000001
        
                if len(bt) > 0:
                    if token_synbol == 'WAX':
                        print('https://wax.atomichub.io/market/sale/' + token['sale_id'] + '\n' + 'цена:', str(price), str(token_synbol) + '\n' + 'зашито:', str(int(token['assets'][0]['backed_tokens'][0]['amount'])/100000000), 'WAX' + '\n' + current_time +'\n\n')
                    
                    else:
                        print('https://wax.atomichub.io/market/sale/' + token['sale_id'] + '\n' + 'цена:', str(int(token['price']['amount'])* 0.01), 'USD' + '\n' + 'зашито:', str(int(token['assets'][0]['backed_tokens'][0]['amount'])/100000000), 'WAX' + '\n' + current_time +'\n\n')               
            sleep(10)
    except:
        pass

if __name__ == '__main__':
    main()
