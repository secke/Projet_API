#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 22:59:47 2022

@author: secke
"""

#import tkinter as tk
import sys
sys.path.append('.')
sys.path.append('..')
#from model import *
import Model.model as model
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
    

class supprimer():
    def __init__(self):
        self.addres=model.address()
        self.user=model.user()
        self.company=model.company()
        self.post=model.post()
        self.comments=model.comments()
        self.todos=model.todos()
        self.albums=model.albums()
        self.photos=model.photos()
    def suppAddres(self):
        self.x=self.addres.supprimer()
        return self.x
    def suppUser(self):
        self.x=self.user.supprimer()
        return self.x
    
    def suppCompany(self):
        self.x=self.company.supprimer()
        return self.x
    def suppPost(self):
        self.x=self.post.supprimer()
        return self.x
    def suppComments(self):
        self.x=self.comments.supprimer()
        return self.x
    def suppTodos(self):
        self.x=self.todos.supprimer()
        return self.x
    def suppAlbums(self):
        self.x=self.albums.supprimer()
        return self.x
    def suppPhotos(self):
        self.x=self.photos.supprimer()
        return self.x