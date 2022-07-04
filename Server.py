import argparse

from sys import argv
import socket

parser = argparse.ArgumentParser(description="""This is a very basic server program that reverses string data sent to it by client""")
parser.add_argument('port', type=int, help='This is the port to listen for the client on', action='store')
args = parser.parse_args(argv[1:])

HOST = socket.gethostbyname(socket.gethostname())
PORT = args.port

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST,PORT))
print(f'{HOST} listening on {PORT}')
sock.listen()
conn,addr = sock.accept()
print(f'{addr} has connected')
data = conn.recv(1024)
while(data):
    answer = data.decode('utf-8')
    encoded = answer[::-1].encode('utf-8')
    conn.sendall(encoded)
    data = conn.recv(1024)
sock.close()
print('program has completed')
