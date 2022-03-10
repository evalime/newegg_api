class RequestBody:
    def __init__(self) -> None:
        pass

    def inventoryType(self): 
        self.inventoryReportType = {
            "OperationType": "InternationalInventoryReportRequest",
            "RequestBody": {
            "DailyInventoryReportCriteria": {
                "FulfillType": "0",
                "WarehouseList": {
                    "WarehouseLocation":
                        "USA"
                    },
                    "RequestType": "INTERNATIONAL_INVENTORY_REPORT",
                    "FileType": "XLS"
                    }
                }
            }
        return self.inventoryReportType
    
    def statusType(self,ID):
        self.statusReport = {
            "OperationType": "GetReportStatusRequest",
            "RequestBody": {
                "GetRequestStatus": {
                    "RequestIDList": {
                        "RequestID": ID
                    },
                    "MaxCount": "10"
                }
            }
        }
        return self.statusReport
    
    def sourceType(self,ID):
        source = {
            "OperationType": "InternationalInventoryReportRequest",
            "RequestBody": {
                "RequestID": ID,
                "PageInfo": {
                    "PageSize": "10",
                    "PageIndex": "1"
                }
            }
        }
        return source

    def inventoryUpdateType(self,lists):
        self.inventoryDict = {'inventory':[]}
        for k, v in lists.items():
            self.inventoryFormat = {
                "Type": "1",
                "Value": k,
                "InventoryList": {
                    "Inventory": [
                        {
                            "WarehouseLocation": "USA",
                            "AvailableQuantity": v
                        }
                    ]
                }
            }
            self.inventoryDict['inventory'].append(self.inventoryFormat)
        return self.inventoryDict