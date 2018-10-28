import socket
import time

drone = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
drone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
drone.bind(('',8890))
# sendmessage = input()
sendmessage = 'takeoff'
drone.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
drone.sendto(sendmessage.encode(encoding="utf-8"), 0, ('192.168.10.1', 8889))
message = drone.recv(1024)
print (message)
print("Hello")

time.sleep(5)
drone.sendto('land'.encode(), 0, ('192.168.10.1', 8889))