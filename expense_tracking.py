#Importer les modules
import tkinter as tk
from tkinter import ttk
import pandas as pd 

df_depenses = pd.read_csv('depenses.csv')
#Définir une fonction d'ajout des dépenses
def add_expense():
    global df_depenses
    #Récupé rer les valeurs des champs de saisie
    depense = {
        'Date': [date_var.get()],
        'Montant': [montant_var.get()],
        'Description': [description_var.get()]
    }
    
    #Créer un DataFrame à partir de la nouvelle dépense
    df_depense = pd.DataFrame(depense)

    #Charger le fichier CSV 
    try:
        df_depenses = pd.read_csv('depenses.csv')
    except FileNotFoundError:
        df_depenses = pd.DataFrame()  #Si le fichier n'existe pas encore, créer un DataFrame vide

    #Ajouter la nouvelle dépense au DataFrame existant
    df_depenses = pd.concat([df_depenses, df_depense], ignore_index=True)
    
    #Sauvegarder le DataFrame dans le fichier CSV en mode append
    df_depenses.to_csv('depenses.csv', index=False, mode='a', header=False)

    print("La nouvelle dépense a été ajoutée au fichier 'depense.csv'.")

    #Effacer les champs de saisie après l'ajout de la dépense
    date_var.set('')
    montant_var.set(0)
    description_var.set('')


def clear_entries():
    # Effacer les entrées des champs de saisie
    date_var.set('')
    montant_var.set(0)
    description_var.set('')

def display_expenses():
    # Récupérer les enregistrements 
    try:
        df_records = pd.read_csv('depenses.csv')
    except FileNotFoundError:
        print("Le fichier 'depenses.csv' n'existe pas encore.")
        return

    # Effacer les données précédentes dans le Treeview
    for row in expenses_view.get_children():
        expenses_view.delete(row)

    # Afficher les enregistrements dans le Treeview
    for index, row in df_records.iterrows():
        expenses_view.insert(parent='', index='end', values=(index+1, row['Date'], row['Montant'], row['Description']))


def exit_window():
    window.destroy()

def refreshData():
    # Effacer les données précédentes dans le Treeview
    for item in expenses_view.get_children():
        expenses_view.delete(item)
    # Recharger les enregistrements
    display_expenses()

def update_expense():
    pass
    
def trends():
    pass
    
    
    
    
window = tk.Tk()
window.title('Expense tracking')
window.geometry('1200x900')
window.resizable(False,False)

date_var = tk.StringVar()
montant_var = tk.IntVar()
description_var = tk.StringVar()

fnt = ('Times new roman', 20)

f1 = tk.Frame(window, padx = 50, pady = 50)
f1.pack()

f2 = tk.Frame(window, padx = 100, pady = 100)
f2.pack()

date_label = tk.Label(f1,text='Date', font=fnt).grid(row=0, column=0, sticky='w')
date = tk.Entry(f1,textvariable=date_var).grid(row=0, column=1, padx=20, pady=10)

montant_label = tk.Label(f1,text='Montant', font=fnt).grid(row=1, column=0, sticky='w')
montant = tk.Entry(f1,textvariable=montant_var).grid(row=1, column=1, padx=20, pady=10)

description_label = tk.Label(f1,text='Description', font=fnt).grid(row=2, column=0, sticky='w')
description = tk.Entry(f1, textvariable=description_var).grid(row=2, column=1, padx=20, pady=10)

add_btn = tk.Button(f1, font=fnt, text='Ajouter une dépense', bg='#007889', command=add_expense).grid(row=0, column=2, sticky='nsew', padx=20, pady=10)
display_btn = tk.Button(f1, font=fnt, text='Afficher les dépenses', bg='#007889', command=display_expenses).grid(row=1, column=2, sticky='nsew', padx=20, pady=10)
update_btn = tk.Button(f1, font=fnt, text='Modifier une dépense', bg='#007889', command=update_expense).grid(row=2, column=2, sticky='nsew', padx=20, pady=10)
trends_btn = tk.Button(f1, font=fnt, text='Visualiser les tendances', bg='#007889', command=trends).grid(row=0, column=3, sticky='nsew', padx=20, pady=10)
clear_btn = tk.Button(f1, font=fnt, text='Effacer les entrées', bg='#007889', command=clear_entries).grid(row=1, column=3, sticky='nsew', padx=20, pady=10)
exit_btn = tk.Button(f1, font=fnt, text='Exit', bg='#007889', command=exit_window).grid(row=2, column=3, sticky='nsew', padx=20, pady=10)

expenses_view = ttk.Treeview(f2, columns=(1,2,3,4), show='headings', height=50)
expenses_view.pack()

expenses_view.column(1, anchor="center", stretch="no", width=70)

expenses_view.column(2, anchor="center", width=250)
expenses_view.column(3, anchor="center", width=250)
expenses_view.column(4, anchor="center", width=500)
expenses_view.heading(1, text='Id')
expenses_view.heading(2, text='Date')
expenses_view.heading(3, text='Montant')
expenses_view.heading(4, text='Description')


scrollbar = tk.Scrollbar(f2, orient='vertical')
scrollbar.configure(command=expenses_view.yview)
scrollbar.pack(side="right", fill="y")
expenses_view.config(yscrollcommand=scrollbar.set)



window.mainloop()
