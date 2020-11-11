import csv
import json

def get_stu_name(filename):
    return filename.split('_')[-1][:-2]

def addMarks(fileNames,outPath,testPassList,testCasePath,bScore):

    with open(testCasePath,"r") as jfile:
        data=json.load(jfile)

    allMarks=[]
    j=0
    for student in testPassList:
        i=0
        totalMarks=0
        for inData in data["test_cases"]:
            totalMarks = totalMarks +(testPassList[j][i]*inData["marks"])
            i+=1
        if bScore:
            allMarks.append(totalMarks+bScore[j])
        else:
            allMarks.append(totalMarks)
        j+=1

    with open(outPath,'w') as file:
        writer=csv.writer(file)

        for k in range(len(fileNames)):
            writer.writerow([get_stu_name(fileNames[k]),allMarks[k]])
    return 0