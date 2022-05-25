import os
import pathlib
import csv
import re
import logging
import datetime
import sys
  
sys.path.append('../foliocommunication')
from FolioCommunication import FolioCommunication

logging.basicConfig(filename='/usr/local/bin/python_scripts/logs/automaticRenewals.log', filemode = 'a', level=logging.INFO)

try:
    folio = FolioCommunication()

    userBarcode = ""
    itemBarcode = ""

    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    todayPlusTwo = today + datetime.timedelta(days=3)


    data = folio.getLoansByDueDate(str(tomorrow), str(todayPlusTwo))



    for loan in data['loans']:

        itemBarcode = loan['item']['barcode']
        userBarcode = loan['borrower']['barcode']

        #print("Title:   " + loan['item']['title'])
        #print("dueDate: " + loan['dueDate'])
        #print("-------------------------------------")


        result = folio.renewByBarcode(itemBarcode, userBarcode)
    
    logging.info("Renewals ok " + str(today))
except:
    logging.error("Renewals error " + str(today))


