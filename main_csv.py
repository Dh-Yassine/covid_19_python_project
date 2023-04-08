from PyQt5.QtWidgets import QMainWindow , QApplication
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi

import test_csv




app = QApplication([])


window = loadUi("untitled.ui")
window.show()



window2=loadUi("fenetre_ajouter.ui")

window.actionAjouter.triggered.connect(window2.show)

window2.pushButton.clicked.connect(lambda : test_csv.add_personne(window2))



window_Supp=loadUi("Supp_Personne.ui")

window.actionSupprimer_personne.triggered.connect(window_Supp.show)

window_Supp.pushButton.clicked.connect(lambda : test_csv.delete(window_Supp))



window_Supp_tel=loadUi("Supp_Tel.ui")

window.bout_supp_tel.triggered.connect(window_Supp_tel.show)

window_Supp_tel.pushButton.clicked.connect(lambda: test_csv.supprimer_telephone(window_Supp_tel))



window_Supp_nat=loadUi("Supp_Nat.ui")

window.bout_supp_nat.triggered.connect(window_Supp_nat.show)

window_Supp_nat.pushButton.clicked.connect(lambda: test_csv.supprimer_nationalite(window_Supp_nat))



window_mod_tel=loadUi("Mod_tel.ui")

window.actionModifier_telephone.triggered.connect(window_mod_tel.show)

window_mod_tel.pushButton.clicked.connect(lambda: test_csv.modifier_telephone(window_mod_tel))



window_mod_ad=loadUi("Mod_ad.ui")

window.actionModifier_Adresse.triggered.connect(window_mod_ad.show)

window_mod_ad.pushButton.clicked.connect(lambda: test_csv.modifier_adresse(window_mod_ad))



window_rech_tel=loadUi("rech_tel.ui")

window.rech_tel.triggered.connect(window_rech_tel.show)

window_rech_tel.pushButton.clicked.connect(lambda: test_csv.recherche_tel(window_rech_tel))




window_rech_ind=loadUi("rech_ind.ui")

window.rech_ind.triggered.connect(window_rech_ind.show)

window_rech_ind.pushButton.clicked.connect(lambda: test_csv.recherche_2digit_tel(window_rech_ind))



window_rech_dec=loadUi("rech_dec.ui")

window.rech_dec.triggered.connect(window_rech_dec.show)

window_rech_dec.pushButton.clicked.connect(lambda: test_csv.recherche_pers_dec(window_rech_dec))




window_show_contenu=loadUi("show_contenu.ui")

window.show_contenu_action.triggered.connect(window_show_contenu.show)

window_show_contenu.pushButton.clicked.connect(lambda: test_csv.affichage(window_show_contenu))


app.exec()


