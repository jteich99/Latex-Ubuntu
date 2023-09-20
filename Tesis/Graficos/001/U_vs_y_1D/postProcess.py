#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 18:40:44 2023

@author: juan
"""

import csv
import matplotlib.pyplot as plt
plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.rm'] = 'Bitstream Vera Sans'
plt.rcParams['mathtext.it'] = 'Bitstream Vera Sans:italic'
plt.rcParams['mathtext.bf'] = 'Bitstream Vera Sans:bold'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.family'] = 'STIXGeneral'

def is_float(string):
    try:
        # float() is a built-in function
        float(string)
        return True
    except ValueError:
        return False

U_inlet=6
D=100

fig, ax = plt.subplots()
for i in [2,4,5,7,9]:
    inputfilename='D1_U_' + str(i) + '.csv'
    inputfile=csv.reader(open(inputfilename,'r'))
    
    inputlist=list(inputfile)
    yrel_list=[]
    Urel_list=[]
    for row in inputlist:
        if is_float(row[1])==True:
            yrel_list.append(float(row[0])/D)
            Urel_list.append((float(row[1])-U_inlet)/U_inlet)
    
    #fig, ax = plt.subplots()
    label_legend=str(i) + ' celdas por D'
    ax.plot(Urel_list, yrel_list, linewidth=0.75, label=label_legend)
    
    outputfilename='D1_U_rel_' + str(i) + '.csv'
    outputfile=open(outputfilename,'w')
    outputfile.write('y,Ux\n')

    for row in inputfile:
        if is_float(row[1])==True:
            pos_y=float(row[0])
            pos_rel=pos_y/D
            U=float(row[1])
            relU=(U-U_inlet)/U_inlet
            outputfile.write(str(pos_rel) + ',' + str(relU) + '\n')
        ## else:
            ## print(row[1])
    
    outputfile.close
    
    outputfile=csv.reader(open(outputfilename,'r'))

ax.set_xlabel('(Ux-Uinlet)/Uinlet', fontsize=15)
ax.set_ylabel('y/D', fontsize=15)
ax.set_title('Estela a 1 diámetro aguas abajo del actuador para distintos mallados')
ax.grid(True)
fig.legend(loc='upper left', borderaxespad=7)
plt.savefig('D1_U_rel.png',dpi=1200)