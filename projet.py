from numpy import *
from numpy.linalg import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import QtCore

    
class Tab(QDialog):    # we have created a class tab that inherits the class QDialog
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Projet d'été")   #setWIndowTitle and setWindowIcon are methods of the class QDialog 
        self.setWindowIcon(QIcon("home.png")) 
        
        vbox = QVBoxLayout()
        self.tabWidget = QTabWidget()  # tabWidget est un attribut de classe de type QTabWidget 
        self.tabWidget.setFont(QtGui.QFont("Sanserif", 12))  # setFont and addTab are methods of the class QTabWidget() 
        self.tabWidget.addTab(CalculMatricielle(), "Calcul Matricielle") # we add a Tab of the type CalculMatricielle to the tabWidget 
        vbox.addWidget(self.tabWidget) # we add the tabWidget to vbox
        self.setLayout(vbox)
        
class CalculMatricielle(QDialog):  # we have created a class CalculMatricielle that inherits the class QDialog
    def __init__(self):
        super().__init__()
        self.CreateLayout() # execute the function 'CreateLayout'
        vbox = QVBoxLayout() # we create a qvboxLayout (a vertical layout)
        vbox.addWidget(self.groupBox) 
        self.label = QLabel(self)  #We created an attribute of the CalculMatricielle class (type QLabel) and assigned it to the variable label
        self.label.setFont(QtGui.QFont("Sanserif",15)) 
        self.label.setStyleSheet('color:blue')
        vbox.addWidget(self.label) # add the label to vbox
        button=QPushButton ( "suivant" ,self)  # we create a button named 'suivant'
        button.clicked.connect(self.openSecondDialog)  # we connected the button to openSecondDialog function
        vbox.addWidget(button)
    
        self.setLayout(vbox)
        self.show()    # show() is called to display the window
         
 
 
    def CreateLayout(self):
        self.groupBox = QGroupBox("Est ce que tu va faire une operation sur 1 ou 2 matrices ?") # we create a groupbox 
        self.groupBox.setFont(QtGui.QFont("Sanserif",13)) # text font size
        hboxLayout = QHBoxLayout() # we create a qhboxlayout ( a horizontal layout )
        self.radiobtn1 = QRadioButton("Une seule matrice") # we created first radio button and set to it a text ("une seule matrice")
        self.radiobtn1.setFont(QtGui.QFont("Sanserif", 13)) # text font size
        hboxLayout.addWidget(self.radiobtn1)  # add the button to hboxLayout
        self.radiobtn1.toggled.connect(self.onRadioBtn) # if you choose 'radiobtn1' we execute the function 'onRadioBtn'
        self.radiobtn2 = QRadioButton("Deux matrices") # we created second radio button and set to it a text ("Deux matrices")
        self.radiobtn2.setFont(QtGui.QFont("Sanserif", 13)) # text font size
        self.radiobtn2.toggled.connect(self.onRadioBtn) # if you choose 'radiobtn2' we execute the function 'onRadioBtn'
        hboxLayout.addWidget(self.radiobtn2)  # add the button to hboxLayout
        self.groupBox.setLayout(hboxLayout)  
 
 
    def openSecondDialog(self):
        if self.radiobtn1 .isChecked():  # if the radiobutton is checked
            self.mydialog=onematrice()  # if you choose the first radio ("un seul matrice") we move to the new dialog called mydialog(class onematrice)
        else:
            self.mydialog=twomatrice() # if you choose the second radio ("deux matrices") we move to the new dialog called mydialog (class twomatrice)

            
            
        tabdialog.close()    
        
      
        self.mydialog.show() # show the next Window chosen in the tabdialog window
            
            
    def onRadioBtn(self):
        radioBtn= self.sender() # radioBtn get the radiobutton that checked in CreateLayout function
        if radioBtn.isChecked():
            self.label.setText("Vous avez choisir de faire l'operation sur " + radioBtn.text()) # poster a text
            
            
            
        
