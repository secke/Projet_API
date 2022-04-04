#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 21:02:36 2022

@author: secke
"""
import sys
sys.path.insert(1,'/home/secke/projet_API/Controller')
import contoller



class voir():
    def __init__(self):
        self.obj=contoller.afficher()
        #self.ob_User=contoller.
        #self.ob_Addres=contoller.afficher()
        #self.ob_Addres=contoller.afficher()
        #self.ob_Addres=contoller.afficher()
        #self.ob_Addres=contoller.afficher()
        #self.ob_Addres=contoller.afficher()
        #self.ob_Addres=contoller.afficher()
    def voirAddres(self):
        self.vr=self.obj.avoirAddres()
        return self.vr
    def voirUser(self):
        self.vr=self.obj.avoirUser()
        return self.vr
    def voirCompany(self):
        self.vr=self.obj.avoirCompany()
        return self.vr
    def voirPost(self):
        self.vr=self.obj.avoirPost()
        return self.vr
    def voirComments(self):
        self.vr=self.obj.avoirComments()
        return self.vr
    def voirTodos(self):
        self.vr=self.obj.avoirTodos()
        return self.vr
    def voirAlbums(self):
        self.vr=self.obj.avoirAlbums()
        return self.vr
    def voirPhotos(self):
        self.vr=self.obj.avoirPhotos()
        return self.vr
    
    

    
    
    
    
    
    
    
    
while True:
    print("###################################")
    print("###         MENU                ###")
    print("###################################")
    print("1: Afficher les informations de ADDRESS")
    print("2: Afficher les informations de USER")
    print("3: Afficher les informations de COMPANY")
    print("4: Afficher les informations de POST")
    print("5: Afficher les informations de COMMENTS")
    print("6: Afficher les informations de ALBUMS")
    print("7: Afficher les informations de TODOS")
    print("8: Afficher les informations de PHOTOS")
    print("0: Pour QUITTER")
    y=input("entrer votre choix: ")
    if y=='1':
        obj_Addr=voir().voirAddres()
        print(obj_Addr)
    elif y=='2':
        obj_User=voir().voirUser()
        print(obj_User)
    elif y=='3':
        obj_Compt=voir().voirCompany()
        print(obj_Compt)
    elif y=='4':
        obj_Post=voir().voirPost()
        print(obj_Post)
    elif y=='5':
        obj_Comment=voir().voirComments()
        print(obj_Comment)
    elif y=='6':
        obj_Todos=voir().voirTodos()
        print(obj_Todos)
    elif y=='7':
        obj_Alb=voir().voirAlbums()
        print(obj_Alb)
    elif y=='8':
        obj_Photo=voir().voirPhotos()
        print(obj_Photo)
        
        
    elif y=='0':
        print("A BIENTÔT!")
        break
            