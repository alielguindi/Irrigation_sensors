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



#definition des fonctions
def clean_data(data) :
    #changer les donnees egale a 200 a nan
    donnes_modifies = data.replace(200.0, np.nan)
    return donnes_modifies



def save_plot_to_file(dataframe, title, labels, start_date, end_date, filename) :
    # La fonction qui va dessiner les 3 graphes avec les precisions du prof.
    fig, axis = plt.subplots(3,sharex = True,dpi=100)
    fig.set_figheight(10)
    fig.set_figwidth(10)
    fig.suptitle(title)
    fig.autofmt_xdate()
    plt.setp(axis, ylim=(0,200))
    y_at = [0,15,30,60,100] 
    y_ticks = ['saturated','too wet','perfect','plan to water','dry']
   
    
    plt.sca(axis[0])
    plt.yticks(y_at, y_ticks)
    
    plt.sca(axis[1])
    plt.yticks(y_at, y_ticks)
    
    plt.sca(axis[2])
    plt.yticks(y_at, y_ticks)
    
    dates = dataframe[start_date:end_date].index
    
    y_values_1 = dataframe[start_date:end_date][JSON_DATA[0]['datasets']['label']].values
    y_values_2 = dataframe[start_date:end_date][JSON_DATA[1]['datasets']['label']].values
    y_values_3 = dataframe[start_date:end_date][JSON_DATA[2]['datasets']['label']].values
    
   
    axis[0].fill_between(dates.to_pydatetime(),0,15, color='red', alpha= 0.2)
    axis[1].fill_between(dates.to_pydatetime(),0,15, color='red', alpha= 0.2)
    axis[2].fill_between(dates.to_pydatetime(),0,15, color='red', alpha= 0.2)
    
    axis[0].fill_between(dates.to_pydatetime(),15,30, color='orange', alpha= 0.2)
    axis[1].fill_between(dates.to_pydatetime(),15,30, color='orange', alpha= 0.2)
    axis[2].fill_between(dates.to_pydatetime(),15,30, color='orange', alpha= 0.2)
    
    axis[0].fill_between(dates.to_pydatetime(),30,60, color='green', alpha= 0.2)
    axis[1].fill_between(dates.to_pydatetime(),30,60, color='green', alpha= 0.2)
    axis[2].fill_between(dates.to_pydatetime(),30,60, color='green', alpha= 0.2)
    
    axis[0].fill_between(dates.to_pydatetime(),60,100, color='yellow', alpha= 0.2)
    axis[1].fill_between(dates.to_pydatetime(),60,100, color='yellow', alpha= 0.2)
    axis[2].fill_between(dates.to_pydatetime(),60,100, color='yellow', alpha= 0.2)
    
    axis[0].fill_between(dates.to_pydatetime(),100,200, color='red', alpha= 0.2)
    axis[1].fill_between(dates.to_pydatetime(),100,200, color='red', alpha= 0.2)
    axis[2].fill_between(dates.to_pydatetime(),100,200, color='red', alpha= 0.2)
    
   
    
    axis[0].plot(dates.to_pydatetime(),y_values_1, label="1: 1m/30cm [kPa]")
    axis[1].plot(dates.to_pydatetime(),y_values_2, label="2: 1m/30cm [kPa]")
    axis[2].plot(dates.to_pydatetime(),y_values_3, label="3: 1m/30cm [kPa]")
    
    axis[0].legend(loc="upper left")
    axis[1].legend(loc="upper left")
    axis[2].legend(loc="upper left")
    
    plt.savefig(filename+".png")
    

#Lecture de fichier json
with open(JSON_NAME) as json_file:
    JSON_DATA = json.load(json_file)




if __name__ == '__main__':
   #Variable pour le temps des mesures effectuées, utilisation librairie panda
   temps_dict = JSON_DATA[0]['labels']
   humidity_dataframe = pd.DataFrame( data={
        JSON_DATA[0]['datasets']['label']: JSON_DATA[0]['datasets']['data'],
        JSON_DATA[1]['datasets']['label']: JSON_DATA[1]['datasets']['data'],
        JSON_DATA[2]['datasets']['label']: JSON_DATA[2]['datasets']['data'],
        }, index= temps_dict, dtype='float')
   humidity_dataframe.index = pd.to_datetime(humidity_dataframe.index)
   
   humidity_dataframe =clean_data(humidity_dataframe)
   save_plot_to_file(humidity_dataframe, 'Irrigation june 2020', '', '2020-06-01', '2020-06-30', 'irrigation_graph_2020-06')
   save_plot_to_file(humidity_dataframe, 'Irrigation july 2020', '', '2020-07-01', '2020-07-30', 'irrigation_graph_2020-07')
   save_plot_to_file(humidity_dataframe, 'Irrigation august 2020', '', '2020-08-01', '2020-08-30', 'irrigation_graph_2020-08')
   
   
                                             