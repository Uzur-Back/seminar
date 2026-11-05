from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests


def update_currency_label(event):
    code = target_combobox.get()
    name = currencies[code]
    target_label.config(text=name)


def price():
    pass


currencies = {

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
