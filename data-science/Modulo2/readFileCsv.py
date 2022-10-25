#import csv
 
#with open('planets.csv', newline='') as File:  
#    reader = csv.reader(File)
#    for row in reader:
#        print(row)

minRotacional = 100000000
maxOrbital = -1

planetaRotacional = ''
planetaOrbital = ''

file_hander = open('planets.csv', 'r')
next(file_hander)
for line in file_hander:
    separaPlaneta = line.split(",")

    if separaPlaneta[0] != 'NA' and separaPlaneta[1] != 'NA' and separaPlaneta[2] != 'NA':
        
        PeriodoRotacional = int(separaPlaneta[1])

        PeriodoOrbital = int(separaPlaneta[2])

        if PeriodoRotacional < minRotacional:
            minRotacional = PeriodoRotacional
            planetaRotacional = separaPlaneta[0] 
        
        if maxOrbital < PeriodoOrbital:
            maxOrbital = PeriodoOrbital
            planetaOrbital = separaPlaneta[0]

print("Menor Periodo Rotacional: ",planetaRotacional," - ", minRotacional)
print("Mayor Periodo Orbital: ",planetaOrbital," - ", maxOrbital)
    
file_hander.close()

