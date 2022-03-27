import glob

"""
    param:A route for a specific folder
    return:List of all files in the same folder
"""
def collect_file(path):
    listt = glob.glob(path + "\deep*.*")
    return listt

def check_to_file(listt):
    if len(listt) == 2:
        for i in range(len(listt)):
            if not listt[i].split(".")[-1] in ['jpg', 'png']:
                return False
    else:
        return False
    return True

if __name__ == "__main__":
    path = input("Enter path of folder: ")
    listt = collect_file(path)
    if_two_file = check_to_file(listt)
    if if_two_file:
        print("The folder contains two files")
    else:

        print("The folder not contains two files")