import xml.etree.ElementTree as ET 
import csv
from os import path 

def extractTree(folder):
    with open(folder, 'r') as file:
        data = file.read()
    return ET.fromstring(data)
    
def extractData(folder):
    tree = extractTree(folder)
    npath, nfile = path.split(folder)
    lstFile = nfile.split('.')
    
    lstReview = [['Id', 'Sentences', 'Aspects', 'Polarities']]
    for review in tree.findall('Review'):
        rid = review.get('rid')
        lstSentence = []
        lstAspect = []
        lstPolarity = []
        for sentence in review.find('sentences').findall('sentence'):
            lstSentence.append(sentence.find('text').text)
        for opinion in review.find('Opinions').findall('Opinion'):
            lstAspect.append(opinion.get('category'))
            lstPolarity.append(opinion.get('polarity'))
        lstReview.append([rid, lstSentence, lstAspect, lstPolarity])
        
        with open(npath + '/' + lstFile[0] + '.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerows(lstReview)