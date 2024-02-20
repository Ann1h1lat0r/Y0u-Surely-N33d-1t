import dns 
import dns.resolver 
import socket

#This program is a simple DNS exploration tool that can be used to find subdomains and their IP addresses.

def ReverseDNS(ip): #Reverse DNS lookup
 try:
    result = socket.gethostbyaddr(ip)
 except: 
    return []
 return [result[0]]+result[1] #result[0] is the primary domain name, result[1] is the list of aliases



def DNSRequest(domain): #DNS query
 try:
  result = dns.resolver.resolve(domain,"A") #A is the type of the record
  if result:
   print(domain)
   for answer in result :
    print(answer)
    print("Domain Names: %s" %ReverseDNS(answer.to_text()))
 except (dns.resolver.NXDOMAIN, dns.exception.Timeout, dns.resolver.NoAnswer): #If the domain does not exist or the server does not respond or there is no answer
  return

def SubdomainSearch(domain, dictionary, nums): #Search for subdomains
 for word in dictionary:
   subdomain = word+"."+domain
   DNSRequest(subdomain)
   if nums: #If the user wants to add numbers to the subdomains
     for i in range(0,10):
       s = word+str(i)+"."+domain
       DNSRequest(s) 


domain = "google.com"  #Change it and put the domain you want to scan
d = "/home/../../subdomains-top1mil-110000.txt" #The path to the dictionary file your wordlist

dictionary = []

with open(d,"r") as f : 
 dictionary = f.read().splitlines() #split the file into lines and store them in the list
 print(dictionary)


SubdomainSearch(domain,dictionary,True) #The last parameter is a boolean, if it is True, the program will add numbers to the subdomains
