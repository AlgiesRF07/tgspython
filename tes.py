# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 07:46:18 2021

@author: L
"""


print("Algies Rifkha Fadillah")   
type(5)


def pelangi(warna):
  print(f'Salah satu warna pelangi adalah {warna}')
  

class namaClass():
    def __init__(self):
        print("Hallo World")
cetak = namaClass()


def odd(n):
 hasil = n % 2
 if hasil != 0:
     hasilnya=True
 else:
     hasilnya=False
 return hasilnya


class Point:
    def reset(self): 
        self.x = 0
        self.y  = 0

p = Point() 
p.reset() 
print(p.x, p.y)

