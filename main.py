from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from ui_layout import Ui_MainWindow
import sys
import time
sys.path.append('./modules')
from hubspotAPI import *
from hubspotPipeline import *
from googleAPI import *
from googlePipeline import *
from emailAPI import *
from emailPipeline import *
from PySide2 import QtXml

# deal_id = "2778886432" # one associated contact; deal of test account
# deal_id = "2386617450" # two associated contacts; deal of test account

'''
Note: On email page, remove from Recipient Email to Sign-off.
'''
class Thread1(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.deal_id = None
        self.loop = None
        self.data = None

    def run(self):
        self.loop.run_until_complete(self.fetchData())

    async def fetchData(self):
        self.data = None
        try:
            self.data = await getData(self.deal_id)
        except:
            pass
        
    def getDataFromThread1(self):
        return self.data

class Thread2(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.origin_file_link = None
        self.folder_link = None
        self.copy_title = None
        self.requests = None
        self.copy_link = None

    def run(self):
        self.copy_link = makeCopy(self.origin_file_link, self.folder_link, self.copy_title)
        populateData(self.copy_link, self.requests)
        
    def getCopyLinkFromThread2(self):
        return self.copy_link

class Thread3(QThread, Ui_MainWindow):
    def __init__(self):
        QThread.__init__(self)
        self.email_data = None
        self.label_11 = None
        self.headerData = None

    def run(self):
        try:
            session = smtplib.SMTP('smtp.gmail.com', 587) # Gmail port : 587
            session.starttls() # Enable security
            session.login(self.email_data["sender"], self.email_data["password"])
            download(self.email_data["google_docs_link"], self.email_data["pdf_file_name"])
            sendEmail(self.email_data, session)
            updateDealObject(self.headerData["quote_number"], self.email_data["google_docs_link"], "qualifiedtobuy")
            self.label_11.setText("Sent email")
        except:
            self.label_11.setText("Err: Something went wrong. Please try again.")

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Demo')
        self.home_btn.clicked.connect(self.handleDealButton), self.quote_btn.clicked.connect(self.handleQuoteButton), self.email_btn.clicked.connect(self.handleEmailButton), self.info_btn.clicked.connect(self.handleInfoButton)
        #self.setWindowIcon(QIcon('app_icon.png'))
        self.next_button.clicked.connect(self.handleNextButton)
        self.next_button_2.clicked.connect(self.handleNextButton2)
        self.next_button_3.clicked.connect(self.handleNextButton3)
        self.thread1 = Thread1()
        self.thread1.finished.connect(self.thread1Finished)
        self.thread2 = Thread2()
        self.thread2.finished.connect(self.thread2Finished)
        self.thread3 = Thread3()
        self.thread3.finished.connect(self.thread3Finished)
        self.deal_id = None
        self.data = None
        self.contact_objects = None
        self.contact_list = None
        self.loop = loop
        self.selected_id = None
        self.headerData = None
        self.template = {
            0: "https://docs.google.com/document/d/1mZ_W9r-cYIJLX2uC1A4x_IZMuw-QCyQHR3Q569WWLeA/edit#heading=h.7a9vzqcg994w", # industry
            1: "https://docs.google.com/document/d/1gIFAtkT0iF67w9Wz25kzFy7qxKgmvanAenfgDK9WV2o/edit#heading=h.7a9vzqcg994w", # education
            2: "https://docs.google.com/document/d/1v4z18_E4IPGIZSJ0HOCSDeMSAB8HZXO0-MjzTnqqguY/edit#heading=h.7a9vzqcg994w" # research center
        }
        self.folder_link = "https://drive.google.com/drive/u/0/folders/1k_Qsivs7Db6kPtg74k-SsH_x9zarq-Hd" # Quotes
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_4.setCurrentIndex(0)
        self.preparer_name = {0: "Albert Dunford",
            1: "Shannon Chesley",
            2: "Tricia Boer"
        }
        self.email_data = None


    def thread1Finished(self):
        try:
            temp = self.thread1.getDataFromThread1()
            self.contact_objects = temp["contact_objects"]
            #self.data = self.thread1.getDataFromThread1()
            #self.contact_objects = self.data["contact_objects"]
            self.contact_list = getContactList(self.contact_objects)
            #print("self.contact_list:\n{0}\n".format(self.contact_list))
            self.label_7.setText("")
            self.updateComboBox_2()
            self.label_5.setText("")
            self.textEdit.setText("")
            self.comboBox_3.setCurrentIndex(0)
            self.comboBox_4.setCurrentIndex(0)
            self.handleQuoteButton()
            self.data = temp
            #print("self.data:\n{0}\n".format(self.data))
        except:
            self.label_7.setText("Err: Invalid ID or network error. Please try again.")
        self.next_button.setEnabled(True)
        
    def handleNextButton(self):
        self.deal_id = str(self.lineEdit1.text())
        self.thread1.deal_id = self.deal_id
        if self.deal_id == "" or self.deal_id == " " or self.deal_id == None:
            self.label_7.setText("Err: Invalid ID or network error. Please try again.")
        else:
            if not self.thread1.isRunning():
                self.thread1.loop = self.loop
                self.next_button.setEnabled(False)
                self.label_7.setText("Fetching data...")
                self.thread1.start()
        print("next button clicked")
        return 0

    def thread2Finished(self):
        self.label_5.setText("")
        self.textEdit.setText(self.thread2.getCopyLinkFromThread2())
        self.next_button_2.setEnabled(True)
        '''
        Fill in Email part
        '''
        self.lineEdit_3.setText(getRecipientEmail(self.contact_objects, self.selected_id))
        self.lineEdit_4.setText(getCcEmailList(self.contact_objects, self.selected_id))
        self.lineEdit_8.setText(getSubjectName(self.headerData))
        self.lineEdit_9.setText(getAddressee(self.headerData))
        self.lineEdit_10.setText(getSignOff(self.headerData))
        self.textEdit_2.setText(self.thread2.getCopyLinkFromThread2())
        
    def handleNextButton2(self):
        if not self.thread2.isRunning():
            try:
                self.next_button_2.setEnabled(False)
                self.selected_id = list(self.contact_list.keys())[self.comboBox_2.currentIndex()]
                self.headerData = getHeaderData(self.data, self.selected_id)
                print(self.preparer_name[int(self.comboBox_4.currentIndex())])
                self.headerData["preparer_name"] = self.preparer_name[int(self.comboBox_4.currentIndex())]
                #print("self.headerData: {0}".format(self.headerData))
                origin_file_link = self.template[self.comboBox_3.currentIndex()]
                copy_title = makeCopyTitle(self.headerData)
                requests = makeRequests(self.headerData)
                self.thread2.origin_file_link = origin_file_link
                self.thread2.folder_link = self.folder_link
                self.thread2.copy_title = copy_title
                self.thread2.requests = requests
                self.label_5.setText("Creating a quote...")
                self.thread2.start()
            except:
                self.next_button_2.setEnabled(True)
                self.label_5.setText("Err: Something went wrong. Please try again.")
        print("next button2 clicked")
        return 0

    def thread3Finished(self):
        #self.label_11.setText("Sent email")
        self.next_button_3.setEnabled(True)

    def handleNextButton3(self):
        if not self.thread3.isRunning():
            print("handleNextButton3 clicked")
            self.email_data = {"sender": self.lineEdit.text().strip(),
                            "password": self.lineEdit_2.text().strip(),
                            "recipient": self.lineEdit_3.text().strip(),
                            "cc": [i.strip() for i in self.lineEdit_4.text().split(",") if i.strip() != ""],
                            "bcc": [i.strip() for i in self.lineEdit_5.text().split(",") if i.strip() != ""],
                            "reply_to": self.lineEdit_6.text().strip(),
                            "subject": self.lineEdit_8.text().strip(),
                            "addressee": self.lineEdit_9.text().strip(),
                            "sign_off": self.lineEdit_10.text().strip(),
                            "quote_email_template": "under_5000" if self.comboBox.currentIndex() == 0 else "over_5000",
                            "pdf_file_name": self.thread2.copy_title,
                            "google_docs_link": self.textEdit_2.toPlainText()
            }
            if self.email_data["sender"] != "" and self.email_data["password"] != "":
                try:
                    self.next_button_3.setEnabled(False)
                    self.label_11.setText("Please wait...")
                    self.thread3.email_data = self.email_data
                    self.thread3.headerData = self.headerData
                    self.thread3.label_11 = self.label_11
                    self.thread3.start()
                except:
                    self.next_button_3.setEnabled(True)
                    self.label_11.setText("Err: Something went wrong. Please try again.")
            else:
                self.label_11.setText("Err: Something went wrong. Please try again.")

    def updateComboBox_2(self):
        for i in range(0, self.comboBox_2.count()):
            self.comboBox_2.removeItem(0)
        for key in self.contact_list.keys():
            self.comboBox_2.addItem(self.contact_list[key])

    def handleDealButton(self):
        self.current.setText("Deal   ") # space = 3
        self.home_btn.setChecked(True), self.quote_btn.setChecked(False), self.email_btn.setChecked(False), self.info_btn.setChecked(False)
        print("Deal Button")
        self.stackedWidget.setCurrentIndex(0) # page 1

    def handleQuoteButton(self):
        self.current.setText("Quote   ") # space = 3
        self.home_btn.setChecked(False), self.quote_btn.setChecked(True), self.email_btn.setChecked(False), self.info_btn.setChecked(False)
        print("Quote Button")
        self.stackedWidget.setCurrentIndex(1) # page 2
    
    def handleEmailButton(self):
        self.current.setText("Email   ") # space = 3
        self.home_btn.setChecked(False), self.quote_btn.setChecked(False), self.email_btn.setChecked(True), self.info_btn.setChecked(False)
        print("Email Button")
        self.stackedWidget.setCurrentIndex(2) # page 3
    
    def handleInfoButton(self):
        self.current.setText("Information   ") # space = 3
        self.home_btn.setChecked(False), self.quote_btn.setChecked(False), self.email_btn.setChecked(False), self.info_btn.setChecked(True)
        print("Info Button")
        self.stackedWidget.setCurrentIndex(3) # page 4

app = QApplication(sys.argv)
form = Window()
form.show()
app.exec_()