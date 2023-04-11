import pandas as pd
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import os
from datetime import datetime

path = "BD_Personnes.csv"
header = ['CIN', 'Nom', 'Prenom', 'Age', 'Adresse', 'Nationalite', 'Telephone', 'Date_infection', 'deceder']


                
def verif_date(date_infection, window2):
    try:
        datetime.strptime(date_infection, "%d-%m-%Y")
        return True
    except:
        window2.label_11.setText("Il faut que le date soit en format jj-mm-aaaa")
        return False
    
    
def cin_verif(cin):
    if len(cin) == 8 and cin.isdigit():
        if os.path.exists(path) and os.path.getsize(path) > 0:
            with open(path, 'r', newline='') as f:
                reader = csv.DictReader(f)
                f.seek(0)
                rows = [row for row in reader if row['CIN'] == cin]
                if rows:
                    return True
                else:
                    return False
                
                
def add_personne(window2):
    cin = window2.lineEdit_2.text()
    nom = window2.lineEdit_3.text()
    prenom = window2.lineEdit_4.text()
    age = window2.lineEdit_5.text()
    adresse = window2.lineEdit_6.text()
    nationalite = window2.lineEdit_7.text()
    telephone = window2.lineEdit_8.text()
    date_infection = window2.lineEdit_9.text()
    dec1 = window2.dec_oui.isChecked()
    dec0 = window2.dec_non.isChecked()
    err = ""

    if len(cin) != 8 or not cin.isnumeric():
        err += "* Vérifier le numéro de CIN\n"
    if len(nom) < 3 or not nom.isalpha():
        err += "* Vérifier le nom\n"
    if len(prenom) < 3 or not prenom.isalpha():
        err += "* Vérifier le prénom\n"
    if len(adresse) < 3 or not adresse.isalnum():
        err += "* Vérifier l'adresse\n"
    if len(telephone) != 8 or not telephone.isnumeric():
        err += "* Vérifier le numéro de téléphone\n"
    if not age.isnumeric():
        err += "* Vérifier l'âge\n"
    if len(nationalite) < 3 or not nationalite.isalpha():
        err += "* Vérifier la nationalité\n"
    if not dec1 and not dec0:
        err += "* Vérifier l'état de décès\n"
    if not verif_date(date_infection, window2):
        err += "* Vérifier la date d'infection\n"

    if err:
        window2.label_11.setText("Erreur : \n" + err)
        return
    
    # Create a dictionary with the new person's data
    personne_dict = {
        'CIN': cin,
        'Nom': nom,
        'Prenom': prenom,
        'Age': age,
        'Adresse': adresse,
        'Nationalite': nationalite,
        'Telephone': telephone,
        'Date_infection': date_infection,
        'deceder': 'Oui' if dec1 else 'Non'
    }

    # Write the dictionary to the CSV file
    with open(path, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=personne_dict.keys())
        if os.stat(path).st_size == 0:
            writer.writeheader()
        else :
            with open(path, 'r', newline='') as f:
                reader = csv.DictReader(f)
                rows = [row for row in reader if row['CIN'] == cin]
            if rows:
                window2.label_11.setText("Le CIN existe déjà")
                return
        
        writer.writerow(personne_dict)

    window2.label_11.setText("Personne ajoutée avec succès")





