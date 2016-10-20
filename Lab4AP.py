import csv

f = open('D:\NUST\Semester 5\Advanced Programming\Labs\Academic _Schedule.csv')
csv_f = csv.reader(f)

#for row in csv_f:
  #print row
  
activity_list = []
for row in csv_f:
  activity_list.append(row[2])
print activity_list

priority_set = set(activity_list)
print priority_set

