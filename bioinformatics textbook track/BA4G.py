# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 16:06:29 2018

@author: palan
"""

def AAtoWeight(pep):
    AAs = {'G': 57, 'A': 71, 'S':87, 'P':97, 'V':99, 'T':101, 'C':103, 'I':113, 'N':114, 'D':115, 'K':128, 'E':129, 'M':131, 'H':137, 'F':147, 'R':156, 'Y':163, 'W':186}
    weight = 0
    for p in pep:
        weight += AAs[p]
    return weight
   

def expand(leaders):
    AAs = ['G', 'A', 'S' ,   'P',     'V',     'T',     'C',     'I',     'N',     'D' ,    'K',     'E',     'M' ,    'H',     'F',     'R',     'Y',     'W']
    newLead = []
    for l in leaders:
        for aa in AAs:
            newLead.append(l + aa) 
    
    return newLead

def spectrumInt(spectrum):
    spectrum = spectrum.split()
    intSpec = []
    
    for s in spectrum:
        intSpec.append(int(s))
    
    return intSpec


def removeBad(leaderboard, removeList):
    
    for r in removeList:
        if r in leaderboard:
            leaderboard.remove(r)
    
    return leaderboard

def cycloSubPep(pep):
    fragments = []
    fragments.append("")
    #print pep
    size = 1
    while size < len(pep):
        x = 0
        while x < len(pep):
            y = (x + size) % len(pep)
            
            if x < y:
                fragments.append(pep[x:y])
            else:
                fragments.append(pep[x:] + pep[:y])
            
            x += 1
        size += 1
    
    fragments.append(pep)
    
    #print fragments
    return fragments


def theoSpec(pep):
    tSpec = []
    allFragments = []
    allFragments = cycloSubPep(pep)
    
    for aF in allFragments:
        tSpec.append(AAtoWeight(aF))
        
    return tSpec

def score(pep, spec):
    value = 0
    testSpec = list(spec)
    
    tpep = theoSpec(pep)
    #print tpep
    for x in tpep:
        if x in testSpec:
            value += 1
            testSpec.remove(x)
            
    
    return value

def keepHigh(sca, k):
    highScores = []
    sortedHS = sorted(sca.items(), key=lambda x:x[1], reverse=True)
    #print sortedHS
    #print len(sortedHS)
    #print k
    x = 0
    while (x < k and x < len(sortedHS) ):
        #print x, sortedHS[x][0], sortedHS[x][1]
        highScores.append(sortedHS[x][0])
        x += 1
        
    if k < len(sortedHS):
        tieScore = sortedHS[k-1][1]
        #print tieScore
        
        y = k
        while y < len(sortedHS) and tieScore == sortedHS[y][1]:
            #print y, sortedHS[y][0], sortedHS[y][1]
            highScores.append(sortedHS[y][0])
            y += 1
        
    
    
  
    return highScores
    

def cut(leaderboard, spectrum, k):
    leaderDic = {}
    for pep in leaderboard:
        sc = 0
        sc = score(pep, spectrum)
        #print pep, sc
        leaderDic[pep] = sc
    
    #print leaderDic
    highScores = keepHigh(leaderDic, k)
    #print highScores
    
    return highScores

def massPrint(pep):
    s = ""
    for m in pep:
        s += str(AAtoWeight(m)) + "-"
    return s

def getFile():
    from os.path import expanduser
    
    fileName = "rosalind_ba4g.txt"
    path = fileName 
    #print path
    fileToOpen = open(path , 'r')
    return fileToOpen

#
#N = 10
#s = '0 71 113 129 147 200 218 260 313 331 347 389 460'
    

if __name__ == '__main__':
    f = getFile()
#     f.readline()
    k = int(f.readline().rstrip())
    spectrum = f.readline().rstrip()
    f.close()
    spectrum = spectrumInt(spectrum)
    
    print k
    print spectrum
    parentMass = spectrum[-1]
    print parentMass
    
    
    leaderboard = [""]
    leaderPeptide = ""
    
    
    x = 0
    done = False
    while not done and len(leaderboard) != 0:
         leaderboard = expand(leaderboard)
         removeList = []
         for p in leaderboard:
                if AAtoWeight(p) == parentMass:
                    if score(p, spectrum) > score(leaderPeptide, spectrum):
                        leaderPeptide = p
                
                if AAtoWeight(p) > parentMass:
                    removeList.append(p)
         
         
         leaderboard = cut( leaderboard, spectrum, k )
         leaderboard = removeBad(leaderboard, removeList)
#         print leaderboard
#         print len(leaderboard)
#         print ""
#         
         
         
    print massPrint(leaderPeptide)[:-1]