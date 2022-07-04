import argparse

from sys import argv
import socket

parser = argparse.ArgumentParser(description="""This is a very basic server program that reverses string data sent to it by client""")
parser.add_argument('port', type=int, help='This is the port to listen for the client on', action='store')
args = parser.parse_args(argv[1:])

HOST = socket.gethostbyname(socket.gethostname())
PORT = args.port

MAX = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Timeout value is 20 seconds.')
sock.settimeout(20)
sock.bind((HOST,PORT))
print(f'{HOST} listening on {PORT} :')
sock.listen()
conn,addr = sock.accept()
print(f'{addr} has connected.')
data = conn.recv(MAX)
while(data):
    answer = data.decode('utf-8')
    conn.sendall(answer[::-1].encode('utf-8'))
    data = conn.recv(MAX)
sock.close()
print('Program has completed.')
