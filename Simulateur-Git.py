import sys
import sqlite3
from PyQt5.QtWidgets import  QDialog , QMainWindow , QPushButton, QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout,QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton

#############################################

class Dialog(QtWidgets.QDialog):
	def __init__(self):
		QtWidgets.QDialog.__init__(self)
		# Les champs

		self.__champTexteNomAuteur = QtWidgets.QLineEdit("")
		self.__champTextePrenomAuteur = QtWidgets.QLineEdit("")
		self.__champTexteTelfon = QtWidgets.QLineEdit("")

		self.__champDateNaissanceAuteur = QtWidgets.QDateEdit()
		self.__champDateNaissanceAuteur.setCalendarPopup(True)
        
		
		self.__champTexteAntecedent = QtWidgets.QLineEdit("")
		self.__champTexteDerniereVisite = QtWidgets.QLineEdit("")
		self.__champTexteDateEdition = QtWidgets.QLineEdit("")
		self.__champTexteIdUser = QtWidgets.QLineEdit("")
        #Bouton


		# Les widgets
		self.__widgetAuteur = QtWidgets.QWidget()
		self.__layoutAuteur = QtWidgets.QFormLayout()
		self.__layoutAuteur.addRow("Nom : ", self.__champTexteNomAuteur)
		self.__layoutAuteur.addRow("Prénom : ", self.__champTextePrenomAuteur)
		self.__layoutAuteur.addRow("Date de naissance : ", self.__champDateNaissanceAuteur)
		self.__widgetAuteur.setLayout(self.__layoutAuteur)
		#self.__layoutLivre = QtWidgets.QFormLayout()
		self.__layoutAuteur.addRow("Tel : ", self.__champTexteTelfon)
		self.__layoutAuteur.addRow("Antecedent : ", self.__champTexteAntecedent)
		self.__layoutAuteur.addRow("Derniere Visite : ", self.__champTexteDerniereVisite)
		self.__layoutAuteur.addRow("Date d'Edition : ", self.__champTexteDateEdition)
		self.__layoutAuteur.addRow("Id User : ", self.__champTexteIdUser)


		self.__tabWidget = QtWidgets.QTabWidget()
		self.__tabWidget.addTab(self.__widgetAuteur, "PATIENT")

		self.__mainLayout = QtWidgets.QVBoxLayout()
		self.__mainLayout.addWidget(self.__tabWidget)

		self.setLayout(self.__mainLayout)

#############################################
    
