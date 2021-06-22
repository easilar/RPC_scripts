import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

def get_df_from_csv(csv="SweepData/fpga_2_top_2021-06-21_10_16_47.csv", channel1=70,channel15=84)
    csv_file_name = csv
    df = pd.read_csv(csv_file_name,index_col=None, delimiter=',', header =0)
    return df
    
def get_scurve_param(df):
    df = df.T
    normalized_df=(df-df.min())/(df.max()-df.min())
    new_df = normalized_df
    channel_mean_list = []
    channel_mean_5sigma_diff_list = []
    for i in range(channel1,channel15):
            channel_mean_low = float(new_df.index[new_df[i] < round(new_df.mean()[i],5)].tolist()[0])
            channel_mean_high = float(new_df.index[new_df[i] > round(new_df.mean()[i],5)].tolist()[-1])
            channel_mean = 0.5*(channel_mean_low+channel_mean_high)
            channel_mean_list.append(channel_mean)
            channel_mean_5sigma = float(new_df.index[new_df[i] < 0.00006].tolist()[0])
            channel_mean_5sigma_diff = channel_mean_5sigma-channel_mean
            channel_mean_5sigma_diff_list.append(channel_mean_5sigma_diff)
            print(channel_mean,channel_mean_5sigma,channel_mean_5sigma_diff)
    return (channel_mean_list,channel_mean_5sigma_diff_list)

def get_new_df(csv_file):
        df = pd.read_csv(csv_file,index_col=None, delimiter=',', header =0)
        new_df = pd.DataFrame(columns=[x for x in df.columns if "Number" in x])
        new_df["DAC T"] = [i for i in range(400,500)]
        new_df.set_index('DAC T', inplace=True)
        for r in range(len(df)):
            for i in range(16):
                #print(i)
                new_df.loc[df.loc[r,"DAC T - Tracé "+str(i)],"Number of TDC in time window - Tracé "+str(i)]  = df.loc[r, "Number of TDC in time window - Tracé "+str(i)]
        return new_df
    
def dropcol(df):
    return df.drop(['Number of TDC in time window - Tracé 0'], axis=1)

def normalise_max(df):
    normalized_df=(df-df.min())/(df.max()-df.min())
    return normalized_df

def normalise(df,max_norm=1539):
    normalized_df=(df-df.min())/(max_norm-df.min())
    return normalized_df

def get_3Sigma(new_df):
    channel_mean_3sigma_diff_list = []
    for i in range(0,16):
        channel_mean = new_df.index[new_df['Number of TDC in time window - Tracé '+str(i)] < round(new_df.mean()[i],5)].tolist()[0]
        channel_mean_3sigma = new_df.index[new_df['Number of TDC in time window - Tracé '+str(i)] < 0.0015].tolist()[0]
        channel_mean_3sigma_diff = channel_mean_3sigma-channel_mean
        #print(i,channel_mean_3sigma_diff,channel_mean_3sigma_diff_charge)
        channel_mean_3sigma_diff_list.append(channel_mean_3sigma_diff)
    return channel_mean_3sigma_diff_list

def get_5Sigma(new_df):
    channel_mean_5sigma_diff_list = []
    for i in range(0,16):
        channel_mean = new_df.index[new_df['Number of TDC in time window - Tracé '+str(i)] < round(new_df.mean()[i],5)].tolist()[0]
        channel_mean_5sigma = new_df.index[new_df['Number of TDC in time window - Tracé '+str(i)] < 0.00006].tolist()[0]
        channel_mean_5sigma_diff = channel_mean_5sigma-channel_mean
        #print(i,channel_mean_3sigma_diff,channel_mean_3sigma_diff_charge)
        channel_mean_5sigma_diff_list.append(channel_mean_5sigma_diff)
    return channel_mean_5sigma_diff_list

def get_mean(new_df):
    channel_mean_list = []
    for i in range(0,16):
        channel_mean_low = new_df.index[new_df['Number of TDC in time window - Tracé '+str(i)] < round(new_df.mean()[i],5)].tolist()[0]
        channel_mean_high = new_df.index[new_df['Number of TDC in time window - Tracé '+str(i)] > round(new_df.mean()[i],5)].tolist()[-1]
        channel_mean = 0.5*(channel_mean_low+channel_mean_high)
        #print(i,channel_mean_3sigma_diff,channel_mean_3sigma_diff_charge)
        channel_mean_list.append(channel_mean)
    return channel_mean_list
    
def times5p5(x):
    return 5.5*x
