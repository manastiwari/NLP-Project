import csv
import pandas as pd

def main(l1):
    xl = pd.read_excel(l1)
    xl1 = xl.set_index('Test ID')
    pd.options.display.max_colwidth = 0
    xl=xl.replace('\n',' ', regex=True)
    j=0
    n=0
    sent=""
    sent1=""
    sent2=[]
    k=0
    for i in range(0,149):
        sent1=sent1+sent
        for rows in xl.iterrows():
            sent=str(xl["Step Description"][j])+str(xl["Expected Result"][j])
            
            #sent1=sent1+sent
           # print(xl["Test ID"][j])
            
            if (str((xl["Test ID"][j]))=="nan"):
                sent1=sent1+sent
                j=j+1 
                
            else:
                break
           
                  

            #item=item+1
           
        #print(sent1)
        #print('\n')
        sent2.append(sent1)
        #print(sent2)
        #print("i=",i)
        sent1=""
        i=i+1
        #sent2=[]  
        k=0
        j=j+1


    #with open('sent2.csv', 'wb') as myfile:
    #    wr = csv.writer(sent2.csv, quoting=csv.QUOTE_ALL)
    #    wr.writerow(sent2)   
    df = pd.DataFrame(data={"col1": sent2})
    df.to_csv("sent3.csv", sep=',',index=False)