def delete(window_Supp):
    num = window_Supp.lineEdit.text()
    if len(num) == 8 and num.isdigit():
        if os.path.exists(path) and os.path.getsize(path) > 0:
            with open(path, 'r', newline='') as f:
                reader = csv.DictReader(f)
                print(reader)
                f.seek(0)
                rows = [row for row in reader if row['CIN'] != num]

            with open(path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(header)
                for row in rows:
                    writer.writerow(row.values())

            window_Supp.label_2.setText(f"Le personne avec le CIN {num} a été supprimé")
        else:
            window_Supp.label_2.setText("La base de données est vide ou n'existe pas")
    else:
        window_Supp.label_2.setText("Vérifier le numéro de CIN donné")
def supprimer_telephone(window_Supp_tel):
     telephone = window_Supp_tel.lineEdit.text()
     if len(telephone) == 8 and telephone.isdigit():
         if os.path.exists(path) and os.path.getsize(path) > 0:
             with open(path, 'r', newline='') as f:
                 reader = csv.DictReader(f)
                 rows = [row for row in reader if row['Telephone'] != telephone]

             with open(path, 'w', newline='') as f:
                 fieldnames = ['CIN', 'Nom', 'Prenom', 'Age', 'Adresse', 'Nationalite', 'Telephone', 'Date_infection', 'deceder']
                 writer = csv.DictWriter(f, fieldnames=fieldnames)
                 writer.writeheader()
                 writer.writerows(rows)

             window_Supp_tel.label.setText(f"tout personne qui a le num de tel {telephone} a été supprimer")
         else:
             window_Supp_tel.label.setText("La base de donner est vide ou n'existe pas")
     else:
         window_Supp_tel.label.setText("Vérifier le numéro de téléphone")

def supprimer_nationalite(window_Supp_nat):
    nationalite = window_Supp_nat.lineEdit.text()
    if len(nationalite) < 3 or not nationalite.isalpha():
         window_Supp_nat.label_2.setText("*Verifier la nationalité\n")
    else :
        if os.path.exists(path) and os.path.getsize(path) > 0:
            with open(path, 'r', newline='') as f:
                reader = csv.DictReader(f)
                rows = [row for row in reader if row['Nationalite'] != nationalite]
            with open(path, 'w', newline='') as f:
                fieldnames = ['CIN', 'Nom', 'Prenom', 'Age', 'Adresse', 'Nationalite', 'Telephone', 'Date_infection', 'deceder']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)

            window_Supp_nat.label_2.setText(f"tout personne qui a la  nationalité {nationalite} a été supprimé")
        else:
             window_Supp_nat.label_2.setText("La base de donner est vide ou n'existe pas")


def affichage(window_show_contenu):
    # Create a new QStandardItemModel
    model = QStandardItemModel()

    # Clear the contents of the model
    model.clear()

    # Read the data from the CSV file
    df = pd.read_csv('BD_Personnes.csv')

    # Add the data to the model
    for row in range(df.shape[0]):
        model.insertRow(row)
        for col in range(df.shape[1]):
            item = QStandardItem(str(df.iloc[row, col]))
            model.setItem(row, col, item)

    # Set the model on the table view
    window_show_contenu.tableView.setModel(model)

    # Define a function to update the table view
    def update_table_view():
        # Clear the contents of the model
        model.clear()

        # Read the data from the CSV file
        data = pd.read_csv('BD_Personnes.csv')

        # Add the data to the model
        for row in range(data.shape[0]):
            model.insertRow(row)
            for col in range(data.shape[1]):
                item = QStandardItem(str(data.iloc[row, col]))
                model.setItem(row, col, item)

        # Set the model on the table view
        window_show_contenu.tableView.setModel(model)
import csv

def modifier_telephone(window_mod_tel):
    num,telephone = window_mod_tel.lineEdit.text() , window_mod_tel.lineEdit_2.text()
    if (len(num)==8 or num.isdigit()==True) and (len(telephone)==8 or telephone.isdigit()==True):
        if(os.path.exists(path) and os.path.getsize(path) > 0):
            with open(path, 'r', newline='') as file:
                reader = csv.DictReader(file)
                rows = list(reader)

            found = False
            for row in rows:
                if row['CIN'] == num:
                    row['Telephone'] = telephone
                    found = True
                    break

            if found:
                with open(path, 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)
                window_mod_tel.label_3.setText(f"Téléphone de personne avec le NCIN {num} a été modifié")
            else:
                window_mod_tel.label_3.setText(f"Personne avec le NCIN {num} n'existe pas")
        else:
            window_mod_tel.label_3.setText("La base de donneés est vide ou n'existe pas")
    else:
        window_mod_tel.label_3.setText("Vérifier le NCIN ou le numéro de téléphone ")

