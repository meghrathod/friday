import numpy as np

def get_bonus_score(allTime,maxM):
    firstQ=np.percentile(allTime,25)
    secQ=np.percentile(allTime,50)
    thirQ=np.percentile(allTime,75)

    bScore=[]
    for stu in allTime:
        if stu == 0:
            bScore.append(0)
        elif stu >= thirQ:
            bScore.append(0.25*maxM)
        elif stu >= secQ:
            bScore.append(0.5*maxM)
        elif stu >= firstQ:
            bScore.append(0.75*maxM)
        else:
            bScore.append(maxM)
    return bScore
