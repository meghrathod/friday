import os
import subprocess
import json

def runTest(testCasePath,filesPath,filename):

    with open(testCasePath, "r") as jfile:
        data = json.load(jfile)
    testResult = []

    fullFilePath = os.path.join(filesPath, filename)
    fullExecPath = os.path.join(filesPath, 'a.out')

    p1 = subprocess.Popen(['gcc', fullFilePath, '-o', fullExecPath], stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding='utf8')
    if p1.communicate()[1].find('error:') != -1:
        for cases in data["test_cases"]:
            testResult.append(0)
        return testResult

    #print(p1.communicate()[1])
    p1.communicate()

    for indata in data["test_cases"]:
        process = subprocess.Popen([fullExecPath], stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,stderr=subprocess.PIPE, encoding='utf8')
        process.stdin.write(indata["test_case"])
        if(process.communicate()[1]):
            testResult.append(0)
        else:
            testResult.append(1 if process.communicate()[0] == indata["output"] else 0)
    return testResult
