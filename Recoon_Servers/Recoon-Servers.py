from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import ttk
from tkinter import *
from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import Qt
from colorama import init
from termcolor import colored
import folium
import dns.name
import dns.resolver
from ip2geotools.databases.noncommercial import DbIpCity
import socket
import pandas as pd
import socket
import os
import html
import whois
import os
import folium
import dns.name
import dns.resolver
from ip2geotools.databases.noncommercial import DbIpCity
import socket
import pandas as pd

import back1
import dns_error


class Ui_Dialog_dns(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(478, 181)
        Dialog.setFixedSize(478, 181)
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(60, 100, 351, 28))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("font: 25 italic 10pt \"Ubuntu\";\n"
                                      "color: rgb(178,34,34);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 110, 41, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(190, 150, 81, 21))
        self.pushButton.setStyleSheet("font: 25 italic 10pt \"Pagul\";\n"
                                      "color: rgb(0,100,0);") #170, 85, 255
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 161, 31))
        self.label_2.setStyleSheet("font: 25 italic 10pt \"URW Bookman [UKWN]\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(7, 5, 81, 81))
        self.label_3.setStyleSheet("image: url(:/newPrefix/white.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(340, 160, 141, 20))
        self.label_4.setStyleSheet("font: 10pt \"Pagul\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(110, 40, 311, 31))
        self.label_5.setStyleSheet("\n"
                                   "font: 12pt \"Purisa\";")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Recoon-Servers"))
        self.label.setText(_translate("Dialog",
                                      "<html><head/><body><p><span style=\" font-size:12pt; color:#55ff00;\">DNS :</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Starting"))
        self.label_2.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:16pt; color:#55ff00;\">Recoon Servers</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" color:#55ff00;\">By </span><span style=\" color:#ffffff;\">F0rbidden-Equation</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" color:#ffffff;\">Mapping Infos Gathering Servers</span></p></body></html>"))


class Ui_Dialog_error_dns(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(297, 93)
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 71))
        self.label.setStyleSheet("image: url(:/newPrefix/DNS_Error.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(130, 30, 111, 21))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:14pt; color:#aa5500;\">Error </span><span style=\" font-size:14pt; color:#ffffff;\">Dns </span><span style=\" font-size:14pt; color:#aa5500;\">!!</span></p></body></html>"))


class Ui_Dialog_progressbar(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(438, 169)
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0);")
        Dialog.move(50, 50)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(80, 100, 311, 23))
        self.progressBar.setProperty("value", 10)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(160, 0, 161, 31))
        self.label_2.setStyleSheet("font: 25 italic 10pt \"URW Bookman [UKWN]\";")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(110, 40, 311, 31))
        self.label_5.setStyleSheet("\n"
                                   "font: 12pt \"Purisa\";")
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 81, 81))
        self.label_3.setStyleSheet("image: url(:/newPrefix/white.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 140, 141, 20))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:16pt; color:#55ff00;\">Recoon Servers</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" color:#ffffff;\">Mapping Infos Gathering Servers</span></p></body></html>"))
        self.label.setText(_translate("Dialog",
                                      "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Please </span><span style=\" font-size:12pt; color:#55ff00;\">Patient ...</span></p></body></html>"))



    def action(self):
        self.fenetre1 = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.fenetre1)
        self.fenetre1.close()

        import time

        self.fenetre2.show()
        time.sleep(5)
        import time
        self.ui2.progressBar.setProperty("value", 60)
        self.fenetre1.close()

        self.fenetre2 = QtWidgets.QDialog()
        self.ui2 = Ui_Dialog_progressbar()
        self.ui2.setupUi(self.fenetre2)
        self.fenetre2.setProperty("value", 40)
        self.fenetre2.show()
        time.sleep(5)
        print("ok")
        dns1 = self.ui.lineEdit.text()
        import socket
        import os
        import html
        import whois
        f = open('template3.html', 'wb')
        ip = (socket.gethostbyname(dns1))

        import whois

        w = whois.whois(dns1)
        domain = (w.domain_name)
        regis = (w.registar)
        whois = (w.whois_server)
        referral = (w.referral_url)
        update = (w.updated_date)
        creation = (w.creation_date)
        expiration = (w.expiration_date)
        name = (w.name_servers)
        sta = (w.status)
        emails = (w.emails)
        dnssec = (w.dnssec)
        name = (w.name)
        org = (w.org)
        adress = (w.adress)
        city = (w.city)
        state = (w.state)
        zipcode = (w.zipcode)
        country = (w.country)
        import os
        import json
        import requests
        dno = ("http://" + dns1)
        r = requests.get(dno)  # http://nmap.org
        data1 = r.headers
        versions_srerver = (data1["server"])
        server = (versions_srerver)
        message = """<html>
                            <head></head>



                                            <h2 style="background-color: black;">
                                            <p style="color: black;font-size:15px;text-shadow: 1px 1px 1px red,2px 2px 1px red";><span><B> Informations Server Secondary : </B><p>
                                            <body><p><span style="color: green;font-size:15px"><B> DNS Versions Server : </B></span><span style="color: red;font-size:15px">{SERVER}</span></p></body
                                            <body><p><span style="color: green;font-size:15px"><B>DNS Ip Adress : </span><span style="color: red;font-size:15px">{IP}</B></span></p></body>
                                            <body><p><span style="color: green;font-size:15px"><B>DNS target : </span><span style="color: red;font-size:15px">{TARGET}</B></span></p></body>
                                            <body><p><span style="color: green;font-size:15px"><B>DNS registar : </span><span style="color: red;font-size:15px">{REGISTRAR}</B></span></p></body>
                                            <body><p><span style="color: green;font-size:15px"><B>DNS Whois_Server : </span><span style="color: red;font-size:15px">{WHOIS_SERVER}</B></span></p></body>
                                            <body><p><span style="color: green;font-size:15px"><B>DNS referral_url : </span><span style="color: red;font-size:15px" >{REFERRAL_URL}</B></span></p></body>
                                            <body><p><span style="color: green;font-size:15px"><B>DNS last_updated : </span><span style="color: red;font-size:15px">{LAST_UPDATED}</B></span></p></body>
                                            <body><p><span style="color: green;font-size:15px"><B>DNS Creation_date : </span><span style="color: red;font-size:15px">{CREATION}</B></span></p></body>
                                            <body><p><span style="color: green;font-size:15px"><B>DNS expiration_date : </span><span style="color: red;font-size:15px">{EXPIRATION}</B></span></p></body>
                                            <body><p><span style="color: green;font-size:15px"><B>DNS Name_Servers : </span><span style="color: red;font-size:15px">{NAME_SERVERS}</B></span></p></body>
                                            <body><p><span style="color: green;font-size:15px"><B>DNS status : </span><span style="color: red;font-size:15px">{STATUS}</B></span></p></body>
                                            <body><p><span style="color: green;font-size:15px"><B>DNS Emails : </span><span style="color: red;font-size:15px">{EMAILS}</B></span></p></body>
                                            <body><p><span style="color: green;font-size:15px"><B>DNS_secondary : </span><span style="color: red;font-size:15px">{DNSSEC}</B></span></p></body>
                                            <body><p><span style="color: green;font-size:15px"><B>DNS Name : </span><span style="color: red;font-size:15px">{NAME}</B></span></p></body>
                                            <body><p><span style="color: green;font-size:15px"><B>DNS Organisation : </span><span style="color: red;font-size:15px" >{ORGANISATION}</B></span></p></body>
                                            <body><p><span style="color: green;font-size:15px"><B>DNS Adress : </span><span style="color: red;font-size:15px">{ADRESS}</B></span></p></body>
                                            <body><p><span style="color: green;font-size:15px"><B>DNS City : </span><span style="color: red;font-size:15px">{CITY}</B></span></p></body>
                                            <body><p><span style="color: green;font-size:15px"><B>DNS State : </span><span style="color: red;font-size:15px">{STATE}</B></span></p></body>
                                            <body><p><span style="color: green;font-size:15px"><B>DNS Zip_Code : </span><span style="color: red;font-size:15px">{ZIPCODE}</B></span></p></body>
                                            <body><p><span style="color: green;font-size:15px"><B>DNS Country : </span><span style="color: red;font-size:15px">{COUNTRY}</B></span></p></body>

                                            </html>""".format(

            IP=ip,
            TARGET=domain,
            REGISTRAR=regis,
            WHOIS_SERVER=whois,
            REFERRAL_URL=referral,
            LAST_UPDATED=update,
            CREATION=creation,
            EXPIRATION=expiration,
            NAME_SERVERS=name,
            STATUS=state,
            EMAILS=emails,
            DNSSEC=dnssec,
            NAME=name,
            ORGANISATION=org,
            ADRESS=adress,
            CITY=city,
            STATE=state,
            ZIPCODE=zipcode,
            COUNTRY=country,
            SERVER=server,

        )
        print("ok")
        bytes = message.encode(encoding='UTF-8')
        f.write(bytes)
        f.close()
        self.ui2.progressBar.setProperty("value", 100)

