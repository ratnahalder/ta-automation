import subprocess, os, sys
sys.path.insert(0,'../..')# to import module from parant-parant dir 
import config as cfg

final_result_path = os.getcwd() + '/'+cfg.diff['final_output']
student_result_path = os.getcwd() + '/'+cfg.diff['student_output']
meld = 'meld'
cmd = [meld, final_result_path, student_result_path]

subprocess.call(cmd)
