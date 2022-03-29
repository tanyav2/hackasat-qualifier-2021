import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 12345))
data = s.recv(22)

# split string into two variables
ns = data.decode("utf-8").split(" ")

n1 = int(ns[0])
n2 = int(ns[2])
sum = n1 + n2
str_sum = str(sum)
s.send(str_sum.encode())
