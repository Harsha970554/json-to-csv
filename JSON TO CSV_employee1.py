import json
import csv



with open('C:/Users/Harsha vardhan reddy/json to csv/employeesdatajson.json') as json_file:
	data = json.load(json_file)

employee_data = data['emp_details']



data_file = open('data_file.csv', 'w')


csv_writer = csv.writer(data_file)
count=0
for i in employee_data:
        header=i.keys()
        if count==0:
                csv_writer.writerow(header)
                count+=1
        else:
                break

for emp in employee_data:
        csv_writer.writerow(emp.values())
data_file.close()


