#from xml.etree.ElementTree import Element, SubElement, Comment, tostring
#file = open('2-Uberit.txt', 'r')
#x = file.read()
#y = x.split("\n\n\n")
#top = Element('England')
#
#i = 0
#for item in y:
#    if i%2==0:
#        child = SubElement(top, 'item')
#        title = SubElement(child, 'title')
#        title.text = item
#    else:
#        body = SubElement(child, 'body')
#        body.text = item 
#    i+=1
#print(tostring(top))

x = "1 -"
int(x[0:2])