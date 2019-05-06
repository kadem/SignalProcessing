# -*- coding: utf-8 -*-
"""
Created on Wed May  1 20:28:41 2019

@author: Kamil Adem
"""
import scipy.io
import pandas as pd
import numpy as np
import math

def initialize():
    mat = scipy.io.loadmat("train.mat")
    mat.pop('__header__')
    mat.pop('__globals__')
    mat.pop('__version__')

    cyl_ch1 = pd.DataFrame(mat['cyl_ch1_full'])
    cyl_ch2 = pd.DataFrame(mat['cyl_ch2_full'])
    
    hook_ch1 = pd.DataFrame(mat['hook_ch1_full'])
    hook_ch2 = pd.DataFrame(mat['hook_ch2_full']) 
    
    lat_ch1 = pd.DataFrame(mat['lat_ch1_full'])
    lat_ch2 = pd.DataFrame(mat['lat_ch2_full'])
    
    palm_ch1 = pd.DataFrame(mat['palm_ch1_full'])
    palm_ch2 = pd.DataFrame(mat['palm_ch2_full']) 
    
    spher_ch1 = pd.DataFrame(mat['spher_ch1_full'])
    spher_ch2 = pd.DataFrame(mat['spher_ch2_full']) 
    
    tip_ch1 = pd.DataFrame(mat['tip_ch1_full'])
    tip_ch2 = pd.DataFrame(mat['tip_ch2_full']) 
    
    data_ch1 = pd.concat([cyl_ch1, hook_ch1], ignore_index = True)
    data_ch1 = pd.concat([data_ch1, lat_ch1], ignore_index = True)
    data_ch1 = pd.concat([data_ch1, palm_ch1], ignore_index = True)
    data_ch1 = pd.concat([data_ch1, spher_ch1], ignore_index = True)
    data_ch1 = pd.concat([data_ch1, tip_ch1], ignore_index = True)

    data_ch2 = pd.concat([cyl_ch2, hook_ch2], ignore_index = True)
    data_ch2 = pd.concat([data_ch2, lat_ch2], ignore_index = True)
    data_ch2 = pd.concat([data_ch2, palm_ch2], ignore_index = True)
    data_ch2 = pd.concat([data_ch2, spher_ch2], ignore_index = True)
    data_ch2 = pd.concat([data_ch2, tip_ch2], ignore_index = True)
    
    cyl_class = pd.DataFrame(index = cyl_ch1.index, columns = ['class'])
    cyl_class['class'] = 1
    
    hook_class = pd.DataFrame(index = hook_ch1.index, columns = ['class'])
    hook_class['class'] = 2
    
    lat_class = pd.DataFrame(index = lat_ch1.index, columns = ['class'])
    lat_class['class'] = 3
    
    palm_class = pd.DataFrame(index = palm_ch1.index, columns = ['class'])
    palm_class['class'] = 4
    
    spher_class = pd.DataFrame(index = spher_ch1.index, columns = ['class'])
    spher_class['class'] = 5

    tip_class = pd.DataFrame(index = tip_ch1.index, columns = ['class'])
    tip_class['class'] = 6
    
    classes = pd.concat([cyl_class, hook_class], ignore_index = True)
    classes = pd.concat([classes, lat_class], ignore_index = True)
    classes = pd.concat([classes, palm_class], ignore_index = True)
    classes = pd.concat([classes, spher_class], ignore_index = True)
    classes = pd.concat([classes, tip_class], ignore_index = True)

    return data_ch1, data_ch2, classes

def MeanAbsVal(data):
    list_mav = []
    for i in range(data.shape[0]):
        mav = data.query('@i')
        mav = abs(mav)
        mav = mav.sum()/mav.shape[0]
        list_mav.append(mav)
    return list_mav

def RootMeanSquare(data):
    list_rms  = []
    for i in range(data.shape[0]):
        rms = data.query('@i')
        rms = rms**2
        rms = rms.sum()/rms.shape[0]
        rms = math.sqrt(rms)
        list_rms.append(rms)
    return list_rms

def IntegratedAbsVal(data):
    list_iav = []
    for i in range(data.shape[0]):
        iav = data.query('@i')
        iav = iav.abs()
        iav = iav.sum()
        list_iav.append(iav)
    return list_iav

def SimpleSquaredInterval(data):
    list_ssi = []
    for i in range(data.shape[0]):
        ssi = data.query('@i')
        ssi = ssi **2
        ssi = ssi.sum()
        list_ssi.append(ssi)
    return list_ssi

def Variance(data):
    list_var = []
    for i in range(data.shape[0]):
        var = data.query('@i')
        var = var **2
        var = var.sum()/((var.shape[0])-1)
        list_var.append(var)
    return list_var

