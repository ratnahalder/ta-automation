import subprocess, os,sys
sys.path.insert(0,'../..')# to import module from parant-parant dir 
import config as cfg

dec2hex_program =  cfg.execute['dec2hex_program'] # get exe file name for dec2hex program from config
dec2hex_arguments = cfg.execute['dec2hex_arguments']# get input value for dec2hex program from config

hex2dec_program = cfg.execute['hex2dec_program']
hex2dec_arguments = cfg.execute['hex2dec_arguments']

#execute dec2hex .exe file with argument/input and write the output into a file 
f_dec2hex = open(cfg.execute['dec2hex_output_file'],'w')
for argument in dec2hex_arguments: #loop for input values
    #temp = subprocess.call([program, argument])
    res = subprocess.Popen([dec2hex_program, argument], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
    result = res.communicate(argument)[0]
    f_dec2hex.write(result) # write output into a text file        
f_dec2hex.close()# file writing completed  

#execute hex2dec .exe file with argument/input and write the output into a file 
f_hex2dec = open(cfg.execute['hex2dec_output_file'],'wb')
for argument in hex2dec_arguments:
    res = subprocess.Popen([hex2dec_program, argument], stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, close_fds=True)
    result = (res.communicate(argument)[0]).strip('\x00') #remove extra '\x00' from output string   
    #f_hex2dec.write(bytearray(int(result, 16)))
    f_hex2dec.write(result)         
f_hex2dec.close() # file writing completed
