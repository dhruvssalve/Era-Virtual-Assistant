import this
from tkinter import filedialog

import notif as notif
from PyQt5.QtWidgets import *
from PyQt5 import uic


import smtplib
from email import encoders
from email.mime.text import  MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI,self).__init__()
        uic.loadUi("GmailGuinew.ui",self)
        self.show()

        self.pushButton1.clicked.connect(self.login)
        self.pushButton2.clicked.connect(self.attach_sth)
        self.pushButton3.clicked.connect(self.send_mail)


    def login(self):
        try:
            self.server = smtplib.SMTP(self.text3.text(), self.text4.text())
            self.server.ehlo()
            self.server.starttls()
            self.server.ehlo()
            self.server.login(self.text1.text(), self.text2.text())

            self.text1.setEnabled(False)
            self.text2.setEnabled(False)
            self.text3.setEnabled(False)
            self.text4.setEnabled(False)
            self.pushButton1.setEnabled(False)

            self.text5.setEnabled(True)
            self.text6.setEnabled(True)
            self.text7.setEnabled(True)
            self.pushButton2.setEnabled(True)
            self.pushButton3.setEnabled(True)

            self.msg = MIMEMultipart()

        except smtplib.SMTPAuthenticationError:
            message_box = QMessageBox()
            message_box.setText("Invalid Login Info!!!")
            message_box.exec()
        except :
            message_box = QMessageBox()
            message_box.setText("Login Failed")
            message_box.exec()



    def attach_sth(self):
        options = QFileDialog.Options()
        filenames, _ = QFileDialog.getOpenFileNames(self, "Open File", "", "All Files (*.*)", options=options)
        if filenames != []:
            for filename in filenames:
                attachment = open(filename, 'rb')

                filename = filename[filename.rfind("/") + 1:]

                p = MIMEBase('application', 'octet-stream')
                p.set_payload(attachment.read())
                encoders.encode_base64(p)
                p.add_header("Content-Disposition", f"attachment; filename={filename}")
                self.msg.attach(p)
                if not self.label10.text().endswith(":"):
                    self.label10.setText(self.label10.text() + ",")
                self.label10.setText(self.label10.text + " " + filename)


    def send_mail(self):
        dailog = QMessageBox()
        dailog.setText("Do you want to send this mail?")
        dailog.addButton(QPushButton("Yes"), QMessageBox.YesRole) # 0
        dailog.addButton(QPushButton("No"), QMessageBox.NoRole) # 1

        if dailog.exec_() == 0:
            try:
                self.msg['From'] = self.text1.text()
                self.msg['To'] = self.text5.text()
                self.msg['Subject'] = self.text6.text()
                self.msg.attach(MIMEText(self.text7.toPlainText(), 'plain'))
                text = self.msg.as_string()
                self.server.sendmail(self.text1.text(), self.text5.text(), text)
                message_box = QMessageBox()
                message_box.setText("Mail sent!!!")
                message_box.exec()
                self.destroy()
                

            except:
                message_box = QMessageBox()
                message_box.setText("Sending Mail Failed!!!")
                message_box.exec()

app = QApplication([])
window = MyGUI()
app.exec()