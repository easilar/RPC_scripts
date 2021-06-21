import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from mapping_dict import mapping_dict

data_path = "/Users/asilar/Dropbox/IPNL/RPC/NewFirmware_26April/100V/Plate5mm_grounded/scratch_surface/FanCloser/tape_erny/Ground_with_braid/tape_at_the_twoside/Coolingpads/4DAC/"
#data_path = "/Users/asilar/Dropbox/IPNL/RPC/NewFirmware_26April/6500/80DAC/"
slist = os.listdir(data_path)
Return_strip = True
x_tot = []
y_tot = []
for Return_strip in [True, False]:
    for s in slist:
        if "raw" in s : continue
        if not ".txt" in s : continue
        print(s)
        file_name = data_path+s
        df = pd.read_csv(file_name,index_col=None, delimiter='\t', header =None)
        max_time = df.max(axis=1).max()
        tot_sec = max_time*1e-11
        print(max_time, tot_sec)
        f = plt.figure()
        x_list = []
        y_list = []
        for i in mapping_dict.keys():
            if mapping_dict[i]==-99: continue
            if Return_strip :
                if "s" in mapping_dict[i]: continue
                nstrip = int(mapping_dict[i].split("r")[1])
            else:
                if "r" in mapping_dict[i]: continue
                nstrip = int(mapping_dict[i].split("s")[1])
            #print(nstrip, len(df[(df[i] > 0.0)]))
            x_list.append(nstrip)
            y_list.append(len(df[(df[i] > 0.0)])/(tot_sec*130))
        plt.scatter(x_list, y_list, marker='o');
        plt.xticks(np.arange(0, 48, step=2))
        plt.xlabel("Channels")
        plt.ylabel("Counts Hz / cm^2 ")
        if Return_strip: plt.savefig(data_path+"/"+s.split(".")[0]+"_NoiseCount_Return.png")
        else: plt.savefig(data_path+"/"+s.split(".")[0]+"_NoiseCount_Direct.png")
        plt.clf()
        x_tot.append(x_list)
        y_tot.append(y_list)

#print("#"*8)
#x = np.array(x_tot[0])
#y = np.array(y_tot[0])/4+np.array(y_tot[1])/4+np.array(y_tot[2])/4+np.array(y_tot[3])/4
#
#f = plt.figure()
#plt.scatter(x, y, marker='o');
#plt.xlabel("Channels")
#plt.ylabel("Counts Hz / strips ")
#if Return_strip: plt.savefig(data_path+"/"+"_NoiseCount_All_Return.png")
#else: plt.savefig(data_path+"/"+"_NoiseCount_All_Direct.png")
