# -*- coding: utf-8 -*- " 
"""Created on Sat Dec 17 09:22:55 2022
                        @author:John Pafutes """
                ##PRINCIPAL PACKAGE###
                ########################
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams
from scipy.signal import savgol_filter
import scipy.signal as signal
import pandas as pd
import numpy as np
from matplotlib.ticker import AutoMinorLocator
from os import listdir
import math
from scipy.stats import linregress
           #######################
            ## Configurar letras dentro do gráfico##
            #####################################
            # from peakdetect import peakdetect
            # rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
            ## for Palatino and other serif fonts use:
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 22
                ##############################################
                ######Puxar os dados do diretório drive D####
                ########################################

directory = 'D:/Mestrado/Ensaios de adsorção/40 graus/'
data = np.genfromtxt(directory + "Cinetica_capacidade_concentracao_remocao_40graus.txt", skip_header=3, delimiter="\t", comments="#")

###########################################################################
#########  PLOT KINETICS BASED ON CONCENTRATIONS VS TIME ###########
#########################################################################
tempo = data[:, 0]  # First column
ydata1 = data[:, 1]  # 40ppm
ydata2 = data[:, 2]  # 60 ppm
ydata3 = data[:, 3]  # 80ppm
ydata4 = data[:, 4]  # 100ppm
ydata5 = data[:, 5]  # 120ppm

# Creating the figure
#fig, ax = plt.subplots(figsize=(width, height))
fig, ax = plt.subplots(figsize=(6,6))

# Plotting the data as scatter plot
ax.scatter(tempo, ydata1, color='red', marker='o', s=50, label="40 mgL$^{-1}$")
ax.scatter(tempo, ydata2, color='blue', marker='o', s=50, label="60 mgL$^{-1}$")
ax.scatter(tempo, ydata3, color='green', marker='o', s=50, label="80 mgL$^{-1}$")
ax.scatter(tempo, ydata4, color='orange', marker='o', s=50, label="100 mgL$^{-1}$")
ax.scatter(tempo, ydata5, color='purple', marker='o', s=50, label="120 mgL$^{-1}$")
ax.legend(fontsize=16)
legend = ax.get_legend()
for text in legend.get_texts():
    text.set_fontweight('bold')
# Set graph details
ax.set_xlabel("Time (h)",fontsize=22, fontweight='bold')
ax.set_ylabel('C (mg g$^{-1}$)',fontsize=22, fontweight='bold')
# Set starting point to zero for x and y
ax.set_xlim(left=0)
ax.set_ylim(bottom=0)
#ax.set_title("Concentração do Equilibrio do CM_CV")
ax.legend()
# Save the figure as a PDF with high resolution (300 DPI)
fig.savefig('Concentrações_CV_MC_40_graus', dpi=600, format='pdf', bbox_inches='tight')

###########################################################################
#########  PLOT KINETICS BASED ON ADSORPTIONS CAPACITY VS TIME ###########
#########################################################################
ydata6 = data[:, 6]  # 40ppm
ydata7 = data[:, 7]  # 60 ppm
ydata8 = data[:, 8]  # 80ppm
ydata9 = data[:, 9]  # 100ppm
ydata10 = data[:,10]  # 120ppm

# Creating the figure
fig, ax = plt.subplots(figsize=(6, 6))

# Plotting the data as scatter plot
ax.scatter(tempo, ydata6, color='red', marker='o', s=50, label="40 mgL$^{-1}$")
ax.scatter(tempo, ydata7, color='blue', marker='o', s=50, label="60 mgL$^{-1}$")
ax.scatter(tempo, ydata8, color='green', marker='o', s=50, label="80 mgL$^{-1}$")
ax.scatter(tempo, ydata9, color='orange', marker='o', s=50, label="100 mgL$^{-1}$")
ax.scatter(tempo, ydata10, color='purple', marker='o', s=50, label="120 mgL$^{-1}$")
ax.legend(fontsize=16)
legend = ax.get_legend()
for text in legend.get_texts():
    text.set_fontweight('bold')
# Set graph details
ax.set_xlabel("Time (h)",fontsize=22, fontweight='bold')
ax.set_ylabel('Qe (mg g$^{-1}$)',fontsize=22, fontweight='bold')
# Set starting point to zero for x and y
ax.set_xlim(left=0)
ax.set_ylim(bottom=0)
#ax.set_title("Concentração do Equilibrio do CM_CV")
ax.legend()

# Save the figure as a PDF with high resolution (300 DPI)
fig.savefig('Capacidade de adsorção_CV_MC_40_graus', dpi=600, format='pdf', bbox_inches='tight')
###########################################################################
#########  PLOT KINETICS BASED ON PERCENTAGE REMOVAL VS TIME ###########
#########################################################################
ydata11 = data[:, 11]  # 40ppm
ydata12 = data[:, 12]  # 60 ppm
ydata13 = data[:, 13]  # 80ppm
ydata14 = data[:, 14]  # 100ppm
ydata15 = data[:, 15]  # 120ppm

# Creating the figure
fig, ax = plt.subplots(figsize=(6, 6))

# Plotting the data as scatter plot
ax.scatter(tempo, ydata11, color='red', marker='o', s=50, label="40 mgL$^{-1}$")
ax.scatter(tempo, ydata12, color='blue', marker='o', s=50, label="60 mgL$^{-1}$")
ax.scatter(tempo, ydata13, color='green', marker='o', s=50, label="80 mgL$^{-1}$")
ax.scatter(tempo, ydata14, color='orange', marker='o', s=50, label="100 mgL$^{-1}$")
ax.scatter(tempo, ydata15, color='purple', marker='o', s=50, label="120 mgL$^{-1}$")
ax.legend(fontsize=16)
legend = ax.get_legend()
for text in legend.get_texts():
    text.set_fontweight('bold')
# Set graph details
ax.set_xlabel("Time (h)",fontsize=22, fontweight='bold')
ax.set_ylabel('Removal (%)',fontsize=22, fontweight='bold')
# Set starting point to zero for x and y
ax.set_xlim(left=0)
ax.set_ylim(bottom=0)
#ax.set_title("Concentração do Equilibrio do CM_CV")
ax.legend()

# Save the figure as a PDF with high resolution (300 DPI)
fig.savefig('Porcentagem de remocao_CV_MC_40graus', dpi=600, format='pdf', bbox_inches='tight')


