#!/usr/bin/python
from subprocess import Popen, PIPE, STDOUT

def checkIfPortIsOpen(ip, port, timeout):
    """
        Parameters:
            ip [string]: ip address
            port [string]: port number
            timeout [string]: timeout in seconds
        Check if a port is open on a given ip using netcat command.
        Returns True if port is open, False otherwise.
    """
    p = Popen(["nc", "-zvw{timeout}".format(timeout=timeout), ip, port], stdout=PIPE, stderr=STDOUT)
    output = p.stdout.read().decode('utf-8')
    if("succeeded!" not in output):
        print("{ip}:{port} is closed".format(ip=ip, port=port))
        return None
    else:
        print("{ip}:{port} is open".format(ip=ip, port=port))
        return "{ip}:{port}".format(ip=ip, port=port)
