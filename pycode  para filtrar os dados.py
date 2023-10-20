########### Pacotes para filtros dos dados 
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

# x = np.arange(100)

diretorio = 'D:/Mestrado/Modelagens/Dados do Excel/'
# listdir(diretorio)
## 
data_filter = np.genfromtxt(diretorio+'tempo0_6h_T30GRAUS.txt',skip_header=8, delimiter="\t",comments="#", encoding= 'unicode_escape')# KF paper uem on glass 
###### PONTOS Iniciais de filtro. 
x=data_filter[:,0]
y1=data_filter[:,1]
y2=data_filter[:,2]
y3=data_filter[:,3]
y4=data_filter[:,4]
y5=data_filter[:,5]
# Sleciona os pontos da leitura
get = 1
skip =973 ## equivale 10minutos
## Variaáveis da leitura dos pontos
k = [item for z in [np.arange(get) + idx for idx in np.arange(0, x.size, skip+get)] for item in z]
l1 = [item for z in [np.arange(get) + idx for idx in np.arange(0, y1.size, skip+get)] for item in z]
l2 = [item for z in [np.arange(get) + idx for idx in np.arange(0, y2.size, skip+get)] for item in z]
l3 = [item for z in [np.arange(get) + idx for idx in np.arange(0, y3.size, skip+get)] for item in z]
l4 = [item for z in [np.arange(get) + idx for idx in np.arange(0, y4.size, skip+get)] for item in z]
l5 = [item for z in [np.arange(get) + idx for idx in np.arange(0, y5.size, skip+get)] for item in z]
plt.figure(1)
fig, ax = plt.subplots(figsize=(5, 3), layout='constrained')
plt.clf()
plt.plot(x[k],y1[l1],'ks-',markevery=1,lw=1.0,markersize=5,label='(teste de filtros)')
plt.plot(x[k],y2[l2],'ks-',markevery=1,lw=1.0,markersize=5,label='(teste de filtros)')
plt.plot(x[k],y3[l3],'ks-',markevery=1,lw=1.0,markersize=5,label='(teste de filtros)')
plt.plot(x[k],y4[l4],'ks-',markevery=1,lw=1.0,markersize=5,label='(teste de filtros)')
plt.plot(x[k],y5[l5],'ks-',markevery=1,lw=1.0,markersize=5,label='(teste de filtros)')

a = np.array([x[k], y1[l1]]).T
b = np.array([x[k], y2[l2]]).T
c = np.array([x[k], y3[l3]]).T
d = np.array([x[k], y4[l4]]).T
e = np.array([x[k], y5[l5]]).T

#file_30g = [a, b, c, d, e] 
#with open("list1.txt", "w") as file:
#    for x in zip(*file_30g):
#        file.write("{0}\t{1}\n".format(*x))

