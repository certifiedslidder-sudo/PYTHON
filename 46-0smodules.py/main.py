import os
if(not os.path.exists("data")):
    os.mkdir("data") #in fraction of seconds 100 folders are created under the data directory.
    
     #ek directory ban jaegi data naam se
for i in range(0,100):
    os.mkdir(f"data/Day{i+1}")      #throgh error that data file already exists
    
    
    