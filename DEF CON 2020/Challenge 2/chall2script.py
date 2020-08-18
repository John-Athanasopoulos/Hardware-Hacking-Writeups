import csv;

c = ''
eeproms = []
with open('untitled.csv') as csvfile:    #Adds all the lines of the .csv file to c
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    i = 0
    for row in spamreader:
        if len(str(i)) == 1:
            c += '00'
        elif len(str(i)) == 2:
            c += '0'
        c += str(i)+' '
        c += ', '.join(row)
        c += '\n'
        i += 1

for line in c.splitlines():
    d = int(line[0]+line[1]+line[2]) #d is the number of the line. For every 3 lines collect the data of the first one, it's the address of an eeprom
    if d % 3 == 1:
        eep = line[45]+line[46]+line[47]+line[48]
        if eep not in eeproms:
            eeproms.append(eep) #append the eeprom's address to an array

lines = c.splitlines()
eepromsData = []

for eep in eeproms: #for every eeprom
    u = [] 
    tempList = []
    for line in range(0,len(lines)): #for every line
        d = int(lines[line][0]+lines[line][1]+lines[line][2]) #d is the number of the line
        if d % 3 == 1: 
            e = lines[line][45]+lines[line][46]+lines[line][47]+lines[line][48] #e is the current eeprom
            if e == eep: #if the current eeprom is the one we check at the moment
                p = (lines[line+1])[26]+(lines[line+1])[27]+(lines[line+1])[28]+(lines[line+1])[29] #p is the hex value of the next line (Internal Address)
                t = (lines[line+2])[26]+(lines[line+2])[27]+(lines[line+2])[28]+(lines[line+2])[29] #t is the hex value of the second line following (Data)
                tempList.append([int(p,16),int(t,16)]) #tempList contains arrays with first index a internal address and second the corresponding data of an eeprom
    tempList.sort(key=lambda x: x[0]) #sort the tempList based on the internal address. Thus, the data will be in the correct order
    for inArr in tempList:
        inArr[1] = chr(inArr[1]) #convert the data from hex to ascii
        u.append(inArr[1]) #and add them to u
    print "--------------------------------------------------------------"
    print "Eeprom with the address "+ eep + " received the following message:\n" + "".join(u)

print "--------------------------------------------------------------"