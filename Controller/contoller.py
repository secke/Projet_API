#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 22:59:47 2022

@author: secke
"""

#import tkinter as tk
import sys
sys.path.insert(1,'/home/secke/projet_API/Model')
#from model import *
import model
#mon_ob=model.address()

#mon_ob.ajout()
#x=mon_ob.avoir()
#print(x)

class afficher():
    def __init__(self):
        self.addres=model.address()
        self.user=model.user()
        self.company=model.company()
        self.post=model.post()
        self.comments=model.comments()
        self.todos=model.todos()
        self.albums=model.albums()
        self.photos=model.photos()
        
        
    
    def avoirAddres(self):
        self.x=self.addres.avoir()
        return self.x
    def avoirUser(self):
        self.x=self.user.avr()
        return self.x
    
    def avoirCompany(self):
        self.x=self.company.obtenir()
        return self.x
    def avoirPost(self):
        self.x=self.post.obtenir()
        return self.x
    def avoirComments(self):
        self.x=self.comments.obtenir()
        return self.x
    def avoirTodos(self):
        self.x=self.todos.obtenir()
        return self.x
    def avoirAlbums(self):
        self.x=self.albums.obtenir()
        return self.x
    def avoirPhotos(self):
        self.x=self.photos.obtenir()
        return self.x
    
