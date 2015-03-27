#!/usr/bin/env python
# -*- coding:utf-8 -*-

import ntpath
import subprocess
import os
import tkinter as tk
#import pyx
from PIL import Image

# TODO добавить корректное преобразование Русских символов

def convertToDosPath(prepare_str):
    prepare_str = ntpath.abspath(prepare_str)
    tempList = prepare_str.split(os.sep)
    for i in range(0, len(tempList)):
        tempList[i] = tempList[i].upper()
        if len(tempList[i]) > 8:
            tmp = tempList[i][0:6] + r'~1'
            tempList[i] = tmp
    
    return '\\'.join(tempList)
    

def getImageFromScanner(tmp_file_name, temp_folder, one_file_folder, multiple_file_folder, params):
    # Получаем место расположения скрипта
    # ~~~~~
    #base_path = os.path.dirname(os.path.realpath(__file__)) 
    #exec_path = base_path  + '.\\bin'
    exec_path = '.\\bin'
    #command_line_exec =  exec_path + '\\' + 'CmdTwain' + ' /PAPER=A4 /%s /DPI=%s /JPG75 ' + temp_folder + '\\' + tmp_file_name + '.jpg'
    command_line_exec =  exec_path + '\\' + 'ScanBmp' + ' /PAPER=A4 /%s /DPI=%s ' + temp_folder + '\\' + tmp_file_name + '.jpg'
    command_line_exec = command_line_exec % (params['color'], params['rezolution'],)
    #print(command_line_exec)
    #if color == '1':
    #    command_line_exec =  exec_path + '\\' + 'CmdTwain' + ' /PAPER=A4 /RGB /DPI=300 /JPG75 ' + temp_folder + '\\' + tmp_file_name + '.jpg'
    #else:
    #    command_line_exec =  exec_path + '\\' + 'CmdTwain' + ' /PAPER=A4 /GRAY /DPI=300 /JPG75 ' + temp_folder + '\\' + tmp_file_name + '.jpg'
    
    #if color == '1': 
        # выполняем сканирование через командную строку через программу IrfanView
    #    command_line_exec =  exec_path + '\\' + 'i_view32' + ' /scanhidden /dpi=(300,300) /gray /convert=' + temp_folder + '\\' + tmp_file_name + '.jpg'
    #if color == '2':
    #    command_line_exec =  exec_path + '\\' + 'i_view32' + ' /scanhidden /dpi=(300,300) /convert=' + temp_folder + '\\' + tmp_file_name + '.jpg'
    
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.SW_HIDE
    subprocess.call(command_line_exec, startupinfo=si)
    
    #os.system(command_line_exec)
    #print(command_line_exec)

    # архаизм который нужно выпилить отсюда
    #command_line_exec2 = exec_path + '\\' + 'jpg2pdf.exe ' + '-o ' + one_file_folder + '\\' + tmp_file_name + '.pdf ' + temp_folder + '\\' + tmp_file_name + '.jpg'
    #command_line_exec2 =  exec_path + '\\' + 'img2pdf.exe ' + '"' + temp_folder + '\\' + tmp_file_name + '.jpg" ' + '"' + one_file_folder + '\\' + tmp_file_name + '.pdf" '
    #si = subprocess.STARTUPINFO()
    #si.dwFlags |= subprocess.SW_HIDE
    #subprocess.call(command_line_exec2, startupinfo=si)
    #print(command_line_exec2)
    #os.system(command_line_exec2)
    tmp_file = temp_folder + '\\' + tmp_file_name + '.jpg'
    if os.path.exists(tmp_file):
        
        output_file = one_file_folder + '\\' + tmp_file_name + '.pdf'
        im = Image.open(tmp_file)
        im.save(output_file, 'PDF')
        os.remove(tmp_file)
    #i = pyx.bitmap.jpegimage(tmp_file)
    #c = pyx.canvas.canvas()
    #c.insert(pyx.bitmap.bitmap(0, 0, i, compressmode=None))
    #c.writePDFfile(output_file)
    # подчищаем за собой каталог tmp (делаем это тихо)
    #command_line_exec3 = 'del /f /s /q ' + temp_folder + '\*.jpg' + ' > nul'
    #os.popen(command_line_exec3)
    #tmpFilename = temp_folder + '\\' + tmp_file_name + '.jpg'
    
    #print (command_line_exec3)
    

def setWindowCenter(rootObj):
    rootObj.update_idletasks()
    ws = rootObj.winfo_screenwidth()
    hs = rootObj.winfo_screenheight()
    
    w = rootObj.winfo_width()
    h = rootObj.winfo_height()
    
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    
    #rootObj.geometry('%dx%d+%d+%d' % (w, h, x, y))
    rootObj.geometry('+%d+%d' % (x, y,))

if __name__ == '__main__':
    tmpStr = r'F:\MAXIM_work\Новая папка\fast_scan\bin'
    print(convertToDosPath(tmpStr))
