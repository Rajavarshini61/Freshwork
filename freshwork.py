# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 19:50:26 2020

@author: MYPC
"""


import os.path
import time
import ast
print("enter the path to be stored if not interested enter no:\n")
save_path=str(input())
if(save_path=='no'):
    save_path = 'D:/example/'
    
print("enter what should be done:\n1.create\n2.Read\n3.Delete\n")
n=int(input())
name_of_file = "hey"
completeName = os.path.join(save_path, name_of_file+".txt") 
dic={}

if(n==1):
    print("enter the key :\n")
    s=input()
    print("enter the value :\n")
    v=input()
    print("enter the time-to-live or 0:\n")
    t=int(input())
    
    
    if s.isalpha()==False:
        print('\nkey should be an string\n')
    else:
        if s in dic:
            print('\nkey already present!\n')
        else:
            if len(dic)<1024*1024*1024 and len(v)<16*1024:
                if t==0:
                    dic[s]=[v,t]
                else:
                    dic[s]=[v,time.time()+t]
            else:
                print('\nthe data storage shld have less than 1GB and 16KB lesser value\n')
    file = open(completeName, "w")
    file.write(str(dic))
    file.close()
    
if(n==2):
    print("enter the key to read:\n")
    s=input()
    
    file = open(completeName, "r")
    dicti=file.read()
    dic = ast.literal_eval(dicti)
    
    if s in dic:
        if (dic[s][1]==0 or dic[s][1]>time.time()):
            
            print("\nread value : \n {}".format(dic[s][0]))
        else:
            print("\ntime-to-live property has expired!\n")
    else:
        print("\nthe key does not exist!!\n")
        
    file = open(completeName, "w")
    file.write(str(dic))
    file.close()

if(n==3):
    print("\nenter the key to delete :\n")
    s=input()
    
    file = open(completeName, "r")
    dicti=file.read()
    dic = ast.literal_eval(dicti)
    
    if s in dic:
        if (dic[s][1]==0 or dic[s][1]>time.time()):
            del dic[s]
            print("\ndeleted {} key\n".format(str(s)))
        else:
            print("\ntime-to-live property has expired!\n")
    else:
        print("\nthe key does not exist!!\n")
        
    file = open(completeName, "w")
    file.write(str(dic))
    file.close()
