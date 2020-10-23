import csv
import re
from os import path

def cleanData(col):
    
    for doc in col.find({}):
        lstSentences = []
        CleanReview = re.sub('[^.,a-zA-ZñÑáÁéÉíÍóÓúÚ0-9. \n\.]', '', doc['Review'])
        for sentence in doc['Sentences']:
            lstSentences.append(re.sub('[^.,a-zA-ZñÑáÁéÉíÍóÓúÚ0-9. \n\.]', '', sentence))
            
        col.update_one({'ID':doc['ID']},{'$set':{'CleanReview':CleanReview,'CleanSentences':lstSentences}})
            