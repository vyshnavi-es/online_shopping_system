with open('OrangeCropTop.png','rb') as f:
    m=f.read()
    print(m)


"""def add_to_tops_tunics_dresses(self):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()

        with open('OrangeCropTop','rb') as f:
            top_photo = f.read()

        self.cur.execute("""
        INSERT INTO tops,tunics and dresses(top_brand, top_name, top_price, top_photo) 
        VALUES(%s,%s,%s,%s)""",(Ali express, Orange Crop Top, 400 ,top_photo)))
     """  
  with open('OrangeCropTop.png','rb') as file:
        m=file.read()
        print(m)







        sql='''SELECT * FROM tops_tunics_and_dresses WHERE top_name =%s '''
        self.cur.execute(sql, [("OrangeCropTop")])
        data = self.cur.fetchall()

        sql1= ''' INSERT INTO cart(pro_name,pro_brand,pro_price,pro_photo) VALUES(%s,%s,%s,%s)''',("Aliexpress", "OrangeCropTop", 400, (':/newPrefix/pics/Orange Crop Top.png'))
        self.db.commit()
        self.statusBar().showMessage("Item Added to Cart")
        



        
 """def showTableData(self):
        for row_number, row_data in enumerate(data):
            self.tableWidget.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                item = str(column_data);
                if(column_data!=4):
                    self.tableWidget.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(item))"""



                    def show_in_cart5(self):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()

        sql='''SELECT * FROM tops_tunics_and_dresses WHERE top_name =%s '''
        self.cur.execute(sql, [("Black and white Striped shorts")])
        data = self.cur.fetchall()

        self.cur.execute(''' INSERT INTO cart(pro_brand,pro_name,pro_price,pro_photo) VALUES(%s,%s,%s,%s)''',("Myntra", "Black and white Striped shorts", 400, ((:/pics/WhatsApp-Image-2020-12-03-at-9.51.43-PM-_1_.png')))
        self.db.commit()
        

        self.statusBar().showMessage("Item Added to Cart")

        
        if data:
            for row_number, row_data in enumerate(data):
                self.tableWidget.insertRow(row_number)
                for column_number, column_data in enumerate(row_data):
                    item = str(column_data)
                    if(column_data == 4):
                        self.tableWidget.setCellWidget(row_number,column_number,label_18)
                    else:
                        self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(item))


                         
    def womens_wear(self):
        tops = self.comboBox.CurrentIndex(0)
        bottoms = self.comboBox.CurrentIndex(1)
        dresses= self.comboBox.CurrentIndex(2)

        if self.comboBox.CurrentIndex(0):
            self.tabWidget_3.setCurrentIndex(0)
        elif self.comboBox.CurrentIndex(1):
            self.tabWidget_3.setCurrentIndex(1)
        else:
            self.tabWidget_3.setCurrentIndex(2)




""" def place_order(self):
        self.tabWidget.setCurrentIndex(7)

        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()

        name = self.lineEdit_11.text()
        del_address = self.lineEdit_4.text()

        self.cur.execute('''select sum(pro_price) from cart''')
        totalPrice = self.cur.fetchone()
        totalPrice = totalPrice[0]
        self.label_53.setText(str(totalPrice))

        self.cur.execute(''' SELECT * FROM cart ''')
        details = self.cur.fetchall()

        sql = INSERT INTO orders('''orders_name,pro_name,pro_brand,pro_price,pro_photo,del_address) VALUES (%s,%s,%s,%s,%s,%s)''',(name, details[2], details[1], details[])"""
        




           self.cur.execute('''INSERT INTO orders(orders_name,pro_name,pro_brand,pro_price,pro_photo,del_address) VALUES (%s,%s,%s,%s,%s,%s)''',(name, details[2], details[1], totalPrice, details[4],del_address))
        self.db.commit()



        def setTheme(self):

        style = open('style.css')
        style = style.read()
        self.setStyleSheet(style)

         self.setTheme()


          self.cur.execute('''
            INSERT INTO tops_tunics_and_dresses(quantity,size)
            VALUES(%s,%s)
        ''',(quantity,size))
        self.db.commit()


       

          warning=QMessageBox.warning(self, 'Remove Item?', "Are you sure you wanna remove this item?", QMessageBox.Yes|QMessageBox.No)
        if warning == QMessageBox.Yes:
            sql = ''' DELETE FROM cart WHERE pro_name = %s '''
            self.cur.execute(sql, [(enter_name)])
            self.db.commit()
            self.statusBar().showMessage("Item Removed")

        if data:
            for row_number, row_data in enumerate(data):
                self.tableWidget.insertRow(row_number)
                for column_number, column_data in enumerate(row_data):
                    if column_number == 6:
                        imgLbl = self.getImageLabel(column_data)
                        self.tableWidget.setCellWidget(row_number,6,imgLbl)
                    else:
                        self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(column_data)))



     # set the environment variable to use a specific wrapper
    # it can be set to pyqt, pyqt5, pyside or pyside2 (not implemented yet)
    # you do not need to use QtPy to set this variable
    os.environ['QT_API'] = 'pyqt5'

    # import from QtPy instead of doing it directly
    # note that QtPy always uses PyQt5 API
    from qtpy import QtWidgets

    # create the application and the main window
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()

    # setup stylesheet
    # the default system in qdarkstyle uses qtpy environment variable
    app.setStyleSheet(qdarkstyle.load_stylesheet())



  else:
            self.tableWidget.setRowCount(0)
            self.tableWidget.insertRow(0)   

 def excel(self):
        self.db = MySQLdb.connect(host='localhost' ,user='root' ,password='vyshnavies_13',db='shopping')
        self.cur = self.db.cursor()

        try:
            self.cur.execute('''select orders_name,pro_id,pro_name,pro_brand,pro_price,pro_quantity,pro_size,del_address,itemTotal from orders''')
            bill = self.cur.fetchall()
            x = datetime.now()
            xlName = 'Details-' + str(x.day) + '-' + str(x.month) + '-' + str(x.year) + '-' + str(x.hour) + '-' + str(
                x.minute) + '-' + str(x.second)
            xlDate = str(x.day) + '-' + str(x.month) + '-' + str(x.year)
            XL = Workbook(xlName + '.xlsx')
            S1 = XL.add_worksheet()

            S1.write(1, 0, 'Details' + xlDate)
            S1.write(3, 0, 'Name')
            S1.write(3, 1, 'product id')
            S1.write(3, 2, 'product name')
            S1.write(3, 3, 'product brand')
            S1.write(3, 4, 'product price')
            S1.write(3, 5, 'product quantity')
            S1.write(3, 6, 'product size')
            S1.write(3, 7, 'delivery address')
            S1.write(3, 8, 'Total')

            rowPos = 9
            for row in bill:
                colPos = 0
                for i in row:
                    S1.write(rowPos, colPos, str(i))
                    colPos += 1
                rowPos += 1

            self.statusBar().showMessage('Bill generated.')
            XL.close()

        except:
            self.statusBar().showMessage('Unable to export to excel')