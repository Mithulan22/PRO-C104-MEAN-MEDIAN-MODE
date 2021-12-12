import csv
import math

with open ("Data.csv", newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data.pop[0]
def mean(data):
    total = 0
    n = len(data)
    for x in data:
        total += int(x)
    mean = total / new_data
    return mean  

squared_list = []
for number in data:
    a = int(number)-mean(data)
    a = a**2
    squared_list.append(a)

sum = 0
for i in squared_list:
    sum = sum+i
result = sum/(len(data)-1)

std = math.sqrt(result)
print(std)