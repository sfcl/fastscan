#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# скрипт написал Хозяинов М. Л. Почта:  m.hozyainov@gmail.com

import configparser
import time
import os
import re
import tkinter as tk
import sys
from mylib import convertToDosPath
from mylib import getImageFromScanner
from mylib import setWindowCenter

from mywrapperpdflib import PdfMerge

# версия программы
Version = '0.2.3'


# производим нормализацию файловых путей
# temp_folder = os.path.abspath(temp_folder)
# one_file_folder = os.path.abspath(one_file_folder)
# multiple_file_folder = os.path.abspath(multiple_file_folder)


def ScanOnePage(file_name = None, adf=False):
    # имя файла выбираем исходя из тайм штампа
    if file_name is None:
        file_name = int(time.time())
        file_name = str(file_name)
    
    parametrs = {'color': '', 'rezolution': '', 'adf': ''}
    if colorQuestion.get() == 1:
        parametrs['color'] = 'GRAY'
    if colorQuestion.get() == 2:
        parametrs['color'] = 'RGB'
    if rezQuestion.get() == 1:
        parametrs['rezolution'] = '300'
    if rezQuestion.get() == 2:
        parametrs['rezolution'] = '600'
    
    parametrs['adf'] = adf
    
    getImageFromScanner(file_name, temp_folder, one_file_folder, multiple_file_folder, parametrs)
    #if  colorQuestion.get() != '1':
    #    getImageFromScanner(file_name, temp_folder, one_file_folder, multiple_file_folder, color)
    #else:
    #    getImageFromScanner(file_name, temp_folder, one_file_folder, multiple_file_folder)
    
    # возвращаем переключателей в исходное сотояние
    colorQuestion.set(1)
    rezQuestion.set(1)
    
# Работает с GUI
class msgBox(object):
    def __init__(self, parent, text_content):
        self.root = parent
        parent.withdraw()
        top = self.top = tk.Toplevel(parent)
        setWindowCenter(self.top)
        #self.top.geometry("200x50")
        sendText = text_content
        self.L1 = tk.Label(top, text=sendText)
        self.L1.pack()
        self.top.protocol("WM_DELETE_WINDOW", self.showPar)
    
    def showPar(self):
        self.root.update()
        self.root.deiconify()
        self.top.destroy()
        
class errorMsqBox(msgBox):
    def __init__(self, parent, text_content):
        msgBox.__init__(self, parent, text_content)
        self.top.protocol("WM_DELETE_WINDOW", self._quit) 
        self.button = tk.Button(self.top, text='OK', command=self._quit)
        self.button.pack(side='bottom')
        
    def _quit(self):
        sys.exit(1)

class MyDialog:
    def __init__(self, parent):
        self.root = parent
        parent.withdraw()
        self.tempList = list()
        top = self.top = tk.Toplevel(parent, relief=tk.SUNKEN)
        setWindowCenter(self.top)
        self.top.geometry("440x120")
        #print dir(self.top)
        #self.top.overrideredirect(True)
        self.top.protocol("WM_DELETE_WINDOW", self._quit) 
        self.button1_1 = tk.Button(top, padx=5, pady=5, bd=4, text='Отсканировать одну страницу', command=self.scanOnePage)
        self.button1_1.grid(row=0, column=0)
        #self.button1_1.pack()
        
        self.button1_2 = tk.Button(top, padx=5, pady=5, bd=4, text='Завершить сканирование',command=self.stopScan)
        self.button1_2.grid(row=0, column=1)
        
        self.parametrs = {'color' :'', 'rezolution': '', 'adf': ''}
        if colorQuestion.get() == 1:
            self.parametrs['color'] = 'GRAY'
        if colorQuestion.get() == 2:
            self.parametrs['color'] = 'RGB'
        if rezQuestion.get() == 1:
            self.parametrs['rezolution'] = '300'
        if rezQuestion.get() == 2:
            self.parametrs['rezolution'] = '600'
        if adf.get() == 0:
            self.parametrs['adf'] = False
        if adf.get() == 1:
            self.parametrs['adf'] = True

        self.labelframe2 = tk.LabelFrame(top, text='Параметры сканирования')
        self.labelframe2.grid(row=1, column=0)
        
        self.l1 = tk.Label(self.labelframe2, text = "Цветность: " + self.parametrs['color'] )
        self.l1.pack(side='bottom')
        
        self.l2 = tk.Label(self.labelframe2, text = "Разрешение: " + self.parametrs['rezolution'] )
        self.l2.pack(side='bottom')
        #self.button1_2.pack()

    def scanOnePage(self):
        self.file_name = int(time.time())
        self.file_name = str(self.file_name)
        self.tempList.append(self.file_name)
        ScanOnePage(self.file_name)


    def stopScan(self):
        PdfMerge(self.tempList, one_file_folder, multiple_file_folder)
        self.root.update()
        self.root.deiconify()
        
        # возвращаем переключателей в исходное сотояние
        colorQuestion.set(1)
        rezQuestion.set(1)
        self.top.destroy()
    
    def _quit(self):
        pass
    

    
