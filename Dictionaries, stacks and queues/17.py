alphabet = {"A":"Alpha","B":"Beta","C":"Charlie","D":"Delta","E":"Echo","F":"Foxstrot","G":"Golf","H":"Hotel","I":"India","J":"Juliett","K":"Kilo","L":"Lima","M":"Mike","N":"November","O":"Oscar","P":"Papa","Q":"Quebec","R":"Romeo","S":"Sierra","T":"Tango","U":"Uniform","V":"Victor","W":"Whiskey","X":"X-Ray","Y":"Yankee","Z":"Zulu"}

file= open("ICAO.txt",'w')
for k,v in alphabet.items():
    file.write(k+" ")
    file.write(v)
    file.write('\n')
file.close()

file=open('ICAO.txt','r')
print(file.read())
