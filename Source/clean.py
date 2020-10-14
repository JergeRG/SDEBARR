import csv
import re
from os import path

def cleanData(col):
    
    for doc in col.find({}):
        lst = []
        for sentence in doc['Sentences']:
            lst.append(re.sub('[^.,a-zA-ZñÑáÁéÉíÍóÓúÚ0-9. \n\.]', '', sentence))
            
        col.update_one({'ID':doc['ID']},{'$set':{'Limpio':lst}})
            