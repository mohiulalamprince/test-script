from pyPdf import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from StringIO import StringIO

imgTemp = StringIO()
imgDoc = canvas.Canvas(imgTemp)

imgPath = "/home/mohiulalamprince/work/python/test/like.jpg"
imgDoc.drawImage(imgPath, 490, 259, 90, 90)    ## at (399,760) with size 160x160
imgDoc.save()

page = PdfFileReader(file("/home/mohiulalamprince/work/python/test/SELISE.pdf","rb")).getPage(0)
overlay = PdfFileReader(StringIO(imgTemp.getvalue())).getPage(0)
page.mergePage(overlay)

output = PdfFileWriter()
output.addPage(page)
output.write(file("output.pdf","w"))
