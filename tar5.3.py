
def read_f(f):
    while True:
     yield f.readline()


f = open("logo.jpg", 'rb')

sum=0
sodi=""
readd=read_f(f)

for i in readd:
    count = 0
    r= list(range(-(len(i)-3),1))
    for u in r:
        r[count]*=-1
        count+=1

    count=0
    for j in r:
        if hex(i[j]) == hex(33):
            sodi+= chr(i[j])
            for k in range(count+1,len(r)):
                if hex(i[r[k]]) <= hex(122) and hex(i[r[k]]) >= hex(97):
                    sum += 1
                    sodi += chr(i[r[k]])
                else:
                    break
            if sum >= 5:
                str = ''
                for letter in sodi:
                    str = letter + str
                print("kod",(str))
                sodi =""
                j += sum
                sum=0
            else:
                sum=0
        count+=1
        sodi = ""
        k=0

