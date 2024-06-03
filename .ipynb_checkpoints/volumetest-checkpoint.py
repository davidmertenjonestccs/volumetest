import numpy as np
import pandas as pd
from datetime import datetime
import yaml

with open('/credentials/config.yml','r') as file:
    config = yaml.safe_load(file)
    
print(config['username'])
print(config['password'])

config['timestamp'] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

print(config['timestamp'])

with open('/credentials/config.yml', 'w') as file:
        yaml.dump(config, file, default_flow_style=False)
        