from scapy.all import *
import os
import sys
import threading
import signal

ports = [21, 22, 23, 25, 53, 80, 443, 445, 443, 8080, 8443]

def SYNscan(target):
    #sr is send and receive
    ans, unans = sr(IP(dst=target)/TCP(dport=ports, flags="S"), timeout=3, verbose=0)
    print("Open ports at:%s" %target)
    for s, r in ans:
        if s[TCP].dport == r[TCP].sport:
            print(s[TCP].dport, "is open")


def DNSscan(target):
    #rd=1 is recursion desired | qd is query domain | DNSQR is DNS query record | qname is query name | timeout is the time to wait for an answer
    ans, unans = sr(IP(dst=target)/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname="www.google.com")), timeout=1, verbose=0)
    for s, r in ans:
        #sprintf is a scapy function to format the string
        print(r.sprintf("%IP.src% is alive"))

target = "8.8.8.8" #string because it's an IP address; if it was a domain, change this to yout target host
SYNscan(target)
DNSscan(target)
