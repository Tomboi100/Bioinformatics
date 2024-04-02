# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 17:19:39 2022

@author: Tommy
"""

def openfile(filePath):#openening and reading the fastafile
    with open (filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]  
    
def GcContent(seq):# calculating the gc content percentage
    return round((seq.count('C')+ seq.count('G'))/len(seq)*100, 6)

def n50(totalLen):# calculating the n50 value
    hn50 = ((sum(totalLen))/2)# half the total length
    total = 0
    for i in totalLen:
       total = total + i
       if total >= hn50:
           return i
       
def n90(totalLen):# calculating the n90
    hn90 = ((sum(totalLen))*0.9)# 90% of the total length
    total = 0
    for i in totalLen:
       total = total + i
       if total >= hn90:
           return i

def l50(totalLen):# calculating the l50  
    hl50 = ((sum(totalLen))/2)# half the total length
    total = 0
    c = 0
    for i in totalLen:
       total = total + i
       c = c+1
       if total >= hl50:
           return c
       
Files = {"RUG213.fa","RUG384.fa","RUG413.fa","RUG545.fa"}# the fasta files provided in a list
for element in Files: #does each calcaluation for each file and displays it
    FastaFile = openfile(element)
    FDict = {}
    Label = ""
    
    for line in FastaFile:#correctly reads the file into the dictionary
        if '>' in line:
            Label = line
            FDict[Label] = ""
        else:
            FDict[Label] += line
            
    Results = {key: GcContent(value) for (key, value) in FDict.items()}#creates a results dictionary with the gc% and the contig
    totalLen = [len(value) for (key, value) in FDict.items()]
    totalLen.sort(reverse=True)
    N50 = n50(totalLen)
    N90 = n90(totalLen)
    L50 = l50(totalLen)
    
    print("File = "+element+"\n")
    print("The length of each of the contigs = " + str(totalLen))
    print("n50 = "+ str(N50))
    print("n90 = "+ str(N90))
    print("l50 = "+ str(L50))
    print("Total gc content for "+element+" = "+ (str(sum(Results.values())/len(Results)))+"\n\n")

