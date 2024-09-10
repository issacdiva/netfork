import paramiko

def run_traceroute(host, username, password, destination):
    # 创建SSH客户端
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # 连接到远程主机
        ssh_client.connect(hostname=host, username=username, password=password)

        # 执行traceroute命令
        command = f'traceroute {destination}'
        stdin, stdout, stderr = ssh_client.exec_command(command)

        # 获取命令输出
        output = stdout.read().decode()
        error = stderr.read().decode()

        if output:
            print("Traceroute Output:")
            print(output)
        if error:
            print("Traceroute Errors:")
            print(error)
        
    except paramiko.AuthenticationException:
        print("Authentication failed, please verify your credentials.")
    except paramiko.SSHException as sshException:
        print(f"Unable to establish SSH connection: {sshException}")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        # 关闭SSH连接
        ssh_client.close()

# 使用示例
remote_host = "192.168.1.10"  # 远程主机的IP地址
username = "your_username"    # 远程主机的用户名
password = "your_password"    # 远程主机的密码
destination_host = "google.com"  # 你想要追踪路由的目标主机

run_traceroute(remote_host, username, password, destination_host)