np.savetxt('20_06_30graus', a,delimiter='\t')
np.savetxt('40_06_30graus', b,delimiter='\t')
np.savetxt('60_06_30graus', c,delimiter='\t')
np.savetxt('80_06_30graus',d,delimiter='\t')
np.savetxt('100_06_30graus',e,delimiter='\t')
## Pontos Finais
data_filter_1 = np.genfromtxt(diretorio+'tempo6_12h_T30GRAUS.txt',skip_header=8, delimiter="\t",comments="#", encoding= 'unicode_escape')# KF paper uem on glass 
###### PONTOS Iniciais de filtro. 
x=data_filter_1[:,0]
y7=data_filter_1[:,1]
y8=data_filter_1[:,2]
y9=data_filter_1[:,3]
y10=data_filter_1[:,4]
y11=data_filter_1[:,5]
# Sleciona os pontos da leitura
get = 1
skip =2919## equivale 30 minutos
## Variaáveis da leitura dos pontos
k = [item for z in [np.arange(get) + idx for idx in np.arange(0, x.size, skip+get)] for item in z]
l7 = [item for z in [np.arange(get) + idx for idx in np.arange(0, y7.size, skip+get)] for item in z]
l8 = [item for z in [np.arange(get) + idx for idx in np.arange(0, y8.size, skip+get)] for item in z]
l9 = [item for z in [np.arange(get) + idx for idx in np.arange(0, y9.size, skip+get)] for item in z]
l10 = [item for z in [np.arange(get) + idx for idx in np.arange(0, y10.size, skip+get)] for item in z]
l11 = [item for z in [np.arange(get) + idx for idx in np.arange(0, y11.size, skip+get)] for item in z]
plt.figure(2)
fig, ax = plt.subplots(figsize=(5, 3), layout='constrained')
plt.clf()
plt.plot(x[k],y7[l7],'ks-',markevery=1,lw=1.0,markersize=5,label='(teste de filtros)')
plt.plot(x[k],y8[l8],'ks-',markevery=1,lw=1.0,markersize=5,label='(teste de filtros)')
plt.plot(x[k],y9[l9],'ks-',markevery=1,lw=1.0,markersize=5,label='(teste de filtros)')
plt.plot(x[k],y10[l10],'ks-',markevery=1,lw=1.0,markersize=5,label='(teste de filtros)')
plt.plot(x[k],y11[l11],'ks-',markevery=1,lw=1.0,markersize=5,label='(teste de filtros)')

f = np.array([x[k], y7[l7]]).T
g = np.array([x[k], y8[l8]]).T
h = np.array([x[k], y9[l9]]).T
i = np.array([x[k], y10[l10]]).T
j = np.array([x[k], y11[l11]]).T

np.savetxt('20_612_30graus', f,delimiter='\t')
np.savetxt('40_612_30graus', g,delimiter='\t')
np.savetxt('60_612_30graus', h,delimiter='\t')
np.savetxt('80_612_30graus',i,delimiter='\t')
np.savetxt('100_612_30graus',j,delimiter='\t')

########### Join TXT file into One document 
############ 20ppm#####################
data = data2 = ""
 
# Reading data from file1
with open('20_06_30graus') as fp:
    data = fp.read()
 
# Reading data from file2
with open('20_612_30graus') as fp:
    data2 = fp.read()
 
# Merging 2 files
# To add the data of file2
# from next line
data += "\n"
data += data2
 
with open ('20_datafilter_30graus.txt', 'w') as fp:
    fp.write(data)
    
############### 40ppm ###
data = data3 = ""
 
# Reading data from file1
with open('40_06_30graus') as fp:
    data = fp.read()
 
# Reading data from file2
with open('40_612_30graus') as fp:
    data3 = fp.read()
 
# Merging 2 files
# To add the data of file2
# from next line
data += "\n"
data += data3
 
with open ('40_datafilter_30graus.txt', 'w') as fp:
    fp.write(data)
##### 60ppm ########
################
data = data4 = ""
 
# Reading data from file1
with open('60_06_30graus') as fp:
    data = fp.read()
 
# Reading data from file2
with open('60_612_30graus') as fp:
    data4 = fp.read()
 
# Merging 2 files
# To add the data of file2
# from next line
data += "\n"
data += data4
 
with open ('60_datafilter_30graus.txt', 'w') as fp:
    fp.write(data)
################ 80ppm 
#######################
data = data5 = ""
 
# Reading data from file1
with open('80_06_30graus') as fp:
    data = fp.read()
 
# Reading data from file2
with open('80_612_30graus') as fp:
    data5 = fp.read()
 
# Merging 2 files
# To add the data of file2
# from next line
data += "\n"
data += data5
 
with open ('80_datafilter_30graus.txt', 'w') as fp:
    fp.write(data)
############### 100ppm 
#####################
data = data6 = ""
 
# Reading data from file1
with open('100_06_30graus') as fp:
    data = fp.read()
 
# Reading data from file2
with open('100_612_30graus') as fp:
    data6 = fp.read()
 
# Merging 2 files
# To add the data of file2
# from next line
data += "\n"
data += data6
 
with open ('100_datafilter_30graus.txt', 'w') as fp:
    fp.write(data)
