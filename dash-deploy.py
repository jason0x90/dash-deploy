from scapy.all import *
import requests
import time
WEBHOOK_URL = 'https://YOURACCOUNTSUBDOMAIN.deploybot.com/webhook/deploy'

def arp_record(mac_addr):
  if mac_addr == '01:00:00:00:00:00':
    button_name = ''  # Button Name for your reference.
    deployed_by = ''  # Name of person or device deploying.
    env_name = ''     # Environment name.
    env_id = ''       # Environment ID.
    secret = ''       # Your webhook secret key.
  elif mac_addr == '02:00:00:00:00:00':
    button_name = ''
    deployed_by = ''
    env_name = ''          
    env_id = ''     
    secret = ''
  else: 
    return False
  post_data = {
    "env_id": env_id,
    "secret": secret,
    "deployed_by": deployed_by  
  }
  print "Button "+button_name+" was pressed. Deploying Environment \'"+env_name+"\'"
  r = requests.post(WEBHOOK_URL, post_data, verify=False)
  print(r.text)
  return r.text

def arp_listen(pkt):
  timestamp = time.strftime("%Y-%m-%d %H:%M")
  if pkt[ARP].op == 1: #who-has (request)
    arp_record(pkt[ARP].hwsrc)

print sniff(prn=arp_listen, filter="arp", store=0, count=0)
