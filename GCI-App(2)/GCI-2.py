magnitude=int(input("Enter magnitude: "))
source=input("Enter source unit: ")
target=input("Enter target unit: ")
l=[]
l1=['mm','cm','m','km','second','minute','hour','day','week','year','cm/s','cm/min','cm/hr','m/s','m/min','m/hr','km/s','km/,min','km/hr']
value=[]
l.append(target)
d={
"mm":"1 mm",
"cm":"10 mm",
"m":"100 cm",
"km":"1000 m",
"second":"1 second",
"minute":"60 second",
"hour":"60 minute",
"day":"24 hour",
"week":"7 day",
"year":"52 week",
"cm/s":"1 cm/s",
"cm/min":"0.016666666666666666 cm/s",
"cm/hr":"0.016666666666666666 cm/min",
"m/s":"360000 cm/hr",
"m/min":"0.016666666666666666 m/s",
"m/hr":"0.016666666666666666 m/min",
"km/s":"3600000 m/hr",
"km/min":"0.016666666666666666 km/s",
"km/hr":"0.016666666666666666 km/min"
}
a=""
if 0<=l1.index(source)<=3 and 0<=l1.index(target)<=3 or 4<=l1.index(source)<=9 and 4<=l1.index(target)<=9 or 10<=l1.index(source)<=18 and 10<=l1.index(target)<=18:
    if l1.index(source)<l1.index(target):
        while target!=source:
            for i in d.keys():
                if str(i)==target:
                    target = d[target]
                    a=target.split(" ")
                    target=a[-1]
                    l.append(a[-1])
                    value.append(float(a[0]))
        pro=1
        for i in value:
            pro*=i
        print(magnitude/pro,target)
    elif l1.index(source)==l1.index(target):
        print(magnitude,target)
    else:
        while target!=source:
            for i in d.keys():
                if str(i)==source:
                    source = d[source]
                    a=source.split(" ")
                    source=a[-1]
                    l.append(a[-1])
                    value.append(float(a[0]))
        pro=1
        for i in value:
            pro*=i
        print(magnitude*pro,target)
else:
    print("INVALID INPUT")
