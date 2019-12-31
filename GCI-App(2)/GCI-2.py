num = int(input("Enter magnitude: "))
source = input("Enter source unit: ")
target = input("Enter target unit: ")
d = {'milimeter':[1,'len'],
    'centimeter':[10,'len'],
    'meter':[1000,'len'],
    'kilometer':[1000000,'len'],
    'inch':[25.4,'len'],
    'feet':[304.8,'len'],
    'yard':[914.4,'len'],
    'mile':[1609344,'len'],
    'second':[1,'time'],
    "minute":[60,'time'],
    "hour":[60*60,'time'],
    "day":[24*60*60,'time'],
    "week":[7*24*60*60,'time'],
    "year":[365*24*60*60,'time'],
    'cm/s':[1,"speed"],
    'cm/min':[60,"speed"],
    'cm/hr': [60*60,"speed"],
    'm/s':[1/100,"speed"],
    'm/min':[60/100,"speed"],
    'm/hr': [60*60/100,"speed"],
    'km/s':[1/100000,"speed"],
    'km/min':[60/100000,"speed"],
    'km/hr': [60*60/100000,"speed"]
     }
if source in d.keys():
    if target in d.keys():
        if d[source][1] == d[target][1]:
            if d[source][1] == 'speed':
                print((num)*(d[target][0]/d[source][0]),target)
            else:
                print((num)*(d[source][0]/d[target][0]),target)
        else:
            print("ENTER COMPARABLE PARAMETERS...")
    else:
        print("INVALID INPUT")
else:
    print("INVALID INPUT")
