from tkinter import *
from tkinter import messagebox
from tkinter import ttk

f = Tk()
f.title('Oussama Lap Store')

BRAND = Label(f, text="Oussama Lap Store", font=("Arial", 16, 'bold'))
BRAND.grid(row=0, column=0)

# Configure styles
style = ttk.Style()
style.theme_use("clam")

# Define colors
primary_color = "#00b4d3"
secondary_color = "#ffffff"
accent_color = "#00a2bf"

# Configure style elements
style.configure("Treeview", background=secondary_color, foreground="black", fieldbackground=secondary_color)
style.configure("Treeview.Heading", background=primary_color, foreground="white", font=("Helvetica", 10, "bold"))
style.map("Treeview", background=[("selected", accent_color)])

tree = ttk.Treeview(f)

tree.heading("#0", text="", anchor="w")
tree.column("#0", width=1, minwidth=1, stretch=NO)


#Mettre les données dans le fichier :
monOrdinateur = []

def marque_selectionnee(*args):
    return marE.get()

def so_selectionnee(*args):
    return soE.get()

def msgActualiser():
    messagebox.showinfo("Infomation", "Veuillez Entrez a Nouveau pour Voir les Modifications")

######:)######
## AJOUTER ##
def ajouter():

    mar = marque_selectionnee() or ""
    so = so_selectionnee() or ""
    ram = ramE.get() or ""
    cpu = cpuE.get() or ""
    col = colE.get() or ""

    monOrdinateur = [mar, so, ram, cpu, col]
    with open("Stock Ordinateurs.txt", "a") as file:
        file.write(','.join(map(str, monOrdinateur)) + '\n')
    with open("Stock Ordinateurs.txt", "r") as file:
        lines = file.readlines()

    msgActualiser()

########:)########
## RECHERCHER ##
def search(donnes):
    keyword = rechE.get().lower()
    tree.delete(*tree.get_children())

    for row in donnes[1:]:
        if keyword in row[0].lower():
            tree.insert("", "end", values=row)

rechL = Label(f, text="Recherche par marque:",font=("Verdana",8, 'bold'))
rechE = Entry(f, bd=2)

def toggle_rechE():
    if rechE.grid_info() != {}:
        search(donneesOrdinateur)
    else:
        rechL.grid(row=8, column=0, padx=10, pady=10)
        rechE.grid(row=8, column=1, padx=10, pady=10)


#######:)#######
## MODIFIER ##
row_index = None

def on_select(event):
    global row_index 
    selected_item = tree.focus()
    row_index = tree.index(selected_item)

def modifier():
    global row_index
    supprimer()
    
    mar = marque_selectionnee() or ""
    so = so_selectionnee() or ""
    ram = ramE.get() or ""
    cpu = cpuE.get() or ""
    col = colE.get() or ""

    monOrdinateur = [mar, so, ram, cpu, col]
    with open("Stock Ordinateurs.txt", "r") as file:
        lines = file.readlines()

    lines.insert(row_index, ','.join(map(str, monOrdinateur)) + '\n')

    with open("Stock Ordinateurs.txt", "w") as file:
        file.writelines(lines)

    row_index = None


#######:)#######
## SUPPRIMER ##
def supprimer():
    selected_item = tree.focus()
    index = int(tree.index(selected_item))
    with open('Stock Ordinateurs.txt', 'r') as file:
        lines = file.readlines()

    if index >= 0 and index < len(lines):
        del lines[index]

    with open('Stock Ordinateurs.txt', 'w') as file:
        file.writelines(lines)

    tree.delete(selected_item)


marL = Label(f, text='Marque : ',font=("Verdana",8, 'bold'))
marE = StringVar()
options = ttk.OptionMenu(f, marE, "Marque", "APPLE", "HP", "LENOVO", "ASUS", "DELL")
marL.grid(row=1, column=0)
options.grid(row=1, column=1)
marE.trace("w", marque_selectionnee )


soL = Label(f, text='Système opérateur : ',font=("Verdana",8, 'bold'))
soE = StringVar()
options2 = ttk.OptionMenu(f, soE, "Système opérateur", "Windows 7", "Windows 10", "Windows11", "macOS", "Linux", "Autre...")
soL.grid(row=2, column=0)
options2.grid(row=2, column=1)
soE.trace("w", so_selectionnee )

ramL = Label(f, text='Mémoire RAM : ',font=("Verdana",8, 'bold'))
ramE = Entry(f, bd=2)
ramL.grid(row=3, column=0)
ramE.grid(row=3, column=1)

cpuL = Label(f, text='CPU : ',font=("Verdana",8, 'bold'))
cpuE = Entry(f, bd=2)
cpuL.grid(row=4, column=0)
cpuE.grid(row=4, column=1)

colL = Label(f, text='Couleur : ',font=("Verdana",8, 'bold'))
colE = Entry(f, bd=2)
colL.grid(row=5, column=0)
colE.grid(row=5, column=1)

btnAjouter = Button(text='Ajouter', command=ajouter, bg='#00b4d3', fg="black")
btnAjouter.grid(row=8, column=3, padx=10, pady=10)

btnRechercher =Button(f, text="Rechercher", command=toggle_rechE, bg='#00b4d3', fg="black")
btnRechercher.grid(row=8, column=4, padx=10, pady=10)

btnModifier = Button(text='Modifier', command=modifier, bg='#00b4d3', fg="black")
btnModifier.grid(row=8, column=5, padx=10, pady=10)

btnSupprimer = Button(text='Supprimer', command=supprimer, bg='red', fg="white")
btnSupprimer.grid(row=8, column=6, padx=10, pady=10)


#récupérer les données du fichier :
def create_table(donnes):
    tree["columns"] = tuple(range(len(donnes[0])))

    for i, header in enumerate(donnes[0]):
        tree.heading(i, text=header)
        tree.column(i, width=100, anchor="center")

    for row_index, row in enumerate(donnes[1:]):
        background_color = "#e9e9e9" if row_index % 2 == 0 else "white"
        tree.insert("", "end", values=row, tags=(row_index,))
        tree.tag_configure(row_index, background=background_color)

    tree.grid(row=1, column=3, columnspan=4, rowspan=5, padx=10, pady=10)

    f.mainloop()



with open('Stock Ordinateurs.txt', 'r') as file:
    contenu = file.readlines()

contenu = [line.strip() for line in contenu]

donneesOrdinateur = [["Marque", "Système", "Mémoire RAM", "CPU", "Couleur"]]

for line in contenu:
    donneesOrdinateur.append(line.split(","))

tree.bind("<<TreeviewSelect>>", on_select)

create_table(donneesOrdinateur)


