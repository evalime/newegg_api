import requests
import json
from requests.structures import CaseInsensitiveDict

class ServerAccess:
    def __init__(self, sellerId = '', version = '', authorization_key = '', secret_key = '') -> None:
        self.sellerId = sellerId
        self.version = version
        self.authorization_key = authorization_key
        self.secret_key = secret_key
        self.callback = 'https://api.newegg.com/marketplace/'
        self.invUrl = f"{self.callback}contentmgmt/item/international/inventory?sellerid={self.sellerId}"
        self.requestReportUrl = f"{self.callback}reportmgmt/report/submitrequest?sellerid={self.sellerId}&version={self.version}"
        self.statusUrl = f"{self.callback}reportmgmt/report/status?sellerid={self.sellerId}"
        self.resourceUrl = f"{self.callback}reportmgmt/report/result?sellerid={self.sellerId}"

    def header(self):
        self.headers = CaseInsensitiveDict()
        self.headers["Authorization"] = self.authorization_key
        self.headers["SecretKey"] = self.secret_key
        self.headers["Accept"] = "application/json"
        self.headers["Content-Type"] = "application/json"
        return self.headers
 
    def updateInventory(self,invReports):
        self.status = []
        self.error_msg = []
        for invReport in invReports['inventory']:
            self.data =json.dumps(invReport)
            reqInv = requests.post(self.invUrl, headers=self.header(), data = self.data)
            if reqInv.status_code == 400:
                self.error_msg.append( f"{invReport['Value']} {reqInv.json()[0]['Message']}")
            else:                
                self.status.append(reqInv.status_code)
        return self.status, self.error_msg


    def requestReport(self, inventoryReportType):
        self.jsonInventoryReportType = json.dumps(inventoryReportType)
        self.reqReports = requests.post(self.requestReportUrl, headers=self.header(), data = self.jsonInventoryReportType)
        self.requestId = self.reqReports.json()['ResponseBody']['ResponseList'][0]['RequestId']
        return self.requestId
    
    def requestStatus(self, statusReport):
        self.jsonStatusReport = json.dumps(statusReport)
        self.statusReports = requests.put(self.statusUrl, headers=self.header(), data = self.jsonStatusReport)
        self.status = self.statusReports.json()
        return self.status

    def requestSource(self, sourceReport):
        self.jsonSourceReport = json.dumps(sourceReport)
        self.souceReports = requests.put(self.resourceUrl, headers=self.header(), data = self.jsonSourceReport)
        self.source = self.souceReports.json()
        return self.source
