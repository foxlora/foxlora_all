# -*- coding: utf-8 -*-
'''

'''
__author__ = 'Foxlora'
__time__ = '2020/11/6 12:42'

from socket import *
s = socket(AF_INET, SOCK_STREAM)
# s.sendto(b'',('localhost',14000))
s.connect(('localhost', 16000))
print(s.send(b'Hello'))
print(s.recv(234))