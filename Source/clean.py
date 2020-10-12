import csv
import re
from os import path

def cleanData(folder):
    npath, nfile = path.split(folder)
    lstFile = nfile.split('.')

    lstReview = []
    with open(folder) as file: 
        reader = csv.reader(file)
        for row in reader:
            lst = []
            for element in row:
                if element[0] == '[' : 
                     lst.append(element.strip('[]').replace("'","").split(", "))
                else:
                    lst.append(element)
            lstReview.append(lst)
    
    for  count, Review in enumerate(lstReview[1:], 1): 
        lst = []
        for sentence in Review[1]:
            lst.append(re.sub('[^.,a-zA-ZñÑáÁéÉíÍóÓúÚ0-9. \n\.]', '', sentence.replace('_',',')))
        lstReview[count][1] = lst
    
    with open(npath + '/Clean_' + lstFile[0] + '.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(lstReview)