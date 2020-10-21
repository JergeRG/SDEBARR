import xml.etree.ElementTree as ET 
import csv
from os import path 

def extractTree(folder):
    with open(folder, 'r') as file:
        data = file.read()
    return ET.fromstring(data)
    
def extractData(folder,col):
    tree = extractTree(folder)
    npath, nfile = path.split(folder)
    lstFile = nfile.split('.')
    
    lstReview = [['Id', 'Sentences', 'Aspects', 'Polarities']]
    totalReviews, totalSentences  = 0, 0
    dictAspects, dictPolarities = {}, {}
    for review in tree.findall('Review'):
        textReview = ""
        totalReviews = totalReviews + 1 
        rid = review.get('rid')
        lstSentence, lstAspect, lstPolarity = [], [], []
        for sentence in review.find('sentences').findall('sentence'):         
            totalSentences = totalSentences + 1
            lstSentence.append(sentence.find('text').text)
            textReview +=" "+ sentence.find('text').text
        for opinion in review.find('Opinions').findall('Opinion'):
            aspect = opinion.get('category').split('#')[0]
            lstAspect.append(aspect)
            if aspect in dictAspects:
                dictAspects[aspect] = dictAspects[aspect] + 1 
            else:
                dictAspects[aspect] = 0
            
            polarity = opinion.get('polarity')
            if polarity in dictPolarities:
                dictPolarities[polarity] = dictPolarities[polarity] + 1 
            else:
                dictPolarities[polarity] = 0
            lstPolarity.append(polarity)
        textReview = textReview[1:]
        col.insert_one({
            'ID':rid,
            'Sentences':lstSentence,
            'Aspectos':lstAspect,
            'Polaridad':lstPolarity
        })
        
                
    with open(npath + '/Resume_' + lstFile[0] + '.txt', 'w') as file:
        file.write('*'*10 + 'Resumen de datos leídos' +'*'*10 + '\n')
        file.write('\t Total de reseñas leídas:\t' + str(totalReviews) + '\n')
        file.write('\t Total de parrafos leídas:\t' + str(totalSentences) + '\n')
        file.write('\t Total de aspectos hallados:' + '\n')
        for (key, value) in dictAspects.items():
            file.write('\t\t' + str(key) + ':\t' + str(value) + '\n')
        file.write('\t Total de polaridades halladas:' + '\n')   
        for (key, value) in dictPolarities.items():
            file.write('\t\t' + str(key) + ':\t' + str(value) + '\n')
            