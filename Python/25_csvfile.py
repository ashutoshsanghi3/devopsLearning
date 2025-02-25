import csv 
with open('samplecsvfile.csv') as f:
    csv_reader=csv.reader(f,delimiter=',')
    linecount=0
    for i in csv_reader:
        print(f'{i}')
    print(type(i))
    print(type(csv_reader))