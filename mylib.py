#!/usr/bin/env python
# -*- coding:utf-8 -*-

import ntpath
import subprocess
import os
import tkinter as tk
from PIL import Image
from mywrapperpdflib import PdfMerge

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
    exec_path = '.\\bin'
    #command_line_exec =  exec_path + '\\' + 'CmdTwain' + ' /PAPER=A4 /%s /DPI=%s /JPG75 ' + temp_folder + '\\' + tmp_file_name + '.jpg'
    if params['adf']:
        # очищаем tmp каталог от временных файлов
        filelist = [ f for f in os.listdir(temp_folder) ]
        for f in filelist:
            f = os.path.join(temp_folder, f)
            os.remove(f)

        command_line_exec =  exec_path + '\\' + 'ScanBmp' + ' /PAPER=A4 /%s /DPI=%s /S %s val* ' + '"' + temp_folder + '\\' + tmp_file_name + '.jpg' + '"'
        command_line_exec = command_line_exec % (params['color'], params['rezolution'], 'ADF')
    else:
        command_line_exec =  exec_path + '\\' + 'ScanBmp' + ' /PAPER=A4 /%s /DPI=%s ' + '"' + temp_folder + '\\' + tmp_file_name + '.jpg' + '"'
        command_line_exec = command_line_exec % (params['color'], params['rezolution'])
    
    print('command_line_exec=', command_line_exec)
    #if color == '1':
    #    command_line_exec =  exec_path + '\\' + 'CmdTwain' + ' /PAPER=A4 /RGB /DPI=300 /JPG75 ' + temp_folder + '\\' + tmp_file_name + '.jpg'
    #else:
    #    command_line_exec =  exec_path + '\\' + 'CmdTwain' + ' /PAPER=A4 /GRAY /DPI=300 /JPG75 ' + temp_folder + '\\' + tmp_file_name + '.jpg'
    

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
    if params['adf']:
        filelist = [ f for f in os.listdir(temp_folder) ]
        pdf_files_list = list()
        for fitem in filelist:
            tmp_file = os.path.join(temp_folder, fitem)
            fitem = os.path.splitext(fitem)[0]
            output_file = one_file_folder + '\\' + fitem + '.pdf'
            with Image.open(tmp_file) as im:
                im.save(output_file, 'PDF')
            try:
                os.remove(tmp_file)
            except:
                pass

            # сохраням в список только имя файла без расшерения и пути
            output_file = os.path.basename(output_file)
            output_file = os.path.splitext(output_file)[0]
            pdf_files_list.append(output_file)
        
        PdfMerge(pdf_files_list, one_file_folder, multiple_file_folder)

    else:
        tmp_file = temp_folder + '\\' + tmp_file_name + '.jpg'
        if os.path.exists(tmp_file):
            output_file = one_file_folder + '\\' + tmp_file_name + '.pdf'
            with Image.open(tmp_file) as im:
                im.save(output_file, 'PDF')
            try:
                os.remove(tmp_file)
            except:
                pass
        

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
    #tmpStr = r'F:\MAXIM_work\Новая папка\fast_scan\bin'
    #print(convertToDosPath(tmpStr))
    pass
