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