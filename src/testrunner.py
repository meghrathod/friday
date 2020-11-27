import os
import subprocess
import json
import time

def changeFormatting(str,compType):
    if compType=='abs':
        return str
    elif compType=='part':
        return str.strip()
    elif compType=='rAll':
        return "".join(str.split())

def runTest(testCasePath,filesPath,filename,timeOut,cname,compType):

    with open(testCasePath, "r") as jfile:
        data = json.load(jfile)
    testResult = []

    fullFilePath = os.path.join(filesPath, filename)
    fullExecPath = os.path.join(filesPath, 'a.out')

    p1 = subprocess.Popen([cname, fullFilePath, '-o', fullExecPath], stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding='utf8')
    if p1.communicate()[1].find('error:') != -1:
        for cases in data["test_cases"]:
            testResult.append(0)
        return testResult,0
    p1.communicate()
    start=time.time()
    #print(start)
    checkTimout=1
    for indata in data["test_cases"]:
        process = subprocess.Popen([fullExecPath], stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,stderr=subprocess.PIPE, encoding='utf8')
        process.stdin.write(indata["test_case"])
        try:
            if(process.communicate(timeout=timeOut)[1]):
                testResult.append(0)
            else:
                if changeFormatting(process.communicate(timeout=timeOut)[0], compType) == changeFormatting(
                        indata["output"], compType):
                    testResult.append(1)
                else:
                    testResult.append(0)
        except subprocess.TimeoutExpired:
            process.kill()
            testResult.append(0)

    end=time.time()

    return testResult, (end-start)*checkTimout
