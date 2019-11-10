
# # Python code to search .py files in current 
# # folder (We can change file type/name and path 
# # according to the requirements. 
# import os 
  
# # This is to get the directory that the program  
# # is currently running in. 
# dir_path = os.path.dirname(os.path.realpath(__file__)) 
  
# for root, dirs, files in os.walk(dir_path): 
#     for file in files:
#         # change the extension from '.mp3' to  
#         # the one of your choice. 
#         if file.endswith('.py'): 
#             print(root+'/'+str(file)) 

# from os.path import exists, join
# from os import pathsep
# from string import *

# def search_file(filename, search_path):
#    """Given a search path, find file
#    """
#    file_found = 0
#    paths = string.split(search_path, pathsep)
#    for path in paths:
#       if exists(join(path, filename)):
#           file_found = 1
#           break
#    if file_found:
#       return abspath(join(path, filename))
#    else:
#       return None

# if __name__ == '___main__':
#    search_path = '/bin' + pathsep + '/usr/bin'  # ; on windows, : on unix
#    find_file = search_file('ls',search_path)
#    if find_file:
#       print("File found at %s" % find_file)
#    else:
#       print("File not found")

