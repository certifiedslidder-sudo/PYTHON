import os

for i in range(0,100):
    os.rename(f"data/Day{i+1}",f"data/Tutorial {i+1}")  
    #rename: source, destination
    #all 1000 folders under data directory are renamed as Tutorial from Day in fraction of seconds..
    
    