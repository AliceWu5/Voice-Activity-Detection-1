#!/usr/bin/python


import os, sys


def write_to_file(array_1, array_2):
  f = open('../silences.txt','w')
  for i in range (0,len(array_1)):
   #string1 = str(array_1[i]) + ' ' + str(array_2[i]) + ' ' + 'SIL' + '\n'
   print i, float(array_1[i])/float(200) , float(array_2[i])/float(200)
   string2 = str((float(array_1[i])/float(200))) + ' ' + str(float(array_2[i])/(float(200))) + ' ' + 'SIL' + '\n'
   #f.write(string1)
   f.write(string2)
  f.close()  

def get_breaks(array):
   break_array = []
   start_array = []
   start_array.append(array[0])
   for i in range(0,len(array)-1):
        
        current_count = array[i]
        next_count = array[i+1]
        if int(next_count) - int(current_count) == 1:
             pass
        else:
             break_array.append(array[i])
             start_array.append(array[i+1])
   break_array.append(array[i+1])
   return break_array, start_array 

def convert(folder):
    print folder
    os.chdir(folder)
    files = os.listdir('.')
    for file in files:
         #print file
         f = open(file)
         start_silence = []
         end_silence = []
         line_number = 0
         #print line_number
         for line in f:
              #print line 
              if line.split('\n')[0] == '0':
                    
                    start_silence.append(line_number)
              else:
                    end_silence.append(line_number)
              line_number = line_number  + 1 
         #print start_silence        
         print start_silence 
         breaks, start = get_breaks(start_silence)   
         print start
         print  breaks  
         write_to_file(start,breaks)                  


if __name__ == '__main__':
    folder = '../energy'
    convert(folder)






