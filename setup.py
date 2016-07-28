#!/usr/bin/env python

import os

os.system("mkdir /opt/elpscrk")
print "[+] Criando diretorios do arquivo..."
os.system("mv elpscrk.py /opt/elpscrk/elpscrk.py")
print "[+] Configurando o arquivo..."
os.system("chmod 777 /opt/elpscrk/elpscrk.py")
print "[+] Dando permissoes necessarias para o arquivo..."
fl = open(os.path.expanduser('~')+"/.bashrc", "a")
print "[+] Criando atalho para o terminal..."
fl.write("alias elpscrk='/opt/elpscrk/elpscrk.py'")
print "[+] Instalado com sucesso..."
