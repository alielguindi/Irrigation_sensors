#1!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 11:37:12 2020

@author: alielguindi
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import json

#Nom du fichier JSON lu
JSON_NAME = 'eco-sensors_irrigation_2020-06-01_2020-08-31.json' 

#Lecture de fichier json
with open(JSON_NAME) as json_file:
    JSON_DATA = json.load(json_file)


if __name__ == '__main__':
   #Variable pour le temps des mesures effectuées
   temps_dict = JSON_DATA[0]['labels']
   humidity_dataframe = pd.DataFrame( data={
        JSON_DATA[0]['datasets']['label']: JSON_DATA[0]['datasets']['data'],
        JSON_DATA[1]['datasets']['label']: JSON_DATA[1]['datasets']['data'],
        JSON_DATA[2]['datasets']['label']: JSON_DATA[2]['datasets']['data'],
        }, index= temps_dict, dtype='float')
   humidity_dataframe.index = pd.to_datetime(humidity_dataframe.index)
   print(humidity_dataframe)
   
                                             