from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, ElementTree
from xml.dom import minidom
import sys

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def createXML(gDrive, country, folderId, outFile):
  try:
    #files stored in dictionary file_list with index as key and text as value
    drive_file_list = drive.ListFile({'q': "'"+folderId+"' in parents and trashed=false"}).GetList()
    file_list = {} 
    for file1 in drive_file_list:
      #print('title: %s, id: %s' % (file1['title'], file1['id']))
      file1.GetContentFile(file1['title'],'text/plain')
      file = open(file1['title'], 'r')
      content = file.read()
      index = int(file1['title'][:2]) #get index from title
      file_list[index]=content

    top = Element("Country") #Create xml tree
    countryCode = SubElement(top,"CountryCode")
    countryCode.text = country

    #Iterates through all possible key values. Adds text value to XML tree
    for f in range(0,len(file_list)*2):
      try:
        c = file_list[f]
        if(c!=None):
          navigation = SubElement(top, 'Navigation')
          c = c.replace("\n \n","\n\n") #removes single space character from newline
          y = c.split("\n\n\n\n")
          i = 0
          for item in y:
            item = item.strip()
            item = item.replace("\n\n\n","\n\n")
            if i==0:
              navTitle = SubElement(navigation, 'Navigation_Title')
              navTitle.text = item
            elif i==1:
              icon = SubElement(navigation, 'Navigation_Icon')
              icon.text = item.lower().replace(" ","") #navigation icon text gets lower case version of string
            elif i%2==0:
              child = SubElement(navigation, 'Details_Item')
              title = SubElement(child, 'Item_Title')
              title.text = item
            else:
              body = SubElement(child, 'Item_Body')
              body.text = item 
            i+=1

      except KeyError:
        pass
      index+=1
    #write XML output  
    output = open("xmlDocs/"+outFile+'.xml','w')
    #print(tostring(top))
    output.write(prettify(top))
  except KeyError:
    print(country+" failed")
    

#Access Drive

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
drive = GoogleDrive(gauth)

if len(sys.argv)==2: #Single argument, a document name with countryName,folderID pairs separated by lines
  countries = open(sys.argv[1], 'r').read().split("\n")
  for country in countries:
    country = country.split(",")
    createXML(drive, country[0], country[1], country[2])
else: #Three arguments, Country ID, FolderID, Country name specified in command line
  createXML(drive, sys.argv[1], sys.argv[2],sys.argv[3])



