import os

# find current scripts directory
# https://stackoverflow.com/questions/4934806/how-can-i-find-scripts-directory-with-python
cwd = os.path.dirname(os.path.realpath(__file__))
print(cwd)
print(cwd+'\ data')
print(type(cwd))

# os.path.exists() checks if given path(file or directory) exists
# os.path.isfile() checks if given input file exists and that it is a file not directory.
print(os.path.exists(cwd+'\\data'))

#script_dir = os.path.dirname(os.path.realpath(__file__))
#if not os.path.exists(script_dir+'\data\input'):
#    os.makedirs(script_dir+'\data\input')