class onematrice(QWidget):  # we have created a class onematrice that inherits the class QWidget
     def __init__(self, parent=None):
        super(onematrice,self).__init__(parent)
        self.title = "Dimension de la matrice"  # title of window
        self.top = 200  # the distnace between the window and the top 
        self.left = 300  # the distnace between the window and the left 
        self.width = 300  # the width of the window
        self.height = 300  # the height of the window
        self.setWindowIcon(QtGui.QIcon("matrice.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)  #setGeometry execute the geometry of the window
        vbox = QVBoxLayout()  # we create a qvboxLayout (a vertical layout)
        labelImage = QLabel(self)  #we create a label and we assigned it to the variable labelImage
        pixmap = QPixmap("backs1.jpg")
        
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)
        self.setLayout(vbox)
        self.textbox = QLineEdit(self)  # create a input text
        self.textbox.move(20, 20)  # move textbox compared the right and the top of window
        self.textbox.resize(280,40)  # dimension of textbox
        self.textbox.setPlaceholderText("Nombre de Lignes de matrice") # the first sentence showed on the textbox
        self.textbox1 = QLineEdit(self)  # create a input text
        self.textbox1.move(20, 70)  # move textbox1 compared the right and the top of window
        self.textbox1.resize(280,40)  # dimension of textbox1
        self.textbox1.setPlaceholderText("Nombre de Colonnes de matrice") # the first sentence showed on the textbox1
        button = QPushButton("suivant",self) # we create a button named 'suivant'
        button.clicked.connect(self.onclick)  # we connected the button to onclick function
        button1=QPushButton("précédant",self) # we create a button named 'précédant'
        button1.clicked.connect(self.onclick1)  # we connected the button to onclick1 function
        button1.move(20,120)
        button.move(140,120)
        self.show()
        
     def onclick(self):
         self.mydialog1=creatematrice()  # we move to the new dialog called  mydialog1 (class creatematrice)
         tabdialog.tabWidget.currentWidget().mydialog.close()  # we close the dialog called mydialog
         self.mydialog1.show
         
     def onclick1(self):
         tabdialog.tabWidget.currentWidget().mydialog.close()  # we close the  dialog called mydialog
         tabdialog.show()    
         
         
class twomatrice(QWidget):  # we have created a class twomatrice that inherits the class QWidget
     def __init__(self, parent=None):
        super(twomatrice,self).__init__(parent)
        self.title = "Dimension de deux matrices" # title of window
        self.top = 200  # the distance between the window and the top 
        self.left = 300  # the distance between the window and the left 
        self.width = 500 # the width of the window
        self.height = 500 # the height of the window
        self.setWindowIcon(QtGui.QIcon("matrice.png")) #setWIndowTitle and setWindowIcon are methods of the class QWidget 
        self.setWindowTitle(self.title)
        
        self.setGeometry(self.left, self.top, self.width, self.height)  #setGeometry execute the geometry of the window
        vbox = QVBoxLayout()  # we create a qvboxLayout (a vertical layout)
        labelImage = QLabel(self) #we create a label and we assigned it to the variable labelImage
        pixmap = QPixmap("backs1.jpg") 
        
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)
        self.setLayout(vbox)
        self.textbox = QLineEdit(self)  # create a input text
        self.textbox.move(20, 20) # move textbox compared the right and the top of window
        self.textbox.resize(280,40) # dimension of textbox
        self.textbox.setPlaceholderText("Nombre de Lignes de 1ere  matrice") # the first sentence showed on the textbox
        self.textbox1 = QLineEdit(self) # create a input text
        self.textbox1.move(20, 70)  # move textbox1 compared the right and the top of window
        self.textbox1.resize(280,40)  # dimension of textbox1
        self.textbox1.setPlaceholderText("Nombre de Colonnes de 1ere matrice")  # the first sentence showed on the textbox1
        self.textbox2 = QLineEdit(self) # create a input text
        self.textbox2.move(20, 130)  # move textbox2 compared the right and the top of window
        self.textbox2.resize(280,40)  # dimension of textbox2
        self.textbox2.setPlaceholderText("Nombre de Lignes de 2eme  matrice")  # the first sentence showed on the textbox2
        self.textbox3 = QLineEdit(self)  # create a input text
        self.textbox3.move(20, 180)   # move textbox3 compared the right and the top of window
        self.textbox3.resize(280,40)  # dimension of textbox3
        self.textbox3.setPlaceholderText("Nombre de Colonnes de 2eme  matrice") # the first sentence showed on the textbox3

        button = QPushButton("suivant",self)  # we create a button named 'suivant'
        button.clicked.connect(self.onclick)  # we connected the button to onclick function
       
        button1=QPushButton("précédant",self)    # we create a button named 'précédant'
        button1.clicked.connect(self.onclick1)   # we connected the button to onclick1 function
        
        button1.move(20,230)  # move button1 compared the right and the top of window
        button.move(140,230)  # move button compared the right and the top of window
        
        
        self.show()        
     def onclick(self):
         self.mydialog2=create2matrice() # we move to the new dialog called  mydialog2 (class create2matrice )
         tabdialog.tabWidget.currentWidget().mydialog.close() # we close the dialog called mydialog
         self.mydialog2.show
     def onclick1(self):
         tabdialog.tabWidget.currentWidget().mydialog.close() # we close the  dialog called mydialog
         tabdialog.show()       
         
         
         
