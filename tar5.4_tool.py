
def find_min(*interleave):
    min =interleave[0]
    min_len=len(interleave[0])
    for item in interleave:
        if min_len>len(item):
            min=item
    return min

def interleave(*interleave):
    count=0
    intr = []
    for i in  interleave:
        intr += [i]
    while intr:
        this_item = find_min(*intr)
        for i in range(len(this_item)-count):
            l=[]
            for item in intr:
                l+= [item[count]]

            yield l
            count += 1
        temp=intr
        intr=[]
        for it in temp:
            if not len(it) == len(this_item):
                intr +=[it]



func = interleave('abc', [1, 2, 3], ('!', '@', '#'))
func1 = interleave('abc', [1, 2], ('!', '@', '#'))

all=[]
for i in func:
    all+=i
    print(all)


for i in func1:
    all+=i
    print(all)



