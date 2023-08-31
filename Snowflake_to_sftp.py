import snowflake.connector
import paramiko
import io

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
headers=[i[0] for i in cursor.description]
csv_matter=",".join(headers)+'\n'
for i in rows:
    csv_matter+= ",".join(map(str,i))+'\n'
cursor.close()
conn.close()
file_name = 'Uplad_file.csv'
host = '13.77.172.130'
port = 22
username = 'sftp_user'
password='sftp_user123'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host, port=port, username=username, password=password)

sftp = ssh.open_sftp()
csv_io = io.StringIO(csv_matter)
sftp.putfo(csv_io, file_name)
sftp.close()

ssh.close()

print("File uploaded successfully.")
