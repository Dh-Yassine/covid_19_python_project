from PyQt5.QtWidgets import QMainWindow , QApplication
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
import myli
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




ajout_maladie=loadUi("ajout_maladie.ui")

window.ajout_maladie.triggered.connect(ajout_maladie.show)

ajout_maladie.pushButton.clicked.connect(lambda : test_csv.add_maladie(ajout_maladie))




window_supp_malad=loadUi("supp_malad.ui")

window.supp_malad.triggered.connect(window_supp_malad.show)

window_supp_malad.pushButton.clicked.connect(lambda : test_csv.delete_maladie(window_supp_malad))




window_mod_nombre_anne=loadUi("mod_nombre_anne.ui")

window.mod_years.triggered.connect(window_mod_nombre_anne.show)

window_mod_nombre_anne.pushButton.clicked.connect(lambda: test_csv.modifier_nombre_anne(window_mod_nombre_anne))




window_mod_dec=loadUi("mod_deceder.ui")

window.mod_deceder.triggered.connect(window_mod_dec.show)

window_mod_dec.pushButton.clicked.connect(lambda: test_csv.modifier_dec(window_mod_dec))




window_show_contenu_mal=loadUi("show_contenu2.ui")

window.aff_dictionnaire_maladies.triggered.connect(window_show_contenu_mal.show)

window_show_contenu_mal.pushButton.clicked.connect(lambda: test_csv.affichage2(window_show_contenu_mal))




window_rech_mal=loadUi("rech_maladie.ui")

window.rech_mal.triggered.connect(window_rech_mal.show)

window_rech_mal.pushButton.clicked.connect(lambda: test_csv.recherche_mal(window_rech_mal))




window_rech_mal_pers=loadUi("rech_maladie_pers.ui")

window.rech_mal_pers.triggered.connect(window_rech_mal_pers.show)

window_rech_mal_pers.pushButton.clicked.connect(lambda: test_csv.recherche_mal_pers(window_rech_mal_pers))




window_all_mal_pers=loadUi("aff_maladie_pers.ui")

window.rech_all_pers.triggered.connect(window_all_mal_pers.show)

window_all_mal_pers.pushButton.clicked.connect(lambda: test_csv.maladie_chaque_pers(window_all_mal_pers))




window_pourcentage_pers=loadUi("rech_pourcentage_mal.ui")

window.pourcentage_maladie.triggered.connect(window_pourcentage_pers.show)

window_pourcentage_pers.pushButton.clicked.connect(lambda: test_csv.pourcentage_maladies(window_pourcentage_pers))




window_quarantaine=loadUi("rech_pers_quarantaine.ui")

window.quarantaine.triggered.connect(window_quarantaine.show)

window_quarantaine.pushButton.clicked.connect(lambda: test_csv.afficher_en_quarantaine(window_quarantaine))




window_deceder=loadUi("rech_deceder_mal.ui")

window.deceder_pers_mal.triggered.connect(window_deceder.show)

window_deceder.pushButton.clicked.connect(lambda: test_csv.afficher_deceder(window_deceder))




window_risque=loadUi("risque.ui")

window.rech_risque.triggered.connect(window_risque.show)

window_risque.pushButton.clicked.connect(lambda: test_csv.afficher_en_risque(window_risque))



window_nationalite=loadUi("aff_nationalite.ui")

window.aff_nationalite.triggered.connect(window_nationalite.show)

window_nationalite.pushButton.clicked.connect(lambda: test_csv.chaque_nationalite(window_nationalite))




window_rech_nationalite=loadUi("rech_nationalite.ui")

window.rech_nationalite.triggered.connect(window_rech_nationalite.show)

window_rech_nationalite.pushButton.clicked.connect(lambda: test_csv.rech_nationalite(window_rech_nationalite))
app.exec()


