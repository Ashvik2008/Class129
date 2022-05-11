import csv
import pandas as pd 

data = []
with open("/Users/vtai/Downloads/Class129/dataset_2.csv","r") as f :
    csvreader= csv.reader(f)
    for row in csvreader:
        data.append(row)

headers = data[0]
planet_data = data[1:]


#convert all planet names to lower case 
for data_point in planet_data :
    data_point[2]= data_point[2].lower()


#Sorting Planet names in alphabetical order 
planet_data.sort(key=lambda planet_data:planet_data[2])
with open("/Users/vtai/Downloads/Class129/Sorted_Dataset_2.csv","a+") as f :
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)

#remove blank lines
with open('Sorted_Dataset_2.csv') as input, open('Sorted_Dataset_2_Fianl.csv', 'w', newline='') as output:
     writer = csv.writer(output)
     for row in csv.reader(input):
         if any(field.strip() for field in row):
             writer.writerow(row)