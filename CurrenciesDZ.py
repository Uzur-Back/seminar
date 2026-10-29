from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests


def update_currency_label(event):
    code = target_combobox.get()
    name = currencies[code]
    target_label.config(text=name)


def update_base_label(event):
    code = base_combobox.get()
    name = currencies[code]
    base_label.config(text=name)


def update_base2_label(event):
    code = base2_combobox.get()
    name = currencies[code]
    base2_label.config(text=name)


def exchange():
    target_code = target_combobox.get().strip()
    base_code = base_combobox.get().strip()
    if target_code and base_code:
        try:
            resp = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            resp.raise_for_status()
            data = resp.json()
            if target_code in data['rates']:
                exchange_rate = data['rates'][target_code]
                base = currencies[base_code]
                target = currencies[target_code]
                mb.showinfo('Курс обмена',
                            f'Курс: {exchange_rate:.1f} {target} за 1 {base}')
            else:
                mb.showerror('Ошибка', f'Валюта {target_code} не найдена')
        except Exception as e:
            mb.showerror('Ошибка', e)

    else:
        mb.showwarning('Внимание', 'Введите код валюты')


currencies = {
    'USD': 'Американский доллар',
    'EUR': 'Евро',
    'JPY': 'Японская йена',
    'GBP': 'Фунт стерлингов',
    'AUD': 'Австралийский доллар',
    'CAD': 'Канадский доллар',
    'CHF': 'Швейцарский франк',
    'CNY': 'Китайский юань',
    'RUB': 'Российский рубль',
    'KZT': 'Казахстанский тенге',
    'UZS': 'Узбекский сум'
}

root = Tk()
root.title('Курсы обмена валют')
root.geometry('320x300')

Label(root, text='Базовая валюта').pack()
base_combobox = ttk.Combobox(root, values=list(currencies.keys()))
base_combobox.pack(padx=10, pady=5)
base_combobox.bind('<<ComboboxSelected>>', update_base_label)
base_label = ttk.Label()
base_label.pack()

Label(text='Вторая базовая валюта').pack(padx=10, pady=(15,0))
base2_combobox = ttk.Combobox(root, values=list(currencies.keys()))
base2_combobox.pack(padx=10, pady=5)
base2_combobox.bind('<<ComboboxSelected>>', update_base2_label)
base2_label = ttk.Label()
base2_label.pack()

Label(text='Целевая валюта').pack(padx=10, pady=(15,0))
target_combobox = ttk.Combobox(root, values=list(currencies.keys()))
target_combobox.pack(padx=10, pady=5)
target_combobox.bind('<<ComboboxSelected>>', update_currency_label)

target_label = ttk.Label()
target_label.pack()

Button(text='Получить курс обмена валют',
       command=exchange).pack(pady=5)

root.mainloop()

