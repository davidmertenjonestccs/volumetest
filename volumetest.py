import numpy as np
import pandas as pd
from datetime import datetime
import yaml
import os

os.system('ls')

with open('/credentials/config.yaml','r') as file:
    config = yaml.safe_load(file)
    
print(config['username'])
print(config['password'])

print('old timestamp:')
print(config['timestamp'])

config['timestamp'] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

print('new timestamp:')
print(config['timestamp'])

with open('/credentials/config.yaml', 'w') as file:
        yaml.dump(config, file, default_flow_style=False)
        
