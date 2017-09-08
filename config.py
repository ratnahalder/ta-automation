#!/usr/bin/env python
init = {'course_name': 'cse221_',
        'course_num': '_hw0'}

execute={'dec2hex_program': './dec2hex',
         'dec2hex_arguments': ['10','20','23'],
         'dec2hex_output_file': 'dec2hex.sout',
         'hex2dec_program': './hex2dec',
         'hex2dec_arguments': ['FF','-FF','0xFF','ff','0xff', '+0xff','-0xff','fF','-fF','+fF','-0xFf','+0XfF'],
         'hex2dec_output_file': 'hex2dec.sout'}
         
diff = {'final_output': 'hex2dec.out',
        'student_output': 'hex2dec.sout'}         
