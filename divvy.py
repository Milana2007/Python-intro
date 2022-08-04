'''
def analyze():
    f = open("202206-divvy-tripdata.csv")
    line = f.readline()
    classic_bike_total=0
    electric_bike_total=0
    for line in f .readlines():
        fields = line.split(",")
        bike_type = fields[1] 
        if bike_type == "classic_bike":
            classic_bike_total += 1
        elif bike_type == "electric_bike":
            electric_bike_total += 1
    return (classic_bike_total, electric_bike_total)

c,e = analyze()
print(f"classic bike rides: {c}")
print(f"classic bike rides: {e}")
'''

import matplotlib.pyplot as plt 
#import csv.divvy as div
import csv
def analyze():
    total_male=0
    total_female=0
    with open ("age_life(1)/AgeDataset-V1.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        for fields in reader:
            gender = fields[3]
            if gender == "Male":
                total_male += 1
            elif gender == "Female":
                total_female += 1
            
    return (total_male, total_female)
M,F = analyze()
print(f"male total: {M}")
print(f"female total: {F}")

x = ["female","male"]
y = [F,M]
plt.bar (x,y)
plt.show()