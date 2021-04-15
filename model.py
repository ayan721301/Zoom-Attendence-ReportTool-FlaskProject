import numpy as np
import pandas as pd 
import re

def model(name,name1):
        s = name
        stexcel = name1
        colnames=['time','tottext']
        df1=pd.read_csv(s,sep='\t',names=colnames)
        lst=[i.split(sep=':')[1] for i in df1['tottext']]
        lst1=[i.split(sep=':')[0] for i in df1['tottext']]
        df1new=pd.DataFrame()
        df1new['given_roll']=lst
        lst2=[i.split(sep=' ')[3] for i in lst1]
        lstre=[re.sub('[^0-9]','',i) for i in lst2]
        lstwd=[re.sub('[^a-z ^A-Z]','',i) for i in lst2]
        lstwdup=[i.upper() for i in lstwd]
        dfroll=pd.read_excel(stexcel)
        indlist=list()
        l=len(lstre)
        for i in range(l):
                if lstwdup[i]!='':
                        roll=dfroll[dfroll['Student Name']==lstwdup[i]]['Roll No.']
                        lstre[i]=str(roll)
        lstre=[re.sub('[a-z A-Z]','',k) for k in lstre]
        present_list=list()
        lst=[str(j) for j in lst]
        lst=[j.strip() for j in lst]
        lstre=[str(j) for j in lstre]
        lstre=[re.sub(",:.,64",'',j) for j in lstre]
        for i in range(l):
                if lstre[i]==lst[i]:
                        present_list.append(lstre[i])
        present_set=set(present_list)
        tot_list=[str(j) for j in dfroll['Roll No.']]
        tot_set=set(tot_list)
        abs_list=list(tot_set.difference(present_set))
        a = abs_list
        return a