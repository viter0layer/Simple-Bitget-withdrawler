import time
import ccxt
import random

# api_keys of bitget
API_KEY = ""
API_SECRET = ""
password = '' # api pass

symbolWithdraw = "ETH"
chain = 'zkSyncEra'

def bitget_withdraw(address, amount_to_withdrawal, symbolWithdraw, API_KEY, API_SECRET):
    account_bitget = ccxt.bitget({
        'apiKey': API_KEY,
        'secret': API_SECRET,
        'password': password,
        'enableRateLimit': True,
        'options': {
            'defaultType': 'spot'
        }
    })

    try:
        account_bitget.withdraw(
            code=symbolWithdraw,
            amount=amount_to_withdrawal,
            address=address,
            tag=None,
            params={"chain": chain}
        )
        print(f">>> Успешно | {address} | {amount_to_withdrawal}")
    except Exception as error:
        print(f">>> Неудачно | {address} | ошибка : {error}")


if __name__ == "__main__":

    with open("wallets.txt", "r") as f:
        wallets_list = [row.strip() for row in f]

    print('/// start withdrawing...')
    for wallet in wallets_list:
        amount_to_withdrawal = round(random.uniform(0.0014323, 0.001443), 7)  # amount from ... to ... (минимум для минта нфт 0.00139)
        bitget_withdraw(wallet, amount_to_withdrawal, symbolWithdraw, API_KEY, API_SECRET)
        time.sleep(random.randint(5, 20)) # delay from 5 to 20 sec