def createNewWindow():
    #ScanOnePage()
    inputDialog = MyDialog(root)
    root.wait_window(inputDialog.top)

def showMsgBox():
    
    mb = msgBox(root, 'Автор программы: Хозяинов Максим\nПочта: sfcl@mail.ru\nВерсия:' + ' ' + Version)
    root.wait_window(mb.top)
    
    
root = tk.Tk()
setWindowCenter(root)

# читаем настройки программы из конфигурационного файла
config = configparser.ConfigParser()
config.read('config.ini')

# инициализируем значения переменных, хранящих пути
temp_folder = config.get('PathConfiguration', 'temp_folder' )
one_file_folder = config.get('PathConfiguration', 'one_file_folder' )
multiple_file_folder = config.get('PathConfiguration', 'multiple_file_folder' )

if temp_folder == 'none' or one_file_folder == 'none' or multiple_file_folder == 'none':
    txt = 'Вы не настроили каталоги в файле config.ini'
    errorMsqBox(root, txt)
    #sys.exit(1)


button1 = tk.Button(root, padx=5, pady=5, bd=4, text='Многостраничное\nсканирование', command=(lambda : createNewWindow()))
button1.grid(row=0, column=0)
#button1.pack(side="left")


button2 = tk.Button(root, padx=5, pady=5, bd=4, text='Одностраничное\nсканирование', command=(lambda : ScanOnePage(adf=False)))
button2.grid(row=0, column=1)
#button2.pack(side="left")

button3 = tk.Button(root, padx=5, pady=5, bd=4, text='АПД', command=(lambda : ScanOnePage(adf=True)))
button3.grid(row=0, column=2)


colorQuestion = tk.IntVar()
colorQuestion.set("1")

rezQuestion = tk.IntVar()
rezQuestion.set("1")

adf = tk.IntVar()
adf.set('0')
# фрейм определяющий цветность
labelframe = tk.LabelFrame(root, text='Цветность сканирования')
#labelframe.pack(side='left')
labelframe.grid(row=1, column=0)

radioButton1 = tk.Radiobutton(labelframe, text = "ЧБ", variable=colorQuestion, value="1")
radioButton2 = tk.Radiobutton(labelframe, text = "Цветное", variable=colorQuestion, value="2")
radioButton2.pack(side='bottom')
radioButton1.pack(side='bottom')

# фрейм определяющий разрешение сканирования
labelframe2 = tk.LabelFrame(root, text='Разрешение сканирования')
labelframe2.grid(row=1, column=1)

radioButton3 = tk.Radiobutton(labelframe2, text = "300 dpi", variable=rezQuestion, value="1")
radioButton4 = tk.Radiobutton(labelframe2, text = "600 dpi", variable=rezQuestion, value="2")
radioButton4.pack(side='bottom')
radioButton3.pack(side='bottom')



# фрейм определяющий кнопку для вызова справки
labelframe3 = tk.LabelFrame(root, text='')
labelframe3.grid(row=1, column=2)
button_help = tk.Button(labelframe3, text='?', command=(lambda : showMsgBox()))
#button_help.pack(side="bottom", fill='', expand=False, padx=4, pady=4)
#button_help.pack(side="right")
button_help.pack(side='bottom')


root.title('Помощник в сканировании')
root.geometry("360x120")
root.mainloop()

