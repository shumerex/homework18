from pprint import pprint

file_name = 'stihi.txt'
file = open(file_name, mode='rb')
file_content = file.read()
file.close()
pprint(file_content)