import os
import sys
import json

from dotenv import find_dotenv, load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)


import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


class NetworkSecurityData():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json(self,file_path) -> str:
        """
        Convert the DataFrame to JSON format.
        """
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_to_mongo(self,records, collection_name,database):
        """
        Insert the data into MongoDB.
        """
        try:
            self.database=database
            self.collection_name=collection_name
            self.records=records
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.db=self.mongo_client[self.database]
            self.collection=self.db[self.collection_name]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__=='__main__':
    FILE_PATH="networkdata\phisingData.csv"
    DATABASE="NetworkSecurity"
    COLLECTION_NAME="NetworkData"
    networkobj=NetworkSecurityData()
    records=networkobj.csv_to_json(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_to_mongo(records,COLLECTION_NAME,DATABASE)
    print(f"Number of records inserted: {no_of_records}")


