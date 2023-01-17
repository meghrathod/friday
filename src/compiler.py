import os
import subprocess


def compileFile(filePath,folderPath, cname, fileExtension):
    # print("Reaches Compiler!")
    outName = filePath[:len(filePath) - len(fileExtension)] + '.out'
    print(outName)
    fullExecPath = outName
    # print(fullExecPath)

    p1 = subprocess.Popen([cname, filePath, '-o', fullExecPath], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          encoding='utf8')
    # out =
    if p1.communicate()[1].find('error:') != -1:
        return -1, False
    return fullExecPath, True
