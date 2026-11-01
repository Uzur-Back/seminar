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
    base_code2 = base2_combobox.get().strip()
    if target_code and base_code and base_code2:
        try:
            resp = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            resp.raise_for_status()
            resp2 = requests.get(f'https://open.er-api.com/v6/latest/{base_code2}')
            resp2.raise_for_status()
            data = resp.json()
            data2 = resp2.json()
            if target_code in data['rates'] and target_code in data2['rates']:
                exchange_rate = data['rates'][target_code]
                exchange_rate2 = data2['rates'][target_code]
                base = currencies[base_code]
                base2 = currencies[base_code2]
                target = currencies[target_code]
                mb.showinfo('Курс обмена',
                            f'Курс:\n{exchange_rate:.1f} {target} за 1 {base},\n'
                            f'{exchange_rate2:.1f} {target} за 1 {base2}')
            else:
                mb.showerror('Ошибка', f'Валюта {target_code} не найдена')
        except Exception as e:
            mb.showerror('Ошибка', f'Произошла ошибка при запросе курса валют: {e}')
    else:
        mb.showwarning('Внимание', 'Выберите коды валют')


currencies = {
    'USD': 'Американский доллар',
    'EUR': 'Евро',
    'JPY': 'Японская йена',
    'GBP': 'Британский фунт стерлингов',
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
root.geometry('300x320')

Label(root, text='Базовая валюта').pack()
base_combobox = ttk.Combobox(root, values=list(currencies.keys()))
base_combobox.pack(padx=10, pady=5)
base_combobox.bind('<<ComboboxSelected>>', update_base_label)
base_label = ttk.Label()
base_label.pack()

Label(text='Вторая базовая валюта').pack(padx=10, pady=(15, 0))
base2_combobox = ttk.Combobox(root, values=list(currencies.keys()))
base2_combobox.pack(padx=10, pady=5)
base2_combobox.bind('<<ComboboxSelected>>', update_base2_label)
base2_label = ttk.Label()
base2_label.pack()

Label(text='Целевая валюта').pack(padx=10, pady=(15, 0))
target_combobox = ttk.Combobox(root, values=list(currencies.keys()))
target_combobox.pack(padx=10, pady=5)
target_combobox.bind('<<ComboboxSelected>>', update_currency_label)
target_label = ttk.Label()
target_label.pack(pady=10)

Button(text='Получить курс обмена валют',
       command=exchange).pack()

root.mainloop()
