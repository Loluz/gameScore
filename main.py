import cherrypy, os
from htmlGenerator import HtmlGenerator
from archivo,csv import
archivo = open("archivo.csv", "r")
for line in archivo.readlines():
    print(line.split(",")[0]);

archivo.close()

archivo = open("archivo.csv", "r")
for line in archivo.readlines():
    print(line.split(",")[1]);

archivo.close()