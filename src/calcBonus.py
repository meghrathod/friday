import numpy as np

def get_bonus_score(allTime,maxM):
    firstQ=np.percentile(allTime,25)
    secQ=np.percentile(allTime,50)
    thirQ=np.percentile(allTime,75)

    bScore=[]
    for stu in allTime:
        if stu >= thirQ:
            if stu==0:
                bScore.append(0)
            else:
                bScore.append(0.25*maxM)
        elif stu >= secQ:
            if stu==0:
                bScore.append(0)
            else:
                bScore.append(0.5*maxM)
        elif stu >= firstQ:
            if stu==0:
                bScore.append(0)
            else:
                bScore.append(0.75*maxM)
        else:
            if stu==0:
                bScore.append(0)
            else:
                bScore.append(maxM)
    return bScore
