#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 21:02:36 2022

@author: secke
"""
import sys
sys.path.append('.')
sys.path.append('..')
import Controller.controller as controller
from mes_entetes import *
from tabulate import tabulate


class voir():
    def __init__(self):
        self.obj=controller.afficher()

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



class supprimer():
    def __init__(self):
        self.obj=controller.supprimer()

    def supAddres(self):
        self.sup=self.obj.suppAddres()
        return self.sup
    def supUser(self):
        self.sup=self.obj.suppUser()
        return self.sup
    def supCompany(self):
        self.sup=self.obj.suppCompany()
        return self.sup
    def supPost(self):
        self.sup=self.obj.suppPost()
        return self.sup
    def supComments(self):
        self.sup=self.obj.suppComments
        return self.sup
    def supTodos(self):
        self.sup=self.obj.suppTodos
        return self.sup
    def supAlbums(self):
        self.sup=self.obj.suppAlbums()
        return self.sup
    def supPhotos(self):
        self.sup=self.obj.suppPhotos
        return self.sup
    

    
    
    
    
    
    
    
class Menu:   
    def affichage():
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
                aff=tabulate(obj_Addr,headers=entete.entAdd())
                print(aff)
            elif y=='2':
                obj_User=voir().voirUser()
                aff=tabulate(obj_User,headers=entete.entUser())
                print(aff)
            elif y=='3':
                obj_Compt=voir().voirCompany()
                aff=tabulate(obj_Compt,headers=entete.entComp())
                print(aff)
            elif y=='4':
                obj_Post=voir().voirPost()
                aff=tabulate(obj_Post,headers=entete.entPost())
                print(aff)
            elif y=='5':
                obj_Comment=voir().voirComments()
                aff=tabulate(obj_Comment,headers=entete.entComt())
                print(aff)
            elif y=='6':
                obj_Todos=voir().voirTodos()
                aff=tabulate(obj_Todos,headers=entete.entTodo())
                print(aff)
            elif y=='7':
                obj_Alb=voir().voirAlbums()
                aff=tabulate(obj_Alb,headers=entete.entAlb())
                print(aff)
            elif y=='8':
                obj_Photo=voir().voirPhotos()
                aff=tabulate(obj_Photo,headers=entete.entPh())
                print(aff)
        
        
            elif y=='0':
                print("A BIENTÔT!")
                break

client=Menu
client.affichage()