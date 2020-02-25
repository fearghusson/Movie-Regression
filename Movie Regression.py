'''superhero regression project 
the idea is to see to what extent rating has on boxoffice from 2007 to 2019'''

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import requests

#url = r'http://www.omdbapi.com/?apikey=d42d26d9&t=Avengers'

#r = requests.get(url)

#print(r.json())

def getmovie(title, year = None):
    #this will get a list of elements from the json data
    try:
        #blank values that are used to fill out info
        boxoffice_string = ''
        listvalue = []
   
        #if statement to determine if year is used
        if year == None:
            url = 'http://www.omdbapi.com/?apikey=d42d26d9&t=' + str(title)
        else:
            url =  'http://www.omdbapi.com/?apikey=d42d26d9&t=' + str(title) + '&y=' +str(year)
   
        #requesting info from omdb and storing it to r
        r = requests.get(url)
        #pulling the json data
        json_data = r.json()
   
        #create if/else to determine whether the boxoffice is na or not. if it is
        #not it will put put the number
        if json_data['BoxOffice'] != 'N/A':
        #if the boxoffice isn't NA then it will use regex to get all the digits
            import re
        #define the regex to get just digits
            regex = re.compile(r'(\d)')
            digit = regex.findall(json_data['BoxOffice'])
        #loop to put all the number strings into
            for i in digit:
                boxoffice_string += i
        #convert the string into a number
            boxoffice_int = int(boxoffice_string)
        #final value to return
            listvalue = [json_data['Title'], boxoffice_int, int(json_data['Metascore']),
                 int(json_data['Year'])]
        else:
            listvalue = [json_data['Title'], 0, int(json_data['Metascore']),
                 int(json_data['Year'])]
                
        return listvalue
    
    except (ValueError, KeyError) :
       print('error - ' + title + ' may not be the correct title')
    
    return listvalue



frame = {'Title':, '}




