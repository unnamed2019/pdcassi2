import socket

s = socket.socket()

host = socket.gethostname()
port = 60000

s.connect((host, port))
s.send('HelloServer!'.encode())  

with open('received.txt', 'wb') as f:
    print('File opened')
    while True:
        print('Receiving data...')
        data = s.recv(1024)
        if not data:
            break
        print('Data =>', data.decode())
        f.write(data)

print('Successfully received the file')
s.close()
print('Connection closed')
