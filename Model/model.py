#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 13:47:10 2022

@author: secke
"""

import requests
import pymysql
#import json
#import inspect

################ RÉCUPÉRATION DES API'S ###############
lien="https://jsonplaceholder.typicode.com/users"
reponse=requests.get(lien)

f=reponse.json()
###################################################

######## data ADDRESS #############
addr=[]
for s in f:
    addr.append(s['address'])
###################################
class address():
    def __init__(self):
        self.conext=pymysql.connect(user='root',password='secke2022',host='localhost',database='API_db')
        self.stylo=self.conext.cursor()
    def ajout(self):
        self.donnees=addr
        for a in self.donnees:
            self.stylo.execute("insert into address (street,suite,city, zipcode,lat,lng) values (%s,%s,%s,%s,%s,%s)",(a['street'],a['suite'],a['city'],a['zipcode'],a['geo']['lat'],a['geo']['lng']))
            #self.vid.append(a)
            #self.vid=a['street']
        #return self.vid
    def avoir(self):
        self.stylo.execute("select * from address")
        return self.stylo.fetchall()
    
    def modifier(self,donne,idt):
        self.stylo.execute("update address set street=%s, suite=%s, city=%s, zipcode=%s,lat=%s, lng=%s where id=%s",
                           (donne[0],donne[1],donne[2],donne[3],donne[4],donne[5],idt))
        return self.conext.commit()
    
    def supprimer(self,idt):
        self.stylo.execute("delete from address where id=%s",
                           (idt,))
        return self.conext.commit()
    
    def valider(self):
        self.conext.commit()
      
ob=address()


######## data USER #############
util=[]
for r in f:
    util.append((r['phone'],r['name'],r['username'],r['email']))

######################################################################

class user():
    def __init__(self):
        self.connex=pymysql.connect(user='root',password='secke2022',host='localhost',database='API_db')
        self.stylo=self.connex.cursor()
    def ajt(self):
        #self.obb=address()
        #self.recup=self.obb.ajout(addr)
        #self.recup1=self.obb.avoir()
        #self.adres=addr.copy()
        self.utill=[]
        self.vvid=[]
        self.stylo.execute("select id,zipcode from address")
        for rec in self.stylo.fetchall():
            self.vvid.append(rec)
        for i in range(len(addr)):
            if self.vvid[i][1]==addr[i]['zipcode']:
                self.utill.append((self.vvid[i][0],f[i]['phone'],f[i]['name'],
                                   f[i]['username'],f[i]['email']))
        
        for j in self.utill:
            self.stylo.execute("insert into user (idAdd, phone, name, username, email) values (%s,%s,%s,%s,%s)",  (j[0],j[1],j[2],j[3],j[4]))
        #return self.utill
        
    def avr(self):
        self.stylo.execute("select * from user")
        return self.stylo.fetchall()
    
    
    
    
    
    
    
    
    def valid(self):
        self.connex.commit()
ss=user()


########################### CLASS COMPANY ################################
comp=[]
for c in f:
    comp.append(c['company'])
class company():
    def __init__(self):
        self.connext=pymysql.connect(user='root',password='secke2022',host='localhost',database='API_db')
        self.stylo=self.connext.cursor()
    def ajouter(self):
        self.donne=[]
        self.recup=[]
        self.stylo.execute("select id, name from user")
        for i in self.stylo.fetchall():
            self.recup.append(i)
        for j in range(len(util)):
            if self.recup[j][1]==util[j][1]:
                self.donne.append((self.recup[j][0],f[j]['company']['name'],f[j]['company']['catchPhrase'],
                                   f[j]['company']['bs']))
        for k in self.donne:
            self.stylo.execute("insert into company (idUser,name,catchPhrase,bs) values (%s,%s,%s,%s)",
                               (k[0],k[1],k[2],k[3]))
    def obtenir(self):
        self.stylo.execute("select * from company")
        return self.stylo.fetchall()
    
    
    def valide(self):
        self.connext.commit()


dd=company()



############################# CLASS POST ##################################

lien_p="https://jsonplaceholder.typicode.com/posts"
reponse_p=requests.get(lien_p)

f_p=reponse_p.json()


class post():
    def __init__(self):
        self.connex=pymysql.connect(user='root',password='secke2022',host='localhost',database='API_db')
        self.stylo=self.connex.cursor()
    def ajout(self):
        #self.donnee=[]
        #self.recup=[]
        #self.stylo.execute("select id, name from user")
        #for i in self.stylo.fetchall():
         #   self.recup.append(i)
        
        for j in f_p:
            #if self.recup[1]==util[1]:
            #for v in range(len(util)):
             #   if self.recup[v][1]==util[v][1]:
                    #self.iduser=self.recup[v][0]
              #      self.donnee.append((self.recup[v][0],j['title'],j['body']))
             self.stylo.execute("insert into post (idUser,title,body) values (%s,%s,%s)",
                                 (j['userId'],j['title'],j['body']))
        #for k in self.donnee:
            #self.stylo.execute("insert into post (idUser,title,body) values (%s,%s,%s)",
             #                  (k[0],k[1],k[2]))
        
    def obtenir(self):
        self.stylo.execute("select * from post")
        return self.stylo.fetchall()
    
    def cinq(self):
        self.stylo.execute("select * from post limit 5")
        return self.stylo.fetchall()
    
    def valider(self):
        self.connex.commit()


ff=post()

########################### CLASS COMMENTS ################################
lien_c="https://jsonplaceholder.typicode.com/comments"
reponse_c=requests.get(lien_c)

f_c=reponse_c.json()

class comments():
    def __init__(self):
        self.connex=pymysql.connect(user='root',password='secke2022',host='localhost',database='API_db')
        self.stylo=self.connex.cursor()
    
    def ajout(self):
        #self.donnee=[]
        #self.recup=[]
        #self.stylo.execute("select id, title from post")
        #for i in self.stylo.fetchall():
         #   self.recup.append(i)
        for j in f_c:
          #  for el in range(len(f_p)):
           #     if self.recup[el][1]==f_p[el]['title']:
            #        self.donnee.append((self.recup[el][0],j['name'],j['email'],j['body']))
            self.stylo.execute("insert into comments (idPost,name,email,body) values(%s,%s,%s,%s)",
                               (j['postId'],j['name'],j['email'],j['body']))
        #for k in self.donnee:
           # self.stylo.execute("insert into comments (idPost,name,email,body) values(%s,%s,%s,%s)",
            #                   (k[0],k[1],k[2],k[3]))
    def obtenir(self):
        self.stylo.execute("select * from comments")
        return self.stylo.fetchall()
    
    
    def valider(self):
        self.connex.commit()

gg=comments()


############################# CLASS TODOS ######################################
lien_t="https://jsonplaceholder.typicode.com/todos"
reponse_t=requests.get(lien_t)

f_t=reponse_t.json()

class todos():
    def __init__(self):
        self.connex=pymysql.connect(user='root',password='secke2022',host='localhost',database='API_db')
        self.stylo=self.connex.cursor()
    def ajout(self):
        #self.donnee=[]
        #self.recup=[]
        #self.stylo.execute("select id,phone from user")
        #for i in self.stylo.fetchall():
         #   self.recup.append(i)
        #for j in range(len(f_t)):
         #   for el in range(len(self.recup)):
          #      if self.recup[el][1]==util[el][0]:
                    #iduser=self.recup[0]
           #         self.donnee.append((self.recup[el][0],f_t[j]['title']))
        for elemt in f_t:
            self.stylo.execute("insert into todos (idUser,title) values (%s,%s)", 
                               (elemt['userId'],elemt['title']))
        #for k in self.donnee:
           # self.stylo.execute("insert into todos (idUser,title) values (%s,%s)", 
            #                   (k[0],k[1]))
    def obtenir(self):
        self.stylo.execute("select * from todos")
        return self.stylo.fetchall()
    
    
    
    def valider(self):
        self.connex.commit()
        

hh=todos()

############################### CLASS ALBUMS #######################################
lien_alb="https://jsonplaceholder.typicode.com/albums"
reponse_alb=requests.get(lien_alb)

f_alb=reponse_alb.json()

class albums():
    def __init__(self):
        self.connex=pymysql.connect(user='root',password='secke2022',host='localhost',database='API_db')
        self.stylo=self.connex.cursor()
    def ajout(self):
        #self.donnee=[]
        #self.recup=[]
        #self.stylo.execute("select id, name from user")
        #for i in self.stylo.fetchall():
         #   self.recup.append(i)
        for j in f_alb:
            #for el in range(len(util)):
             #   if self.recup[el][1]==util[el][1]:
              #      iduser=self.recup[el][0]
               # self.donnee.append((iduser,j['title']))
            self.stylo.execute("insert into albums (idUser,title) values (%s,%s)", 
                               (j['userId'],j['title']))
        #for k in self.donnee:
         #   self.stylo.execute("insert into albums (idUser,title) values (%s,%s)", 
          #                     (k[0],k[1]))
    def obtenir(self):
        self.stylo.execute("select * from albums")
        return self.stylo.fetchall()
   
    
    
    def valider(self):
        self.connex.commit()


jj=albums()


############################### CLASS PHOTOS #######################################
lien_ph="https://jsonplaceholder.typicode.com/photos"
reponse_ph=requests.get(lien_ph)

f_ph=reponse_ph.json()

class photos():
    def __init__(self):
        self.connex=pymysql.connect(user='root',password='secke2022',host='localhost',database='API_db')
        self.stylo=self.connex.cursor()
    def ajout(self):
        for ele in f_ph:
            self.stylo.execute("insert into photos (idAlb,title,url,thumbnailUrl) values (%s,%s,%s,%s)",
                               (ele['albumId'],ele['title'],ele['url'],ele['thumbnailUrl']))
    
    def obtenir(self):
        self.stylo.execute("select * from photos")
        return self.stylo.fetchall()
   
    
    
    def valider(self):
        self.connex.commit()


ll=photos()
