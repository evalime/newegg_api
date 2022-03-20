import pandas as pd
import datetime
import os
import zipfile

class Inventory:
    def __init__(self,sbt_loc,newegg_loc):
        self.sbt_loc = sbt_loc
        self.newegg_loc = newegg_loc
        pass

    def openSbtInv(self):
        self.cols = ['item','onhand','aloc']
        self.inv = pd.read_excel(self.sbt_loc, usecols = self.cols, engine='xlrd')
        self.inv['total'] = self.inv['onhand'] - self.inv['aloc']
        self.inv.drop(['onhand','aloc'],axis=1,inplace=True)
        return self.inv

    def check_inv(self):
        self.invDate = datetime.datetime.fromtimestamp(os.path.getctime(self.sbt_loc))
        return self.invDate.strftime("%d/%m/%y")
    
    def openNeweggInv(self): #Unzipping the Newegg SKU List
        self.cols = ['Seller Part #','Fulfillment Option','Inventory']
        self.sheet_name = 'BatchInventoryUpdate'
        
        self.file = os.listdir(self.newegg_loc)
        zf = zipfile.ZipFile(f'{self.newegg_loc}{self.file[0]}')
        self.filename = zf.namelist()[0]
        self.neweggSKU = pd.read_excel(zf.open(self.filename),sheet_name=self.sheet_name,header=1,usecols=self.cols)
        self.neweggSKU = self.neweggSKU[self.neweggSKU['Fulfillment Option']=='Seller']
        zf.close()
        return self.neweggSKU
    
    def delNeweggInv(self): #Delete old Newegg SKU list
        file = os.listdir(self.newegg_loc)
        if file:
            os.remove(f'{self.newegg_loc}{file[0]}')

    def todayDate(self):
        return datetime.datetime.today().strftime("%d/%m/%y")