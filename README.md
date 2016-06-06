# Dash Deploy

Dash Deploy allows you to fire deployments from Deploybot.com using Amazon Dash buttons. Multiple buttons can be configured at a time.  Configuration:

button_name = ''  # Button Name for your reference.
    
deployed_by = ''  # Name of person or device deploying.
    
env_name = ''     # Environment name.
    
env_id = ''       # Your environment ID, can be found under repository "Settings" -> "Webhooks & Badges".
    
secret = ''       # Your webhook secret key, can be found under repository "Settings" -> "Webhooks & Badges".

Included is also a supervisord config file for daemonizing dash-deploy.

For information on how to setup your amazon dash button to find its mac address, check out this article here: https://medium.com/@edwardbenson/how-i-hacked-amazon-s-5-wifi-button-to-track-baby-data-794214b0bdd8

# Deploybots roll out!
![alt text](http://i.imgur.com/YyiYx7K.jpg "Deploybots roll out!")
