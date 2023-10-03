"""Crie um código em Python que teste se o site pudim
está acessível por este computador."""
import urllib.request
from urllib.error import URLError

try:
    site = urllib.request.urlopen("http://pudim.com.br")
except URLError:
    print("O site não está acessível no momento!")
else:
    print("Acesso ao site com sucesso")
# print(site.read)
