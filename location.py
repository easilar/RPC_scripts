import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from mapping_dict import mapping_dict

#data_path = "/Users/asilar/Dropbox/IPNL/RPC/NewFirmware_26April/5kV/data_left/10DAC/"
data_path = "/Users/asilar/Dropbox/IPNL/RPC/NewFirmware_26April/6500/80DAC/WithSource/"
slist = os.listdir(data_path)
for s_t in slist:
    if "raw" in s_t : continue
    if not ".txt" in s_t : continue
    s = s_t
    
print(s)
file_name = data_path+s
df = pd.read_csv(file_name,index_col=None, delimiter='\t', header =None)
f = plt.figure()
for i in mapping_dict.keys():
    if mapping_dict[i]==-99: continue
    if "r" in mapping_dict[i]: continue
    nstrip = int(mapping_dict[i].split("s")[1])
    print(df[i+1] - df[i])
#plt.scatter(x_list, y_list, marker='o');
#plt.xlabel("Channels")
#plt.ylabel("Counts / strips / sec ")
#if Return_strip: plt.savefig(data_path+"/"+s.split(".")[0]+"_NoiseCount_Return.png")
#else: plt.savefig(data_path+"/"+s.split(".")[0]+"_NoiseCount_Direct.png")
#plt.clf()

