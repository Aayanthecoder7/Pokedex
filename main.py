'''
Author: Aayan Ahmad Khan

Date: 11/12/2024

Infos: An program that shows you the Basics infos about an Pokemon.

'''

#Location: C:\Users\amna_\OneDrive\Dokumente\Codes,program\Python files

from tkinter import *
import requests

root = Tk()
root.geometry("300x300")
root.title("TRACKER🚥")
root.config(bg="black")

def get_api():
  try:
    pokemon = entry11.get()
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    responses = requests.get(url)
    responses.raise_for_status()
    data = responses.json()
    name = data.get("name", "Unknown")
    height = data.get("height", "Unknown")
    weight = data.get("weight", "Unknown")
    types = ", ".join([t['type']['name'] for t in data['types']])
    result = f"Name: {name.title()}\nHeight: {height / 10}m\nWeight: {weight / 10}kg\nTypes: {types}"
    config_label.config(text=result, fg="Red", font=(12))
  except:
    config_label.config(text="Couldn't get the Pokemon infos.")

title_label = Label(root, text="🚦Pokedex🚦", bg="Black", foreground="Yellow", font=("Arial", 22))
title_label.pack()

entry11 = Entry(root)
entry11.pack()

config_label = Label(root, text="", bg="Black", fg="Red")
config_label.pack(pady=20)

update_button = Button(root, text="Update💱", width=10, height=1, command=get_api)
update_button.pack(side="bottom")

root.mainloop()