def modifier_adresse(window_mod_ad):
    num, adresse = window_mod_ad.lineEdit.text(), window_mod_ad.lineEdit_2.text()
    path = 'BD_Personnes.csv'
    
    if (len(num) == 8 or num.isdigit() == True) and (len(adresse) > 3 or adresse.isalpha() == True):
        if(os.path.exists(path) and os.path.getsize(path) > 0):
            with open(path, 'r', newline='') as file:
                reader = csv.DictReader(file)
                rows = list(reader)

            found = False
            for row in rows:
                if row['CIN'] == num:
                    row['Adresse'] = adresse
                    found = True
                    break

            if found:
                with open(path, 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                    window_mod_ad.label_3.setText(f"Adresse de personne avec le NCIN {num} a été modifié")
            else:
                window_mod_ad.label_3.setText(f"Personne avec le NCIN {num} n'existe pas")
        else:
            window_mod_ad.label_3.setText("La base de données est vide ou n'existe pas")
    else:
        window_mod_ad.label_3.setText("Vérifier le NCIN ou l'adresse")


def recherche_tel(window_rech_tel):
    telephone = window_rech_tel.lineEdit.text()
    if (len(telephone) == 8 and telephone.isdigit()):
        if os.path.exists(path) and os.path.getsize(path) > 0:
            with open(path, 'r', newline='') as f:
                reader = csv.DictReader(f)
                rows = []
                for row in reader:
                    if row['Telephone'] == telephone:
                        rows.append(row)

                if rows:
                    fieldnames = ['CIN', 'Nom', 'Prenom', 'Age', 'Adresse', 'Nationalite', 'Telephone', 'Date_infection', 'deceder']
                    model = CsvTableModelDict(rows, fieldnames)
                    window_rech_tel.tableView.setModel(model)
                    window_rech_tel.label_3.setText("")
                else:
                    window_rech_tel.tableView.setModel(None)
                    window_rech_tel.label_3.setText("Aucun résultat trouvé pour ce numéro de téléphone")
        else:
            window_rech_tel.tableView.setModel(None)
            window_rech_tel.label_3.setText("La base de données est vide ou n'existe pas")
    else:
        window_rech_tel.tableView.setModel(None)
        window_rech_tel.label_3.setText("Vérifier le numéro de téléphone (8 chiffres)")


class CsvTableModelDict(QtCore.QAbstractTableModel):
    def __init__(self, data, header, parent=None):
        super().__init__(parent)
        self._data = data
        self._header = header

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(self._header)

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            col = index.column()
            try:
                return str(self._data[row][self._header[col]])
            except KeyError:
                return None


def recherche_2digit_tel(window_rech_ind):
    telephone = window_rech_ind.lineEdit.text()
    if len(telephone)==2 and telephone.isdigit():
        if os.path.exists(path) and os.path.getsize(path) > 0:
            with open(path, 'r', newline='') as f:
                reader = csv.reader(f)
                rows = []
                header = next(reader)
                for row in reader:
                    if row[6][:2] != telephone:
                        continue
                    rows.append(row)

            if not rows:
                window_rech_ind.tableView.setModel(None)
                window_rech_ind.label_3.setText("Aucune personne avec ce numéro de téléphone trouvé.")
            else:
                model = CsvTableModel(rows, header)
                window_rech_ind.tableView.setModel(model)
                window_rech_ind.label_3.setText("")

        else:
            window_rech_ind.tableView.setModel(None)
            window_rech_ind.label_3.setText("La base de donnée est vide ou n'existe pas.")
    else:
        window_rech_ind.tableView.setModel(None)
        window_rech_ind.label_3.setText("Vérifier l'indicatif.")

class CsvTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, header, parent=None):
        super().__init__(parent)
        self._data = data
        self._header = header
        self._header_dict = {header[i]: i for i in range(len(header))}

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(self._header)

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            col = index.column()
            return str(self._data[row][col])
        return None

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return str(self._header[section])
            if orientation == QtCore.Qt.Vertical:
                return str(section + 1)
        return None




class CsvTableModel_dec(QtCore.QAbstractTableModel):
    def __init__(self, rows, header, parent=None):
        super().__init__(parent)
        self._data = rows
        self._header = header
        self._header_dict = {header[i]: i for i in range(len(header))}

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(self._header)

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            row = self._data[index.row()]
            col = index.column()
            return str(row[self._header[col]])
        return None

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return str(self._header[section])
            if orientation == QtCore.Qt.Vertical:
                return str(section + 1)
        return None
