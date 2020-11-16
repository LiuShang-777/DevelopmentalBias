# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:10:06 2020

@author: liushang
"""
import numpy as np
dic_={'A':2,'B':0,'C':1,'a':-2,'b':1,'c':1}
#dic_={'A':2,'B':2,'C':2,'a':2,'b':2,'c':2}
class species():
    def __init__(self):
        self.phenoA=None
        self.phenoB=None
        self.phenoC=None
        self.survival=False
        self.compete=0
        self.iter=0
    
    def set_gene(self,thresholds,thresholdo):
        p=np.random.rand()
        if p<=thresholds:
            self.phenoA='A'
            pb=np.random.rand()
            if pb<=0.8:    
                self.phenoB='B'
            else:
                self.phenoB='b'
        else:
            self.phenoA='a'
            pb=np.random.rand()
            if pb<=0.8:    
                self.phenoB='b'
            else:
                self.phenoB='B'
        p=np.random.rand()
        if p<=thresholdo:
            self.phenoC='C'
        else:
            self.phenoC='c'
    def cal_comp(self):
        if self.iter==0:    
            self.compete= dic_[self.phenoA]+dic_[self.phenoB]+dic_[self.phenoC]
        else:
            pass
    def remain(self):
        if self.survival==False:
            pass
        else:
            self.iter+=1
        

species_thre=1000
def generate(num):
    list_=[]
    for i in range(0,num):
        c=species()
        c.set_gene(0.5,0.5)
        c.cal_comp()
        list_.append(c)
    return ([(i.phenoA,i.phenoB,i.phenoC) for i in list_],list_)
def competetion(list_):
    tmp=[i.compete for i in list_]
    tmp.sort()
    thre=tmp[int(len(tmp)*0.75)]
    sur=[]
    for i in list_:
        if i.compete>=thre:
            i.survival=True
            i.remain()
            sur.append(i)
        else:
            i.surval=False
            i.remain()
    return sur


    
dic_stat={}
list_total=[]
iteration=0
while(len(list_total)<=1000):
    dic_stat[iteration],list_tmp=generate(100)
    for i in list_tmp:
        list_total.append(i)
    list_total=competetion(list_total)
    iteration+=1
#plot the result   
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Times New Roman'
list_pic_all=[len([i for i in list_total if i.phenoA=='A']),len([i for i in list_total if i.phenoA=='a']),
 len([i for i in list_total if i.phenoB=='B']),len([i for i in list_total if i.phenoB=='b']),
 len([i for i in list_total if i.phenoC=='C']),len([i for i in list_total if i.phenoC=='c'])]
plt.figure(figsize=(10,4),dpi=300)
plt.bar(np.arange(6),list_pic_all,color=['#ff0000','#669900','#00ff00','#996600','#0000ff','#00f0ff'],
        alpha=0.3)   
plt.xticks(np.arange(6),['A','a','B','b','C','c'],fontsize=20)

plt.title('phenotype of survived species(threshold=0.2)',fontsize=25)
plt.savefig('F:/friends/surv0.5.png') 
plt.clf()              

plt.rcParams['font.size']=18
plt.figure(figsize=(10,4),dpi=300)
plt.plot(dic_stat.keys(),[len([j for j in dic_stat[i] if j[0]=='A']) for i in dic_stat.keys()],linestyle='dashed',color='#ff0000')  
plt.plot(dic_stat.keys(),[len([j for j in dic_stat[i] if j[0]=='a']) for i in dic_stat.keys()],linestyle='dashed',color='#ff0000',alpha=0.5) 
plt.plot([iteration-i for i in dic_stat.keys()],[len([j for j in list_total if (j.phenoA=='A')&(j.iter==i)]) for i in dic_stat.keys()],color='#ff0000')
plt.plot([iteration-i for i in dic_stat.keys()],[len([j for j in list_total if (j.phenoA=='a')&(j.iter==i)]) for i in dic_stat.keys()],color='#ff0000',alpha=0.5)
plt.xticks(np.arange(iteration),np.arange(1,iteration+1)) 
plt.legend(['A generated','a generated','A survived','a survived'])
plt.savefig('F:/friends/surv0.5A.png') 
plt.clf()   
    
plt.figure(figsize=(10,4),dpi=300)        
plt.plot(dic_stat.keys(),[len([j for j in dic_stat[i] if j[1]=='B']) for i in dic_stat.keys()],linestyle='dashed',color='#00ff00') 
plt.plot(dic_stat.keys(),[len([j for j in dic_stat[i] if j[1]=='b']) for i in dic_stat.keys()],linestyle='dashed',color='#00ff00',alpha=0.3) 
plt.plot([iteration-i for i in dic_stat.keys()],[len([j for j in list_total if (j.phenoB=='B')&(j.iter==i)]) for i in dic_stat.keys()],color='#00ff00')
plt.plot([iteration-i for i in dic_stat.keys()],[len([j for j in list_total if (j.phenoB=='b')&(j.iter==i)]) for i in dic_stat.keys()],color='#00ff00',alpha=0.3)
plt.xticks(np.arange(iteration),np.arange(1,iteration+1))  
plt.legend(['B generated','b generated','B survived','b survived']) 
plt.savefig('F:/friends/surv0.5B.png') 
plt.clf()  
       
plt.figure(figsize=(10,4),dpi=300)          
plt.plot(dic_stat.keys(),[len([j for j in dic_stat[i] if j[2]=='C']) for i in dic_stat.keys()],linestyle='dashed',color='#0000ff') 
plt.plot(dic_stat.keys(),[len([j for j in dic_stat[i] if j[2]=='c']) for i in dic_stat.keys()],linestyle='dashed',color='#0000ff',alpha=0.5) 
plt.plot([iteration-i for i in dic_stat.keys()],[len([j for j in list_total if (j.phenoC=='C')&(j.iter==i)]) for i in dic_stat.keys()],color='#0000ff')
plt.plot([iteration-i for i in dic_stat.keys()],[len([j for j in list_total if (j.phenoC=='c')&(j.iter==i)]) for i in dic_stat.keys()],color='#0000ff',alpha=0.3)
plt.xticks(np.arange(iteration),np.arange(1,iteration+1))
plt.legend(['C generated','c generated','C survived','c survived'])
plt.savefig('F:/friends/surv0.5C.png') 
plt.clf()  

   
      