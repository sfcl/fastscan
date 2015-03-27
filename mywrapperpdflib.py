#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# скрипт написал Хозяинов М. Л. Почта:  m.hozyainov@gmail.com

import configparser
from PyPDF2 import PdfFileMerger, PdfFileReader
import os
import time


def PdfMerge(filenames, onFFolder, mulFFolder):
    if len(filenames) == 0:
        return 
        
    merger = PdfFileMerger()
    tmpContent = ''
    for filename in filenames:
        filename = onFFolder + '\\' + filename + '.pdf'
        if os.path.exists(filename):
            tp = open(filename, 'rb')
            merger.append(PdfFileReader(tp))
            tp.close()
            os.remove(filename)

        
    file_name = int(time.time())
    file_name = str(file_name)

    outputfile = mulFFolder + '\\' + file_name + ".pdf"
    merger.write(outputfile)


if __name__ == '__main__':
    # читаем настройки программы из конфигурационного файла
    config = configparser.ConfigParser()
    config.read('config.ini')

    # инициализируем значения переменных, хранящих пути
    temp_folder = config.get('PathConfiguration', 'temp_folder' )
    one_file_folder = config.get('PathConfiguration', 'one_file_folder' )
    multiple_file_folder = config.get('PathConfiguration', 'multiple_file_folder' )
    # написать скрипт по смене файла для сканирования

    # производим нормализацию файловых путей
    temp_folder = os.path.abspath(temp_folder)
    one_file_folder = os.path.abspath(one_file_folder)
    multiple_file_folder = os.path.abspath(multiple_file_folder)
    
    filelist = ['1414381672', '1414381691', '1414381712']
    
    PdfMerge(filelist, one_file_folder, multiple_file_folder)