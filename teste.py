
#How open and close files in python

#Example

#with open (r"C:\Users\exmarcsd\Documents\Python\My Code\file.txt") as newfile:
 #   for line in newfile:
  #      line = line.strip()
 #       print(line)
 #   print("Goodbye")
#print(" The file is closed now")


import psutil as ps

print('Lista de processos em execução:')
for proc in ps.process_iter():
    info = proc.as_dict(attrs=['pid', 'name'])
    #processos = [proc.name() for proc in ps.process_iter()]
    print('Processo: {} (PID: {})'.format(info['pid'], info['name']))
    