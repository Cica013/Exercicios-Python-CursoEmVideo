# Faça um programa que acesse o site pudim
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.youtube.com')
except urllib.error.URLError:
    print('\033[31mO site pudim não está acessível no momento.\033[m')
else:
    print('\033[1;4;32mDeu certo.\033[m')
    print(site.read())
