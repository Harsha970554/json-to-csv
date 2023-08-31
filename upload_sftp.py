import paramiko

host = '13.77.172.130'
port = 22
username = 'sftp_user'
password='sftp_user123'


local_path = 'c:/Users/Harsha vardhan reddy/outputfile.csv'
remote_path = '/sftp_user/Upload_file.txt'

transport = paramiko.Transport((host, port))
transport.connect(username=username,password=password)
sftp = paramiko.SFTPClient.from_transport(transport)

sftp.put(local_path, remote_path)

sftp.close()
transport.close()
