# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 23:34:44 2020

@author: patry
"""

import requests
from bs4 import BeautifulSoup
import time
import csv
import tkinter as tk
from tkinter import scrolledtext
import pathlib
from pathlib import Path
import tkinter.messagebox




def close():

    root.destroy()


def clear():
    e.delete(0, 9999)


def scrapp():

    for q in range(1, int(p.get())):
        try:
            page = requests.get(e.get() + "&p=" + str(q))
            soup = BeautifulSoup(page.content, 'html.parser')
            artykuly = soup.find_all('article')
            for i in range(61):
                try:
                    artykul = artykuly[i]
                    tytuly = artykul.h2.extract()
                    ceny = artykul.find("span", class_='_9c44d_1zemI')
                    osoby = artykul.find("span", class_="_9c44d_2o04k")
                    lista = [tytuly.get_text(), ceny.get_text(), osoby.get_text()]
                    with open('{current_dir}allegro.csv', 'a', newline='') as csvfile:
                        new_row = csv.writer(csvfile, delimiter=" ",
                                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
                        new_row.writerow(lista)
                except AttributeError:
                    break
        except:
            break
    return tk.messagebox.showinfo('Koniec', 'Udało się zapisać wszystkie aukcje :) lub nie :D:D')

current_dir = Path.cwd()

root = tk.Tk()
root.title("Allegro Scrap")
root.geometry("500x90")
root.resizable(0, 0)

label1 = tk.LabelFrame(text="Wklej link poniżej")
label2 = tk.Label(text="Ile jest stron?")

e = tk.Entry(label1, width="65", borderwidth="5")
p = tk.Entry(root, width="10", borderwidth="5")
start_button = tk.Button(root, text="Scrap", padx=25, pady=5, command=scrapp)
clear_button = tk.Button(root, text="Wyczyść", padx=25, pady=5, command=clear)
exit_button = tk.Button(root, text="Zakończ", padx=25, pady=5, command=close)


label1.grid(row=0, column=0)
e.grid(row="0", column="0")
label2.place(x=140,y=52)
p.place(x=230, y=50)
start_button.place(x=410, y=10)
clear_button.place(x=300, y=50)
exit_button.place(x=400, y=50)


root.mainloop()
