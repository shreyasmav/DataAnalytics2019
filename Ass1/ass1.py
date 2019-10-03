import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os




d = pd.read_csv("data.csv")




#all winner

winnerParty = []
winnerAge = []
winnerName = []

for i in range(len(d.Party)):
    if d.Winner[i] == "Yes":
        winnerParty.append(d.Party[i])
        winnerAge.append(d.Age[i])
        winnerName.append(d.Candidate[i])

print("Age distribution of candidate who won : ")
# Age 
num_bins = 20
n, bins, patches = plt.hist(winnerAge, num_bins, facecolor='blue', alpha=0.5)
plt.show()


#Party

bjp = 0
inc = 0
oth = 0

for i in winnerParty:
    if i == 'BJP':
        bjp = bjp + 1
    elif i == 'INC':
        inc = inc + 1
    else:
        oth = oth + 1
        
pii = [bjp, inc, oth]
label = ['BJP', 'INC', 'OTH']
print("Pie chart on # candidate who won (party) : ")

colors = ['gold', 'yellowgreen', 'lightcoral']
explode = (0.1, 0, 0)  # explode 1st slice

plt.pie(pii, explode=explode, labels=label, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()


#criminals

criminalParty = []
criminalAge = []
criminalName = []

for i in range(len(d.Party)):
    if d.Criminal_Case[i] > 0:
        criminalParty.append(d.Party[i])
        criminalAge.append(d.Age[i])
        criminalName.append(d.Candidate[i])

print("Age distribution of candidate who has/had criminal case(s) : ")

# Age 
num_bins = 20
n, bins, patches = plt.hist(criminalAge, num_bins, facecolor='blue', alpha=0.5)
plt.show()


#Party

bjp = 0
inc = 0
oth = 0

for i in criminalParty:
    if i == 'BJP':
        bjp = bjp + 1
    elif i == 'INC':
        inc = inc + 1
    else:
        oth = oth + 1
        
pii = [bjp, inc, oth]
label = ['BJP', 'INC', 'OTH']
print("Pie chart on # candidate who has/had criminal case(s) : ")

colors = ['gold', 'yellowgreen', 'lightcoral']
explode = (0, 0, 0.1)  # explode 1st slice

plt.pie(pii, explode=explode, labels=label, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()









#criminals won

wcriminalParty = []
wcriminalAge = []
wcriminalName = []

for i in range(len(d.Party)):
    if d.Criminal_Case[i] > 0 and d.Winner[i] == "Yes":
        wcriminalParty.append(d.Party[i])
        wcriminalAge.append(d.Age[i])
        wcriminalName.append(d.Candidate[i])



#Party

bjp = 0
inc = 0
oth = 0

for i in wcriminalParty:
    if i == 'BJP':
        bjp = bjp + 1
    elif i == 'INC':
        inc = inc + 1
    else:
        oth = oth + 1
        
pii = [bjp, inc, oth]
label = ['BJP', 'INC', 'OTH']


colors = ['gold', 'yellowgreen', 'lightcoral']
explode = (0.1, 0, 0)  # explode 1st slice
print("Age distribution of candidate who has/had criminal case(s) and won : ")
plt.pie(pii, explode=explode, labels=label, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()


# bjp non criminal win vs criminal win:

bjp = 0
cbjp = 0

for i in range(len(d.Party)):
    if d.Criminal_Case[i] > 0 and d.Winner[i] == "Yes" and d.Party[i] == 'BJP':
        cbjp = cbjp + 1
    if d.Criminal_Case[i] == 0 and d.Winner[i] == "Yes" and d.Party[i] == 'BJP':
        bjp = bjp + 1
        
print("WINNER of BJP with criminal casses to without -> " + str(cbjp) +":" + str(bjp) + " = " + str(cbjp/bjp) )
print("Percent of BJP candidate won who has/had criminal case = ", "%.2f"%round(100*cbjp/(cbjp+bjp),2),"%")


