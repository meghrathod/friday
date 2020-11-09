def takeio(filepath):
    with open(filepath, "r") as infile:
        args = infile.readlines()
    i=0
    temp=[]
    for ar in args:
        temp.append(ar.split(' '))
    return temp
