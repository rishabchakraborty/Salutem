#!/usr/bin/python

# libraries
import numpy as np
import matplotlib.pyplot as plt
import time

print('\n\n\n\n\n\t\t >>>Medical Expert - Disease Detector<<< \n\n\n')

print('Help us with your symptoms to predict your disease:\n')

symptoms = ['fever','cough','conjunctivitis','runny_nose','rash','sneezing','headache','body ache','chills','sore throat','swollen glands'];
detection = [0,0,0,0,0,0,0,0,0,0,0];

#disease
measles = 0
german_measles = 0
flu = 0
mumps = 0
chicken_pox = 0
common_cold = 0


for symptom in symptoms:
    index = symptoms.index(symptom)
    print('Does the patient has',symptom,'? (Yes or No)')
    detection[index] = input()
    if(detection[index] == "yes" or detection[index] == "Yes" or detection[index] == "y" or detection[index] == "Y"):
        detection[index] = 1
    else:
        detection[index] = 0
    print('\n')

print('\n\n\t\t  Loading Graph.....\t\t')
#fever
if(detection[0] == 1):
    measles += 1
    german_measles += 1
    flu += 1
    mumps += 1
    chicken_pox += 1

#cough    
if(detection[1] == 1):
    measles += 1
    flu += 1

#conjunctivitis
if(detection[2] == 1):
    measles += 1
    flu += 1
        
#runny nose
if(detection[3] == 1):
    measles += 1
    german_measles += 1
    flu += 1
    common_cold += 1

#rash
if(detection[4] == 1):
    measles += 1
    german_measles += 1
    chicken_pox += 1
        
#sneezing
if(detection[5] == 1):
    measles += 1
    common_cold += 1
        
#headache
if(detection[6] == 1):
    german_measles += 1
    flu += 1
    common_cold += 1
        
#body ache
if(detection[7] == 1):
    flu += 1
    chicken_pox += 1

#chills
if(detection[8] == 1):
    flu += 1
    chicken_pox += 1
    common_cold += 1
        
#sore throat
if(detection[9] == 1):
    flu += 1
    common_cold += 1
        
#swollen glands'
if(detection[10] == 1):
    mumps += 1

measles = (measles/6)*100
german_measles = (german_measles/4)*100
flu = (flu/8)*100
common_cold = (common_cold/5)*100
mumps = (mumps/2)*100
chicken_pox = (chicken_pox/4)*100



# Choose the height of the bars
height = [measles, german_measles, flu, common_cold, mumps, chicken_pox]

# Choose the names of the bars
bars = ('Measles ', ' German Measles ', ' Flu', ' Common Cold ', 'Mumps', ' Chicken Pox')

# Choose the position of each barplots on the x-axis (space=1,4,3,1)
y_pos = [0,3,5,7,9,11]


# Create bars
plt.bar(y_pos, height)

# Add title and axis names
plt.title('Disease Prediction Chart (based on Symptoms)')
plt.xlabel('Diseases')
plt.ylabel('Probability of having the disease(in %)')
 
# Create names on the x-axis
plt.xticks(y_pos, bars, color='blue')
plt.yticks(color='orange')
 
# Show graphic
plt.show()

time.sleep(.200)
print('\n\n\t\t>>>Chart Report<<<\t\t\n\n')

if( measles > 0 ):
    print('You have',measles,'% probability to have Measles.\n')
if( german_measles > 0 ):
    print('You have',german_measles,'% probability to have German Measles.\n')
if( flu > 0 ):
    print('You have',flu,'% probability to have Flu.\n')
if( common_cold > 0 ):
    print('You have',common_cold,'% probability to have Common Cold.\n')
if( mumps > 0 ):
    print('You have',mumps,'% probability to have Mumps.\n')
if( chicken_pox > 0 ):
    print('You have',chicken_pox,'% probability to have Chicken Pox.\n\n\n\n')
if(measles == 0 and german_measles == 0 and flu==0 and common_cold==0 and mumps==0 and chicken_pox==0):
    print('Soryy, Your disease is not detected. Please Consult with doctor.\n')
