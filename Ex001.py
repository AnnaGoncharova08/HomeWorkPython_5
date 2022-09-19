# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# Входные и выходные данные первой и четвертой задач хранятся в отдельных текстовых файлах.

with open('File_Ex001.txt', 'r') as data:
    line = data.read()

def func(line):
    line = list(filter(lambda x: 'абв' not in x, line.split()))
    return ' '.join(line)

line = func(line)
with open('File.txt', 'a') as f:
    f.write(line)