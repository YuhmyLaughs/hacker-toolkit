import PyPDF2
from PyPDF2 import PdfFileReader

fileName=input("Type Filename with  \'.pdf\' at the end...\n ::>")
pdfFile = PdfFileReader(open(fileName, 'rb'))
docInfo = pdfFile.getDocumentInfo()
print ('[*] PDF MetaData For: ' + str(fileName))
for metaItem in docInfo:
        print( '[+] ' + metaItem + ':' + str(docInfo[metaItem].encode('utf-8')))