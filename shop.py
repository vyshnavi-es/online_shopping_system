from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui
import sys,threading
import webbrowser
import qdarkstyle
import os
import MySQLdb
from xlsxwriter.workbook import Workbook
from datetime import datetime

from PyQt5.uic import  loadUiType

ui,_=loadUiType('shopping.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handle_ui_changes()
        self.handle_buttons()
        self.clearCart()
        self.setWindowTitle("Online Shopping")
        self.setTheme()
    
    
    def handle_ui_changes(self):
        self.tabWidget.tabBar().setVisible(False)
        self.tabWidget_3.tabBar().setVisible(False)


    def handle_buttons(self):
        self.pushButton_101.clicked.connect(self.show_new_user)
        self.pushButton_102.clicked.connect(self.login)
        self.pushButton_7.clicked.connect(self.add_new_user)
        self.pushButton_99.clicked.connect(self.confirm)
        self.pushButton_3.clicked.connect(self.home)
        self.pushButton_4.clicked.connect(self.categories)
        self.pushButton_82.clicked.connect(self.categories)
        self.pushButton_184.clicked.connect(self.categories)
        self.pushButton_16.clicked.connect(self.accessories)
        self.pushButton_77.clicked.connect(self.accessories)
        self.pushButton_5.clicked.connect(self.cart)
        self.pushButton_183.clicked.connect(self.cart)
        self.pushButton_185.clicked.connect(self.cart)
        self.pushButton_6.clicked.connect(self.show_tops)
        self.pushButton_76.clicked.connect(self.show_tops)
        self.pushButton_26.clicked.connect(self.show_bottoms)
        self.pushButton_78.clicked.connect(self.show_bottoms)
        self.pushButton_27.clicked.connect(self.show_dresses)
        self.pushButton_79.clicked.connect(self.show_dresses)
        self.pushButton_3.clicked.connect(self.show_home)
        self.pushButton_8.clicked.connect(self.show_in_cart)
        #self.pushButton_8.clicked.connect(self.enable_cart)
        self.pushButton_9.clicked.connect(self.show_in_cart1)
        #self.pushButton_9.clicked.connect(self.enable_cart)
        self.pushButton_10.clicked.connect(self.show_in_cart2)
        self.pushButton_11.clicked.connect(self.show_in_cart3)
        self.pushButton_12.clicked.connect(self.show_in_cart4)
        self.pushButton_13.clicked.connect(self.show_in_cart5)
        self.pushButton_14.clicked.connect(self.show_in_cart6)
        self.pushButton_18.clicked.connect(self.show_in_cart7)
        self.pushButton_15.clicked.connect(self.show_in_cart8)
        self.pushButton_17.clicked.connect(self.show_in_cart9)
        self.pushButton_25.clicked.connect(self.show_in_cart10)
        self.pushButton_21.clicked.connect(self.show_in_cart11)
        self.pushButton_22.clicked.connect(self.show_in_cart12)
        self.pushButton_23.clicked.connect(self.show_in_cart13)
        self.pushButton_24.clicked.connect(self.show_in_cart14)
        self.pushButton_37.clicked.connect(self.show_in_cart15)
        self.pushButton_38.clicked.connect(self.show_in_cart16)
        self.pushButton_34.clicked.connect(self.show_in_cart17)
        self.pushButton_39.clicked.connect(self.show_in_cart18)
        self.pushButton_20.clicked.connect(self.place_order)
        self.pushButton_42.clicked.connect(self.home)
        self.pushButton_80.clicked.connect(self.home)
        self.pushButton_44.clicked.connect(self.home)
        self.pushButton_46.clicked.connect(self.home)
        self.pushButton_49.clicked.connect(self.home) 
        self.pushButton_103.clicked.connect(self.vyshinsta)
        self.tableWidget.cellClicked.connect(self.on_click)
        
    
    def enable_colour(self):
        self.label_70.setStyleSheet("background-color: red")
        self.label_74.setStyleSheet("background-color: red")
        self.label_71.setStyleSheet("background-color: red")

    
    def enable_cart_no(self):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()

        self.enable_colour()
        
        sql = ''' SELECT count(*) FROM cart '''
        self.cur.execute(sql)
        count=self.cur.fetchone()
        count=count[0]
        self.label_70.setText(str(count))
        self.label_74.setText(str(count))
        self.label_71.setText(str(count))

    
    def vyshinsta(self):
        webbrowser.open('https://www.instagram.com/vyshnavi_es/')
    
    def show_home(self):
        self.tabWidget.setCurrentIndex(2)

    def show_new_user(self):
        self.tabWidget.setCurrentIndex(1)
    
    def register(self):
        self.tabWidget.setCurrentIndex(2)

    def home(self):
        self.tabWidget.setCurrentIndex(2)
        self.label_77.setText("Store")
        self.clearLabel()

    def categories(self):
        self.tabWidget.setCurrentIndex(3)
    
    def accessories(self):
        self.tabWidget.setCurrentIndex(5)
        self.label_64.setText("ACCESSORIES")
        self.clearLabel()

    def cart(self):
        self.tabWidget.setCurrentIndex(6)

    def confirm_order(self):
        self.tabWidget.setCurrentIndex(7)

    def go_to_cart(self):
        self.tabWidget.setCurrentIndex(6)

    def show_tops(self):
        self.tabWidget.setCurrentIndex(4)
        self.tabWidget_3.setCurrentIndex(0)
        self.label_63.setText("Tops")
        self.clearLabel()

    def show_bottoms(self):
        self.tabWidget.setCurrentIndex(4)
        self.tabWidget_3.setCurrentIndex(1)
        self.label_17.setText("Bottoms")
        self.clearLabel()
    
    def show_dresses(self):
        self.tabWidget.setCurrentIndex(4)
        self.tabWidget_3.setCurrentIndex(2)
        self.label_22.setText('Dresses')
        self.clearLabel()

    
    def show_in_cart(self):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()

        quantity=self.comboBox_2.currentText()
        quantity = int(quantity)
        size=self.comboBox_3.currentText()
        total = 0

        self.cur.execute('''select * from tops_tunics_and_dresses where top_name = "OrangeCropTop" ''')
        info = self.cur.fetchone()
    

        if size == str("S") and  quantity > info[5]  :
            self.statusBar().showMessage("Out of stock")
        elif size == str("M") and quantity > info[6] :
            self.statusBar().showMessage("Out of stock")
        elif  size == str("L") and quantity > info[7] :
            self.statusBar().showMessage("Out of stock")

        else:
            self.cur.execute(''' 
                INSERT INTO cart(pro_brand,pro_name,pro_price,quantity,size,pro_photo,itemTotal) 
                VALUES(%s,%s,%s,%s,%s,%s,%s)
            ''',("Aliexpress","OrangeCropTop", 400, quantity, size, ':/newPrefix/pics/Orange Crop Top.png', total))
            self.db.commit()
        

            sql = ''' SELECT pro_id,pro_brand,pro_name,pro_price,quantity,size,pro_photo FROM cart'''
            self.cur.execute(sql)
            data = self.cur.fetchall()

            self.statusBar().showMessage("Item Added to Cart")
            self.enable_cart_no()
            self.statusBarClear()
            self.total()
            self.comboBox_2.setCurrentIndex(0)
            self.comboBox_3.setCurrentIndex(0)

            if data:
                self.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(data):
                    self.tableWidget.insertRow(row_number)
                    for column_number, column_data in enumerate(row_data):
                        if column_number == 6:
                            imgLbl = self.getImageLabel(column_data)
                            self.tableWidget.setCellWidget(row_number,6,imgLbl)

                        else:
                            self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(column_data)))
            else:
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)            
  
            
    def show_in_cart1(self):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()

        quantity=self.comboBox_4.currentText()
        quantity = int(quantity)
        size=self.comboBox_5.currentText()
        total = 0

        self.cur.execute('''select * from tops_tunics_and_dresses where top_name = "BlackTunicTop" ''')
        info = self.cur.fetchone()

        if size == str("S") and  quantity > info[5]  :
            self.statusBar().showMessage("Out of stock")
        elif size == str("M") and quantity > info[6] :
            self.statusBar().showMessage("Out of stock")
        elif  size == str("L") and quantity > info[7] :
            self.statusBar().showMessage("Out of stock")
    
        else:
            self.cur.execute(''' 
                INSERT INTO cart(pro_brand,pro_name,pro_price,quantity,size,pro_photo,itemTotal) 
                VALUES(%s,%s,%s,%s,%s,%s,%s)
            ''',("Ajio", "BlackTunicTop", 500,quantity,size ,':/newPrefix/pics/Black Tunic Top.png',total))
            self.db.commit()

            sql = ''' SELECT  pro_id,pro_brand,pro_name,pro_price,quantity,size,pro_photo FROM cart'''
            self.cur.execute(sql)
            data = self.cur.fetchall()
            
            self.statusBar().showMessage("Item Added to Cart")
            self.enable_cart_no()
            self.statusBarClear()
            self.total()
            self.comboBox_4.setCurrentIndex(0)
            self.comboBox_5.setCurrentIndex(0)

            if data:
                self.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(data):
                    self.tableWidget.insertRow(row_number)
                    for column_number, column_data in enumerate(row_data):
                        if column_number == 6:
                            imgLbl = self.getImageLabel(column_data)
                            self.tableWidget.setCellWidget(row_number,6,imgLbl)
                        else:
                            self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(column_data)))

            else:
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)


    def show_in_cart2(self):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()
        
        quantity=self.comboBox_6.currentText()
        quantity = int(quantity)
        size=self.comboBox_7.currentText()
        total = 0

        self.cur.execute('''select * from tops_tunics_and_dresses where top_name = "PinkFloralTop" ''')
        info = self.cur.fetchone()

        if size == str("S") and  quantity > info[5]  :
            self.statusBar().showMessage("Out of stock")
        elif size == str("M") and quantity > info[6] :
            self.statusBar().showMessage("Out of stock")
        elif  size == str("L") and quantity > info[7] :
            self.statusBar().showMessage("Out of stock")
    
        else:
            self.cur.execute(''' 
                INSERT INTO cart(pro_brand,pro_name,pro_price,quantity,size,pro_photo,itemTotal) 
                VALUES(%s,%s,%s,%s,%s,%s,%s)
            ''',("Ajio", "PinkFloralTop", 300,quantity,size, ':/newPrefix/pics/Pink Floral Top.png',total))
            self.db.commit()

            sql = ''' SELECT  pro_id,pro_brand,pro_name,pro_price,quantity,size,pro_photo FROM cart '''
            self.cur.execute(sql)
            data = self.cur.fetchall()

            self.statusBar().showMessage("Item Added to Cart")
            self.enable_cart_no()
            self.statusBarClear()
            self.total() 
            self.comboBox_6.setCurrentIndex(0)
            self.comboBox_7.setCurrentIndex(0)

            if data:
                self.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(data):
                    self.tableWidget.insertRow(row_number)
                    for column_number, column_data in enumerate(row_data):
                        if(column_number == 6):
                            imgLbl = self.getImageLabel(column_data)
                            self.tableWidget.setCellWidget(row_number,6,imgLbl)
                        else:
                            self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(column_data)))
            
            else:
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)


    def show_in_cart3(self):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()

        quantity=self.comboBox_8.currentText()
        quantity = int(quantity)
        size=self.comboBox_9.currentText()
        total = 0

        self.cur.execute('''select * from tops_tunics_and_dresses where top_name = "BlackMeshTop" ''')
        info = self.cur.fetchone()

        if size == str("S") and  quantity > info[5]  :
            self.statusBar().showMessage("Out of stock")
        elif size == str("M") and quantity > info[6] :
            self.statusBar().showMessage("Out of stock")
        elif  size == str("L") and quantity > info[7] :
            self.statusBar().showMessage("Out of stock")
    
      
        else:
            self.cur.execute(''' 
                INSERT INTO cart(pro_brand,pro_name,pro_price,quantity,size,pro_photo,itemTotal) 
                VALUES(%s,%s,%s,%s,%s,%s,%s)
            ''',("DreamDay", "BlackMeshTop", 350,quantity,size,':/newPrefix/pics/Black Mesh Top.png',total))
            self.db.commit()
        

            sql = ''' SELECT pro_id,pro_brand,pro_name,pro_price,quantity,size,pro_photo FROM cart'''
            self.cur.execute(sql) 
            data = self.cur.fetchall()

            self.statusBar().showMessage("Item Added to Cart")
            self.enable_cart_no()
            self.statusBarClear()
            self.total()
            self.comboBox_8.setCurrentIndex(0)
            self.comboBox_9.setCurrentIndex(0)

            if data:
                self.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(data):
                    self.tableWidget.insertRow(row_number)
                    for column_number, column_data in enumerate(row_data):
                        if(column_number == 6):
                            imgLbl = self.getImageLabel(column_data)
                            self.tableWidget.setCellWidget(row_number,6,imgLbl)
                        else:
                            self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(column_data)))
            
            else:
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)

    def show_in_cart4(self):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()

        quantity=self.comboBox_10.currentText()
        quantity = int(quantity)
        size=self.comboBox_11.currentText()
        total = 0
        

        self.cur.execute('''select * from tops_tunics_and_dresses where top_name = "PinkTunicTop" ''')
        info = self.cur.fetchone()

        if size == str("S") and  quantity > info[5]  :
            self.statusBar().showMessage("Out of stock")
        elif size == str("M") and quantity > info[6] :
            self.statusBar().showMessage("Out of stock")
        elif  size == str("L") and quantity > info[7] :
            self.statusBar().showMessage("Out of stock")
        
        else:
            self.cur.execute(''' 
                INSERT INTO cart(pro_brand,pro_name,pro_price,quantity,size,pro_photo,itemTotal) 
                VALUES(%s,%s,%s,%s,%s,%s,%s)
            ''',("Meesho", "PinkTunicTop", 400,quantity,size, (':/newPrefix/pics/Pink Tunic Top.png'),total))
            self.db.commit()

        

            sql = ''' SELECT  pro_id,pro_brand,pro_name,pro_price,quantity,size,pro_photo FROM cart'''
            self.cur.execute(sql)
            data = self.cur.fetchall()
        
            self.statusBar().showMessage("Item Added to Cart")
            self.enable_cart_no()
            self.statusBarClear()
            self.total()
            self.comboBox_10.setCurrentIndex(0)
            self.comboBox_11.setCurrentIndex(0)

            
            if data:
                self.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(data):
                    self.tableWidget.insertRow(row_number)
                    for column_number, column_data in enumerate(row_data):
                        if(column_number == 6):
                            imgLbl = self.getImageLabel(column_data)
                            self.tableWidget.setCellWidget(row_number,6,imgLbl)
                        else:
                            self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(column_data)))
            else:
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)

    def show_in_cart5(self):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()

        quantity=self.comboBox_12.currentText()
        quantity = int(quantity)
        size=self.comboBox_13.currentText()
        total = 0

        self.cur.execute('''select * from bottoms where bottom_name = "Black and white Striped shorts" ''')
        info = self.cur.fetchone()

        if size == str("S") and  quantity > info[5]  :
            self.statusBar().showMessage("Out of stock")
        elif size == str("M") and quantity > info[6] :
            self.statusBar().showMessage("Out of stock")
        elif  size == str("L") and quantity > info[7] :
            self.statusBar().showMessage("Out of stock")

        else:
            self.cur.execute(''' 
                INSERT INTO cart(pro_brand,pro_name,pro_price,quantity,size,pro_photo,itemTotal) 
                VALUES(%s,%s,%s,%s,%s,%s,%s)
            ''',("Myntra", "Black and white Striped shorts", 400,quantity,size, (':/pics/WhatsApp-Image-2020-12-03-at-9.51.43-PM-_1_.png'),total))
            self.db.commit()


            sql = ''' SELECT  pro_id,pro_brand,pro_name,pro_price,quantity,size,pro_photo FROM cart '''
            self.cur.execute(sql)
            data = self.cur.fetchall()
            
            self.statusBar().showMessage("Item Added to Cart")
            self.enable_cart_no()
            self.statusBarClear()
            self.total()
            self.comboBox_12.setCurrentIndex(0)
            self.comboBox_13.setCurrentIndex(0)

            if data:
                self.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(data):
                    self.tableWidget.insertRow(row_number)
                    for column_number, column_data in enumerate(row_data):
                        if(column_number == 6):
                            imgLbl = self.getImageLabel(column_data)
                            self.tableWidget.setCellWidget(row_number,6,imgLbl)
                        else:
                            self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(column_data)))
            else:
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)
    
    def show_in_cart6(self):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()
        
        quantity=self.comboBox_14.currentText()
        quantity = int(quantity)
        size=self.comboBox_15.currentText()
        total = 0
        
        
        self.cur.execute('''select * from bottoms where bottom_name = "Torn Blue Denim" ''')
        info = self.cur.fetchone()

        if size == str("S") and  quantity > info[5]  :
            self.statusBar().showMessage("Out of stock")
        elif size == str("M") and quantity > info[6] :
            self.statusBar().showMessage("Out of stock")
        elif  size == str("L") and quantity > info[7] :
            self.statusBar().showMessage("Out of stock")

        else:
            self.cur.execute(''' 
                INSERT INTO cart(pro_brand,pro_name,pro_price,quantity,size,pro_photo,itemTotal) 
                VALUES(%s,%s,%s,%s,%s,%s,%s)
            ''',("DreamDay", "Torn Blue Denim", 500,quantity,size,(':/pics/WhatsApp-Image-2020-12-03-at-9.51.43-PM.png'),total))
            self.db.commit()


            sql = ''' SELECT  pro_id,pro_brand,pro_name,pro_price,quantity,size,pro_photo FROM cart'''
            self.cur.execute(sql)
            data = self.cur.fetchall()
        
            self.statusBar().showMessage("Item Added to Cart")
            self.enable_cart_no()
            self.statusBarClear()
            self.total()
            self.comboBox_14.setCurrentIndex(0)
            self.comboBox_15.setCurrentIndex(0)

            if data:
                self.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(data):
                    self.tableWidget.insertRow(row_number)
                    for column_number, column_data in enumerate(row_data):
                        if(column_number == 6):
                            imgLbl = self.getImageLabel(column_data)
                            self.tableWidget.setCellWidget(row_number,6,imgLbl)
                        else:
                            self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(column_data)))

            else:
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)

    def show_in_cart7(self):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()

        
        quantity=self.comboBox_16.currentText()
        quantity = int(quantity)
        size=self.comboBox_17.currentText()
        total = 0

        self.cur.execute('''select * from bottoms where bottom_name =  "Maroon Skirt" ''')
        info = self.cur.fetchone()

        if size == str("S") and  quantity > info[5]  :
            self.statusBar().showMessage("Out of stock")
        elif size == str("M") and quantity > info[6] :
            self.statusBar().showMessage("Out of stock")
        elif  size == str("L") and quantity > info[7] :
            self.statusBar().showMessage("Out of stock")
      
        else:
            self.cur.execute(''' 
                INSERT INTO cart(pro_brand,pro_name,pro_price,quantity,size,pro_photo,itemTotal) 
                VALUES(%s,%s,%s,%s,%s,%s,%s)
            ''',("Ajio", "Maroon Skirt", 600,quantity,size,(':/pics/WhatsApp-Image-2020-12-03-at-9.51.44-PM.png'),total))
            self.db.commit()


            sql = ''' SELECT  pro_id,pro_brand,pro_name,pro_price,quantity,size,pro_photo FROM cart '''
            self.cur.execute(sql)
            data = self.cur.fetchall()
            
            self.statusBar().showMessage("Item Added to Cart") 
            self.enable_cart_no()
            self.statusBarClear()
            self.total() 
            self.comboBox_16.setCurrentIndex(0)
            self.comboBox_17.setCurrentIndex(0)

            if data:
                self.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(data):
                    self.tableWidget.insertRow(row_number)
                    for column_number, column_data in enumerate(row_data):
                        if(column_number == 6):
                            imgLbl = self.getImageLabel(column_data)
                            self.tableWidget.setCellWidget(row_number,6,imgLbl)
                        else:
                            self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(column_data)))

            else:
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)

    def show_in_cart8(self):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()
        

        quantity=self.comboBox_20.currentText()
        quantity = int(quantity)
        size=self.comboBox_19.currentText()
        total = 0
        
        self.cur.execute('''select * from bottoms where bottom_name =  "Floral Pencil Skirt" ''')
        info = self.cur.fetchone()

        if size == str("S") and  quantity > info[5]  :
            self.statusBar().showMessage("Out of stock")
        elif size == str("M") and quantity > info[6] :
            self.statusBar().showMessage("Out of stock")
        elif  size == str("L") and quantity > info[7] :
            self.statusBar().showMessage("Out of stock")

        else:
            self.cur.execute(''' 
                INSERT INTO cart(pro_brand,pro_name,pro_price,quantity,size,pro_photo,itemTotal) 
                VALUES(%s,%s,%s,%s,%s,%s,%s)
            ''',("Meesho", "Floral Pencil Skirt", 400,quantity,size,(':/pics/WhatsApp-Image-2020-12-03-at-9.51.43-PM-_2_.png'),total))
            self.db.commit()


            sql = ''' SELECT  pro_id,pro_brand,pro_name,pro_price,quantity,size,pro_photo FROM cart '''
            self.cur.execute(sql)
            data = self.cur.fetchall()
            

            self.statusBar().showMessage("Item Added to Cart")
            self.enable_cart_no()
            self.statusBarClear()
            self.total()
            self.comboBox_19.setCurrentIndex(0)
            self.comboBox_20.setCurrentIndex(0)

            if data:
                self.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(data):
                    self.tableWidget.insertRow(row_number)
                    for column_number, column_data in enumerate(row_data):
                        if(column_number == 6):
                            imgLbl = self.getImageLabel(column_data)
                            self.tableWidget.setCellWidget(row_number,6,imgLbl)
                        else:
                            self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(column_data)))

            else:
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)
        
    def show_in_cart9(self):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()

        quantity=self.comboBox_21.currentText()
        quantity = int(quantity)
        size=self.comboBox_18.currentText()
        total = 0

        self.cur.execute('''select * from bottoms where bottom_name =  "Blue Denim Dungaree" ''')
        info = self.cur.fetchone()

        if size == str("S") and  quantity > info[5]  :
            self.statusBar().showMessage("Out of stock")
        elif size == str("M") and quantity > info[6] :
            self.statusBar().showMessage("Out of stock")
        elif  size == str("L") and quantity > info[7] :
            self.statusBar().showMessage("Out of stock")
        else:
            self.cur.execute(''' 
                INSERT INTO cart(pro_brand,pro_name,pro_price,quantity,size,pro_photo,itemTotal) 
                VALUES(%s,%s,%s,%s,%s,%s,%s)
            ''',("DreamDay", "Blue Denim Dungaree", 500,quantity,size,(':/newPrefix/pics/_Image_2020-12-03_at_10.09.27_PM_1_.png'),total))
            self.db.commit()

            
            sql = ''' SELECT pro_id,pro_brand,pro_name,pro_price,quantity,size,pro_photo FROM cart'''
            self.cur.execute(sql)
            data = self.cur.fetchall()
            
            
            self.statusBar().showMessage("Item Added to Cart")
            self.enable_cart_no()
            self.statusBarClear()
            self.total()
            self.comboBox_18.setCurrentIndex(0)
            self.comboBox_21.setCurrentIndex(0)

            if data:
                self.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(data):
                    self.tableWidget.insertRow(row_number)
                    for column_number, column_data in enumerate(row_data):
                        if(column_number == 6):
                            imgLbl = self.getImageLabel(column_data)
                            self.tableWidget.setCellWidget(row_number,6,imgLbl)
                        else:
                            self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(column_data)))

            else:
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)


    def show_in_cart10(self):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()
        
        quantity=self.comboBox_22.currentText()
        quantity = int(quantity)
        size=self.comboBox_27.currentText()
        total = 0
        
        self.cur.execute('''select * from dresses where dresses_name = "RedGown" ''')
        info = self.cur.fetchone()

        if size == str("S") and  quantity > info[5]  :
            self.statusBar().showMessage("Out of stock")
        elif size == str("M") and quantity > info[6] :
            self.statusBar().showMessage("Out of stock")
        elif  size == str("L") and quantity > info[7] :
            self.statusBar().showMessage("Out of stock")
       
        else:
            self.cur.execute(''' 
                INSERT INTO cart(pro_brand,pro_name,pro_price,quantity,size,pro_photo,itemTotal) 
                VALUES(%s,%s,%s,%s,%s,%s,%s)
            ''',("DreamDay", "RedGown", 800,quantity,size, (':/newPrefix/pics/App_Image_2020-12-03_at_10.09.27_PM.png'),total))
            self.db.commit()

            
            sql = ''' SELECT pro_id,pro_brand,pro_name,pro_price,quantity,size,pro_photo FROM cart  '''
            self.cur.execute(sql)
            data = self.cur.fetchall()

            self.statusBar().showMessage("Item Added to Cart")
            self.enable_cart_no()
            self.statusBarClear()
            self.total() 
            self.comboBox_22.setCurrentIndex(0)
            self.comboBox_27.setCurrentIndex(0)

            if data:
                self.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(data):
                    self.tableWidget.insertRow(row_number)
                    for column_number, column_data in enumerate(row_data):
                        if(column_number == 6):
                            imgLbl = self.getImageLabel(column_data)
                            self.tableWidget.setCellWidget(row_number,6,imgLbl)
                        else:
                            self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(column_data)))

            else:
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)

    def show_in_cart11(self):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()
           
        quantity=self.comboBox_23.currentText()
        quantity = int(quantity)
        size=self.comboBox_28.currentText()
        total = 0
        
        self.cur.execute('''select * from dresses where dresses_name = "Yellow Romper Dress" ''')
        info = self.cur.fetchone()

        if size == str("S") and  quantity > info[5]  :
            self.statusBar().showMessage("Out of stock")
        elif size == str("M") and quantity > info[6] :
            self.statusBar().showMessage("Out of stock")
        elif  size == str("L") and quantity > info[7] :
            self.statusBar().showMessage("Out of stock")
        else:
            self.cur.execute(''' 
                INSERT INTO cart(pro_brand,pro_name,pro_price,quantity,size,pro_photo,itemTotal) 
                VALUES(%s,%s,%s,%s,%s,%s,%s)
            ''',("Ali Express", "Yellow Romper Dress", 400,quantity,size,(':/newPrefix/pics/App_Image_2020-12-03_at_10.09.26_PM.png'),total))
            self.db.commit()


            sql = ''' SELECT  pro_id,pro_brand,pro_name,pro_price,quantity,size,pro_photo FROM cart  '''
            self.cur.execute(sql)
            data = self.cur.fetchall()
            

            self.statusBar().showMessage("Item Added to Cart")
            self.enable_cart_no()
            self.statusBarClear()
            self.total()
            self.comboBox_23.setCurrentIndex(0)
            self.comboBox_28.setCurrentIndex(0)

            if data:
                self.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(data):
                    self.tableWidget.insertRow(row_number)
                    for column_number, column_data in enumerate(row_data):
                        if(column_number == 6):
                            imgLbl = self.getImageLabel(column_data)
                            self.tableWidget.setCellWidget(row_number,6,imgLbl)
                        else:
                            self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(column_data)))

            else:
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)

        
    def show_in_cart12(self):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()

        quantity=self.comboBox_24.currentText()
        quantity = int(quantity)
        size=self.comboBox_29.currentText()
        total = 0

        self.cur.execute('''select * from dresses where dresses_name = "Grey Casual Dress" ''')
        info = self.cur.fetchone()

        if size == str("S") and  quantity > info[5]  :
            self.statusBar().showMessage("Out of stock")
        elif size == str("M") and quantity > info[6] :
            self.statusBar().showMessage("Out of stock")
        elif  size == str("L") and quantity > info[7] :
            self.statusBar().showMessage("Out of stock")
        
        else:
            self.cur.execute(''' 
                INSERT INTO cart(pro_brand,pro_name,pro_price,quantity,size,pro_photo,itemTotal) 
                VALUES(%s,%s,%s,%s,%s,%s,%s)
            ''',("Myntra", "Grey Casual Dress", 500,quantity,size, (':/newPrefix/pics/App_Image_2020-12-03_at_10.09.28_PM.png'),total))
            self.db.commit()

            sql = ''' SELECT pro_id,pro_brand,pro_name,pro_price,quantity,size,pro_photo FROM cart '''
            self.cur.execute(sql)
            data = self.cur.fetchall()
            

            self.statusBar().showMessage("Item Added to Cart")
            self.enable_cart_no()
            self.statusBarClear()
            self.total()
            self.comboBox_24.setCurrentIndex(0)
            self.comboBox_29.setCurrentIndex(0)

            if data:
                self.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(data):
                    self.tableWidget.insertRow(row_number)
                    for column_number, column_data in enumerate(row_data):
                        if(column_number == 6):
                            imgLbl = self.getImageLabel(column_data)
                            self.tableWidget.setCellWidget(row_number,6,imgLbl)
                        else:
                            self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(column_data)))
            else:
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)
        


    def show_in_cart13(self):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()

        quantity=self.comboBox_25.currentText()
        quantity = int(quantity)
        size=self.comboBox_30.currentText()
        total = 0

        self.cur.execute('''select * from dresses where dresses_name = "Red Skirt and Crop Top" ''')
        info = self.cur.fetchone()

        if size == str("S") and  quantity > info[5]  :
            self.statusBar().showMessage("Out of stock")
        elif size == str("M") and quantity > info[6] :
            self.statusBar().showMessage("Out of stock")
        elif  size == str("L") and quantity > info[7] :
            self.statusBar().showMessage("Out of stock")
        else:
            self.cur.execute(''' 
                INSERT INTO cart(pro_brand,pro_name,pro_price,quantity,size,pro_photo,itemTotal) 
                VALUES(%s,%s,%s,%s,%s,%s,%s)
            ''',("Ajio", "Red Skirt and Crop Top", 700,quantity,size, (':/newPrefix/pics/WhatsApp Image 2020-12-05 at 10.53.28 AM.jpeg'),total))
            self.db.commit()
            
            sql = ''' SELECT pro_id,pro_brand,pro_name,pro_price,quantity,size,pro_photo FROM cart '''
            self.cur.execute(sql)
            data = self.cur.fetchall()
            
            self.statusBar().showMessage("Item Added to Cart")
            self.enable_cart_no()
            self.statusBarClear()
            self.total()
            self.comboBox_25.setCurrentIndex(0)
            self.comboBox_30.setCurrentIndex(0)
        

            if data:
                self.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(data):
                    self.tableWidget.insertRow(row_number)
                    for column_number, column_data in enumerate(row_data):
                        if(column_number == 6):
                            imgLbl = self.getImageLabel(column_data)
                            self.tableWidget.setCellWidget(row_number,6,imgLbl)
                        else:
                            self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(column_data)))

            else:
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)
        
    def show_in_cart14(self):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()

        quantity=self.comboBox_26.currentText()
        quantity = int(quantity)
        size=self.comboBox_31.currentText()
        total = 0

        
        self.cur.execute('''select * from dresses where dresses_name ="Black Skirt and Crop Top" ''')
        info = self.cur.fetchone()

        if size == str("S") and  quantity > info[5]  :
            self.statusBar().showMessage("Out of stock")
        elif size == str("M") and quantity > info[6] :
            self.statusBar().showMessage("Out of stock")
        elif  size == str("L") and quantity > info[7] :
            self.statusBar().showMessage("Out of stock")
        else:
            self.cur.execute(''' 
                INSERT INTO cart(pro_brand,pro_name,pro_price,quantity,size,pro_photo,itemTotal) 
                VALUES(%s,%s,%s,%s,%s,%s,%s)
            ''',("Myntra", "Black Skirt and Crop Top", 500,quantity,size, (':/newPrefix/pics/WhatsApp Image 2020-12-05 at 10.53.28 AM (1).jpeg'),total))
            self.db.commit()

            
            sql = ''' SELECT pro_id,pro_brand,pro_name,pro_price,quantity,size,pro_photo FROM cart  '''
            self.cur.execute(sql)
            data = self.cur.fetchall()
            
            self.statusBar().showMessage("Item Added to Cart")
            self.enable_cart_no()
            self.statusBarClear()
            self.total()
            self.comboBox_26.setCurrentIndex(0)
            self.comboBox_31.setCurrentIndex(0)

            if data:
                self.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(data):
                    self.tableWidget.insertRow(row_number)
                    for column_number, column_data in enumerate(row_data):
                        if(column_number == 6):
                            imgLbl = self.getImageLabel(column_data)
                            self.tableWidget.setCellWidget(row_number,6,imgLbl)
                        else:
                            self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(column_data)))

            else:
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)                       

    def show_in_cart15(self):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()

        quantity = self.comboBox_32.currentText()
        quantity = int(quantity)
        total = 0

        self.cur.execute('''select * from  accessories where a_name = "Black and Gold Jhumka"''')
        info=self.cur.fetchone()
    
        if quantity > info[4]:
            self.statusBar().showMessage("Out of Stock")
        else:
            self.cur.execute(''' 
                INSERT INTO cart(pro_brand,pro_name,pro_price,quantity,size,pro_photo,itemTotal) 
                VALUES(%s,%s,%s,%s,%s,%s,%s)
            ''',("Everstyle", "Black and Gold Jhumka", 100,quantity,"-", (':/newPrefix/pics/WhatsApp Image 2020-12-05 at 10.39.33 AM.jpeg'),total))
            self.db.commit()
            
            sql = ''' SELECT  pro_id,pro_brand,pro_name,pro_price,quantity,size,pro_photo FROM cart  '''
            self.cur.execute(sql)
            data = self.cur.fetchall()

            
            self.statusBar().showMessage("Item Added to Cart")
            self.enable_cart_no()
            self.statusBarClear()
            self.total()
            self.comboBox_32.setCurrentIndex(0)
            

            if data:
                self.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(data):
                    self.tableWidget.insertRow(row_number)
                    for column_number, column_data in enumerate(row_data):
                        if(column_number == 6):
                            imgLbl = self.getImageLabel(column_data)
                            self.tableWidget.setCellWidget(row_number,6,imgLbl)
                        else:
                            self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(column_data)))
            else:
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)

    def show_in_cart16(self):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()

        quantity = self.comboBox_33.currentText()
        quantity = int(quantity)
        total = 0

        self.cur.execute('''select * from  accessories where a_name = "Ear cuffs" ''')
        info=self.cur.fetchone()
    
    
        if quantity > info[4]:
            self.statusBar().showMessage("Out of Stock")
        else:
            self.cur.execute(''' 
                INSERT INTO cart(pro_brand,pro_name,pro_price,quantity,size,pro_photo,itemTotal) 
                VALUES(%s,%s,%s,%s,%s,%s,%s)
            ''',("Everstyle", "Ear cuffs", 120,quantity,"-", (':/newPrefix/pics/WhatsApp Image 2020-12-05 at 10.39.33 AM (1).jpeg'),total))
            self.db.commit()

            
            sql = ''' SELECT  pro_id,pro_brand,pro_name,pro_price,quantity,size,pro_photo FROM cart '''
            self.cur.execute(sql)
            data = self.cur.fetchall()

            
            self.statusBar().showMessage("Item Added to Cart")
            self.enable_cart_no()
            self.statusBarClear()
            self.total()
            self.comboBox_33.setCurrentIndex(0)

        
            if data:
                self.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(data):
                    self.tableWidget.insertRow(row_number)
                    for column_number, column_data in enumerate(row_data):
                        if(column_number == 6):
                            imgLbl = self.getImageLabel(column_data)
                            self.tableWidget.setCellWidget(row_number,6,imgLbl)
                        else:
                            self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(column_data)))

            else:
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)
    
    def show_in_cart17(self):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()

        quantity = self.comboBox_34.currentText()
        quantity = int(quantity)
        total = 0

        
        self.cur.execute('''select * from  accessories where a_name = "Dainty stone neckpiece"''')
        info=self.cur.fetchone()

    
        if quantity > info[4]:
            self.statusBar().showMessage("Out of Stock")
        else:
            self.cur.execute(''' 
                INSERT INTO cart(pro_brand,pro_name,pro_price,quantity,size,pro_photo,itemTotal) 
                VALUES(%s,%s,%s,%s,%s,%s,%s)
            ''',("Everstyle", "Dainty stone neckpiece ", 250,quantity,"-", (':/newPrefix/pics/WhatsApp-Image-2020-12-04-at-6.27.08-PM.png'),total))
            self.db.commit()

            
            self.cur.execute( ''' 
            SELECT  pro_id,pro_brand,pro_name,pro_price,quantity,size,pro_photo FROM cart 
            ''')
            data = self.cur.fetchall()

            
            self.statusBar().showMessage("Item Added to Cart")
            self.enable_cart_no()
            self.statusBarClear()
            self.total()
            self.comboBox_34.setCurrentIndex(0)

            if data:
                self.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(data):
                    self.tableWidget.insertRow(row_number)
                    for column_number, column_data in enumerate(row_data):
                        if(column_number == 6):
                            imgLbl = self.getImageLabel(column_data)
                            self.tableWidget.setCellWidget(row_number,6,imgLbl)
                        else:
                            self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(column_data)))
            else:
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)
        
    def show_in_cart18(self):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()

        quantity = self.comboBox_35.currentText()
        quantity = int(quantity)
        total = 0

        self.cur.execute('''select * from  accessories where a_name =  "Black Hangings" ''')
        info=self.cur.fetchone()
    
        if quantity > info[4]:
            self.statusBar().showMessage("Out of Stock")

        else:
            self.cur.execute( ''' 
                INSERT INTO cart(pro_brand,pro_name,pro_price,quantity,size,pro_photo,itemTotal) 
                VALUES(%s,%s,%s,%s,%s,%s,%s)
            ''',("Everstyle", "Black Hangings ", 200,quantity,"-", (':/newPrefix/pics/WhatsApp Image 2020-12-05 at 10.39.32 AM.jpeg'),total))
            self.db.commit()

            self.cur.execute( ''' 
            SELECT  pro_id,pro_brand,pro_name,pro_price,quantity,size,pro_photo FROM cart 
            ''')
            data = self.cur.fetchall()

            
            self.statusBar().showMessage("Item Added to Cart")
            self.enable_cart_no()
            self.statusBarClear()
            self.total()
            self.comboBox_35.setCurrentIndex(0)

            if data:
                self.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(data):
                    self.tableWidget.insertRow(row_number)
                    for column_number, column_data in enumerate(row_data):
                        if(column_number == 6):
                            imgLbl = self.getImageLabel(column_data)
                            self.tableWidget.setCellWidget(row_number,6,imgLbl)
                        else:
                            self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(column_data)))

            else:
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)       


    def getImageLabel(self,img):
        imageLabel = QtWidgets.QLabel(self.tableWidget)
        imageLabel.setText("")
        imageLabel.setScaledContents(True)
        pixmap = QtGui.QPixmap(img)
        imageLabel.setPixmap(pixmap)
        return imageLabel 
    

    def statusBarClear(self):
        clearBar = threading.Timer(2,self.clearStatusBar)
        clearBar.start()

    def clearStatusBar(self):
        self.statusBar().showMessage('')
    
    def clearLabel(self):
        
        clearLabel = threading.Timer(2,self.clearSetLabel)
        clearLabel.start()

    def clearSetLabel(self):
        self.label_11.setText('')
        self.label_2.setText('')
        self.label.setText('')
        self.label_44.setText('')
        self.label_2.setText('')
        self.label_64.setText('')
        self.label_14.setText('')
        self.label_63.setText('')
        self.label_22.setText('')
        self.label_17.setText('')
        self.label_77.setText('')

    
    def total(self):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()

        self.cur.execute('''select sum(itemTotal) from cart''')
        totalPrice = self.cur.fetchone()
        
        totalPrice = totalPrice[0]
        self.label_10.setText(str(totalPrice))


    def on_click(self,row,column):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()
        x = self.tableWidget.itemAt(row,column)
        y=[]
        y.append(x.text())
        y = y[0]
        self.remove_from_cart(y)

        

    def remove_from_cart(self, pro_id):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()
        warning=QMessageBox.warning(self, 'Remove Item?', "Are you sure you wanna remove this item?", QMessageBox.Yes|QMessageBox.No)
        if warning == QMessageBox.Yes:
            self.cur.execute('''delete from cart where pro_id=%s''',[pro_id])
            self.db.commit()
            self.cartTable()
            self.statusBar().showMessage("Item Removed")
            self.enable_cart_no()
            self.statusBarClear()
            self.total()
            
        else:
            self.statusBar().showMessage('Error deleting item from cart')
            self.statusBarClear()


    def cartTable(self):

        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()

        self.cur.execute('''select pro_id,pro_brand,pro_name,pro_price,quantity,size,pro_photo from cart''')
        data = self.cur.fetchall()
            
        if data:
                
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)
                
                for row_number, row_data in enumerate(data):
                    self.tableWidget.insertRow(row_number)
                    for column_number, column_data in enumerate(row_data):
                        if(column_number == 6):
                            imgLbl = self.getImageLabel(column_data)
                            self.tableWidget.setCellWidget(row_number,6,imgLbl)
                        else:
                            self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(column_data)))
                    

        else:

                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)
      
     

    def place_order(self):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()
        self.cur1 = self.db.cursor()

        self.cur1.execute('''select count(pro_id) from cart''')
        n = self.cur1.fetchone()
        n = n[0]
        n = int(n)

        if n == 0 :
            self.label_11.setText("No items in cart.")
            self.clearLabel()
        
            
        else:
            self.tabWidget.setCurrentIndex(7)
            self.cur.execute('''select sum(itemTotal) from cart''')
            totalPrice = self.cur.fetchone()
            totalPrice = totalPrice[0]
            self.label_53.setText(str(totalPrice))


    def confirm(self):
        
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()
        self.cur1 = self.db.cursor()

        name = self.lineEdit_6.text()
        address = self.lineEdit_4.text()
        amt = self.lineEdit_9.text()


        self.cur.execute('''select sum(itemTotal) from cart''')
        totalPrice = self.cur.fetchone()
        totalPrice = totalPrice[0]
        self.label_53.setText(str(totalPrice))


       
        if name == '' or address == '' or amt == '':
            self.label_44.setText("Please enter name , delivery address also confirm final amount.")
            self.clearLabel()

 
        elif int(amt) != int(totalPrice):
            self.label_44.setText("Invalid amount")   

        else:    
            self.statusBar().showMessage("Valid amount. Order Confirmed!")
            self.clearStatusBar()
            self.cur1.execute('''select count(pro_id) from cart''')
            n = self.cur1.fetchone()
            n = n[0]
            n = int(n)
            self.cur.execute(''' SELECT * FROM cart ''')
            details = self.cur.fetchall()
           
            self.tabWidget.setCurrentIndex(8)

            
            for i in range(0,n):
                self.cur.execute(''' 
                    INSERT INTO orders(orders_name,pro_id , pro_name , pro_brand , pro_price ,pro_quantity,pro_size,pro_photo,del_address,itemTotal) 
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    ''' ,(name,details[i][0],details[i][2],details[i][1],details[i][3],details[i][4],details[i][5],details[i][6],address,details[i][7]))
                self.db.commit()


                if details[i][2] == "Grey Casual Dress":
                    if details[i][5] == str("S"):
                        self.cur.execute('''call reduceQuantityDressesS(%s,%s,%s)''',(details[i][4],"Grey Casual Dress",details[i][5]))
                        self.db.commit()

                    elif details[i][5] == str("M"):
                        self.cur.execute('''call reduceQuantityDressesM(%s,%s,%s)''',(details[i][4],"Grey Casual Dress",details[i][5]))
                        self.db.commit()
                    else:
                        self.cur.execute('''call reduceQuantityDressesL(%s,%s,%s)''',(details[i][4],"Grey Casual Dress",details[i][5]))
                        self.db.commit()   
            

                elif details[i][2] == "OrangeCropTop":
                    if details[i][5] == str("S"):
                        self.cur.execute('''call reduceQuantityTopsS(%s,%s,%s)''',(details[i][4], "OrangeCropTop",details[i][5]))
                        self.db.commit()

                    elif details[i][5] == str("M"):
                        self.cur.execute('''call reduceQuantityTopsM(%s,%s,%s)''',(details[i][4], "OrangeCropTop",details[i][5]))
                        self.db.commit()
                    else:
                        self.cur.execute('''call reduceQuantityTopsL(%s,%s,%s)''',(details[i][4], "OrangeCropTop",details[i][5]))
                        self.db.commit()        


                elif details[i][2] == "BlackTunicTop":
                    if details[i][5] == str("S"):
                        self.cur.execute('''call reduceQuantityTopsS(%s,%s,%s)''',(details[i][4],"BlackTunicTop",details[i][5]))
                        self.db.commit()

                    elif details[i][5] == str("M"):
                        self.cur.execute('''call reduceQuantityTopsM(%s,%s,%s)''',(details[i][4], "BlackTunicTop",details[i][5]))
                        self.db.commit()

                    else:
                        self.cur.execute('''call reduceQuantityTopsL(%s,%s,%s)''',(details[i][4], "BlackTunicTop",details[i][5]))
                        self.db.commit()



                elif details[i][2] == "PinkFloralTop":        
                    if details[i][5]  == str("S"):
                        self.cur.execute('''call reduceQuantityTopsS(%s,%s,%s)''',(details[i][4],"PinkFloralTop",details[i][5]))
                        self.db.commit()

                    elif details[i][5] == str("M"):
                        self.cur.execute('''call reduceQuantityTopsM(%s,%s,%s)''',(details[i][4], "PinkFloralTop",details[i][5]))
                        self.db.commit()

                    else:
                        self.cur.execute('''call reduceQuantityTopsL(%s,%s,%s)''',(details[i][4],"PinkFloralTop",details[i][5]))
                        self.db.commit()

                            
                elif details[i][2] == "BlackMeshTop":     
                    if details[i][5] == str("S"):
                        self.cur.execute('''call reduceQuantityTopsS(%s,%s,%s)''',(details[i][4],"BlackMeshTop",details[i][5]))
                        self.db.commit()
                    elif details[i][5] == str("M"):
                        self.cur.execute('''call reduceQuantityTopsM(%s,%s,%s)''',(details[i][4], "BlackMeshTop",details[i][5]))
                        self.db.commit()
                    else:
                        self.cur.execute('''call reduceQuantityTopsL(%s,%s,%s)''',(details[i][4],"BlackMeshTop",details[i][5]))
                        self.db.commit()

                elif details[i][2] == "PinkTunicTop":
                    if  details[i][5]== str("S"):
                        self.cur.execute('''call reduceQuantityTopsS(%s,%s,%s)''',(details[i][4],"PinkTunicTop", details[i][5]))
                        self.db.commit()

                    elif details[i][5] == str("M"):
                        self.cur.execute('''call reduceQuantityTopsM(%s,%s,%s)''',(details[i][4], "PinkTunicTop" ,details[i][5]))
                        self.db.commit()

                    else:
                        self.cur.execute('''call reduceQuantityTopsL(%s,%s,%s)''',(details[i][4],"PinkTunicTop", details[i][5]))
                        self.db.commit()

                elif details[i][2] == "Black and white Striped shorts":        
                    if  details[i][5] == str("S"):
                        self.cur.execute('''call reduceQuantityBottomS(%s,%s,%s)''',(details[i][4],"Black and white Striped shorts",details[i][5]))
                        self.db.commit()

                    elif details[i][5] == str("M"):
                        self.cur.execute('''call reduceQuantityBottomM(%s,%s,%s)''',(details[i][4], "Black and white Striped shorts",details[i][5]))
                        self.db.commit()

                    else:
                        self.cur.execute('''call reduceQuantityBottomL(%s,%s,%s)''',(details[i][4],"Black and white Striped shorts",details[i][5]))
                        self.db.commit()


                elif details[i][2] == "Torn Blue Denim":            
                    if details[i][5] == str("S"):
                        self.cur.execute('''call reduceQuantityBottomS(%s,%s,%s)''',(details[i][4],"Torn Blue Denim",details[i][5]))
                        self.db.commit()

                    elif details[i][5] == str("M"):
                        self.cur.execute('''call reduceQuantityBottomM(%s,%s,%s)''',(details[i][4],"Torn Blue Denim",details[i][5]))
                        self.db.commit()

                    else:
                        self.cur.execute('''call reduceQuantityBottomL(%s,%s,%s)''',(details[i][4],"Torn Blue Denim",details[i][5]))
                        self.db.commit()

                        
                elif details[i][2] == "Maroon Skirt":  
                    if details[i][5] == str("S"):
                        self.cur.execute('''call reduceQuantityBottomS(%s,%s,%s)''',(details[i][4],"Maroon Skirt",details[i][5]))
                        self.db.commit()

                    elif details[i][5] == str("M"):
                        self.cur.execute('''call reduceQuantityBottomM(%s,%s,%s)''',(details[i][4],"Maroon Skirt",details[i][5]))
                        self.db.commit()

                    else:
                        self.cur.execute('''call reduceQuantityBottomL(%s,%s,%s)''',(details[i][4],"Maroon Skirt",details[i][5]))
                        self.db.commit()

                    
                elif details[i][2] == "Floral Pencil Skirt":
                    if details[i][5] == str("S"):
                        self.cur.execute('''call reduceQuantityBottomS(%s,%s,%s)''',(details[i][4],"Floral Pencil Skirt",details[i][5]))
                        self.db.commit()

                    elif details[i][5] == str("M"):
                        self.cur.execute('''call reduceQuantityBottomM(%s,%s,%s)''',(details[i][4],"Floral Pencil Skirt",details[i][5]))
                        self.db.commit()

                    else:
                        self.cur.execute('''call reduceQuantityBottomL(%s,%s,%s)''',(details[i][4],"Floral Pencil Skirt",details[i][5]))
                        self.db.commit()


                elif details[i][2] == "Blue Denim Dungaree":
                    if details[i][5] == str("S"):
                        self.cur.execute('''call reduceQuantityBottomS(%s,%s,%s)''',(details[i][4],"Blue Denim Dungaree",details[i][5]))
                        self.db.commit()

                    elif details[i][5] == str("M"):
                        self.cur.execute('''call reduceQuantityBottomM(%s,%s,%s)''',(details[i][4],"Blue Denim Dungaree",details[i][5]))
                        self.db.commit()

                    else:
                        self.cur.execute('''call reduceQuantityBottomL(%s,%s,%s)''',(details[i][4],"Blue Denim Dungaree",details[i][5]))
                        self.db.commit()

                elif details[i][2] == "RedGown":
                    if details[i][5] == str("S"):
                        self.cur.execute('''call reduceQuantityDressesS(%s,%s,%s)''',(details[i][4],"RedGown",details[i][5]))
                        self.db.commit()

                    elif details[i][5] == str("M"):
                        self.cur.execute('''call reduceQuantityDressesM(%s,%s,%s)''',(details[i][4],"RedGown",details[i][5]))
                        self.db.commit()

                    else:
                        self.cur.execute('''call reduceQuantityDressesL(%s,%s,%s)''',(details[i][4],"RedGown",details[i][5]))
                        self.db.commit()

                elif details[i][2] == "Yellow Romper Dress":
                    if details[i][5] == str("S"):
                        self.cur.execute('''call reduceQuantityDressesS(%s,%s,%s)''',(details[i][4],"Yellow Romper Dress",details[i][5]))
                        self.db.commit()

                    elif details[i][5] == str("M"):
                        self.cur.execute('''call reduceQuantityDressesM(%s,%s,%s)''',(details[i][4],"Yellow Romper Dress",details[i][5]))
                        self.db.commit()

                    else:
                        self.cur.execute('''call reduceQuantityDressesL(%s,%s,%s)''',(details[i][4],"Yellow Romper Dress",details[i][5]))
                        self.db.commit()

                elif details[i][2] == "Red Skirt and Crop Top":
                    if details[i][5] == str("S"):
                        self.cur.execute('''call reduceQuantityDressesS(%s,%s,%s)''',(details[i][4],"Red Skirt and Crop Top",details[i][5]))
                        self.db.commit()

                    elif details[i][5] == str("M"):
                        self.cur.execute('''call reduceQuantityDressesM(%s,%s,%s)''',(details[i][4],"Red Skirt and Crop Top",details[i][5]))
                        self.db.commit()

                    else:
                        self.cur.execute('''call reduceQuantityDressesL(%s,%s,%s)''',(details[i][4],"Red Skirt and Crop Top",details[i][5]))
                        self.db.commit()

                elif details[i][2] == "Black Skirt and Crop Top":
                    if details[i][5] == str("S"):
                        self.cur.execute('''call reduceQuantityDressesS(%s,%s,%s)''',(details[i][4],"Black Skirt and Crop Top",details[i][5]))
                        self.db.commit()

                    elif details[i][5] == str("M"):
                        self.cur.execute('''call reduceQuantityDressesM(%s,%s,%s)''',(details[i][4],"Black Skirt and Crop Top",details[i][5]))
                        self.db.commit()

                    else:
                        self.cur.execute('''call reduceQuantityDressesL(%s,%s,%s)''',(details[i][4],"Black Skirt and Crop Top",details[i][5]))
                        self.db.commit()

                elif details[i][2] == "Black and Gold Jhumka" or "Ear Cuffs" or "Dainty stone neckpiece" or "Black Hangings" :
                    self.cur.execute('''call reduceQuantityAccessories(%s,%s)''',(details[i][4],details[i][2]))
                    self.db.commit()

                else:
                    print("error")
            
                    
    
   



    def add_new_user(self):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()

        username = self.lineEdit_3.text()
        phone = self.lineEdit_5.text()
        password = self.lineEdit_7.text()
        password2 = self.lineEdit_8.text()
        lx = len(phone)
        if username == '' or phone == '' or password == '' or password2 == '':
               self.label.setText("Please enter a valid data.")
               self.clearLabel()
        

        try:
            if lx==10 and phone.isdigit():
                if password == password2 :
                    self.cur.execute('''INSERT INTO users(user_name , phone , password) VALUES (%s,%s,%s)''',(username , phone, password))
                    self.db.commit()
                    self.statusBar().showMessage('New User Added.')
                    self.statusBarClear()
                    self.tabWidget.setCurrentIndex(2)
                else:
                    self.label.setText("Please enter a valid password twice.")
                    self.clearLabel()
            else:
                self.statusBar().showMessage('Enter a valid phone number')

            
        except:
            self.statusBar().showMessage('User name exists')
            self.clearLabel()

        self.lineEdit_3.setText('')
        self.lineEdit_5.setText('')
        self.lineEdit_7.setText('')
        self.lineEdit_8.setText('')


    def login(self):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()

        username = self.lineEdit_21.text()
        password = self.lineEdit_22.text()

        sql = '''SELECT * FROM users '''
        self.cur.execute(sql)
        data = self.cur.fetchall()
       
        if data:
            for row in data:
                if username == row[1] and password == row[3] :

                    self.statusBar().showMessage("Logged in succesfully.")
                    self.statusBarClear()
                    self.tabWidget.setCurrentIndex(2)
                else:
                    self.label_2.setText("Invalid Username and Password.")
                    self.clearLabel()
    
        self.lineEdit_21.setText('')
        self.lineEdit_22.setText('')

            
    def done(self):
        self.tabWidget.setCurrentIndex(8)


    def clearCart(self):

        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()

        try:
            self.cur.execute('''delete from cart''')
            self.db.commit()

        except:
            pass

    def setTheme(self):
        style = open('stylesheet/darkstyle.css')
        style = style.read()
        self.setStyleSheet(style)

    

    #app = QtWidgets.QApplication(sys.argv)
    #window = QtWidgets.QMainWindow()
    #os.environ['QT_API'] = 'pyqt5'
    #app.setStyleSheet(qdarkstyle.load_stylesheet())


 
  
               
def main():
    app=QApplication(sys.argv)
    window=MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
