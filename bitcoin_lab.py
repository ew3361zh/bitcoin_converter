import requests
from pprint import pprint

print('Welcome to the bitcoin converter program that gives you up to date rates on how much your bitcoin is worth in US dollars')

def main():
    user_bitcoin = get_user_bitcoin()
    current_rate = get_current_bitcoin_exchange_rate()
    conversion_amt = convert_bitcoin_to_dollars(user_bitcoin, current_rate)
    share_result(user_bitcoin, current_rate, conversion_amt)

def get_user_bitcoin():
    while True:
        try:
            bitcoin = float(input('How much bitcoin do you have? '))
            if bitcoin <= 0:
                raise ValueError('Bitcoin amount must be a positive number')
            return bitcoin
        except:
            print('Enter a positive number')

def get_current_bitcoin_exchange_rate():
    response = request_rate()
    rate = extract_rate(response)
    return rate

def request_rate():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    return requests.get(url).json()

def extract_rate(response):
    return response['bpi']['USD']['rate_float']

def convert_bitcoin_to_dollars(user_bitcoin, current_rate):
    return user_bitcoin*current_rate

def share_result(user_bitcoin, current_rate, conversion_amt):
    print(f'At the current rate of {current_rate:.2f} USD/Bitcoin, your {user_bitcoin} Bitcoin would be worth ${conversion_amt:.2f} USD')

if __name__ == '__main__':
    main()