# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 18:49:28 2018

@author: KrySt
"""




hrac = input("Jak se jmenuje zadávající?: ")
slovo = input(hrac + ", vyber slovo, které budou ostatní hádat: ")
print ("\n" * 100)
print ("Začněte hádat!")
pokusy = ''
tahy = 10
while tahy > 0:         
    zbyva = 0             
    for char in slovo:      
        if char in pokusy:    
            print (char,)  
        else:
            print ("_",)     
            zbyva += 1    
    if zbyva == 0:        
        print ("Vyhrál jsi")  
        break         
    print    
    pokus = input("       Uhádni písmeno: ") 
    pokusy += pokus   
    print ("\n" * 100)             
    if pokus not in slovo:  
        tahy -= 1       
        print ("Špatně")
        print ("Máš další", + tahy, "tahy" )
        if tahy == 0:    
            print ("\n" * 100)
            print ("Prohrál jsi")
