import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from mapping_dict import mapping_dict

#data_path = "/Users/asilar/Dropbox/IPNL/RPC/NewFirmware_26April/100V/Plate5mm_grounded/scratch_surface/FanCloser/6DAC/"
data_path = "/Users/asilar/Dropbox/IPNL/RPC/NewFirmware_26April/100V/Plate5mm_grounded/scratch_surface/FanCloser/tape_erny/Ground_with_braid/tape_at_the_twoside/Coolingpads/10DAC/"
#data_path = "/Users/asilar/Dropbox/IPNL/RPC/NewFirmware_26April/100V/Plate5mm_grounded/scratch_surface/FanCloser/tape_erny/4DAC/"
slist = os.listdir(data_path)
Return_strip = False
for s in slist:
    if "raw" in s : continue
    if not ".txt" in s : continue
    print(s)
    file_name = data_path+s
    df = pd.read_csv(file_name,index_col=None, delimiter='\t', header =None)
    print(df.max(axis=1).max())
    f = plt.figure(figsize=(20,5))
    df[0] = df[0]*0
    ax = df.plot.scatter(x=16, y=0);
    df[0] = df[0]+1
    for i in mapping_dict.keys():
        if mapping_dict[i]==-99: continue
        if Return_strip :
            if "s" in mapping_dict[i]: continue
            nstrip = int(mapping_dict[i].split("r")[1])
        else:
            if "r" in mapping_dict[i]: continue
            nstrip = int(mapping_dict[i].split("s")[1])
        print(nstrip)
        df[0] = df[0]*nstrip
        df.plot.scatter(x=i, y=0 , ax=ax);
        df[0] = df[0]*0
        df[0] = df[0]+1
    if Return_strip:
        plt.savefig(data_path+"/"+s.split(".")[0]+"_Return.png")
    else:
        plt.savefig(data_path+"/"+s.split(".")[0]+"_Direct.png")
    plt.clf()
