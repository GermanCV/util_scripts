#!/usr/bin/env python
# -*- coding: utf-8
import os
import time
start_time = time.time()
path = '/media/yuselenin/TOSHIBA EXT[Yuselenin]/Cursos de platzi/'
# path = '/media/yuselenin/Nuevo vol/Cursos de platzi/Introducción a Linux/'
lstFiles = []
lstDir = os.walk(path)
for root, dirs, files in lstDir:
    for fichero in files:
        (nombreFichero, extension) = os.path.splitext(fichero)
        if(extension == ".TS"):
            lstFiles.append(nombreFichero + extension)
            os.rename(root + "/" + nombreFichero + extension,
                      root + "/" + nombreFichero + ".mp4")
print len(lstFiles), " Archivos modificados"
print time.time() - start_time
