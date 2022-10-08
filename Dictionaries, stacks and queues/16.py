text=input('Enter text: ')

alphabet = {"A":"Alpha","B":"Beta","C":"Charlie","D":"Delta","E":"Echo","F":"Foxstrot","G":"Golf","H":"Hotel","I":"India","J":"Juliett","K":"Kilo","L":"Lima","M":"Mike","N":"November","O":"Oscar","P":"Papa","Q":"Quebec","R":"Romeo","S":"Sierra","T":"Tango","U":"Uniform","V":"Victor","W":"Whiskey","X":"X-Ray","Y":"Yankee","Z":"Zulu",
            "a":"Alpha","b":"Beta","c":"Charlie","d":"Delta","e":"Echo","f":"Foxstrot","g":"Golf","h":"Hotel","i":"India","j":"Juliett","k":"Kilo","l":"Lima","m":"Mike","n":"November","o":"Oscar","p":"Papa","q":"Quebec","r":"Romeo","s":"Sierra","t":"Tango","u":"Uniform","v":"Victor","w":"Whiskey","x":"X-Ray","y":"Yankee","z":"Zulu"} 

for i in text:
    for v,k in alphabet.items():
        if i==v:
            print(k, end=" ")
        else:
            continue
