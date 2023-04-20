import pandas as pd
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import csv
import os
from datetime import datetime
from datetime import date
today = date.today()
#d4 = today.strftime("%b-%d-%Y")


path = "BD_Personnes.csv"
header = ['CIN', 'Nom', 'Prenom', 'Age', 'Adresse', 'Nationalite', 'Telephone', 'Date_infection', 'deceder']


                
def verif_date(date_infection, window2):
    try:
        datetime.strptime(date_infection, "%d-%m-%Y")
        return True
    except:
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
                
                
from PyQt5.QtWidgets import QMessageBox

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
    if dec1 == dec0:
        err += "* Vérifier l'état de décès\n"
    if not verif_date(date_infection, window2):
        err += "* Vérifier la date d'infection\n"

    if err:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Erreur")
        msg.setText("Veuillez corriger les erreurs suivantes :")
        msg.setInformativeText(err)
        msg.exec_()
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
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Attention")
                msg.setText("Le CIN existe déjà")
                msg.exec_()
                return
        
        writer.writerow(personne_dict)

    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle("Succès")
    msg.setText("Personne ajoutée avec succès")
    msg.exec_()






def delete(window_Supp):
    num = window_Supp.lineEdit.text()
    if len(num) == 8 and num.isdigit():
        if os.path.exists(path) and os.path.getsize(path) > 0:
            with open(path, 'r', newline='') as f:
                reader = csv.DictReader(f)
                f.seek(0)
                rows = [row for row in reader if row['CIN'] != num]

            with open(path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(header)
                for row in rows:
                    writer.writerow(row.values())

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(f"Le personne avec le CIN {num} a été supprimé")
            msg.setWindowTitle("Succès")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("La base de données est vide ou n'existe pas")
            msg.setWindowTitle("Erreur")
            msg.exec_()
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Vérifier le numéro de CIN donné")
        msg.setWindowTitle("Erreur")
        msg.exec_()

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

            msg = QMessageBox()
            msg.setWindowTitle("Success")
            msg.setText(f"Toutes les personnes ayant le numéro de téléphone {telephone} ont été supprimées")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("La base de données est vide ou n'existe pas")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Vérifier le numéro de téléphone donné")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

def supprimer_nationalite(window_Supp_nat):
    nationalite = window_Supp_nat.lineEdit.text()
    if len(nationalite) < 3 or not nationalite.isalpha():
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Veuillez vérifier la nationalité donnée (doit contenir au moins 3 lettres alphabétiques)")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()
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

            msg = QMessageBox()
            msg.setWindowTitle("Success")
            msg.setText(f"Toutes les personnes ayant la nationalité {nationalite} ont été supprimées")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("La base de données est vide ou n'existe pas")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
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
                msg = QMessageBox()
                msg.setWindowTitle("Success")
                msg.setText(f"Téléphone de la personne avec le NCIN {num} a été modifié")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText(f"Personne avec le NCIN {num} n'existe pas")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("La base de données est vide ou n'existe pas")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Vérifier le NCIN ou le numéro de téléphone")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

def modifier_adresse(window_mod_ad):
    num, adresse = window_mod_ad.lineEdit.text(), window_mod_ad.lineEdit_2.text()
    path = 'BD_Personnes.csv'

    if (len(num) == 8 or num.isdigit() == True) and (len(adresse) > 3 or adresse.isalpha() == True):
        if os.path.exists(path) and os.path.getsize(path) > 0:
            with open(path, 'r', newline='') as f:
                reader = csv.DictReader(f)
                rows = list(reader)

            found = False
            for row in rows:
                if row['CIN'] == num:
                    row['Adresse'] = adresse
                    found = True
                    break

            if found:
                with open(path, 'w', newline='') as f:
                    fieldnames = ['CIN', 'Nom', 'Prenom', 'Age', 'Adresse', 'Nationalite', 'Telephone', 'Date_infection', 'deceder']
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                msg = QMessageBox()
                msg.setWindowTitle("Success")
                msg.setText(f"L'adresse de la personne avec le NCIN {num} a été modifiée")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText(f"Personne avec le NCIN {num} n'existe pas")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("La base de données est vide ou n'existe pas")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Vérifier le NCIN ou l'adresse")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()


def recherche_tel(window_rech_mal):
    telephone = window_rech_mal.lineEdit.text()
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
                    window_rech_mal.tableView.setModel(model)
                else:
                    window_rech_mal.tableView.setModel(None)
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("Aucun résultat trouvé pour ce numéro de téléphone")
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()

        else:
            window_rech_mal.tableView.setModel(None)
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("La base de données est vide ou n'existe pas")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
            
    else:
        window_rech_mal.tableView.setModel(None)
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Vérifier le numéro de téléphone (8 chiffres)")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()
    


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
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Aucune personne avec ce numéro de téléphone trouvé.")
                msg.setWindowTitle("erreur")
                msg.exec_()
            else:
                model = CsvTableModel(rows, header)
                window_rech_ind.tableView.setModel(model)
                

        else:
            window_rech_ind.tableView.setModel(None)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("La base de donnée est vide ou n'existe pas.")
            msg.setWindowTitle("erreur")
            msg.exec_()
    else:
        window_rech_ind.tableView.setModel(None)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Vérifier l'indicatif.")
        msg.setWindowTitle("erreur")
        msg.exec_()

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
                
            else:
                window_rech_dec.tableView.setModel(None)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Aucun résultat trouvé pour cette recherche")
                msg.setWindowTitle("erreur")
                msg.exec_()
                
    else:
        window_rech_dec.tableView.setModel(None)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("La base de données est vide ou n'existe pas")
        msg.setWindowTitle("erreur")
        msg.exec_()
        

path2 = "BD_Maladies.csv"
header2 = ['Code', 'CIN', 'Nom_maladie', 'nombre_annees']

def code_verif(code):
    if code.isdigit():
        if os.path.exists(path2) and os.path.getsize(path2) > 0:
            with open(path2, 'r', newline='') as f:
                reader = csv.DictReader(f)
                f.seek(0)
                rows = [row for row in reader if row['Code'] == code]
                if rows:
                    return True
                else:
                    return False
    
                
def add_maladie(ajout_maladie):
    
    code= ajout_maladie.lineEdit_2.text()
    cin = ajout_maladie.lineEdit_3.text()
    nom_maladie = ajout_maladie.lineEdit_4.text()
    nombre_annees = ajout_maladie.lineEdit_5.text()
    
    err = ""
    if not code.isnumeric():
        err += "* Vérifier le code du maladie\n"
    if len(cin) != 8 or not cin.isnumeric() :
        err += "* Vérifier le numéro de CIN\n"
    if not cin_verif(cin) :
        err += "*  le numéro de CIN n'existe pas (Ajouter votre personne)\n"
    if len(nom_maladie) < 3 or not nom_maladie.isalpha():
        err += "* Vérifier le nom du maladie\n"
    if len(nombre_annees) > 2 or not nombre_annees.isnumeric():
        err += "* Vérifier le nombre d'annees\n"
        
    if err:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Erreur")
        msg.setText("Veuillez corriger les erreurs suivantes :")
        msg.setInformativeText(err)
        msg.exec_()
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
        else :
            if code_verif(code):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Attention")
                msg.setText("Le Code existe déjà")
                msg.exec_()
                return
        writer.writerow(maladie_dict)

    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle("Succès")
    msg.setText("Maladie ajoutée avec succès")
    msg.exec_()



def delete_maladie(window_supp_malad):
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

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Attention")
            msg.setText(f"La telephone avec le code {code} a été supprimé")
            msg.exec_()
            
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Attention")
            msg.setText("La base de données est vide ou n'existe pas")
            msg.exec_()
            
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Attention")
        msg.setText("Vérifier le code de telephone donné")
        msg.exec_()

        
        
def modifier_nombre_anne(window_mod_tel):
    code, nombre_annee = window_mod_tel.lineEdit.text(), window_mod_tel.lineEdit_2.text()
    err=''
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
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Succès")
                msg.setText(f"Nombre d'années du telephone avec le code {code} a été modifié")
                msg.exec_()
                
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Attention")
                msg.setText(f"La telephone avec le code {code} n'existe pas")
                msg.exec_()
                
        else:
            
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Attention")
            msg.setText("La base de données est vide ou n'existe pas")
            msg.exec_()
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Attention")
        msg.setText("Vérifier le code ou le nombre d'années")
        msg.exec_()
        


def modifier_dec(window_mod_dec):
    code, dec1, dec0 = window_mod_dec.lineEdit.text(), window_mod_dec.dec_oui.isChecked() , window_mod_dec.dec_non.isChecked()
    if not code.isdigit():
        window_mod_dec.label_3.setText("Vérifier le code")
        return
    if dec1 == dec0 :
        window_mod_dec.label_3.setText("Vérifier l'état de décès")
        return
    if os.path.exists(path2) and os.path.getsize(path2) > 0:
        with open(path2, 'r', newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        found = False
        for row in rows:
            if row['Code'] == code:
                cin = row['CIN']
                found = True
                break

        if found:
            with open(path, 'r', newline='') as file0:
                reader0 = csv.DictReader(file0)
                rows0 = list(reader0)
            for row in rows0:
                if row['CIN'] == cin:
                    row['deceder'] = dec1
                    break
            with open(path, 'w', newline='') as file2:
                writer = csv.DictWriter(file2, fieldnames=reader0.fieldnames)
                writer.writeheader()
                writer.writerows(rows0)
        
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Succès")
            msg.setText("status modifier avec succès!")
            msg.exec_()
        else:

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Attention")
            msg.setText(f"La telephone avec le code {code} n'existe pas")
            msg.exec_()
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Attention")
        msg.setText("La base de données est vide ou n'existe pas")
        msg.exec_()
        



def affichage2(window_show_contenu_mal):
    # Create a new QStandardItemModel
    model = QStandardItemModel()

    # Clear the contents of the model
    model.clear()

    # Read the data from the CSV file
    df = pd.read_csv(path2)

    # Add the data to the model
    for row in range(df.shape[0]):
        model.insertRow(row)
        for col in range(df.shape[1]):
            item = QStandardItem(str(df.iloc[row, col]))
            model.setItem(row, col, item)

    # Set the model on the table view
    window_show_contenu_mal.tableView.setModel(model)

    

def recherche_mal(window_rech_mal):
    maladie = window_rech_mal.lineEdit.text()
    if maladie.isalpha():
        if os.path.exists(path2) and os.path.getsize(path2) > 0:
            with open(path2, 'r', newline='') as f:
                reader = csv.DictReader(f)
                rows = []
                for row in reader:
                    if row['Nom_maladie'] == maladie:
                        rows.append(row)

                if rows:
                    fieldnames = header2
                    model = CsvTableModelDict(rows, fieldnames)
                    window_rech_mal.tableView.setModel(model)
                    
                else:
                    window_rech_mal.tableView.setModel(None)
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setWindowTitle("Attention")
                    msg.setText("Aucun résultat trouvé pour ce nom de maladie")
                    msg.exec_()
                            
        else:
            window_rech_mal.tableView.setModel(None)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Attention")
            msg.setText("La base de données est vide ou n'existe pas")
            msg.exec_()
            
    else:
        window_rech_mal.tableView.setModel(None)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Attention")
        msg.setText("Vérifier le nom de la maladie")
        msg.exec_()
        

def recherche_mal_pers(window_rech_mal_pers):
    cin = window_rech_mal_pers.lineEdit.text()
    if cin_verif:
        if os.path.exists(path2) and os.path.getsize(path2) > 0:
            with open(path2, 'r', newline='') as f:
                reader = csv.DictReader(f)
                rows = []
                for row in reader:
                    if row['CIN'] == cin:
                        rows.append(row)

                if rows:
                    fieldnames = header2
                    model = CsvTableModelDict(rows, fieldnames)
                    window_rech_mal_pers.tableView.setModel(model)
                    
                else:
                    window_rech_mal_pers.tableView.setModel(None)
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setWindowTitle("Attention")
                    msg.setText("Aucun résultat trouvé pour ce CIN de malade")
                    msg.exec_()
                    
        else:
            window_rech_mal_pers.tableView.setModel(None)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Attention")
            msg.setText("La base de données est vide ou n'existe pas")
            msg.exec_()
            
    else:
        window_rech_mal_pers.tableView.setModel(None)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Attention")
        msg.setText("Vérifier le CIN du malade")
        msg.exec_()
        

def maladie_chaque_pers(window_all_mal_pers):
    if os.path.exists(path2) and os.path.getsize(path2) > 0:
        with open(path2, 'r', newline='') as f:
            reader = csv.DictReader(f)
            rows = []
            for row in reader:
                if row['CIN'] not in rows:
                    rows.append(row['CIN'])
            rowss = []
            for i in rows:
                o= {'Code': i}
                rowss.append(o)
                with open(path2, 'r', newline='') as f:
                    reader = csv.DictReader(f)
                    
                    for row in reader:
                        if row['CIN'] == i:
                            rowss.append(row)

            fieldnames = header2
            model = CsvTableModelDict(rowss, fieldnames)
            window_all_mal_pers.tableView.setModel(model)
    else:
        window_all_mal_pers.tableView.setModel(None)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Attention")
        msg.setText("La base de données est vide ou n'existe pas")
        msg.exec_()


def pourcentage_maladies(window_pourcentage_pers):
    if os.path.exists(path2) and os.path.getsize(path2) > 0:
        with open(path2, 'r', newline='') as f:
            reader = csv.DictReader(f)
            rows = []
            total=0
            for row in reader:
                total+=1
                if row['Nom_maladie'] not in rows:
                    rows.append(row['Nom_maladie'])
            rowss = []
            for i in rows:
                with open(path2, 'r', newline='') as f:
                    reader = csv.DictReader(f)
                    count=0
                    for row in reader:
                        if row['Nom_maladie'] == i:
                            count+=1
                    p=dict()
                    p["Nom_maladie"]=i
                    p["pourcentage"]=round((count*100)/total ,2)
                    rowss.append(p)

            if rowss:
                fieldnames = ["Nom_maladie","pourcentage"]
                model = CsvTableModelDict(rowss, fieldnames)
                window_pourcentage_pers.tableView.setModel(model)
            else:
                window_pourcentage_pers.tableView.setModel(None)
    else:
        window_pourcentage_pers.tableView.setModel(None)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Attention")
        msg.setText("La base de données est vide ou n'existe pas")
        msg.exec_()



def chaque_nationalite(window_nationalite):
    if os.path.exists(path) and os.path.getsize(path) > 0:
        with open(path, 'r', newline='') as f:
            reader = csv.DictReader(f)
            rows = []
            for row in reader:
                if row['Nationalite'] not in rows:
                    rows.append(row['Nationalite'])
            rowss = []
            for i in rows:
                o={'CIN': i}
                rowss.append(o)
                with open(path, 'r', newline='') as f:
                    reader = csv.DictReader(f)
                    
                    for row in reader:
                        if row['Nationalite'] == i:
                            rowss.append(row)

            fieldnames = header
            model = CsvTableModelDict(rowss, fieldnames)
            window_nationalite.tableView.setModel(model)
    else:
        window_nationalite.tableView.setModel(None)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Attention")
        msg.setText("La base de données est vide ou n'existe pas")
        msg.exec_()



def afficher_en_quarantaine(window_quarantaine):
    if os.path.exists(path) and os.path.getsize(path) > 0:
        with open(path, 'r', newline='') as f:
            reader = csv.DictReader(f)
            rows = []
            for row in reader:
                if abs(datetime.now()-datetime.strptime(row['Date_infection'], "%d-%m-%Y")).days <=14 :
                    rows.append(row)
            if rows:
                fieldnames = header
                model = CsvTableModelDict(rows, fieldnames)
                window_quarantaine.tableView.setModel(model)
            else:
                window_quarantaine.tableView.setModel(None)
    else:
        window_quarantaine.tableView.setModel(None)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Attention")
        msg.setText("La base de données est vide ou n'existe pas")
        msg.exec_()


def afficher_deceder(window_deceder):
    if os.path.exists(path) and os.path.getsize(path) > 0:
        total=0
        count=0
        with open(path, 'r', newline='') as f:
            reader = csv.DictReader(f)
            rows = []
            for row in reader:
                total+=1
                if row['deceder'] =="True":
                    count+=1
                    rows.append(row)
            p=dict()
            p["CIN"]=str(round((count*100)/total ,2))+"%"
            rows.append(p)
            if rows:
                fieldnames = header
                model = CsvTableModelDict(rows, fieldnames)
                window_deceder.tableView.setModel(model)
            else:
                window_deceder.tableView.setModel(None)
    else:
        window_deceder.tableView.setModel(None)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Attention")
        msg.setText("La base de données est vide ou n'existe pas")
        msg.exec_()

header3=['CIN', 'Nom', 'Prenom', 'Age', 'Adresse', 'Nationalite', 'Telephone', 'Date_infection', 'deceder', 'risque']
def afficher_en_risque(window_risque):
    if os.path.exists(path) and os.path.getsize(path) > 0:
        
        with open(path, 'r', newline='') as f:
            reader = csv.DictReader(f)
            rows = []
            for row in reader:
                risque=0
                if int(row['Age'])>70:
                    risque+=20
                if 50<int(row['Age'])<70:
                    risque+=10
                with open(path2, 'r', newline='') as f:
                    readerr = csv.DictReader(f)
                    for rowi in readerr:
                        if rowi['CIN']==row["CIN"]:
                            if rowi["Nom_maladie"]=="diabete" :
                                risque+=20
                            if rowi["Nom_maladie"]=="hypertension" :
                                risque+=20
                            if rowi["Nom_maladie"]=="asthme" :
                                risque+=20
                print(risque)
                if risque!=0:
                    row["risque"]=risque
                    rows.append(row)
            if rows:
                fieldnames = header3
                model = CsvTableModelDict(rows, fieldnames)
                window_risque.tableView.setModel(model)
            else:
                window_risque.tableView.setModel(None)
    else:
        window_risque.tableView.setModel(None)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Attention")
        msg.setText("La base de données est vide ou n'existe pas")
        msg.exec_()





def rech_nationalite(window_nationalite):
    if os.path.exists(path) and os.path.getsize(path) > 0:
        nationalite=window_nationalite.lineEdit.text()
        with open(path, 'r', newline='') as f:
            reader = csv.DictReader(f)
            rows = []
            
            with open(path, 'r', newline='') as f:
                reader = csv.DictReader(f)
                
                for row in reader:
                    if row['Nationalite'] == nationalite:
                        rows.append(row)

            fieldnames = header
            model = CsvTableModelDict(rows, fieldnames)
            window_nationalite.tableView.setModel(model)
    else:
        window_nationalite.tableView.setModel(None)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Attention")
        msg.setText("La base de données est vide ou n'existe pas")
        msg.exec_()