import glob


def func(path):
    listt = glob.glob(path + "\deep*.*")
    return listt


path = input("Enter path of folder: ")
listt = func(path)
flag = True
if len(listt) == 2:
    for i in range(len(listt)):
        if not listt[i].split(".")[-1] in ['jpg', 'png']:
            flag = False
else:
    flag = False
if flag:
    print("The folder contain two file")
else:

    print("The folder not contain two file")