class creatematrice(QWidget):# we have created a class creatematrice that inherits the class QWidget
    def __init__(self,parent=None):
        super(creatematrice,self).__init__(parent)
        self.title = "Operation sur une seule matrice" # title of window
        self.top = 200     # the distance between the window and the top 
        self.left = 300    # the distance between the window and the left
        self.width = 500    # the width of the window
        self.height = 500   # the height of the window
        self.setWindowIcon(QtGui.QIcon("operation.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)  #setGeometry execute the geometry of the window
        self.creatingTables()  # execute the function 'creatingTables'
        
        
        self.show()
    def creatingTables(self):
        self.tableWidget = QTableWidget() #we have created a matrice named tableWidget 
        self.tableWidget.setRowCount(int(tabdialog.tabWidget.currentWidget().mydialog.textbox.text())) # we set to  matrice the number  of rows  (inputted on the mydialog window)
        self.tableWidget.setColumnCount(int(tabdialog.tabWidget.currentWidget().mydialog.textbox1.text())) # we set  to matrice the number of columns (inputted on the mydialog window) 
        self.tableWidget.verticalHeader().hide()  #we hide the vertical and horizental header of the tableWidget 
        self.tableWidget.horizontalHeader().hide()
        
        
      
        button=QPushButton("suivant",self) #we create a button named 'suivant'
        button.clicked.connect(self.pushbutton)  #we connected the button to pushbutton function 
        button.setStyleSheet("background-color:#a69359") # we change the color of the button 
        button1=QPushButton("précédant",self)   # we create a button named 'précédant'
        button1.clicked.connect(self.pushbutton1) #we connected the button to pushbutton1 function
        button1.setStyleSheet("background-color:#a69359")# we change the color of the button
        self.vBoxLayout = QVBoxLayout()   # we create a qvboxLayout (a vertical layout)
        self.vBoxLayout.addWidget(self.tableWidget) # we add the matrice to the vboxlayout
        self.vBoxLayout.addWidget(button) # we add the two buttons to the vBoxLayout
        self.vBoxLayout.addWidget(button1)
        self.setLayout(self.vBoxLayout) 
        
    def pushbutton(self):
        self.window1=operation1()# we move to the new dialog called  window1 (class operation1)
        tabdialog.tabWidget.currentWidget().mydialog.mydialog1.close() #we close the dialog called mydialog1
        self.window1.show()
        
    def pushbutton1(self):
        tabdialog.tabWidget.currentWidget().mydialog.mydialog1.close() #we close the dialog called mydialog1
        tabdialog.tabWidget.currentWidget().mydialog.show()
        
class create2matrice(QWidget): # we have created a class create2matrice that inherits the class QWidget
    def __init__(self,parent=None):
        super(create2matrice,self).__init__(parent)
        self.title = "Operation sur deux matrice" # title of window
        self.top = 200    # the distance between the window and the top
        self.left = 300    # the distance between the window and the left
        self.width = 500   # the width of the window
        self.height = 500  # the height of the window
        self.setWindowIcon(QtGui.QIcon("operation.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)  #setGeometry execute the geometry of the window
        self.creatingTables() # execute the function 'creatingTables'
        vbox = QVBoxLayout()   # we create a qvboxLayout (a vertical layout)
        button=QPushButton("suivant",self)  #we create a button named 'suivant'
        button.clicked.connect(self.pushbutton)  #we connected the button to pushbutton function 
        button.setStyleSheet("background-color:#a69359") # we change the color of the button
        button1=QPushButton("précédant",self)#we create a button named 'précédant'
        button1.clicked.connect(self.pushbutton1) #we connected the button to pushbutton1 function 
        button1.setStyleSheet("background-color:#a69359") # we change the color of the button
        vbox.addWidget(self.groupbox1)  #we add the two groupbox to the vbox
        vbox.addWidget(self.groupbox2)
        vbox.addWidget(button)   #we add the two buttons to the vbox
        vbox.addWidget(button1)
        self.setLayout(vbox)
        
        self.show()
    def creatingTables(self):
        self.groupbox1=QGroupBox("1ere matrice") #we create a groupbox1
        self.tableWidget1 = QTableWidget() #we have created first matrice named tableWidget1
        self.tableWidget1.setRowCount(int(tabdialog.tabWidget.currentWidget().mydialog.textbox.text())) # we set to  matrice the number  of rows  (inputted on the mydialog window)
        self.tableWidget1.setColumnCount(int(tabdialog.tabWidget.currentWidget().mydialog.textbox1.text()))  # we set  to matrice the number of columns (inputted on the mydialog window)
        self.tableWidget1.verticalHeader().hide()
        self.tableWidget1.horizontalHeader().hide()#we hide the vertical and horizental header of the tableWidget1
        self.groupbox2=QGroupBox("2ème matrice") #we create a groupbox2
        self.tableWidget2 = QTableWidget() #we have created first matrice named tableWidget2
        self.tableWidget2.setRowCount(int(tabdialog.tabWidget.currentWidget().mydialog.textbox2.text())) # we set to  matrice the number  of rows  (inputted on the mydialog window)
        self.tableWidget2.setColumnCount(int(tabdialog.tabWidget.currentWidget().mydialog.textbox3.text())) # we set  to matrice the number of columns (inputted on the mydialog window)
        self.tableWidget2.verticalHeader().hide() #we hide the vertical and horizental header of the tableWidget1
        self.tableWidget2.horizontalHeader().hide()
    
        
        self.hBoxLayout1 = QHBoxLayout() # we create a qhboxLayout (a horizontal layout) named hBoxLayout1
        self.hBoxLayout1.addWidget(self.tableWidget1) # we add the first matrice to the hboxlayout1
        self.groupbox1.setLayout(self.hBoxLayout1) # we set the hboxlayout1 to the groupbox1
        
        
        self.hBoxLayout2=QHBoxLayout() # we create a qhboxLayout (a horizontal layout) named hBoxLayout2
        self.hBoxLayout2.addWidget(self.tableWidget2)  # we add the second matrice to the hboxlayout2
    
        self.groupbox2.setLayout(self.hBoxLayout2) # we set the hboxlayout2 to the groupbox2
        
        
    def pushbutton(self):
        self.window2=operation2() # we move to the new dialog called window2 (class operation2)
        tabdialog.tabWidget.currentWidget().mydialog.mydialog2.close()  #we close the dialog called mydialog2
        self.window2.show()
    def pushbutton1(self):
        tabdialog.tabWidget.currentWidget().mydialog.mydialog2.close() #we close the dialog called mydialog2
        tabdialog.tabWidget.currentWidget().mydialog.show()         
         
         
         
class operation1(QWidget): # we have created a class operation1 that inherits the class QWidget
    def __init__(self, parent=None):
        super(operation1,self).__init__(parent)
        self.title = "Operation sur une seule matrice" # title of window
        self.top = 200    # the distance between the window and the top
        self.left = 300    # the distance between the window and the left
        self.width = 500   # the width of the window
        self.height = 500  # the height of the window
        self.setWindowIcon(QtGui.QIcon("operation.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height) #setGeometry execute the geometry of the window
        vbox = QVBoxLayout() # we create a QVBOxLAyout (a vertical layout)
        self.groupBox = QGroupBox("Les operations") # we create a GroupBox
        vbox.addWidget(self.groupBox) # we add the groupbox to the vboxlayout
        self.setLayout(vbox)
        gridLayout = QGridLayout() # we created a gridlayout


        button1 = QPushButton("inverse d'une matrice",self) # we create a button named 'inverse d'une matrice'
        button1.setIcon(QtGui.QIcon("inverse.png")) # we set an icon to the button
        button1.setIconSize(QtCore.QSize(40,40))
        button1.setMinimumHeight(40)
        button1.clicked.connect(self.inverse) # we connect the button1 to inverse function
        gridLayout.addWidget(button1,0,0) # add  button1 at specified row and column ( row=0 and column=0)
        button2 = QPushButton("transposeé d'une matrice",self)  # we create a button named 'transposeé d'une matrice'
        button2.setIcon(QtGui.QIcon("transpose.png"))
        button2.setIconSize(QtCore.QSize(40,40))
        button2.setMinimumHeight(40)
        button2.clicked.connect(self.transpose) # we connect the button2 to transpose function
        gridLayout.addWidget(button2,1,0) # add button2 at specified row and column ( row=1 and column=0)
        button3 = QPushButton("trace d'une matrice",self)  # we create a button named 'trace d'une matrice'
        button3.setIcon(QtGui.QIcon("trace.png"))
        button3.setIconSize(QtCore.QSize(40,40))
        button3.setMinimumHeight(40)
        button3.clicked.connect(self.trace) # we connect the button3 to trace function
        gridLayout.addWidget(button3,2,0) # add button3 at specified row and column ( row=2 and column=0)
        button4=QPushButton("précédant",self)
        button4.setStyleSheet("background-color:#a69359")
        button4.clicked.connect(self.back) # we connect  the button4 to back function
        gridLayout.addWidget(button4,3,0) #♦add button4 at specified row and column (row=3 and column=0)
        
        
        self.groupBox.setLayout(gridLayout) # we set the gridlayout to the groupbox
       
        
        self.show()
        
    def back(self):
        tabdialog.tabWidget.currentWidget().mydialog.mydialog1.window1.close() # we close the dialog called window1
        tabdialog.tabWidget.currentWidget().mydialog.mydialog1.show()
        
    def inverse(self):
        L=int(tabdialog.tabWidget.currentWidget().mydialog.textbox.text()) # we assigned the number of rows of tableWidget inputted in mydialog window  to the variable L
        C=int(tabdialog.tabWidget.currentWidget().mydialog.textbox1.text())  # we assigned the number of columns of tableWidget inputted in mydialog window  to the variable C
        
        M1=tabdialog.tabWidget.currentWidget().mydialog.mydialog1.tableWidget # we assigned the tableWidget inputted in mydialog1 window to M1
        M2=empty((L,C)) #we create an empty matrice named M2
        self.M3=empty((L,C)) # we assigned an empty matrice to the attribut of class M3
        for i in range (L):
            for j in range (C):
                M2[i][j]=int(M1.item(i,j).text()) # we put the value inputted in M1 on the new matrice M2 to facilitate the acces to this values 
                
        if (L==C):
            if det( M2) !=0:  # if determinant of M2 ≠ 0
                self.M3=inv(M2) # we set the inverse of M2 to M3
                        
            
                self.inversewindow=inversewindow()    # we move to the new dialog called inversewindow ( class inversewindow)
            
            else:
                self.inversewindow=inversewindow1()  # we move to the new dialog called inversewindow ( class inversewindow1)
                
        else:
            self.inversewindow=inversewindow2()   # we move to the new dialog called inversewindow (class inversewindow2)
        
        tabdialog.tabWidget.currentWidget().mydialog.mydialog1.window1.close()     #we close the dialog called window1        
        self.inversewindow.show() 
        
    def transpose(self):
        L=int(tabdialog.tabWidget.currentWidget().mydialog.textbox.text()) # we assigned the number of rows of tableWidget inputted in mydialog window  to the variable L
        C=int(tabdialog.tabWidget.currentWidget().mydialog.textbox1.text())  # we assigned the number of columns of tableWidget inputted in mydialog window  to the variable C
        
        M1=tabdialog.tabWidget.currentWidget().mydialog.mydialog1.tableWidget # we assigned the tableWidget inputted in mydialog1 window to M1

        self.M3=empty((C,L))  # we assigned an empty matrice to the attribut of class M3
        M2=empty((L,C))  #we create an empty matrice named M2
        for i in range (L):
            for j in range (C):
                M2[i][j]=int(M1.item(i,j).text())  # we put the value inputted in M1 on the new matrice M2 to facilitate the acces to this values 
        
        self.M3=M2.transpose() # we set the transpose of M2 to M3
                
        
                 
        self.transposewindow=transposewindow() # we move to the new dialog called transposewindow (class transpodewindow)
        
        tabdialog.tabWidget.currentWidget().mydialog.mydialog1.window1.close() #we close the dialog called window1
        self.transposewindow.show() 
        
    def trace(self):
        L=int(tabdialog.tabWidget.currentWidget().mydialog.textbox.text()) # we assigned the number of rows of tableWidget inputted in mydialog window  to the variable L
        C=int(tabdialog.tabWidget.currentWidget().mydialog.textbox1.text()) # we assigned the number of columns of tableWidget inputted in mydialog window  to the variable C
        
        M1=tabdialog.tabWidget.currentWidget().mydialog.mydialog1.tableWidget # we assigned the tableWidget inputted in mydialog1 window to M1
        
    
        self.t=0  # we assigned a 0 to the attribut of class t
        if (L==C):
            for i in range (L):
                self.t=self.t+int(M1.item(i,i).text())
            
            self.tracewindow=tracewindow() # we move to the new dialog called tracewindow (class tracewindow)
            
            
        
        else:
            self.tracewindow=tracewindow1() # we move to the new dialog called tracewindow (class tracewindow1)
            
        tabdialog.tabWidget.currentWidget().mydialog.mydialog1.window1.close()  #we close the dialog called window1           
        self.tracewindow.show()    
        
        
            
        
        
        
        
class operation2(QWidget):
    def __init__(self,parent=None):
        super(operation2,self).__init__(parent)
        self.title = "Operation sur deux matrices" # title of window
        self.top = 200    # the distance between the window and the top
        self.left = 300    # the distance between the window and the left
        self.width = 500   # the width of the window
        self.height = 500  # the height of the window
        self.setWindowIcon(QtGui.QIcon("operation.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)  #setGeometry execute the geometry of the window
        vbox = QVBoxLayout() # we create a QVBoxLayout named vbox
        self.groupBox = QGroupBox("Les operations") # we create a groupbox
        vbox.addWidget(self.groupBox) #we add the groupbox to vbox
        self.setLayout(vbox)
        gridLayout = QGridLayout() #we create a gridlayout


        button1 = QPushButton("addition de deux matrices",self) #we create a button named "addition de deux matrices"
        button1.setIcon(QtGui.QIcon("addition.png"))
        button1.setIconSize(QtCore.QSize(40,40))
        button1.setMinimumHeight(40)
        button1.clicked.connect(self.addition) # we connect the button1 to addition function
        gridLayout.addWidget(button1,0,0) # we add button1 to specified row and column( row=0 and column=0)
        button2 = QPushButton("produit de deux matrice",self)# we create a button named ' produit de deux matrices'
        button2.setIcon(QtGui.QIcon("produit.png"))
        button2.setIconSize(QtCore.QSize(40,40))
        button2.setMinimumHeight(40)
        button2.clicked.connect(self.produit) # we connect the button2 to produit function
        gridLayout.addWidget(button2,1,0) # we add button2 to specified row and column (row =1 and column=0)
        button3=QPushButton("précédant",self) # we create a button named 'précédant'
        button3.setStyleSheet("background-color:#a69359")
        button3.clicked.connect(self.back) # we connect the button3 to back function
        gridLayout.addWidget(button3,2,0)  # we add button 3 to specified row and column (row =2 and column=0)
        self.groupBox.setLayout(gridLayout) #we set the gridlayout to the groupbox
        self.show()
        
    def back(self):
        tabdialog.tabWidget.currentWidget().mydialog.mydialog2.window2.close() # we close the dialog called window2
        tabdialog.tabWidget.currentWidget().mydialog.mydialog2.show()
        
    def produit(self):
       L1=int(tabdialog.tabWidget.currentWidget().mydialog.textbox.text())  # we assigned the number of rows of tableWidget1 inputted in mydialog window  to the variable L1
       C1=int(tabdialog.tabWidget.currentWidget().mydialog.textbox1.text())   # we assigned the number of columnss of tableWidget1 inputted in mydialog window  to the variable C1
       L2=int(tabdialog.tabWidget.currentWidget().mydialog.textbox2.text())  # we assigned the number of rows of tableWidget2 inputted in mydialog window  to the variable L2
       C2=int(tabdialog.tabWidget.currentWidget().mydialog.textbox3.text())   # we assigned the number of columnss of tableWidget2 inputted in mydialog window  to the variable C2
       mat1=tabdialog.tabWidget.currentWidget().mydialog.mydialog2.tableWidget1# we assigned the tableWidget1 inputted in mydialog2 window to mat1
       mat2=tabdialog.tabWidget.currentWidget().mydialog.mydialog2.tableWidget2# we assigned the tableWidget2 inputted in mydialog2 window to mat2
       M1=empty((L1,C1)) #we create an empty matrice named M1
         
       for i in range (L1):
           for j in range (C1):
               M1[i][j]=int(mat1.item(i,j).text()) # we put the value inputted in mat1 on the new matrice M1 to facilitate the acces to this values
       
       
       M2=empty((L2,C2)) #we create an empty matrice named M2
       for i in range (L2):
           for j in range (C2):
               M2[i][j]=int(mat2.item(i,j).text())   # we put the value inputted in mat2 on the new matrice M2 to facilitate the acces to this values      
        
       if (C1==L2):
           self.M3=empty((L1,C2))  # we assigned an empty matrice to the attribut of class M3
           for i in range (L1):
                for j in range (C2):
                    self.M3[i][j]=0
                    for k in range (C1):
                        self.M3[i][j]=M1[i][k]*M2[k][j]+self.M3[i][j]
                        
           self.produitwindow=produitwindow() #we move to the new dialog called produitwindow(class produitwindow)
           
       else: 
           self.produitwindow=produitwindow1() #we move to the new dialog called produitwindow(class produitwindow1)
           
       tabdialog.tabWidget.currentWidget().mydialog.mydialog2.window2.close()    # we close the dialog called window2        
       self.produitwindow.show()    
             
        
      
    def addition(self):
       L1=int(tabdialog.tabWidget.currentWidget().mydialog.textbox.text())# we assigned the number of rows of tableWidget1 inputted in mydialog window  to the variable L1
       C1=int(tabdialog.tabWidget.currentWidget().mydialog.textbox1.text())# we assigned the number of columnss of tableWidget1 inputted in mydialog window  to the variable C1
       L2=int(tabdialog.tabWidget.currentWidget().mydialog.textbox2.text())# we assigned the number of rows of tableWidget2 inputted in mydialog window  to the variable L2
       C2=int(tabdialog.tabWidget.currentWidget().mydialog.textbox3.text()) # we assigned the number of columnss of tableWidget2 inputted in mydialog window  to the variable C2
       mat1=tabdialog.tabWidget.currentWidget().mydialog.mydialog2.tableWidget1 # we assigned the tableWidget1 inputted in mydialog2 window to mat1
       mat2=tabdialog.tabWidget.currentWidget().mydialog.mydialog2.tableWidget2 # we assigned the tableWidget2 inputted in mydialog2 window to mat2
       M1=empty((L1,C1))#we create an empty matrice named M1
         
       for i in range (L1):
           for j in range (C1):
               M1[i][j]=int(mat1.item(i,j).text())# we put the value inputted in mat1 on the new matrice M1 to facilitate the acces to this values  
       
       
       M2=empty((L2,C2))#we create an empty matrice named M2
       for i in range (L2):
           for j in range (C2):
               M2[i][j]=int(mat2.item(i,j).text())# we put the value inputted in mat2 on the new matrice M2 to facilitate the acces to this values  
       
       if (L1==L2 and C1==C2):
           self.M3=empty((L1,C1))
           for i in range (L1):
               for j in range (C1):
                   self.M3[i][j]=M1[i][j]+M2[i][j]
                  
                   
           self.additionwindow=additionwindow()#we move to the new dialog called additionwindow(class additionwindow)
       else:
           self.additionwindow=additionwindow1()#we move to the new dialog called additionwindow(class additionwindow1)
           
           
       tabdialog.tabWidget.currentWidget().mydialog.mydialog2.window2.close() #we close the dialog called window2        
       self.additionwindow.show() 

class transposewindow(QWidget):
    def __init__(self,parent=None):
        super(transposewindow,self).__init__(parent)
        self.title = " transposeé d'une matrice" #title of window
        self.top = 200    # the distance between the window and the top
        self.left = 300    # the distance between the window and the left
        self.width = 500   # the width of the window
        self.height = 500  # the height of the window
        self.setWindowIcon(QtGui.QIcon("transpose.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height) #setGeometry execute the geometry of the window
        vbox=QVBoxLayout()  # we create a QVBoxLayout named vbox
        self.tableWidget = QTableWidget() # we create a tablewidget 
        self.tableWidget.setRowCount(int(tabdialog.tabWidget.currentWidget().mydialog.textbox1.text()))
        self.tableWidget.setColumnCount(int(tabdialog.tabWidget.currentWidget().mydialog.textbox.text()))# we set the number of columns and rows for the tableWidget
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.horizontalHeader().hide() #we hide the vertical and horizontal header of the tableWidget
        M4=tabdialog.tabWidget.currentWidget().mydialog.mydialog1.window1.M3 # we assigned the matrix M3 (created in the class operation1) to M4

        for i in range (shape(M4)[0]):
            for j in range(shape(M4)[1]):
                 self.tableWidget.setItem(i,j,QTableWidgetItem(str(M4[i][j])))
        
        vbox.addWidget(self.tableWidget)
        button=QPushButton("précédant",self) # we create a button named précédant
        button.clicked.connect(self.back) #we connect the button to back function
        button.setStyleSheet("background-color:#a69359")
        vbox.addWidget(button)
        self.setLayout(vbox)
        self.show()
    def back(self):
        tabdialog.tabWidget.currentWidget().mydialog.mydialog1.window1.transposewindow.close() # we close the dialog called transposewindow
        tabdialog.tabWidget.currentWidget().mydialog.mydialog1.window1.show()     

class tracewindow(QWidget):
    def __init__(self,parent=None):
        super(tracewindow,self).__init__(parent)
        self.title = "Trace d'une matrice" #title of window
        self.top = 200    # the distance between the window and the top
        self.left = 300    # the distance between the window and the left
        self.width = 500   # the width of the window
        self.height = 500  # the height of the window
        self.setWindowIcon(QtGui.QIcon("trace.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height) #setGeometry execute the geometry of the window
        vbox = QVBoxLayout()  # we create a QVBoxLayout named vbox
        label=QLabel(str(tabdialog.tabWidget.currentWidget().mydialog.mydialog1.window1.t))
        label.setFont(QtGui.QFont("Sanserif",25))
        vbox.addWidget(label)
        button=QPushButton("précédant",self)  # we create a button named précédant
        button.setStyleSheet("background-color:#a69359")
        button.clicked.connect(self.back) #we connect the button to back function
        vbox.addWidget(button)
        self.setLayout(vbox)
        self.show()
        
    def back(self):
        tabdialog.tabWidget.currentWidget().mydialog.mydialog1.window1.tracewindow.close() # we close the dialog called tracewindow
        tabdialog.tabWidget.currentWidget().mydialog.mydialog1.window1.show()    
        
class tracewindow1(QWidget):
    def __init__(self,parent=None):
        super(tracewindow1,self).__init__(parent)
        self.title = "Trace d'une matrice" #title of window
        self.top = 200    # the distance between the window and the top
        self.left = 300    # the distance between the window and the left
        self.width = 500   # the width of the window
        self.height = 500  # the height of the window
        self.setWindowIcon(QtGui.QIcon("trace.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height) #setGeometry execute the geometry of the window
        vbox = QVBoxLayout()  # we create a QVBoxLayout named vbox
        label=QLabel("nombre de ligne != nombre de colonne donc on ne peut pas calculer le trace")
        label.setFont(QtGui.QFont("Sanserif",25))
        vbox.addWidget(label)
        button=QPushButton("précédant",self)  # we create a button named précédant
        button.setStyleSheet("background-color:#a69359")
        button.clicked.connect(self.back) #we connect the button to back function
        vbox.addWidget(button)
        self.setLayout(vbox)
        self.show()
    def back(self):
        tabdialog.tabWidget.currentWidget().mydialog.mydialog1.window1.tracewindow.close() # we close the dialog called tracewindow
        tabdialog.tabWidget.currentWidget().mydialog.mydialog1.window1.show()
        
        
class inversewindow2(QWidget):
    def __init__(self,parent=None):
        super(inversewindow2,self).__init__(parent)
        self.title = "Inverse d'une matrice" #title of window
        self.top = 200    # the distance between the window and the top
        self.left = 300    # the distance between the window and the left
        self.width = 500   # the width of the window
        self.height = 500  # the height of the window
        self.setWindowIcon(QtGui.QIcon("inverse.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height) #setGeometry execute the geometry of the window
        vbox = QVBoxLayout()  # we create a QVBoxLayout named vbox
        label=QLabel("matrice non carré")
        label.setFont(QtGui.QFont("Sanserif",25))
        vbox.addWidget(label)
        button=QPushButton("précédant",self)  # we create a button named précédant
        button.setStyleSheet("background-color:#a69359")
        button.clicked.connect(self.back) #we connect the button to back function
        vbox.addWidget(button)
        self.setLayout(vbox)
        self.show()        

    def back(self):
        tabdialog.tabWidget.currentWidget().mydialog.mydialog1.window1.inversewindow.close() # we close the dialog called inversewindow
        tabdialog.tabWidget.currentWidget().mydialog.mydialog1.window1.show()
    

class inversewindow(QWidget):
    def __init__(self,parent=None):
        super(inversewindow,self).__init__(parent)
        self.title = "Invere d'une matrice" #title of window
        self.top = 200    # the distance between the window and the top
        self.left = 300    # the distance between the window and the left
        self.width = 500   # the width of the window
        self.height = 500  # the height of the window
        self.setWindowIcon(QtGui.QIcon("inverse.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height) #setGeometry execute the geometry of the window
        vbox=QVBoxLayout()  # we create a QVBoxLayout named vbox
        self.tableWidget = QTableWidget() # we create a tablewidget
        self.tableWidget.setRowCount(int(tabdialog.tabWidget.currentWidget().mydialog.textbox.text()))
        self.tableWidget.setColumnCount(int(tabdialog.tabWidget.currentWidget().mydialog.textbox1.text())) # we set the number of columns and rows for the tableWidget
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.horizontalHeader().hide() #we hide the vertical and horizontal header of the tableWidget
        M4=tabdialog.tabWidget.currentWidget().mydialog.mydialog1.window1.M3 # we assigned the matrix M3 (created in the class operation1) to M4

        for i in range (shape(M4)[0]):
            for j in range(shape(M4)[1]):
                 self.tableWidget.setItem(i,j,QTableWidgetItem(str(M4[i][j])))
        
        vbox.addWidget(self.tableWidget)
        button=QPushButton("précédant",self)  # we create a button named précédant
        button.setStyleSheet("background-color:#a69359")
        button.clicked.connect(self.back) #we connect the button to back function
        vbox.addWidget(button)
        self.setLayout(vbox)
        self.show() 
        
    def back(self):
        tabdialog.tabWidget.currentWidget().mydialog.mydialog1.window1.inversewindow.close() # we close the dialog called inversewindow
        tabdialog.tabWidget.currentWidget().mydialog.mydialog1.window1.show()   
        
        
class inversewindow1(QWidget):    
     def __init__(self,parent=None):
        super(inversewindow1,self).__init__(parent)
        self.title = "Inverse d'une matrice" #title of window
        self.top = 200    # the distance between the window and the top
        self.left = 300    # the distance between the window and the left
        self.width = 500   # the width of the window
        self.height = 500  # the height of the window
        self.setWindowIcon(QtGui.QIcon("inverse.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height) #setGeometry execute the geometry of the window
        vbox = QVBoxLayout()  # we create a QVBoxLayout named vbox
        label=QLabel("matrice non inversible")
        label.setFont(QtGui.QFont("Sanserif",25))
        vbox.addWidget(label)
        button=QPushButton("précédant",self)  # we create a button named précédant
        button.setStyleSheet("background-color:#a69359")
        button.clicked.connect(self.back) #we connect the button to back function
        vbox.addWidget(button)
        self.setLayout(vbox)
        self.show()
        
     def back(self):
         tabdialog.tabWidget.currentWidget().mydialog.mydialog1.window1.inversewindow.close() # we close the dialog called inversewindow
         tabdialog.tabWidget.currentWidget().mydialog.mydialog1.window1.show()         
    
class produitwindow(QWidget):
    def __init__(self,parent=None):
        super(produitwindow,self).__init__(parent)
        self.title ="Produit matricielle" #title of window
        self.top = 200    # the distance between the window and the top
        self.left = 300    # the distance between the window and the left
        self.width = 500   # the width of the window
        self.height = 500  # the height of the window
        self.setWindowIcon(QtGui.QIcon("produit.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height) #setGeometry execute the geometry of the window
        vbox=QVBoxLayout()  # we create a QVBoxLayout named vbox
        self.tableWidget = QTableWidget() # we create a tablewidget
        self.tableWidget.setRowCount(int(tabdialog.tabWidget.currentWidget().mydialog.textbox.text()))
        self.tableWidget.setColumnCount(int(tabdialog.tabWidget.currentWidget().mydialog.textbox3.text()))# we set the number of columns and rows for the tableWidget
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.horizontalHeader().hide() #we hide the vertical and horizontal header of the tableWidget
        M4=tabdialog.tabWidget.currentWidget().mydialog.mydialog2.window2.M3 # we assigned the matrix M3 (created in the class operation2) to M4

        for i in range (shape(M4)[0]):
            for j in range(shape(M4)[1]):
                 self.tableWidget.setItem(i,j,QTableWidgetItem(str(M4[i][j])))
        
        vbox.addWidget(self.tableWidget)
        button=QPushButton("précédant",self)  # we create a button named précédant
        button.setStyleSheet("background-color:#a69359")
        button.clicked.connect(self.back) #we connect the button to back function
        vbox.addWidget(button)
        self.setLayout(vbox)
        self.show()
        
    def back(self):
        tabdialog.tabWidget.currentWidget().mydialog.mydialog2.window2.produitwindow.close() # we close the dialog called produitwindow
        tabdialog.tabWidget.currentWidget().mydialog.mydialog2.window2.show()
        
        
class produitwindow1(QWidget):
    def __init__(self,parent=None):
        super(produitwindow1,self).__init__(parent)
        self.title = "Produit matricielle" #title of window
        self.top = 200    # the distance between the window and the top
        self.left = 300    # the distance between the window and the left
        self.width = 500   # the width of the window
        self.height = 500  # the height of the window
        self.setWindowIcon(QtGui.QIcon("produit.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height) #setGeometry execute the geometry of the window
        vbox = QVBoxLayout()  # we create a QVBoxLayout named vbox
        label=QLabel("on ne peut pas faire le produit de ces deux matrices car nombre de colonne de 1ere matrice != nombre de ligne de 2eme matrice")
        label.setFont(QtGui.QFont("Sanserif",15))
        vbox.addWidget(label)
        button=QPushButton("précédant",self)  # we create a button named précédant
        button.setStyleSheet("background-color:#a69359")
        button.clicked.connect(self.back) #we connect the button to back function
        vbox.addWidget(button)
        self.setLayout(vbox)
        self.show()
        
    def back(self):
        tabdialog.tabWidget.currentWidget().mydialog.mydialog2.window2.produitwindow.close() # we close the dialog called produitwindow
        tabdialog.tabWidget.currentWidget().mydialog.mydialog2.window2.show()     
        
        
        
class additionwindow(QWidget):
    def __init__(self,parent=None):
        super(additionwindow,self).__init__(parent)
        self.title = " Addition de deux matrices" #title of window
        self.top = 200    # the distance between the window and the top
        self.left = 300    # the distance between the window and the left
        self.width = 500   # the width of the window
        self.height = 500  # the height of the window
        self.setWindowIcon(QtGui.QIcon("addition.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height) #setGeometry execute the geometry of the window
        vbox=QVBoxLayout()  # we create a QVBoxLayout named vbox
        self.tableWidget = QTableWidget() # we create a tablewidget
        self.tableWidget.setRowCount(int(tabdialog.tabWidget.currentWidget().mydialog.textbox.text()))
        self.tableWidget.setColumnCount(int(tabdialog.tabWidget.currentWidget().mydialog.textbox1.text()))# we set the number of columns and rows for the tableWidget
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.horizontalHeader().hide() #we hide the vertical and horizontal header of the tableWidget
        M4=tabdialog.tabWidget.currentWidget().mydialog.mydialog2.window2.M3 # we assigned the matrix M3 (created in the class operation2) to M4

        for i in range (shape(M4)[0]):
            for j in range(shape(M4)[1]):
                 self.tableWidget.setItem(i,j,QTableWidgetItem(str(M4[i][j])))
        
        vbox.addWidget(self.tableWidget)
        button=QPushButton("précédant",self)  # we create a button named précédant
        button.setStyleSheet("background-color:#a69359")
        button.clicked.connect(self.back) #we connect the button to back function
        vbox.addWidget(button)
      
        
        self.setLayout(vbox)
        self.show()
    def back(self):
        tabdialog.tabWidget.currentWidget().mydialog.mydialog2.window2.additionwindow.close() # we close the dialog called additionwindow
        tabdialog.tabWidget.currentWidget().mydialog.mydialog2.window2.show()        

class additionwindow1(QWidget):
    def __init__(self,parent=None):
        super(additionwindow1,self).__init__(parent)
        self.title = "Addition de deux matrices" #title of window
        self.top = 200    # the distance between the window and the top
        self.left = 300    # the distance between the window and the left
        self.width = 500   # the width of the window
        self.height = 500  # the height of the window
        self.setWindowIcon(QtGui.QIcon("addition.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height) #setGeometry execute the geometry of the window
        vbox = QVBoxLayout()  # we create a QVBoxLayout named vbox
        label=QLabel("on ne peut pas additionner deux matrices de different demension")
        label.setFont(QtGui.QFont("Sanserif",25))
        vbox.addWidget(label)
        button=QPushButton("précédant",self)  # we create a button named précédant
        button.clicked.connect(self.back) #we connect the button to back function
        button.setStyleSheet("background-color:#a69359")
        vbox.addWidget(button)
        self.setLayout(vbox)
        self.show()
        
    def back(self):
        tabdialog.tabWidget.currentWidget().mydialog.mydialog2.window2.additionwindow.close() # we close the dialog called additionwindow
        tabdialog.tabWidget.currentWidget().mydialog.mydialog2.window2.show() 
        
        
# principal program     
if __name__ == "__main__":
    app = QApplication(sys.argv) #We created an instance of the QApplication class and assigned it to the variable app
    tabdialog = Tab()  #We created an instance of the Tab() class and assigned it to the variable tabdialog
    tabdialog.show()  # we showed the window of the instance tabdialog
    app.exec()
