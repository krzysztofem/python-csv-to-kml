import sys
from bs4 import BeautifulSoup as Soup
from rich.console import Console
from rich.theme import Theme
from modules.getKMLstyle import getKMLstyleList
from modules.createPlacemark import createPlacemark
import xml.dom.minidom
import pandas as pd
from datetime import datetime
from config import PERIODS as CONFIG



fileSource = sys.argv[1]

customConsoleTheme = Theme({"sucess": "green"})
console = Console(theme=customConsoleTheme)
console.print('')
console.print(" ***************************** ")
console.print("        🧭 CSV to KML 📌        ")
console.print(" ***************************** ")
console.print('')

fileCSV = open('_source-for-map/znaleziska.csv', 'r')

# load kml template file
with open('templates/kml-document.xml') as data:
    kml_document = Soup(data, 'lxml-xml')  

# find document
document = kml_document.find('Document')

# load points styles
for k,v in CONFIG.items():
    el = CONFIG.get(k)
    stylesList = getKMLstyleList(el.get('styleId'), el.get('iconUrl'))
    for el in stylesList:
        document.append(Soup(el, 'xml'))


data = pd.read_csv(fileSource)
console.print('💾 Loading data from  [bold magenta]%s[/bold magenta]' % fileSource)
# data = pd.read_csv("_source-for-map/znaleziska.csv")
# dataRowsLength = data.shape[0]


console.print('')
console.print('⚙️  Processing data ... ')
console.print('')

for key,value in CONFIG.items():
    # create google maps <Folder>
    newFolder = Soup('<Folder>', 'xml')
    # append <name> to <Folder>
    newFolder.Folder.append(Soup('<name>%s</name>' % key, 'xml'))

    # filter by period and iterate by period items
    df2 = data[data['Okres']==key]
    # console.print(key, len(df2))
    console.print('📌 [magenta]%s[/magenta] => [bold]%s[/bold]' % (key, len(df2)))
    for index, row in df2.iterrows():
        config = CONFIG.get(row['Okres'])
        newPlacemark = Soup(createPlacemark(
                row['Numer'], row['Id znaleziska'], 
                row['Znalazca'], row['Okres'], 
                config.get('styleId'), 
                row['GPS E'], 
                row['GPS N']
            ), 'xml')
        newFolder.Folder.append(newPlacemark)
    
    # append <Folder> to <Document>        
    document.append(newFolder)


# convert to xml for google maps
xml = xml.dom.minidom.parseString(str(kml_document).replace("\n", ""))
xml_pretty_str = xml.toprettyxml()

# save kml document to file
dateTime = datetime.now().strftime("%Y_%m_%d-%I_%M_%S")

fileName = 'kml-map-%s.kml' % dateTime
with open(fileName, "w", encoding = 'utf-8') as file:    
    file.write(str(xml_pretty_str))

console.print('')
console.print('💾 Done! 💪 Saved to =>  [bold magenta]%s[/bold magenta]' % fileName)
console.print('')