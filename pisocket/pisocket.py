#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# pisocket
# Telnet for sharing texts on LED banner
#
# see ../LICENSE file for licence
# see README.md for more info
# see CHANGELOG.md for detailed changes in each version
#
# (c) 2017 kj/P1X
#

import socket
import struct
import threading
import config

cfg = config.Config()


print('Starting PiSocket Server...')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((cfg.get_setting('server_ip'), cfg.get_setting('server_port')))
sock.listen(1)
print('[i] Server is running at {ip}:{port}'.format(
    ip = cfg.get_setting('server_ip'), 
    port = str(cfg.get_setting('server_port'))))

clients = []

def handler(c, a):
    global clients
    global cfg

    while True:
        data = c.recv(1024)

        for client in clients:
            if not client == c:
                client.send(cfg.get_msg('chat') + bytes(data) + cfg.get_msg('chat_reset'))
        if not data:
            clients.remove(c)
            c.close()
            for client in clients:
                client.send(cfg.get_msg('disconnected'))
                print(cfg.get_msg('disconnected'))
            break

def format_msg(msg):
    return bytes('{color}{msg}\n'.format(
        color = cfg.get_style('info'),
        msg = cfg.get_msg(msg)))

while True:
    c, a = sock.accept()
    thread = threading.Thread(target=handler,args=(c, a))
    thread.daemon = True
    thread.start()
    clients.append(c)
    for cli in clients:
        cli.family
        if not cli == c:
            cli.send(cfg.get_msg('connected'))
        else:  
            color = cfg.get_style('info'),
            cli.send(cfg.get_msg('welcome'))
    print(cfg.get_msg('connected'))  color = cfg.get_style('info'),  color = cfg.get_style('info'),  color = cfg.get_style('info'),