import snowflake.connector
import csv
conn = snowflake.connector.connect(
    user='incentsoft',
    password='V3rySecureN0w',
    account='qa50269',
    warehouse='COMPUTE_WH',
    region='west-us-2.azure',
    database='snowflake_sample_data',
    schema='TPCDS_SF10TCL')
    

cursor = conn.cursor()
query='select * from call_center'
cursor.execute(query)

rows = cursor.fetchall()
output_file = 'outputfile.csv'


with open(output_file, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow([i[0] for i in cursor.description])  
    csv_writer.writerows(rows)  
cursor.close()
conn.close()


