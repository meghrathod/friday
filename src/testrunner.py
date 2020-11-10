import subprocess
import json

def runTest(testCasePath,filesPath,filename):

    p1=subprocess.Popen(['gcc',filesPath+filename,'-o',filesPath+'a.out'])
    p1.communicate()

    with open(testCasePath, "r") as jfile:
        data = json.load(jfile)
    testResult = []
    for indata in data["test_cases"]:
        process = subprocess.Popen([filesPath+'a.out'], stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE, encoding='utf8')
        process.stdin.write(indata["test_case"])

        testResult.append(1 if process.communicate()[0] == indata["output"] else 0)
    return testResult
