#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror

from PyPDF2 import PdfFileWriter, PdfFileReader

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Расщепление PDF")
        self.master.rowconfigure(5, weight=1)
        self.master.columnconfigure(5, weight=1)
        self.grid(sticky=W+E+N+S)

        self.button = Button(self, text="Выбрать файл", command=self.load_file, width=10)
        self.button.grid(row=1, column=0, sticky=W)


    def load_file(self):
        fname = askopenfilename(filetypes=(("Pdf файл", "*.pdf"), ))
        print(fname)
        preparePdf = fname
        tmpPreparePdf = open(preparePdf, 'rb')
        inputpdf = PdfFileReader(tmpPreparePdf)
        tmpPreparePdf.close()
        print(type(inputpdf.getNumPages()))
        #print('Кол-во страниц в PDF = ', inputpdf.numPages)
        # for i in range(inputpdf.numPages):
            # pagenumber = i+1
            # output = PdfFileWriter()
            # output.addPage(inputpdf.getPage(i))
            # fileName = "F:\\MAXIM_work\\fast_scan\\project\\openfile\\splitfiles\\page-%s.pdf" % ( pagenumber, )
            # tmpFilePointer = open(fileName, 'wb')
            # output.write(tmpFilePointer)
            # tmpFilePointer.close()
        # if fname:
            # try:
                # print("""here it comes: self.settings["template"].set(fname)""")
            # except:                     # <- naked except is a bad idea
                # showerror("Open Source File", "Failed to read file\n'%s'" % fname)
            # return


if __name__ == "__main__":
    MyFrame().mainloop()
