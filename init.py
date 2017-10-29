import zipfile
import os
import tarfile,sys,shutil,traceback
import config as cfg

print "extraing zip files"
current_path = os.getcwd() # finding working or current directory path
file_path = current_path + "/submissions"
source_file_path = current_path + "/source"
compile_file_path = source_file_path + "/compile.py"
execution_file_path = source_file_path + "/execute.py"
diff_file_path = source_file_path + "/diff.py"
documentation_file_path = ""
output_file_path_list = []

#creating all submission files directory if not exists  
directory = os.path.dirname(file_path)
if not os.path.exists(directory):
    os.makedirs(directory)
    
# extract zip file to submissions folder    
zip_ref = zipfile.ZipFile( current_path + '/submissions.zip','r')
zip_ref.extractall(file_path)
zip_ref.close() # file extracting completed


# now, find out documentation file path 
for item in os.listdir(source_file_path):# loop for docx file into root dir
    if (item.endswith(".xlsx")):# check for ".xlsx" extension
        documentation_file_path = source_file_path + "/" + item
    elif (item.endswith(".out")):
        output_file_path_list.append(source_file_path + "/" + item)    
        
# now, check all tar files and untar then into separated folder
for item in os.listdir(file_path):# loop through items in submission dir   
    if (item.endswith(".gz")):# check for ".zip" extension 
        # separating student name(firstname and lastname) from tar file(Like:    cse221_Dipanjan_Das_hw0.tar.gz)       
        index_of_dot = item.index('.')
        file_name_without_extension = item[:index_of_dot]
        student_course = ''
        if cfg.init['course_name'] in file_name_without_extension:
            student_course = file_name_without_extension.split(cfg.init['course_name'])[1] # extrating student name with course 
        else: student_course = file_name_without_extension # if student does not maintain folder naming convention            
        student_name = student_course.replace(cfg.init['course_num'],'')
        student_filepath = file_path + '/' + student_name
        
        # make dir for this student 
        if not os.path.exists(student_filepath):
            os.makedirs(student_filepath)
        #already stored tar file path    
        tar_file_path = file_path + '/' + item
        tar_file_new_path = student_filepath + '/'+item # new tar file path 
        
        # move submission tar file to student specific folder
        shutil.move(tar_file_path, tar_file_new_path)
        # Now, extract the submission tar file (exsisting files: dec2hex.c, hex2dec.c, Makefile)
	try:
            tar = tarfile.open(tar_file_new_path)
            tar.extractall(student_filepath)
            tar.close()#extracting completed
	except:
	    print 'error path: ' + tar_file_new_path
	    traceback.print_exc()	    
        
        # copy compile and execution python file to student specific folder
	try:
            shutil.copy2(compile_file_path,student_filepath)
	except IOError as err:
	    print("IO error: {0}".format(err))

	try:
            shutil.copy2(execution_file_path,student_filepath)
	except IOError as err:
	    print("IO error: {0}".format(err))        
        
        # copy output checking python file to student specific folder
	try:
            shutil.copy2(diff_file_path,student_filepath)
	except IOError as err:
	    print("IO error: {0}".format(err))         
           
        # copy documentation file to student specific folder
	try:
            shutil.copy2(documentation_file_path,student_filepath)
	except IOError as err:
	    print("IO error: {0}".format(err)) 
        
        
        # copy all output file to student specific folder
        for output_file_path in output_file_path_list:
	    try:
                shutil.copy2(output_file_path,student_filepath)
	    except IOError as err:
	        print("IO error: {0}".format(err))             
    
    else:
        print "Not a tar.gz file: " + item   

print "all files extracted to submission folder"





