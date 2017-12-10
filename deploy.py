import config as config
import paramiko
import os


paramiko.util.log_to_file('paramiko.log')
configLogstash = config.logstash


def connectToHost():
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(configLogstash["ip"], port=configLogstash["port"],
                       username=configLogstash["user"], password=configLogstash["passwd"])
    return ssh_client
    #sftp = ssh_client.open_sftp()
    #entrada, salida, error = ssh_client.exec_command('pwd')
    #ruta = salida.read().replace('\n', '')
    # sftp = ssh_client.open_sftp()  # Crea un objeto SFTPClient()

def moveFile(conn, file, dest):
     sftp = conn.open_sftp()
     sftp.put(file, dest)

def moveFiles(conn):
    # print(os.listdir(configLogstash["path"]))
    # create folder
    path_folder = configLogstash["path_remote_folder_home"] + "/"+ configLogstash["path_remote_folder_wordir"]
    stdin, stdout, ssh_stderr = conn.exec_command( "mkdir -p " + path_folder)
    for line in stdout.readlines():
         print(line)
    for line in ssh_stderr.readlines():
         print(line)

    sftp = conn.open_sftp()
    for file in os.listdir(configLogstash["path"]):
        print(file)
        sftp.put( configLogstash["path"] + "/" + file, path_folder + "/" + file)

if __name__ == '__main__':
    client = connectToHost()

    # stopEnviroment

    # cleanEnviroment

    moveFiles(client)

    # addPermisos

    # addToCrontab

    client.close()