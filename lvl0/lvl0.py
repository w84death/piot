#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# lvl0 - Level Zero
# Telnet multiplayer game
#
# see LICENSE file for licence
# see README.md for more info
# see CHANGELOG.md for detailed changes in each version
#
# (c) 2017 kj/P1X
#

import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 22))
sock.listen(1)

clients = []

def handler(c, a):
    global clients
    while True:
        data = c.recv(1024)
        for client in clients:
            if not client == c:
                client.send(bytes(data))
        if not data:
            clients.remove(c)
            c.close()
            break

while True:
    c, a = sock.accept()
    thread = threading.Thread(target=handler,args=(c, a))
    thread.daemon = True
    thread.start()
    clients.append(c)
    print(clients)