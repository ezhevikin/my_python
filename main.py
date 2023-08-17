#!/bin/python3

import subprocess

#subprocess.run(["sudo", "apt", "-y", "install", "guake"])

#list_files = subprocess.run(["sudo", "mkdir", "/home/temp"]) #создание временной папки для файлов
#list_files = subprocess.run(["sudo", "mkdir", "/home/temp/install_pack"])

#скачивание файлов для установки
#subprocess.run(["wget", "-O", "/home/temp/cades.tar.gz", "https://cryptopro.ru/products/cades/plugin/get_2_0/cades-linux-amd64.tar.gz"])

#распаковка скачанного архива в папку /home/temp
#subprocess.run(["sudo", "tar", "-xf", "/home/temp/cades.tar.gz", "-C", "/home/temp/install_pack"])
subprocess.run(["sudo tar -xf /home/temp/cades.tar.gz -C /home/temp/install_pack"], shell = True)

#print("-----------------------------install CRYPTOPRO")
#subprocess.run(["sh /home/temp/crypto/install.sh lsb-cprocsp-kc1 cprocsp-rdr-gui-gtk cprocsp-cptools-gtk cprocsp-stunnel lsb-cprocsp-pkcs11"], shell=True)

#print("---------------Install_prog_from_pack.list----------------")
#subprocess.run(["sudo xargs -a /home/temp/pack.list apt-get install"], shell=True)
#print("--------------Fix_broken_install-------------")
#subprocess.run(["sudo apt --fix-broken install"], shell=True)

#subprocess.run(["sudo dpkg -i /home/temp/install_pack/*/*.deb"], shell=True)
print("Hello")
print("Hello")