def StandardDeviation(data):
    list_dev = []
    for i in range(data.shape[0]):
        dev = data.query('@i')
        mean = dev.mean()
        dev = dev - mean
        dev = dev **2
        dev = dev.sum()/((dev.shape[0])-1)
        dev = math.sqrt(dev)
        list_dev.append(dev)
    return list_dev

def DiffAbsStandDevVal(data):
    list_dev = []
    for i in range(data.shape[0]):
        dev = data.query('@i').values
        sum_val = 0
        for w in range(len(dev)-1):
            diff = dev[w+1] - dev[w]
            val = diff **2
            sum_val = sum_val + val
        sum_val = sum_val/(len(dev)-1)
        list_dev.append(math.sqrt(sum_val))
    return list_dev

def ZeroCrossing(data):
    threshold = 0.01
    list_zc = []
    for i in range(data.shape[0]):
        zc = data.query('@i').values
        count = 0
        for w in range(len(zc)-1):
            if (zc[w] >0 and zc[w+1] <0 and abs(zc[w]-zc[w+1]) >= threshold):
                count += 1
            elif (zc[w] <0 and zc[w+1] >0 and abs(zc[w]-zc[w+1]) >= threshold):
                count +=1
        list_zc.append(count)
    return list_zc

def SlopeSignChange(data):
    threshold = 0.01
    list_ssc = []
    for i in range(data.shape[0]):
        ssc = data.query('@i').values
        count = 0
        for w in range(1, len(ssc)-1):
            if ((ssc[w] >ssc[w-1] and ssc[w]>ssc[w+1]) and (abs(ssc[w]-ssc[w+1])>=threshold or abs(ssc[w]-ssc[w-1])>=threshold)):
                count +=1
            elif ((ssc[w]<ssc[w-1] and ssc[w]<ssc[w+1]) and (abs(ssc[w]-ssc[w+1])>=threshold or abs(ssc[w]-ssc[w-1])>=threshold)):
                count+=1
        list_ssc.append(count)
    return list_ssc

def WaveFormLength(data):
    list_wl = []
    for i in range(data.shape[0]):
        wl = data.query('@i').values
        sum_val = 0
        for w in range(len(wl)-1):
            diff = wl[w+1] - wl[w]
            sum_val = sum_val + abs(diff)
        list_wl.append(sum_val)
    return list_wl

def AverageAmplitudeChange(data):
    list_aac = []
    for i in range(data.shape[0]):
        aac = data.query('@i').values
        sum_val = 0
        for w in range(len(aac)-1):
            diff = aac[w+1] - aac[w]
            sum_val = sum_val + abs(diff)
        list_aac.append(sum_val/len(aac))
    return list_aac

def WillisonAmplitude(data):
    list_wamp = []
    threshold = 0.01
    for i in range(data.shape[0]):
        wamp = data.query('@i').values
        count = 0
        for w in range(len(wamp)-1):
            diff = abs(wamp[w] - wamp[w+1])
            if (diff>= threshold):
                count+=1
        list_wamp.append(count/len(wamp))
    return list_wamp


def MyopulsePercentageRate(data):
    list_mypr = []
    threshold = 0.01
    for i in range(data.shape[0]):
        mypr = data.query('@i').values
        count = 0
        for w in range(len(mypr)):
            if (mypr[w]>= threshold):
                count+=1
        list_mypr.append(count)
    return list_mypr

def ModifiedMeanAbsoluteValue1(data):
    list_mav = []
    for i in range(data.shape[0]):
        mav = data.query('@i')
        mav = abs(mav)
        sum_val = 0
        for w in range(len(mav)):
            if (w >= (0.25*len(mav)) or w <= (0.75*len(mav))):
                sum_val += mav[w]
            else:
                sum_val += 0.5 * mav[w]
        mav = sum_val/len(mav)
        list_mav.append(mav)
    return list_mav

def ModifiedMeanAbsoluteValue2(data):
    list_mav = []
    for i in range(data.shape[0]):
        mav = data.query('@i')
        mav = abs(mav)
        sum_val = 0
        for w in range(len(mav)):
            if (w >= (0.25*len(mav)) or w <= (0.75*len(mav))):
                sum_val += mav[w]
            elif (w<0.25*len(mav)):
                sum_val += (4*i)/len(mav) * mav[w]
            else:
                sum_val += 4*(i-len(mav))/len(mav) * mav[w]
        mav = sum_val/len(mav)
        list_mav.append(mav)
    return list_mav

def logDetect(data):
    list_log = []
    val = math.e
    for i in range(data.shape[0]):
        log = data.query('@i')
        log = abs(log)
        log = np.log10(log)   
        log = np.sum(log)/data.shape[1]
        log = val ** log
        list_log.append(log)
    return list_log

