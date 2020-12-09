import sys


#Main
address = sys.argv[1]
output = address.strip().replace('\n', ' ')

#remove name of file from output string
output = output.replace('main.py', '')

print(output)