def recherche_pers_dec(window_rech_dec):
    if (os.path.exists(path) and os.path.getsize(path) > 0):
        with open(path, 'r', newline='') as f:
            reader = csv.DictReader(f)
            rows = []
            if window_rech_dec.dec1.isChecked() and window_rech_dec.dec2.isChecked():
                window_rech_dec.tableView.setModel(None)
                window_rech_dec.label_3.setText("Vous ne pouvez pas sélectionner les deux options")
                return
            for row in reader:
                if window_rech_dec.dec1.isChecked() and row['deceder'] == "Oui":
                    rows.append(row)
                elif window_rech_dec.dec2.isChecked() and row['deceder'] == "Non":
                    rows.append(row)

            if rows:
                fieldnames = ['CIN', 'Nom', 'Prenom', 'Age', 'Adresse', 'Nationalite', 'Telephone', 'Date_infection', 'deceder']
                model = CsvTableModel_dec(rows, fieldnames)
                window_rech_dec.tableView.setModel(model)
                window_rech_dec.label_3.setText("")
            else:
                window_rech_dec.tableView.setModel(None)
                window_rech_dec.label_3.setText("Aucun résultat trouvé pour cette recherche")
    else:
        window_rech_dec.tableView.setModel(None)
        window_rech_dec.label_3.setText("La base de données est vide ou n'existe pas")

path2 = "BD_Maladies.csv"
header2 = ['Code', 'CIN', 'Nom_maladie', 'nombre_annees']


def add_maladie(ajout_maladie):
    
    code= ajout_maladie.lineEdit_2.text()
    cin = ajout_maladie.lineEdit_3.text()
    nom_maladie = ajout_maladie.lineEdit_4.text()
    nombre_annees = ajout_maladie.lineEdit_5.text()
    
    err = ""
    if not code.isnumeric():
        err += "* Vérifier le code de la maladie\n"
    if len(cin) != 8 or not cin.isnumeric() :
        err += "* Vérifier le numéro de CIN\n"
    if not cin_verif(cin) :
        err += "*  le numéro de CIN n'existe pas (Ajouter votre personne)\n"
    if len(nom_maladie) < 3 or not nom_maladie.isalpha():
        err += "* Vérifier le nom de la maladie\n"
    if len(nombre_annees) > 2 or not nombre_annees.isnumeric():
        err += "* Vérifier le nombre d'annees\n"
        
    if err:
        ajout_maladie.label_11.setText("Erreur : \n" + err)
        return

    # Create a dictionary with the new person's data
    maladie_dict = {
        'Code': code,
        'CIN': cin,
        'Nom_maladie': nom_maladie,
        'nombre_annee': nombre_annees,
    }

    # Write the dictionary to the CSV file
    with open(path2, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=maladie_dict.keys())
        if os.stat(path2).st_size == 0:
            writer.writeheader()
        writer.writerow(maladie_dict)

    ajout_maladie.label_11.setText("Personne ajoutée avec succès")


def delete_maladie(window_supp_malad):
#assuming delete maladie bel code
    code = window_supp_malad.lineEdit.text()
    if code.isdigit():
        if os.path.exists(path2) and os.path.getsize(path2) > 0:
            with open(path2, 'r', newline='') as f:
                reader = csv.DictReader(f)
                print(reader)
                f.seek(0)
                rows = [row for row in reader if row['Code'] != code]

            with open(path2, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(header2)
                for row in rows:
                    writer.writerow(row.values())

            window_supp_malad.label_2.setText(f"Le maladie avec le code {code} a été supp_maladrimé")
        else:
            window_supp_malad.label_2.setText("La base de données est vide ou n'existe pas")
    else:
        window_supp_malad.label_2.setText("Vérifier le code de maladie donné")
        

        
        
def modifier_nombre_anne(window_mod_tel):
    code, nombre_annee = window_mod_tel.lineEdit.text(), window_mod_tel.lineEdit_2.text()
    if code.isdigit() and nombre_annee.isdigit():
        if os.path.exists(path2) and os.path.getsize(path2) > 0:
            with open(path2, 'r', newline='') as file:
                reader = csv.DictReader(file)
                rows = list(reader)

            found = False
            for row in rows:
                if row['Code'] == code:
                    row['nombre_annees'] = nombre_annee
                    found = True
                    break

            if found:
                with open(path2, 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)
                window_mod_tel.label_3.setText(f"Nombre d'années du maladie avec le code {code} a été modifié")
            else:
                window_mod_tel.label_3.setText(f"Le maladie avec le code {code} n'existe pas")
        else:
            window_mod_tel.label_3.setText("La base de données est vide ou n'existe pas")
    else:
        window_mod_tel.label_3.setText("Vérifier le code ou le nombre d'années")



