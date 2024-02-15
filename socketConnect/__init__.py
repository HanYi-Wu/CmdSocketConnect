import socket

print("欢迎使用socket便携连接软件")
print("开发者:吴Hen")
print("请注意，如果是本机socket链接，ip填写127.0.0.1，如果不是，请确保服务端具有外网ip")
print("查看ip方式：打开cmd，输入ipconfig，复制ipv4地址")
host = str(input("输入ip："))
port = int(input("输入port："))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
print('已连接到服务器')
while True:
    data = input('请输入要发送给服务器的数据: ')
    if data == 'quit':
        break
    client_socket.send(data.encode())
    response = client_socket.recv(1024).decode()
    print('服务器响应:', response)
client_socket.close()