def TemporalMoments3(data):
    list_tm = []
    for i in range(data.shape[0]):
        tm = data.query('@i')
        tm = tm ** 3
        tm = tm.sum()/tm.shape[0]
        list_tm.append(tm)
    return list_tm

def TemporalMoments4(data):
    list_tm = []
    for i in range(data.shape[0]):
        tm = data.query('@i')
        tm = tm ** 4
        tm = tm.sum()/tm.shape[0]
        list_tm.append(tm)
    return list_tm

def TemporalMoments5(data):
    list_tm = []
    for i in range(data.shape[0]):
        tm = data.query('@i')
        tm = tm ** 5
        tm = tm.sum()/tm.shape[0]
        list_tm.append(tm)
    return list_tm

def extract(data, classes):
    
    MAV = MeanAbsVal(data)
    VAR = Variance(data)
    SD = StandardDeviation(data)
    DASDV = DiffAbsStandDevVal(data)
    AAC = AverageAmplitudeChange(data)
    WAMP = WillisonAmplitude(data)    
    LD = logDetect(data)
    TM3 = TemporalMoments3(data)
    TM4 = TemporalMoments4(data)

#    MAV1 = ModifiedMeanAbsoluteValue1(data)
#    MAV2 = ModifiedMeanAbsoluteValue2(data)
#    RMS = RootMeanSquare(data)
#    IAV = IntegratedAbsVal(data)
#    SSI = SimpleSquaredInterval(data)
#    ZC = ZeroCrossing(data)
#    SSC = SlopeSignChange(data)
#    WL = WaveFormLength(data)
#    MYPR = MyopulsePercentageRate(data)
#    TM5 = TemporalMoments5(data)

    MAV = pd.DataFrame(MAV, columns = ['MAV'])
    VAR = pd.DataFrame(VAR, columns = ['VAR'])
    SD = pd.DataFrame(SD, columns = ['SD'])
    DASDV = pd.DataFrame(DASDV, columns = ['DASDV'])
    AAC = pd.DataFrame(AAC, columns = ['AAC'])
    WAMP = pd.DataFrame(WAMP, columns = ['WAMP']) 
    LD = pd.DataFrame(LD, columns = ['LD'])
    TM3 = pd.DataFrame(TM3, columns = ['TM3'])
    TM4 = pd.DataFrame(TM4, columns = ['TM4'])
    
#    MAV1 = pd.DataFrame(MAV1, columns = ['MAV1'])
#    MAV2 = pd.DataFrame(MAV2, columns = ['MAV2'])
#    RMS = pd.DataFrame(RMS, columns = ['RMS'])
#    IAV = pd.DataFrame(IAV, columns = ['IAV'])
#    SSI = pd.DataFrame(SSI, columns = ['SSI'])
#    ZC = pd.DataFrame(ZC, columns = ['ZC'])
#    SSC = pd.DataFrame(SSC, columns = ['SSC'])
#    WL = pd.DataFrame(WL, columns = ['WL'])
#    MYPR = pd.DataFrame(MYPR, columns = ['MYPR'])
#    TM5 = pd.DataFrame(TM5, columns = ['TM5'])

    data = data.join(MAV, how = 'outer')
    data = data.join(VAR, how = 'outer')
    data = data.join(SD, how = 'outer')
    data = data.join(DASDV, how = 'outer')
    data = data.join(AAC, how = 'outer')
    data = data.join(WAMP, how = 'outer')
    data = data.join(LD, how = 'outer')
    data = data.join(TM3, how = 'outer')
    data = data.join(TM4, how = 'outer')
    
#    x = x.join(MAV1, how = 'outer')
#    x = x.join(MAV2, how = 'outer')
#    x = x.join(RMS, how = 'outer')
#    x = x.join(IAV, how = 'outer')
#    x = x.join(SSI, how = 'outer')
#    x = x.join(ZC, how = 'outer')
#    x = x.join(SSC, how = 'outer')                                                                                                                                                                                                                                                                                                                                             
#    x = x.join(WL, how = 'outer')
#    x = x.join(MYPR, how = 'outer')
#    x = x.join(TM5, how = 'outer')

    data = data.join(classes, how = 'outer')
    return data

def write_to_file(data_ch1, data_ch2):
    data_ch1 = data_ch1.sample(frac = 1)
    data_ch2 = data_ch2.sample(frac = 1)
    
    data_ch1.to_csv(r'complete_features_ch1.txt', index=None, header = None, sep=',', mode='w')
    data_ch2.to_csv(r'complete_features_ch2.txt', index=None, header = None, sep=',', mode='w')


data_ch1, data_ch2, classes = initialize()
data_ch1 = extract(data_ch1, classes)
data_ch2 = extract(data_ch2, classes)
write_to_file(data_ch1, data_ch2)