class Window(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("PATIENT")

        self.resize(270, 400)
        self.move(1300, 0)


        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry( QtCore.QRect(40, 330, 80, 32) )
        self.pushButton.setText(" AJOUTER ")
        self.pushButton.clicked.connect(self.button_click)

        self.pushButton2 = QtWidgets.QPushButton(self)
        self.pushButton2.setGeometry( QtCore.QRect(150, 330, 80, 32) )
        self.pushButton2.setText(" EXIT ")
        self.pushButton2.clicked.connect(self.button_click2)

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit2 = QtWidgets.QLineEdit(self)
        self.lineEdit3 = QtWidgets.QLineEdit(self)
        self.lineEdit4 = QtWidgets.QLineEdit(self)
        self.lineEdit5= QtWidgets.QLineEdit(self)
        self.lineEdit6 = QtWidgets.QLineEdit(self)
        self.lineEdit7 = QtWidgets.QLineEdit(self)
        self.lineEdit8 = QtWidgets.QLineEdit(self)
        self.lineEdit9 = QtWidgets.QLineEdit(self)


        self.lineEdit.setGeometry(QtCore.QRect(30, 60, 220, 20))
        self.lineEdit2.setGeometry(QtCore.QRect(30, 90, 220, 20))
        self.lineEdit3.setGeometry(QtCore.QRect(30, 120, 220, 20))
        self.lineEdit4.setGeometry(QtCore.QRect(30, 150, 220, 20))
        self.lineEdit5.setGeometry(QtCore.QRect(30, 180, 220, 20))
        self.lineEdit6.setGeometry(QtCore.QRect(30, 210, 220, 20))
        self.lineEdit7.setGeometry(QtCore.QRect(30, 240, 220, 20))
        self.lineEdit8.setGeometry(QtCore.QRect(30, 270, 220, 20))
        self.lineEdit9.setGeometry(QtCore.QRect(30, 300, 220, 20))


        self.lineEdit.setObjectName("ID")
        self.lineEdit2.setObjectName("Name")
        self.lineEdit3.setObjectName("Prenom")
        self.lineEdit4.setObjectName("Tel")
        self.lineEdit5.setObjectName("Date_de_naissance")
        self.lineEdit6.setObjectName("Antecedents")
        self.lineEdit7.setObjectName("Derniere_visite")
        self.lineEdit8.setObjectName("Date_edition")
        self.lineEdit9.setObjectName("Id_user")

        self.lineEdit.textEdited.connect(self.line_edited)
        #self.lineEdit2.textEdited.connect(self.line_edited)
    def Ajouter_patient_ASSISTANT(self,ID,Nom , Prenom, Tel, Date_de_naissance, Antecedents , Derniere_visite,Date_edition, Id_user):
                cur.execute('''INSERT INTO PERSON_USER_assistant (ID,Nom , Prenom, Tel, Date_de_naissance, Antecedents , Derniere_visite,Date_edition, Id_user) VALUES (?,?,?,?,?,?,?,?,?)''',(ID,Nom , Prenom, Tel, Date_de_naissance, Antecedents , Derniere_visite,Date_edition, Id_user))
        
        
    def button_click(self):
            print("Button Clicked :", self.lineEdit2.text())
            ID=self.lineEdit.text()
            Nom=self.lineEdit2.text()
            Prenom=self.lineEdit3.text()
            Tel=self.lineEdit4.text()
            Date_de_naissance=self.lineEdit5.text()
            Antecedents=self.lineEdit6.text()
            Derniere_visite=self.lineEdit7.text()
            Date_edition=self.lineEdit8.text()
            Id_user=self.lineEdit9.text()
            self.Ajouter_patient_ASSISTANT(ID, Nom , Prenom, Tel, Date_de_naissance, Antecedents , Derniere_visite,Date_edition, Id_user)
    def button_click2(self):
                self.close()

    def line_edited(self):
             print("Line Edited :",self.lineEdit.text())
  

########################################


####################################
class Fenetre_prinpale(QWidget):
    
    def __init__(self):
        QWidget.__init__(self)
        self.move(400, 400)

        self.label = QLabel("HELLO USER! IDENTIFY YOURSELF !!")
        # creation du bouton
        self.bouton = QPushButton("DOCTOR")
        self.bouton2 = QPushButton("ASSISTANT")
        self.bouton3 = QPushButton("AFFICHER-SERVEUR")
        self.bouton4 = QPushButton("AJOUTER-SERVEUR")
        self.bouton6 = QPushButton('EXIT')

        self.label2 = QLabel("YOU WANT TO EXECUTE SMTHG SERVER ??!!")

        # on connecte le signal "clicked" a la methode appui_bouton
        self.bouton.clicked.connect(self.appui_bouton)
        self.bouton2.clicked.connect(self.line_edited)
        self.bouton3.clicked.connect(self.affichage_SERVER)
        self.bouton4.clicked.connect(lambda : self.Ajouter_patient_SERVER(2,"MUS" , "BED", "22", "222", "2323" , "Derniere_visite","Date_edition", "Id_user"))
        self.bouton6.clicked.connect(QApplication.instance().quit)

        # creation du gestionnaire de mise en forme
        layout = QVBoxLayout()
        layout.addWidget(self.label)

        layout.addWidget(self.bouton)
        layout.addWidget(self.bouton2)
        layout.addWidget(self.bouton2)
       
        layout.addWidget(self.label2)


        layout.addWidget(self.bouton3)
        layout.addWidget(self.bouton4)
        layout.addWidget(self.bouton6)

        self.setLayout(layout)

        self.setWindowTitle("MAIN_SERVER")
    
    def Ajouter_patient_SERVER(self,ID,Nom , Prenom, Tel, Date_de_naissance, Antecedents , Derniere_visite,Date_edition, Id_user):
            cur.execute('''INSERT INTO PERSON_SERVER (ID,Nom , Prenom, Tel, Date_de_naissance, Antecedents , Derniere_visite,Date_edition, Id_user) VALUES (?,?,?,?,?,?,?,?,?)''',(ID,Nom , Prenom, Tel, Date_de_naissance, Antecedents , Derniere_visite,Date_edition, Id_user))
    
    def affichage_SERVER(self):
        print('Welcome to Table server : ')
        cur.execute("SELECT * FROM PERSON_SERVER")
        resultats = cur.fetchall()
        for resultat in resultats:  
            print(resultat)

    def line_edited(self):
        fen3 = Fenetre_ASSISTANT()
        fen3.resize(280,300)
        fen3.show() 
        fen3.exec()   
    
    def appui_bouton(self):
        fen2 = Fenetre_DOCTOR()
        fen2.resize(280,300)
        fen2.show()
        fen2.exec()

########################################

class Fenetre_DOCTOR(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.move(810, 400)

        self.label = QLabel("                      HELLO DOCTOR!!")
        # creation du bouton
        self.bouton = QPushButton("AJOUTER")
        self.bouton2 = QPushButton("AFFICHER")
        self.bouton3 = QPushButton("SYNCHRONISER")
        self.bouton4 = QPushButton("UPDATE_PATIENT")
        self.bouton5 = QPushButton("GET_UPDATES")

        # on connecte le signal "clicked" a la methode appui_bouton
        self.bouton.clicked.connect(self.saisie_doctor)
        self.bouton2.clicked.connect(self.affichage_DOCTOR)
        self.bouton3.clicked.connect(self.Synchro_with_server_dOCTOR)
        self.bouton4.clicked.connect(self.update_doctor)
        self.bouton5.clicked.connect(self.get_updates_doctor)
        # creation du gestionnaire de mise en forme
        layout = QVBoxLayout()
        layout.addWidget(self.label)

        layout.addWidget(self.bouton)
        layout.addWidget(self.bouton2)
        layout.addWidget(self.bouton3)
        layout.addWidget(self.bouton4)
        layout.addWidget(self.bouton5)

        self.setLayout(layout)

        self.setWindowTitle("DOCTOR")


    def line_edited(self):
            print("Line Edited :",self.lineEdit.text())
    
    def appui_bouton(self):
        print("Appui sur le bouton")
   
   
    def affichage_DOCTOR(self):
        print('Welcome to Table doctor : ')
        cur.execute("SELECT * FROM PERSON_USER_doctor")
        resultats = cur.fetchall()
        for resultat in resultats:  
            print(resultat)
    
    
    def Ajouter_patient_DOCTOR(self,ID,Nom , Prenom, Tel, Date_de_naissance, Antecedents , Derniere_visite,Date_edition, Id_user):
            cur.execute('''INSERT INTO PERSON_USER_doctor (ID,Nom , Prenom, Tel, Date_de_naissance, Antecedents , Derniere_visite,Date_edition, Id_user) VALUES (?,?,?,?,?,?,?,?,?)''',(ID,Nom , Prenom, Tel, Date_de_naissance, Antecedents , Derniere_visite,Date_edition, Id_user))
    
    def Synchro_with_server_dOCTOR(self):
  
        cur.execute('''SELECT ID FROM PERSON_SERVER ''')
        valeur_server = cur.fetchall()
        cur.execute('''SELECT ID FROM PERSON_USER_doctor ''')
        valeur_user = cur.fetchall()
        if valeur_server == []:
                cur.execute("SELECT * FROM PERSON_USER_doctor ")
                val= cur.fetchall()
                for i in range(len(val)):
                    (ID, Nom , Prenom, Tel, Date_de_naissance, Antecedents , Derniere_visite,Date_edition, Id_user) = val[i]
                    self.Ajouter_patient_SERVER()
        else:
            cur.execute("SELECT * FROM PERSON_SERVER ")
            server = cur.fetchall()
            cur.execute("SELECT * FROM PERSON_USER_doctor ")
            user = cur.fetchall()
            for i in valeur_user:
                #print('i[0] egale = ',i[0])
                cur.execute("SELECT * FROM PERSON_USER_doctor where ID= {0} ".format(i[0]))
                on1= cur.fetchone()
                cur.execute("SELECT * FROM PERSON_SERVER where ID= {0} ".format(i[0]))
                on2= cur.fetchone()
                cur.execute("SELECT * FROM   PERSON_USER_doctor where ID= {0} ".format(i[0]))
                on3= cur.fetchone()
                #print("assistant_docteur : ",on1)
                #print("serveur : ",on2)
                #print("testeur : ",on3)
                if on2 == None:
                    cur.execute("INSERT INTO PERSON_SERVER SELECT * FROM PERSON_USER_doctor WHERE ID= {0} ".format(i[0]))
                if on1!=on2 and on2==on3 :
                    cur.execute('''DELETE FROM PERSON_SERVER WHERE ID= {0} '''.format(i[0]))
                    cur.execute("INSERT INTO PERSON_SERVER SELECT * FROM PERSON_USER_doctor WHERE ID= {0} ".format(i[0]))
                    cur.execute('''DELETE FROM TESTEUR_PERSON_USER_doctor WHERE ID= {0} '''.format(i[0]))
                    cur.execute('''INSERT INTO TESTEUR_PERSON_USER_doctor SELECT * FROM PERSON_USER_doctor WHERE ID= {0} '''.format(i[0]))
                if on1!=on2 and on2!=on3 and on2!= None:
                    print("THERE IS SOMETHING WRONG! ")
                    cur.execute("SELECT * FROM PERSON_SERVER where ID= {0} ".format(i[0]))
                    print("1: ",cur.fetchone())
                    cur.execute("SELECT * FROM PERSON_USER_doctor where ID= {0} ".format(i[0]))
                    print("2: ",cur.fetchone())
                    mesg = int(input("PLEASE CHOOSE BETWEEN THIS TWO : 1/2: "))
                    if mesg==2:
                            cur.execute('''DELETE FROM PERSON_SERVER WHERE ID= {0} '''.format(i[0]))
                            cur.execute('''INSERT INTO PERSON_SERVER SELECT * FROM PERSON_USER_doctor WHERE ID= {0} '''.format(i[0]))
                            cur.execute('''DELETE FROM TESTEUR_PERSON_USER_doctor WHERE ID= {0} '''.format(i[0]))

                            cur.execute('''INSERT INTO TESTEUR_PERSON_USER_doctor SELECT * FROM PERSON_USER_doctor WHERE ID= {0} '''.format(i[0]))
   
   
    def get_updates_doctor(self):
        cur.execute("DELETE FROM PERSON_USER_doctor WHERE ID>0")
        cur.execute('''INSERT INTO PERSON_USER_doctor SELECT * FROM PERSON_SERVER''')
        


    def update_doctor(self):

        id_user=int(input("IDENTIFIEZ-VOUS! donner votre id_user : "))
        id_patient=int(input("donner id patient : "))
        column=input("Donner le variable désirer changer : ")
        value=input("DOnner sa valeur : ")

        cur.execute('''UPDATE PERSON_USER_doctor SET {0} = '{1}',Id_user = '{2}' WHERE ID = {3}'''.format(column,value,id_user,id_patient));
    def saisie_doctor(self):
        print('ADD A PATIENT : ')
        ID  = int(input('Donner ID PATIENT :'))
        Nom = input('Donner le nom du patient :')
        Prenom = input('Donner le prenom du patient :')
        Tel  = int(input('Donner tel du  PATIENT :'))
        Date_de_naissance = input('Donner la Date_naissance du patient :')
        Antecedents = input('Donner l"Antecedents du patient :')
        Derniere_visite = input('Donner la Derniere_visite du patient :')
        Date_edition = input('Donner la Date_edition du patient :')
        Id_user = input('Donner Id_user du patient ')
        self.Ajouter_patient_DOCTOR(ID, Nom , Prenom, Tel, Date_de_naissance, Antecedents , Derniere_visite,Date_edition, Id_user)

#########################################

class Fenetre_ASSISTANT(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.move(810, 0)

        self.label = QLabel("                      HELLO ASSISTANT!!")
        # creation du bouton
        self.bouton = QPushButton("AJOUTER")
        self.bouton2 = QPushButton("AFFICHER")
        self.bouton3 = QPushButton("SYNCHRONISER")
        self.bouton4 = QPushButton("UPDATE_PATIENT")
        self.bouton5 = QPushButton("GET_UPDATES")

        # on connecte le signal "clicked" a la methode appui_bouton
        #self.bouton.clicked.connect(self.saisie_assistant)
        self.bouton.clicked.connect(self.button_clicked)

        self.bouton2.clicked.connect(self.affichage_ASSISTANT)
        self.bouton3.clicked.connect(self.Synchro_with_server_ASSISTANT)
        self.bouton4.clicked.connect(self.update_assistant)
        self.bouton5.clicked.connect(self.get_updates_assistant)
        # creation du gestionnaire de mise en forme
        layout = QVBoxLayout()
        layout.addWidget(self.label)

        layout.addWidget(self.bouton)
        layout.addWidget(self.bouton2)
        layout.addWidget(self.bouton3)
        layout.addWidget(self.bouton4)
        layout.addWidget(self.bouton5)

        self.setLayout(layout)

        self.setWindowTitle("ASSISTANT")

        
    def button_clicked(self):
            wind=Window()
            wind.show()

            wind.exec()
            #dlg = QDialog(self)
            #dialog = Dialog()
            #dialog.setWindowTitle("Patient!")
            #dialog.exec_()
            #dlg.exec()
    def button_click(self):
            print("Button Clicked :", self.lineEdit.text())
            msg=self.lineEdit.text()
            a=int(msg)
            print("a = ",a)
    def line_edited(self):
            print("Line Edited :",self.lineEdit.text())
    
    def appui_bouton(self):
        print("Appui sur le bouton")
   
   
    def affichage_ASSISTANT(self):
        print('Welcome to Table ASSISTANT : ')
        cur.execute("SELECT * FROM PERSON_USER_assistant")
        resultats = cur.fetchall()
        for resultat in resultats:  
            print(resultat)
    
    
    def Ajouter_patient_ASSISTANT(self,ID,Nom , Prenom, Tel, Date_de_naissance, Antecedents , Derniere_visite,Date_edition, Id_user):
            cur.execute('''INSERT INTO PERSON_USER_assistant (ID,Nom , Prenom, Tel, Date_de_naissance, Antecedents , Derniere_visite,Date_edition, Id_user) VALUES (?,?,?,?,?,?,?,?,?)''',(ID,Nom , Prenom, Tel, Date_de_naissance, Antecedents , Derniere_visite,Date_edition, Id_user))
    
    def Synchro_with_server_ASSISTANT(self):
  
        cur.execute('''SELECT ID FROM PERSON_SERVER ''')
        valeur_server = cur.fetchall()
        cur.execute('''SELECT ID FROM PERSON_USER_assistant ''')
        valeur_user = cur.fetchall()
        if valeur_server == []:
                cur.execute("SELECT * FROM PERSON_USER_assistant ")
                val= cur.fetchall()
                for i in range(len(val)):
                    (ID, Nom , Prenom, Tel, Date_de_naissance, Antecedents , Derniere_visite,Date_edition, Id_user) = val[i]
                    self.Ajouter_patient_ASSISTANT()
        else:
            cur.execute("SELECT * FROM PERSON_SERVER ")
            server = cur.fetchall()
            cur.execute("SELECT * FROM PERSON_USER_assistant ")
            user = cur.fetchall()
            for i in valeur_user:
                #print('i[0] egale = ',i[0])
                cur.execute("SELECT * FROM PERSON_USER_assistant where ID= {0} ".format(i[0]))
                on1= cur.fetchone()
                cur.execute("SELECT * FROM PERSON_SERVER where ID= {0} ".format(i[0]))
                on2= cur.fetchone()
                cur.execute("SELECT * FROM   PERSON_USER_assistant where ID= {0} ".format(i[0]))
                on3= cur.fetchone()
                #print("assistant_docteur : ",on1)
                #print("serveur : ",on2)
                #print("testeur : ",on3)
                if on2 == None:
                    cur.execute("INSERT INTO PERSON_SERVER SELECT * FROM PERSON_USER_assistant WHERE ID= {0} ".format(i[0]))
                if on1!=on2 and on2==on3 :
                    cur.execute('''DELETE FROM PERSON_SERVER WHERE ID= {0} '''.format(i[0]))
                    cur.execute("INSERT INTO PERSON_SERVER SELECT * FROM PERSON_USER_assistant WHERE ID= {0} ".format(i[0]))
                    cur.execute('''DELETE FROM TESTEUR_PERSON_USER_assistant WHERE ID= {0} '''.format(i[0]))
                    cur.execute('''INSERT INTO TESTEUR_PERSON_USER_assistant SELECT * FROM PERSON_USER_assistant WHERE ID= {0} '''.format(i[0]))
                if on1!=on2 and on2!=on3 and on2!= None:
                    print("THERE IS SOMETHING WRONG! ")
                    cur.execute("SELECT * FROM PERSON_SERVER where ID= {0} ".format(i[0]))
                    print("1: ",cur.fetchone())
                    cur.execute("SELECT * FROM PERSON_USER_assistant where ID= {0} ".format(i[0]))
                    print("2: ",cur.fetchone())
                    mesg = int(input("PLEASE CHOOSE BETWEEN THIS TWO : 1/2: "))
                    if mesg==2:
                            cur.execute('''DELETE FROM PERSON_SERVER WHERE ID= {0} '''.format(i[0]))
                            cur.execute('''INSERT INTO PERSON_SERVER SELECT * FROM PERSON_USER_assistant WHERE ID= {0} '''.format(i[0]))
                            cur.execute('''DELETE FROM TESTEUR_PERSON_USER_assistant WHERE ID= {0} '''.format(i[0]))

                            cur.execute('''INSERT INTO TESTEUR_PERSON_USER_assistant SELECT * FROM PERSON_USER_assistant WHERE ID= {0} '''.format(i[0]))
   
   
    def get_updates_assistant(self):
        cur.execute("DELETE FROM PERSON_USER_assistant WHERE ID>0")
        cur.execute('''INSERT INTO PERSON_USER_assistant SELECT * FROM PERSON_SERVER''')
        


    def update_assistant(self):

        id_user=int(input("IDENTIFIEZ-VOUS! donner votre id_user : "))
        id_patient=int(input("donner id patient : "))
        column=input("Donner le variable désirer changer : ")
        value=input("DOnner sa valeur : ")

        cur.execute('''UPDATE PERSON_USER_assistant SET {0} = '{1}',Id_user = '{2}' WHERE ID = {3}'''.format(column,value,id_user,id_patient));
    def saisie_assistant(self):
        print('ADD A PATIENT : ')
        ID  = int(input('Donner ID PATIENT :'))
        Nom = input('Donner le nom du patient :')
        Prenom = input('Donner le prenom du patient :')
        Tel  = int(input('Donner tel du  PATIENT :'))
        Date_de_naissance = input('Donner la Date_naissance du patient :')
        Antecedents = input('Donner l"Antecedents du patient :')
        Derniere_visite = input('Donner la Derniere_visite du patient :')
        Date_edition = input('Donner la Date_edition du patient :')
        Id_user = input('Donner Id_user du patient ')
        self.Ajouter_patient_ASSISTANT(ID, Nom , Prenom, Tel, Date_de_naissance, Antecedents , Derniere_visite,Date_edition, Id_user)

#########################################

class Fenetre(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # création du champ de texte
        self.champ1 = QLineEdit("")
        self.champ2 = QLineEdit("")
        self.champ3 = QLineEdit("")
        self.champ4 = QLineEdit("")
        self.champ5 = QLineEdit("")
        self.champ6 = QLineEdit("")
        self.champ7 = QLineEdit("")
        self.champ8 = QLineEdit("")
        self.champ9 = QLineEdit("")
        
        # création du bouton
        self.bouton = QPushButton("AJOUTER_PATIENT")
        # on connecte le signal "clicked" à la méthode "appui_bouton_copie"
        self.bouton.clicked.connect(self.appui_bouton_copie)
 
        # création de l'étiquette
        self.label = QLabel()
        
        # mise en place du gestionnaire de mise en forme
        layout = QVBoxLayout()
        
        #layout.addWidget(self.champ1)
        layout.addWidget(self.champ2)
        layout.addWidget(self.champ3)
        layout.addWidget(self.champ4)
        layout.addWidget(self.champ5)
        layout.addWidget(self.champ6)
        layout.addWidget(self.champ7)
        layout.addWidget(self.champ8)
        layout.addWidget(self.champ9)
        layout.addWidget(self.bouton)
        layout.addWidget(self.label)

        self.setLayout(layout)
        
        self.setWindowTitle("AJOUTER_PATIENT")

    # on définit une méthode à connecter au signal envoyé
    def appui_bouton_copie(self):
        # la méthode "text" de QLineEdit permet d'obtenir le texte à copier
        texte_a_copier = self.champ1.text()
        #texte_a_copier = self.champ2.text()
        #texte_a_copier = self.champ3.text()
        #texte_a_copier = self.champ4.text()

        # la méthode "setText" de QLabel permet de changer
        # le texte de l'étiquette
        self.label.setText(texte_a_copier)
    def Ajouter_patient_DOCTOR(self,ID,Nom , Prenom, Tel, Date_de_naissance, Antecedents , Derniere_visite,Date_edition, Id_user):
            cur.execute('''INSERT INTO PERSON_USER_doctor (ID,Nom , Prenom, Tel, Date_de_naissance, Antecedents , Derniere_visite,Date_edition, Id_user) VALUES (?,?,?,?,?,?,?,?,?)''',(ID,Nom , Prenom, Tel, Date_de_naissance, Antecedents , Derniere_visite,Date_edition, Id_user))
    
###########################################
def open_data():
    con = sqlite3.connect("main_data_base999.db")
    cur = con.cursor()
def close_data():
    con.commit()
    cur.close
    con.close

#########################################

con = sqlite3.connect("main_data_base999.db")
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS PERSON_SERVER(
    ID INT PRIMARY KEY,
    Nom STR, Prenom STR, Tel INT, Date_de_naissance text, Antecedents STR, Derniere_visite text,
    Date_edition text, Id_user INT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS PERSON_USER_doctor(
    ID INT PRIMARY KEY,
    Nom STR, Prenom STR, Tel INT, Date_de_naissance text, Antecedents STR, Derniere_visite text,
    Date_edition text, Id_user INT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS PERSON_USER_assistant(
    ID INT PRIMARY KEY,
    Nom STR, Prenom STR, Tel INT, Date_de_naissance text, Antecedents STR, Derniere_visite text,
    Date_edition text, Id_user INT)''')  
cur.execute('''CREATE TABLE IF NOT EXISTS TESTEUR_PERSON_USER_doctor(
    ID INT PRIMARY KEY,
    Nom STR, Prenom STR, Tel INT, Date_de_naissance text, Antecedents STR, Derniere_visite text,
    Date_edition text, Id_user INT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS TESTEUR_PERSON_USER_assistant(
    ID INT PRIMARY KEY,
    Nom STR, Prenom STR, Tel INT, Date_de_naissance text, Antecedents STR, Derniere_visite text,
    Date_edition text, Id_user INT)''')


###################################
app = QApplication.instance() 
if not app:
    app = QApplication(sys.argv)
open_data()
fen = Fenetre_prinpale()
fen.resize(280,300)
fen.show()
close_data()
app.exec_()


