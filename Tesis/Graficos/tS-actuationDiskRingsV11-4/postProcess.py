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

U_inlet=10
D=100


#GRAFICOS CON IT VARIABLE
for i in [1,2,4,6,8,10,12,15]:
    fig, ax = plt.subplots()
    for j in [0.05, 0.1, 0.15]:
        inputfilename= 'U' + str(U_inlet) + '_vs_y_' + str(i) + 'D/D' + str(i) + '_U' + str(U_inlet) + '_IT' + str(j) + '_7.csv'
        inputfile=csv.reader(open(inputfilename,'r'))
        
        inputlist=list(inputfile)
        yrel_list=[]
        Urel_list=[]
        for row in inputlist:
            if is_float(row[1])==True:
                yrel_list.append(float(row[0])/D)
                Urel_list.append((float(row[1])-U_inlet)/U_inlet)
        
        #fig, ax = plt.subplots()
        # label_legend=str(i) + ' celdas por D'
        label_legend='IT=' + str(j)
        ax.plot(Urel_list, yrel_list, linewidth=0.75, label=label_legend)
        ax.set_xlim(-0.4,0.1)
        
        # outputfilename='D1_U_rel_' + str(i) + '.csv'
        # outputfile=open(outputfilename,'w')
        # outputfile.write('y,Ux\n')
    
        # for row in inputfile:
        #     if is_float(row[1])==True:
        #         pos_y=float(row[0])
        #         pos_rel=pos_y/D
        #         U=float(row[1])
        #         relU=(U-U_inlet)/U_inlet
        #         outputfile.write(str(pos_rel) + ',' + str(relU) + '\n')
        #     ## else:
        #         ## print(row[1])
        
        # outputfile.close
        
        # outputfile=csv.reader(open(outputfilename,'r'))

    ax.set_xlabel('(Ux-Uinlet)/Uinlet', fontsize=15)
    ax.set_ylabel('y/D', fontsize=15)
    ax.set_title('Estela a ' + str(i) + ' diámetro aguas abajo del actuador para distintos mallados')
    ax.grid(True)
    fig.legend(loc='upper left', borderaxespad=7)
    figname= 'D' + str(i) + '_Urel_ITvar.png'
    plt.savefig(figname,dpi=1200)
    
#GRAFICOS EN UN EJE X

for j in [0.05, 0.1, 0.15]:
    fig, ax = plt.subplots()
    for i in [1,2,4,6,8,10,12,15]:
        inputfilename= 'U' + str(U_inlet) + '_vs_y_' + str(i) + 'D/D' + str(i) + '_U' + str(U_inlet) + '_IT' + str(j) + '_7.csv'
        inputfile=csv.reader(open(inputfilename,'r'))
        
        inputlist=list(inputfile)
        y_list=[]
        Urelx_list=[]
        # y=0
        for row in inputlist:
            if is_float(row[1])==True:
                # y= y + D/len(inputlist) #TIENE QUE SER UN CONTADOR QUE SE REINICIE AL VOLVER A PLOTEAR PARA UN i
                y_list.append(float(row[0]))
                Urelx=(500+100*i)+300*(-(float(row[1])-U_inlet)/U_inlet)
                Urelx_list.append(Urelx)
        
        #fig, ax = plt.subplots()
        # label_legend=str(i) + ' celdas por D'
        label_legend='x=' + str(i*100+500)
        ax.plot(Urelx_list, y_list, linewidth=0.75, label=label_legend)
        ax.set_xlim(0,2500)
        ax.set_ylim(0,900)
        
    ax.set_xlabel('x', fontsize=15)
    ax.set_ylabel('(Ux-Uinlet)/Uinlet', fontsize=15)
    ax.set_title('Estela aguas abajo del actuador')
    ax.grid(True)
    #fig.legend(loc='upper left', borderaxespad=7)
    figname= 'D_Urel_IT' + str(j) + '.png'
    plt.savefig(figname,dpi=1200)