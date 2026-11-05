from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests


def update_currency_label(event):
    code = target_combobox.get()
    name = currencies[code]
    target_label.config(text=name)


def price():
    target_code = target_combobox.get().strip()
    if target_code:
        try:
            resp = requests.get(f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&symbols={target_code}',
                                timeout=10)
            resp.raise_for_status()
            data = resp.json()
            exchange_rate = data[0]['current_price']
            target = currencies[target_code]
            mb.showinfo('Курс обмена', f'Курс:\n{exchange_rate:.1f} {target} за 1 USD')
        except Exception as e:
            mb.showerror('Ошибка', f'Произошла ошибка при запросе курса валют: {e}')
    else:
        mb.showwarning('Внимание', 'Выберите код валюты')


currencies = {
    'BTC': 'Bitcoin',
    'ETH': 'Ethereum',
}

root = Tk()
root.title('Курсы обмена криптовалют к Доллару')
root.geometry('300x150')

Label(text='Целевая криптовалюта').pack(padx=10, pady=(15, 0))
target_combobox = ttk.Combobox(root, values=list(currencies.keys()))
target_combobox.pack(padx=10, pady=5)
target_combobox.bind('<<ComboboxSelected>>', update_currency_label)
target_label = ttk.Label()
target_label.pack(pady=10)

Button(text='Получить курс обмена криптовалюты',
       command=price).pack()

root.mainloop()