class Ui_Dialog_board(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1192, 595)
        Dialog.setFixedSize(1192, 595)
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.webView = QWebView(Dialog)
        self.webView.setGeometry(QtCore.QRect(20, 50, 811, 281))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.webView_2 = QWebView(Dialog)
        self.webView_2.setGeometry(QtCore.QRect(870, 50, 300, 281))
        self.webView_2.setUrl(QtCore.QUrl("about:blank"))
        self.webView_2.setObjectName("webView_2")
        self.webView_3 = QWebView(Dialog)
        self.webView_3.setGeometry(QtCore.QRect(30, 380, 341, 200))
        self.webView_3.setUrl(QtCore.QUrl("about:blank"))
        self.webView_3.setObjectName("webView_3")
        self.webView_4 = QWebView(Dialog)
        self.webView_4.setGeometry(QtCore.QRect(430, 380, 341, 200))
        self.webView_4.setUrl(QtCore.QUrl("about:blank"))
        self.webView_4.setObjectName("webView_4")
        self.webView_5 = QWebView(Dialog)
        self.webView_5.setGeometry(QtCore.QRect(830, 380, 341, 200))
        self.webView_5.setUrl(QtCore.QUrl("about:blank"))
        self.webView_5.setObjectName("webView_5")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(280, 20, 251, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(970, 20, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(130, 350, 141, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(560, 350, 141, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(910, 350, 231, 20))
        self.label_5.setObjectName("label_5")
        current_dir = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(current_dir, "template1.html")  ## plan geo
        url = QUrl.fromLocalFile(filename)
        self.webView.setUrl(QtCore.QUrl(url))
        current_dir = os.path.dirname(os.path.realpath(__file__))
        filename2 = os.path.join(current_dir, "template.html")  ## plan report
        url2 = QUrl.fromLocalFile(filename2)
        self.webView_2.setUrl(QtCore.QUrl(url2))

        filename4 = os.path.join(current_dir,"template4.html")  ## plan geo
        url4 = QUrl.fromLocalFile(filename4)
        self.webView_4.setUrl(QtCore.QUrl(url4))

        filename3 = os.path.join(current_dir, "template3.html")  ## plan geo
        url3 = QUrl.fromLocalFile(filename3)
        self.webView_3.setUrl(QtCore.QUrl(url3))
        filename5 = os.path.join(current_dir, "template5.html")  ## plan geo
        url5 = QUrl.fromLocalFile(filename5)
        self.webView_5.setUrl(QtCore.QUrl(url5))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Recoon-Servers", "Recoon-Servers"))
        self.label.setText(_translate("Dialog",
                                      "<html><head/><body><p><span style=\" font-size:11pt; color:#55ff00;\">Geolocation Mapping Infos Servers</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:11pt; color:#55ff00;\">Infos Dns Server</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:11pt; color:#55ff00;\">Infos Servers MX</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:11pt; color:#55ff00;\">Infos Servers NS</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:11pt; color:#55ff00;\">Infos Brute Force SubDomains</span></p></body></html>"))








class Controller:
    def __init__(self):
        pass


    def Menu(self):
        self.fenetre1 = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.fenetre1)
        self.ui.pushButton.clicked.connect(self.action)
        self.fenetre1.show()


    def action(self):
        c = folium.Map(location=[46.078025, 6.409053], zoom_start=2, tiles='Stamen Toner')
        f_geo = open('template1.html', 'wb')
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Starting Report_DNS_General :", "green"))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            pass
        import os
        print(colored("[Recoon Servers Infos Gathering :] ", 'magenta'))

        dns1 = self.ui.lineEdit.text()
        import validators
        verifdns = (validators.domain(dns1))

        if verifdns == True:
            self.fenetre1.close()
            import socket
            import os
            import html
            import whois


            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Recoon-Servers')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='green', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            # Create text widget and specify size.
            T = Text(mGui, height=5, width=52)
            # Create label
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()

            mpb["value"] = 10
            mpb.update()

            f = open('template.html', 'wb')

            print((colored("|--> Starting Analyse Infos whois DNS :", 'green')), dns1)
            print(colored("|-->  ... [Loading] ... ", 'green'))
            print(colored("|--> Scanning Network ... ", 'green'))
            print((colored("|--> DNS :", "green")), dns1)

            ip = (socket.gethostbyname(dns1))

            import whois

            w = whois.whois(dns1)

            domain = (w.domain_name)
            regis = (w.registar)
            whois = (w.whois_server)
            referral = (w.referral_url)
            update = (w.updated_date)
            creation = (w.creation_date)
            expiration = (w.expiration_date)
            name = (w.name_servers)
            sta = (w.status)
            emails = (w.emails)
            dnssec = (w.dnssec)
            name = (w.name)
            org = (w.org)
            adress = (w.adress)
            city = (w.city)
            state = (w.state)
            zipcode = (w.zipcode)
            country = (w.country)
            import os
            import json
            import requests
            r = requests.get('http://nmap.org')
            data1 = r.headers
            versions_srerver = (data1["server"])
            server = (versions_srerver)
            mpb["value"] = 10
            mpb.update()

            message = """<html>
                                <head></head>



                                                <h2 style="background-color: black;">
                                                <p style="color: black;font-size:15px;text-shadow: 1px 1px 1px red,2px 2px 1px red";><span><B> Informations Server Secondary : </B><p>
                                                <body><p><span style="color: green;font-size:15px"><B> DNS Versions Server : </B></span><span style="color: red;font-size:15px">{SERVER}</span></p></body
                                                <body><p><span style="color: green;font-size:15px"><B>DNS Ip Adress : </span><span style="color: red;font-size:15px">{IP}</B></span></p></body>
                                                <body><p><span style="color: green;font-size:15px"><B>DNS target : </span><span style="color: red;font-size:15px">{TARGET}</B></span></p></body>
                                                <body><p><span style="color: green;font-size:15px"><B>DNS registar : </span><span style="color: red;font-size:15px">{REGISTRAR}</B></span></p></body>
                                                <body><p><span style="color: green;font-size:15px"><B>DNS Whois_Server : </span><span style="color: red;font-size:15px">{WHOIS_SERVER}</B></span></p></body>
                                                <body><p><span style="color: green;font-size:15px"><B>DNS referral_url : </span><span style="color: red;font-size:15px" >{REFERRAL_URL}</B></span></p></body>
                                                <body><p><span style="color: green;font-size:15px"><B>DNS last_updated : </span><span style="color: red;font-size:15px">{LAST_UPDATED}</B></span></p></body>
                                                <body><p><span style="color: green;font-size:15px"><B>DNS Creation_date : </span><span style="color: red;font-size:15px">{CREATION}</B></span></p></body>
                                                <body><p><span style="color: green;font-size:15px"><B>DNS expiration_date : </span><span style="color: red;font-size:15px">{EXPIRATION}</B></span></p></body>
                                                <body><p><span style="color: green;font-size:15px"><B>DNS Name_Servers : </span><span style="color: red;font-size:15px">{NAME_SERVERS}</B></span></p></body>
                                                <body><p><span style="color: green;font-size:15px"><B>DNS status : </span><span style="color: red;font-size:15px">{STATUS}</B></span></p></body>
                                                <body><p><span style="color: green;font-size:15px"><B>DNS Emails : </span><span style="color: red;font-size:15px">{EMAILS}</B></span></p></body>
                                                <body><p><span style="color: green;font-size:15px"><B>DNS_secondary : </span><span style="color: red;font-size:15px">{DNSSEC}</B></span></p></body>
                                                <body><p><span style="color: green;font-size:15px"><B>DNS Name : </span><span style="color: red;font-size:15px">{NAME}</B></span></p></body>
                                                <body><p><span style="color: green;font-size:15px"><B>DNS Organisation : </span><span style="color: red;font-size:15px" >{ORGANISATION}</B></span></p></body>
                                                <body><p><span style="color: green;font-size:15px"><B>DNS Adress : </span><span style="color: red;font-size:15px">{ADRESS}</B></span></p></body>
                                                <body><p><span style="color: green;font-size:15px"><B>DNS City : </span><span style="color: red;font-size:15px">{CITY}</B></span></p></body>
                                                <body><p><span style="color: green;font-size:15px"><B>DNS State : </span><span style="color: red;font-size:15px">{STATE}</B></span></p></body>
                                                <body><p><span style="color: green;font-size:15px"><B>DNS Zip_Code : </span><span style="color: red;font-size:15px">{ZIPCODE}</B></span></p></body>
                                                <body><p><span style="color: green;font-size:15px"><B>DNS Country : </span><span style="color: red;font-size:15px">{COUNTRY}</B></span></p></body>

                                                </html>""".format(

                IP=ip,
                TARGET=domain,
                REGISTRAR=regis,
                WHOIS_SERVER=whois,
                REFERRAL_URL=referral,
                LAST_UPDATED=update,
                CREATION=creation,
                EXPIRATION=expiration,
                NAME_SERVERS=name,
                STATUS=state,
                EMAILS=emails,
                DNSSEC=dnssec,
                NAME=name,
                ORGANISATION=org,
                ADRESS=adress,
                CITY=city,
                STATE=state,
                ZIPCODE=zipcode,
                COUNTRY=country,
                SERVER=server,

            )


            bytes = message.encode(encoding='UTF-8')
            f.write(bytes)
            f.close()
            addr1 = socket.gethostbyname(dns1)
            List_city1 = []
            List_region1 = []
            List_country1 = []
            List_lat1 = []
            List_lon1 = []
            datas_dns1 = DbIpCity.get(addr1, api_key='free')
            List_city1.append(datas_dns1.city)
            List_region1.append(datas_dns1.region)
            List_country1.append(datas_dns1.country)
            List_lat1.append(datas_dns1.latitude)
            List_lon1.append(datas_dns1.longitude)
            df1 = pd.DataFrame({'Server DNS': dns1, "Address IP  ": addr1, 'city': List_city1, 'region': List_region1,
                                '   country': List_country1, 'latitude': List_lat1, 'longitude': List_lon1})
            df1.set_index('Server DNS', inplace=True)
            html1 = df1.to_html().replace('<th>', '<th style = "color: red">').replace('<td>',
                                                                                       '<td style = "color: green">')

            locations1 = df1[['latitude', 'longitude']]
            locationlist1 = locations1.values.tolist()
            max1 = len(locationlist1)
            # c = folium.Map(location=[46.078025, 6.409053], zoom_start=2, tiles='Stamen Toner')

            popup_dns1 = """<html>
                                                            <head></head>

                                                            <body><p><span style="color: red">*DNS* : </span><span class="macouleur2">{TARGET}</span></p></body>
                                                            </html>""".format(
                TARGET=datas_dns1,
            )

            for item in locationlist1:
                folium.Marker(location=item, popup=popup_dns1,
                              tooltip='<p style="color:#FF0000";>* Informations Servers * click <p>',
                              icon=folium.features.CustomIcon('dns.png', icon_size=(30, 30))).add_to(c)
            # legend vue terrain
            folium.TileLayer('Stamen Terrain').add_to(c)
            folium.TileLayer('Stamen Toner').add_to(c)
            folium.TileLayer('Stamen Water Color').add_to(c)
            folium.TileLayer('cartodbpositron').add_to(c)
            folium.TileLayer('cartodbdark_matter').add_to(c)
            folium.LayerControl().add_to(c)
            c.save('maCarte_GPStest2.html')

            mpb["value"] = 30
            mpb.update()

            ###################

            #### NS server:
            import dns.name
            import dns.resolver
            n2 = dns.name.from_text(dns1)

            f = open('template4.html', 'wb')
            from tabulate import tabulate
            LTS_NS = []
            try:
                answer = dns.resolver.resolve(n2, 'NS')
            except dns.resolver.NoAnswer:
                print('|-----> [*] No answer NS ')
                print("no mx")
                no_RE_NS = ("Aucun enregistrement NS : " + dns1)
                message_No_NS = """<html>
                                                                   <head></head>
                                                                   <body style="background-color:white;">
                                                                   <body><p><span class="macouleur2"><B>{NO_RE_NS}</B></span></p></body>
                                                                   </html>""".format(
                    NO_RE_NS=no_RE_NS,
                )

                bytes_No_MX = message_No_NS.encode(encoding='UTF-8')
                f.write(bytes_No_MX)
                f.close()

            else:
                for x in dns.resolver.resolve(dns1, 'NS'):
                    NS = ([LTS_NS.append(x.to_text())])  # ok

                    tableau_mx = (tabulate([[m] for m in LTS_NS], tablefmt='html'))
                    df = pd.DataFrame({'Servers DNS': dns1, "Dns NS ": LTS_NS})
                    df.set_index('Servers DNS', inplace=True)
                    html = df.to_html(justify="center").replace('<th>',
                                                                '<th style = "color: red;font-size:14px">').replace(
                        '<td>', '<td style = "color: green;font-size:14px">')

                message_NS = """<html>
                                                                                            <head></head>
                                                                                            <body style="background-color:black;">
                                                                                            <center>
                                                                                            <body><p><span class="macouleur2"><B>{NS}</B></span></p></body>
                                                                                            </center>
                                                                                            </html>""".format(NS=html,

                                                                                                              )

                bytes_NS2 = message_NS.encode(encoding='UTF-8')
                f.write(bytes_NS2)
                f.close()
                list_ip = []
                for item in LTS_NS:
                    addr = socket.gethostbyname(item)
                    list_ip.append(addr)
                    pass
                List_city = []
                List_region = []
                List_country = []
                List_lat = []
                List_lon = []
                for item in list_ip:
                    response = DbIpCity.get(item, api_key='free')
                    List_city.append(response.city)
                    List_region.append(response.region)
                    List_country.append(response.country)
                    List_lat.append(response.latitude)
                    List_lon.append(response.longitude)
                    pass
                df2 = pd.DataFrame(
                    {'Servers DNS': LTS_NS, "Address IP  ": list_ip, 'city': List_city, 'region': List_region,
                     '   country': List_country, 'latitude': List_lat, 'longitude': List_lon})
                df2.set_index('Servers DNS', inplace=True)
                html2 = df2.to_html(justify="center").replace('<th>', '<th style = "color: red">').replace('<td>',
                                                                                                           '<td style = "color: green">')
                locations2 = df2[['latitude', 'longitude']]
                locationlist2 = locations2.values.tolist()
                max = len(locationlist2)  # compté les points associé au coordonnées > gps = 4

                # ---------------------------------- DNS 1 + dns(2) Multiple ------------------------------------------
                popup_dns2 = """<html>
                                                                                            <head></head>
                                                                                            <body><p><span style="color: red">*DNS* : </span><span class="macouleur2">{TARGET}</span></p></body>
                                                                                            </html>""".format(
                    TARGET=LTS_NS,
                )

                for item in locationlist2:
                    folium.Marker(location=item, popup=popup_dns2,
                                  tooltip='<p style="color:#FF0000";>* Informations Servers * click <p>',
                                  icon=folium.features.CustomIcon('dns2.png', icon_size=(30, 30))).add_to(c)
                    pass

                c.save('maCarte_GPStest2.html')
            message1 = """<html>
                                                                                              <head></head>





                                                                                              <iframe src=maCarte_GPStest2.html width=1200 height=450></iframe>

                                                                                              </html>""".format(

            )

            bytes = message1.encode(encoding='UTF-8')

            f_geo.write(bytes)
            f_geo.close()
            mpb["value"] = 50
            mpb.update()

            ################  mx #################
            f = open('template3.html', 'wb')
            from tabulate import tabulate
            import collections
            LTS_mx = []
            try:
                answer = dns.resolver.resolve(n2, 'MX')
            except dns.resolver.NoAnswer:
                print('|-----> [*] No answer MX ')
                print("no mx")
                no_RE_MX = ("Aucun enregistrement MX : " + dns1)
                message_No_MX = """<html>
                                                                       <head></head>
                                                                       <body style="background-color:white;">
                                                                       <body><p><span  class="macouleur2"><B>{NO_RE_MX}</B></span></p></body>
                                                                       </html>""".format(
                    NO_RE_MX=no_RE_MX,
                )

                bytes_No_MX = message_No_MX.encode(encoding='UTF-8')
                f.write(bytes_No_MX)
                f.close()

            else:
                for x in dns.resolver.resolve(dns1, 'MX'):
                    MX = ([LTS_mx.append(x.to_text())])  # ok
                    result = dns.resolver.resolve(dns1, 'MX')
                    for ipval in result:
                        #print('IP', ipval.to_text())
                        pass
                    tableau_mx = (tabulate([[m] for m in LTS_mx], tablefmt='html'))
                    df = pd.DataFrame({'Servers DNS': dns1, "Dns MX ": LTS_mx})
                    df.set_index('Servers DNS', inplace=True)
                    html = df.to_html(justify="center").replace('<th>',
                                                                '<th style = "color: red;font-size:13px">').replace(
                        '<td>', '<td style = "color: green;font-size:13px">')

                    message_MX2 = """<html>
                                                                                                                                                                <head></head>
                                                                                                                                                                <body style="background-color:black;">
                                                                                                                                                                <center>
                                                                                                                                                                <body><p><span class="macouleur2"><B>{MX}</B></span></p></body>
                                                                                                                                                                </center>
                                                                                                                                                                </html>""".format(
                        MX=html,

                    )
                    f = open('template3.html', 'wb')
                    bytes_MX2 = message_MX2.encode(encoding='UTF-8')
                    f.write(bytes_MX2)
                    f.close()
                mpb["value"] = 70
                mpb.update()

                ########## Subdomain ##########
                import time
                import nmap3
                import json
                f = open('template5.html', 'wb')

                nmap = nmap3.Nmap()
                results = nmap.nmap_dns_brute_script(dns1)
                #print(results)

                dump_results = json.dumps(results)
                subdomain = json.loads(dump_results)
                subdomains_list = []
                for item in subdomain:
                    SU = (item["hostname"])
                    subdomains_list.append(SU)
                    pass

                subadress_list = []
                for item in subdomain:
                    SU = (item["address"])
                    subadress_list.append(SU)
                    pass
                df = pd.DataFrame({'hostname': subdomains_list, 'adress IP': subadress_list})
                # dfs.set_index('',inplace=True) #retiré la colonnes des chiffres
                df.set_index('hostname', inplace=True)
                html = df.to_html().replace('<th>', '<th style = "color: red;font-size:14px">').replace(
                    '<td>', '<td style = "color: green;font-size:14px">')

                message_sub = """<html>
                                                                                            <head></head>
                                                                                                <body style="background-color:black;">
                                                                                                <body><p><span class="macouleur2"><B>{List_subdomains}</B></span></p></body>
                                                                                                </html>""".format(
                    List_subdomains=html,
                    )

                bytes_sub = message_sub.encode(encoding='UTF-8')
                f.write(bytes_sub)
                f.close()
                mpb["value"] = 100
                mpb.update()
                time.sleep(3)
                mGui.destroy()
                self.fenetre4 = QtWidgets.QDialog()
                self.ui = Ui_Dialog_board()
                self.ui.setupUi(self.fenetre4)
                self.fenetre4.show()


        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns1)
            self.fenetre1.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi(self.Dialog_error_dns)
            self.Dialog_error_dns.show()
            #self.fenetre1.show()







if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Controller = Controller()
    Controller.Menu()
    # Controller.fonctions()

    sys.exit(app.exec_())
