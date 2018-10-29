# -*- coding: utf-8 -*- 

import socket
from tkinter import *


tk=Tk()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('',8890))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)

text=StringVar()
name=StringVar()
name.set('ToTello')
text.set('')
tk.title('Command Control Tello')
tk.geometry('400x300')

log = Text(tk)
nick = Entry(tk, textvariable=name)
msg = Entry(tk, textvariable=text)
msg.pack(side='bottom', fill='x', expand='true')
nick.pack(side='bottom', fill='x', expand='true')
log.pack(side='top', fill='both',expand='true')
sock.sendto('command'.encode(encoding="utf-8"),('192.168.10.1',8889))

def loopproc():
	log.see(END)
	s.setblocking(False)
	try:
		msg = s.recv(1024)
		# print(message)
		log.insert(END, msg )
		log.insert(END, '\n' )
	except:
		tk.after(1,loopproc)
		return
	tk.after(1,loopproc)
	return

def sendproc(event):
	sock.sendto((text.get()).encode(encoding="utf-8"),('192.168.10.1',8889))
	text.set('')

msg.bind('<Return>',sendproc)

msg.focus_set()

tk.after(1,loopproc)
tk.mainloop()
