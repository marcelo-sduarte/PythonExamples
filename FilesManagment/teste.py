
#How open and close files in python
sum=0
list= 0
lists = []
with open ("file.txt") as newfile:
    for line in newfile:
        line = line.strip()
        lists.append(line[0])

    for list in lists:
        print(f"{lists[list]}")

'''
import psutil as ps

print('Lista de processos em execução:')
for proc in ps.process_iter():
    info = proc.as_dict(attrs=['pid', 'name'])
    #processos = [proc.name() for proc in ps.process_iter()]
    print('Processo: {} (PID: {})'.format(info['pid'], info['name']))
'''    