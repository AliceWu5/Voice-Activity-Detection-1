#!/usr/bin/python

import sys,re,spy
from subprocess import check_call


if (len(sys.argv)) != 3:
	print 'python gen_sil.py <input wave file> <output label file>'
	sys.exit(1)


wav_file = sys.argv[1]
lab_file = sys.argv[2]

wav,fs = spy.wavread(wav_file)

zff_obj = spy.ZeroFreqFilter()
zff_sig = zff_obj.getZFFSignal(wav,fs)

ss_obj = spy.SegmentSpeech()
vnv_reg = ss_obj.vnv(zff_sig, fs)
gci_val = ss_obj.getGCI(zff_sig, vnv_reg)
sil_lab = ss_obj.segment2c(gci_val, fs, 200)

fp = open(lab_file,'w')
for i in range(0,len(sil_lab)):
	fp.write(str(sil_lab[i][0]/1000.0) + ' ' + str(sil_lab[i][1]/1000.0) + ' ' + sil_lab[i][2]+'\n')
fp.close()
#if line.split('\n')[0] == 'SIL':
 #      sox text_01842.wav new.wav trim 0:00 sil
check_call[( 'sox', '0.2101875','1.2310625','2.4473125','3.8796875' ])
