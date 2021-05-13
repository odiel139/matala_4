# -*- coding: utf-8 -*-
"""
Created on Tue May 11 03:31:25 2021

@author: odiel
"""
#import pprint
import json
import requests
#import urllib
from heapq import nlargest
import sys

def cities (text_doc_name,my_apy_key):
    text_doc_name=text_doc_name+".txt"
    file=open(text_doc_name,encoding='utf-8')
    file = file.readlines()
    apy_key=my_apy_key
    dict_fars=dict()
    the_dictionary=dict()
    count=0
    
    try:    
        for line in file:
            if count==5:
                break
            dict_length=dict()
            dict_width=dict()
            the_tupel_info=tuple()
            line=line.strip()
            city=line
            print(city)
            source='תל אביב'
            dest=city
            url1="https://maps.googleapis.com/maps/api/distancematrix/json?"
            try:
                response=requests.get(url1+'origins='+source+'&destinations='+dest+'&key='+apy_key)
                if not response.status_code==200:
                    print("HTTP error",response.status_code)
                else:
                    print(response)
                    try:
                        response_data=response.json()
                    except:
                        print("response not in valid JSON format")    
            except:
                print("something went wrong with requests.get")
    
            url2="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (city,apy_key)
            try:
                response2=requests.get(url2)
                if not response2.status_code==200:
                    print("HTTP error",response2.status_code)
                else:
                    print(response2)
                    try:
                        response_data2=response2.json()
                    except:
                        print("response not in valid JSON format")    
            except:
                print("something went wrong with requests.get")
        
        
            #pprint.pprint(response_data2)
            dist=response_data['rows'][0]['elements'][0]['distance']['text']
            x = dist.split(' ')[0]
            s=x.split(',')[0]
            a=x.split(',')[1]
            l=s+a
            y=int(l)
            dict_fars[city]=y
            dur=response_data['rows'][0]['elements'][0]['duration']['text']
            dict_length['lng']=response_data2['results'][0]['geometry']['location']['lng']
            dict_width['lat']=response_data2['results'][0]['geometry']['location']['lat']
        
            the_tupel_info=(dist,dur,dict_length,dict_width)
            the_dictionary[city]=the_tupel_info
            count=count+1
            
    except:
        print("There is a problem with the input in the text file. (Misspelling / non-existent city, etc ...)")
        sys.exit()       
                        
     
    for key,item in the_dictionary.items():
        print("the destination is: "+key+"\n"+"the distance from Tel Aviv is: "+str(item[0])+"\n+"+"the duration from Tel Aviv is: "+str(item[1])+"\n+"+"the lag is: "+str(item[2])+"\n+"+"the lat is: "+str(item[3])+"\n"+"\n"+"\n")
    
    three_largest = nlargest(3, dict_fars, key=dict_fars.get)
    print("The 3 cities furthest from Tel Aviv are:")
    print(three_largest)
    print(count)                             
                        
            
#cities("dests","API")

cities("dests","Please enter my API key here. It is in the fourth row of the text file I uploaded to the model")


