# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 09:08:31 2020

@author: pedro-salj

https://www.datacamp.com/community/tutorials/exception-handling-python?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=332602034364&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=1001593&gclid=CjwKCAiAq8f-BRBtEiwAGr3DgQQVaEWhBNdc0E9Pw3UHzU5ka3NrRoxAAFIuEdOExdRW3O8XvUEg5RoCthcQAvD_BwE
"""

try:  
    a = 100 / 0
    print (a)
except ZeroDivisionError:  
        print ("Zero Division Exception Raised." )
else:  
    print ("Success, no error!")
    
    
    
    