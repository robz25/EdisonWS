#!/usr/bin/python
# -*- coding: utf-8  -*-
#Script de Python para enviar datos de sensores a PVcloud usando Edison

import os, time, mraa, urllib2

suAPPID = "CambieEsteValorYDejeLasComillas"
suAPIKEY = "CambieEsteValorYDejeLasComillas"

etiqueta0 = 'Val_Sensor_0'
etiqueta1 = 'Val_Sensor_1'

a0 = mraa.Aio(0)#Sensor 0
a1 = mraa.Aio(1)#Sensor 1

try:
  while(1):
    s0 = a0.read()
    s1 = a1.read()
    info = '{'+etiqueta0+': "'+str(s0)+'",'+etiqueta1+':"'+str(s1)+'"}'
    linkprueba = 'https://costaricamakers.com/pvcloud/backend/vse.php/appdata_write_get/'+suAPPID+'/'+suAPIKEY+'/NombreDeLosDatos/'
    linklisto = 'https://costaricamakers.com/pvcloud/backend/vse.php/appdata_write_get/'+suAPPID+'/'+suAPIKEY+'/NombreDeLosDatos/%7B%22'+etiqueta0+'%22:%20%22'+str(s0)+'%22,%20%22'+etiqueta1+'%22:%22'+str(s1)+'%22%7D'
    linkprueba = linkprueba + info
    print linkprueba
    #Ejecutar subidas a PV cloud por medio de http con el link de prueba
    #urllib2.urlopen(linkprueba)
    #Ejecutar subidas a PV cloud por medio de http
    urllib2.urlopen(linklisto)
    print "Enviado: ", info

except KeyboardInterrupt:
  print "\nTerminado"
