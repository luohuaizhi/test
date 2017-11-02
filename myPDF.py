from pdfminer.pdfinterp import PDFResourceManager#, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content


def main():
    with open(r"D:\code\tk\dainihai_general_product.pdf", "r") as f:
        outputString = readPDF(f)
    print(outputString)


if __name__ == '__main__':
    main()