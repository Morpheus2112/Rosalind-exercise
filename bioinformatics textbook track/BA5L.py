# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 15:10:28 2018

@author: palan
"""

import numpy as np
blosum62 = {'A': {'A': 4, 'C': 0, 'E': -1, 'D': -2, 'G': 0, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 0, 'W': -3, 'V': 0, 'Y': -2}, 'C': {'A': 0, 'C': 9, 'E': -4, 'D': -3, 'G': -3, 'F': -2, 'I': -1, 'H': -3, 'K': -3, 'M': -1, 'L': -1, 'N': -3, 'Q': -3, 'P': -3, 'S': -1, 'R': -3, 'T': -1, 'W': -2, 'V': -1, 'Y': -2}, 'E': {'A': -1, 'C': -4, 'E': 5, 'D': 2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': -2, 'L': -3, 'N': 0, 'Q': 2, 'P': -1, 'S': 0, 'R': 0, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 'D': {'A': -2, 'C': -3, 'E': 2, 'D': 6, 'G': -1, 'F': -3, 'I': -3, 'H': -1, 'K': -1, 'M': -3, 'L': -4, 'N': 1, 'Q': 0, 'P': -1, 'S': 0, 'R': -2, 'T': -1, 'W': -4, 'V': -3, 'Y': -3}, 'G': {'A': 0, 'C': -3, 'E': -2, 'D': -1, 'G': 6, 'F': -3, 'I': -4, 'H': -2, 'K': -2, 'M': -3, 'L': -4, 'N': 0, 'Q': -2, 'P': -2, 'S': 0, 'R': -2, 'T': -2, 'W': -2, 'V': -3, 'Y': -3}, 'F': {'A': -2, 'C': -2, 'E': -3, 'D': -3, 'G': -3, 'F': 6, 'I': 0, 'H': -1, 'K': -3, 'M': 0, 'L': 0, 'N': -3, 'Q': -3, 'P': -4, 'S': -2, 'R': -3, 'T': -2, 'W': 1, 'V': -1, 'Y': 3}, 'I': {'A': -1, 'C': -1, 'E': -3, 'D': -3, 'G': -4, 'F': 0, 'I': 4, 'H': -3, 'K': -3, 'M': 1, 'L': 2, 'N': -3, 'Q': -3, 'P': -3, 'S': -2, 'R': -3, 'T': -1, 'W': -3, 'V': 3, 'Y': -1}, 'H': {'A': -2, 'C': -3, 'E': 0, 'D': -1, 'G': -2, 'F': -1, 'I': -3, 'H': 8, 'K': -1, 'M': -2, 'L': -3, 'N': 1, 'Q': 0, 'P': -2, 'S': -1, 'R': 0, 'T': -2, 'W': -2, 'V': -3, 'Y': 2}, 'K': {'A': -1, 'C': -3, 'E': 1, 'D': -1, 'G': -2, 'F': -3, 'I': -3, 'H': -1, 'K': 5, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -1, 'S': 0, 'R': 2, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 'M': {'A': -1, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': 0, 'I': 1, 'H': -2, 'K': -1, 'M': 5, 'L': 2, 'N': -2, 'Q': 0, 'P': -2, 'S': -1, 'R': -1, 'T': -1, 'W': -1, 'V': 1, 'Y': -1}, 'L': {'A': -1, 'C': -1, 'E': -3, 'D': -4, 'G': -4, 'F': 0, 'I': 2, 'H': -3, 'K': -2, 'M': 2, 'L': 4, 'N': -3, 'Q': -2, 'P': -3, 'S': -2, 'R': -2, 'T': -1, 'W': -2, 'V': 1, 'Y': -1}, 'N': {'A': -2, 'C': -3, 'E': 0, 'D': 1, 'G': 0, 'F': -3, 'I': -3, 'H': 1, 'K': 0, 'M': -2, 'L': -3, 'N': 6, 'Q': 0, 'P': -2, 'S': 1, 'R': 0, 'T': 0, 'W': -4, 'V': -3, 'Y': -2}, 'Q': {'A': -1, 'C': -3, 'E': 2, 'D': 0, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': 0, 'L': -2, 'N': 0, 'Q': 5, 'P': -1, 'S': 0, 'R': 1, 'T': -1, 'W': -2, 'V': -2, 'Y': -1}, 'P': {'A': -1, 'C': -3, 'E': -1, 'D': -1, 'G': -2, 'F': -4, 'I': -3, 'H': -2, 'K': -1, 'M': -2, 'L': -3, 'N': -2, 'Q': -1, 'P': 7, 'S': -1, 'R': -2, 'T': -1, 'W': -4, 'V': -2, 'Y': -3}, 'S': {'A': 1, 'C': -1, 'E': 0, 'D': 0, 'G': 0, 'F': -2, 'I': -2, 'H': -1, 'K': 0, 'M': -1, 'L': -2, 'N': 1, 'Q': 0, 'P': -1, 'S': 4, 'R': -1, 'T': 1, 'W': -3, 'V': -2, 'Y': -2}, 'R': {'A': -1, 'C': -3, 'E': 0, 'D': -2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 2, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -2, 'S': -1, 'R': 5, 'T': -1, 'W': -3, 'V': -3, 'Y': -2}, 'T': {'A': 0, 'C': -1, 'E': -1, 'D': -1, 'G': -2, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': 0, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 5, 'W': -2, 'V': 0, 'Y': -2}, 'W': {'A': -3, 'C': -2, 'E': -3, 'D': -4, 'G': -2, 'F': 1, 'I': -3, 'H': -2, 'K': -3, 'M': -1, 'L': -2, 'N': -4, 'Q': -2, 'P': -4, 'S': -3, 'R': -3, 'T': -2, 'W': 11, 'V': -3, 'Y': 2}, 'V': {'A': 0, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': -1, 'I': 3, 'H': -3, 'K': -2, 'M': 1, 'L': 1, 'N': -3, 'Q': -2, 'P': -2, 'S': -2, 'R': -3, 'T': 0, 'W': -3, 'V': 4, 'Y': -1}, 'Y': {'A': -2, 'C': -2, 'E': -2, 'D': -3, 'G': -3, 'F': 3, 'I': -1, 'H': 2, 'K': -2, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -3, 'S': -2, 'R': -2, 'T': -2, 'W': 2, 'V': -1, 'Y': 7}}


def last_column_score(a, b, indel = 5, scoring = blosum62):
    '''
    CODE CHALLENGE: 
    compute the last column score of a,b global alignement
    '''
    n = len(a)
    m = len(b)
    
    s = np.zeros(shape = (n+1,2), dtype = np.float)
        
    for i in range(n+1):
        s[i, 0] = -indel * i        

    if (m==0):
        # handling special one-column-only case
        return s[:, 0]
    
    for j in range(m):
        s[0, 1] = s[0,0] - indel
        for i in range(n):
            score = scoring[ a[i] ][ b[j] ]
            s[i+1, 1] = max(s[i, 1] - indel, s[i+1, 0] - indel, s[i, 0] + score)
        s[:, 0] = s[:, 1]
    return s[:, 1]

def middle_edge(v, w, indel = 5, scoring = blosum62, c = None):
    n = len(v)
    m = len(w)
        
    # compute middle node column
    if (c is None):
        c = (m-1)/2
        
    wleft = w[:c]
    wmid = w[c]
    wright = w[c+1:]
        
    # compute score of graph left-part
    len1 = last_column_score(v,wleft, indel = indel, scoring = scoring)
    # compute score of graph right-part
    len2 = last_column_score(v[::-1],wright[::-1], indel = indel, scoring = scoring)[::-1]

#    print '-------'
#    print 'v',v,'w',w
#    print ',',wleft,',',wmid,',',wright,','
#    print 'len1',len1
#    print 'len2',len2

    # compute horizontal max score for any i-row [0,n] at column c 
    hs = [ (len1[i] + len2[i] - indel ) for i in range(n+1)]
    # compute diagonal max score for any i-row [0,n-1] at column c 
    ds = [ (len1[i] + len2[i+1] + scoring[ v[i] ][ wmid ]) for i in range(n)]    
    hmax = max(hs)
    dmax = max(ds)
    if (hmax > dmax):
        # horizontal edge
        i = hs.index(hmax)
        j = c
        k = i
        l = c+1
    else:
        # diagonal edge
        i = ds.index(dmax)
        j = c
        k = i+1
        l = c+1
    return ((i,j),(k,l))
    
assert middle_edge('PLEASANTLY','MEASNLY') == ((4, 3), (5, 4))

#v = 'TWLNSACYGVNFRRLNPMNKTKWDCWTWVPMVMAAQYLCRIFIPVMDHWEFFGDWGLETWRLGIHDHVKIPNFRWSCELHIREHGHHFKTRFLKHNQFTQCYGLMPDPQFHRSYDVACQWEVTMSQGLMRFHRQNQIEKQRDRTSTYCMMTIGPGFTSNGYDPFVTITITPVQEPVENWFTPGGSMGFMIISRYMQMFFYLTRFSDMTYLVGVHCENYVCWNNVAKFLNGNLQGIFDQGERAYHQFVTWHSYSQYSRCSVGRYACEQAMSRVNSKMTWHWPIRDQGHEHFSEQYLSEKRNPPCNPRIGNAGQHFYEIHRIAHRVAMCNWAPQGQHPGGPTPHDVETCLWLWSLCLKGSDRGYVDRPWMFLADQLGEANLTLITMFHGCTRGCLMWFMDWEECVCSYSVVNPRCHGSEQWSVQNLGWRTCDTLISLWEPECDKHNTPPCLHWEFEDHPSQLRPVMMCDKYVQSIPTDAKWAWTYSKDFVISHWLIWTPIKLEECVFPQINRLWGTACNQGSQKIVIQNVWLRPSSFFQERSKCSDSSCILNVGGSNVNITGKETRTHVPILHMHEIDLISTASSGMRHNLILPHGMLMLHMNWHHSTRAMNPYSSLKLIPWTFQVCETDDRDQNVATHVADPCHKGEDQEIRCCKGGVDHQWKGDRMWMMCMPDMNYVKQDQAPSGTCEGACENYPADKDKCYMIFTIVFDYRRCTKKVCIWISGFPVDAFNLISIANAGFFCCWLEPTELKWRRTFYLGKGTQGWMCTFPHRNIIPVIICAGFGRWVQGEVPFRPVAQISAHSSDRRQGHHPPGTNMCHDYGDQYPIKRVGMQVEEDDGASYCDCAADWKLADMYEADHLSIGVIDFTDWIYPKNGGIWSEIIKSHFHWYHWETPQNTVGAFNTIVGINGSDMCIYHGNTQWEFGWCWKWLNHGHMRNQGPCHLGILEGRISKFAQVTSWWWQTKHDKDWSIEPYGRHWGEAGRPYTYNYCWMRWAIVYNHGNVISVELVPFMDEYPGKCNKEDVQFELFSPMQA'
#w = 'LWFKFLQCIFQYFKDQQETNCIWTFSPFSEHICQRVCQVYWNWNTPSSRTSDPRELFANSTIHNNRCGEWRYMFYHTRTLVQTAPLMKETLHSDGKHSMYCEQRHFFRSSYLIKVNYDVSHYLELYTFSEIPWKLTTHGWDGFSWFLLVNSCCTFDIDGKCGILSQCGMSRAFRTRQEDAYHFQTSLMHLHLHLHVQEGKHEKADLFAQFYNMLPMHGGTCGRNTEPSDLFDSATMNKYMAEHPASCKACPNVSKECFVYWWSHDFTKKHKLIEFSCGRDTGQTTQRTWNVDENEGGKWIWRFHYFMRAKALQIDPKFKPYWNEPRAIMRPGHVTAAPCICAQHSQNETAVCNRDQMHIHAIEFQQYHSRAFGEVQTWCDIGKENENDFIYEQHWWLVGGTEGMAGVIWKFVCARCRTQDCDFWKTCLTYSAQPMMKVYDTIFYVNSINPWEFEDHPSQCDKCVQSIPTDAKYAICGKFVISHWLYWTPQKFEECVHNNVRCAPMGNRLWGTACMVIQNVWLRPSMGSHFSCILNVGGSNINIQGKETWTHVPILHMHEIDLISTASSGMETCKPCFLSGPTIHMGFSYEIRAQPYSRDYFCMDWMQEADEVDHNRCETVQPTLPLLQQFEWKTSCMGQRWITIFCDHCQIVCFSTFFCVMPTFLPNTSILDKFYCIYLSISWTHYCNVHALGFIMRLHYSYMGWKEHKRMHAWDIGLDELWAQEGIQRAQLWCGDEFEVAKYPEWITEARTAIATRPWFHNCYIKPWWIREKHLWFGKESKLDHGHRGAMFTPVANDNTEWMHHWYMFCWAGSKNRLKRQIKEKLIFIIKFMITEFGLFLMIDYTQCYIAWMWAYTGIACYIDWEKCLKHDLTTTDLGCCVYRLFKWYEVRHRAPPQVNTRLPWSQIPMVAIQCNIVDECKEQWHFSYKASFVVEYLCPGCCTNGNRWQWYQVKETPFMYAFAASIFGFHHENLVVFITGSVTIPNGLFGCIAWTSPKPVQKTPASANTIIAYDKCILMG'
#print middle_edge(v,w)


def linear_space_backtracking(v, w, ioffset = 0, joffset = 0, indel=5, scoring=blosum62):
    n = len(v)
    m = len(w)
    if n==0 and m==0:
        # no string to compare, thus no edge
        return []
    elif n==0:
        # return horizontal edges for a w gap
#        return [((ioffset,joffset+j),(ioffset,joffset+j+1)) for j in range(m)]
        return ['-']*m
    elif m==0:
        # return vertical edges for a v gap
#        return [((ioffset+i,joffset),(ioffset+i+1,joffset)) for i in range(n)]
        return ['|']*n
        
    ((i,j),(k,l)) = middle_edge(v,w,indel=indel,scoring=scoring)

    if (i==k):
        edge = '-'
    else:
        edge = '/'

    wleft = w[:j]
    wright = w[l:]
    vtop = v[:i]
    vbottom = v[k:] 
    
    # back tracking the graph bottom-right part
    bottom_right_track = linear_space_backtracking(vbottom, wright, ioffset = k+ioffset,joffset = l+joffset, indel=indel, scoring=scoring)
    # back tracking the graph upper-left part
    upper_left_track = linear_space_backtracking(vtop, wleft, ioffset = ioffset,joffset = joffset, indel=indel, scoring=scoring)
    
    return upper_left_track + [edge] + bottom_right_track
    
def backtrack_translation(v,w,bt, indel = 5, scoring = blosum62):
    i = 0
    j = 0
    walign = []
    valign = []
    smax = 0
    for e in bt:
        if e == '|':
            walign.append('-')
            valign.append(v[i])
            smax -= indel
            i += 1            
        elif e == '-':
            walign.append(w[j])
            valign.append('-')
            smax -= indel
            j += 1
        else:
            valign.append(v[i])
            walign.append(w[j])
            smax += scoring[ v[i] ][ w[j] ]
            i += 1          
            j += 1 

#        wleft = w[:j]
#        wright = w[j:]
#        vtop = v[:i]
#        vbottom = v[i:]
#        left_len = last_column_score(vtop,wleft)[-1]
#        right_len = last_column_score(vbottom,wright)[-1]
#        print 'score(',vtop,',',wleft,')=',left_len
#        print 'score(',vbottom,',',wright,')=',right_len
#        print 'max(',i,',',j,')=',left_len+right_len
    return (smax,''.join(valign),''.join(walign))
  
def linear_space_alignement(v, w, indel = 5, scoring = blosum62):
    bt = linear_space_backtracking(v,w,scoring = scoring, indel = indel)
    return backtrack_translation(v,w,bt,scoring = scoring, indel = indel)
  
assert linear_space_alignement('PLEASANTLY','MEANLY',5,blosum62) == (8, 'PLEASANTLY', '-MEA--N-LY')

#v = 'PTGQSYVTTARTTAECRVLHVMPFNYHMASIMDSYVFLNFGPALCMHEWYLCTMRCGWSKVGLGYMTCFCKNYHMSVKDAAYDGDK'
#w = 'QVPFPTVDVIVCCTGIKCEPMNVGYDQQMKDCFICTREYDIRRLHTIVCGSEWACRLWIEADWEDCEKSFRDFDAPINIVQYAVWRANV'
#print longest_common_subsequence(v, w, indel = 5, scoring = blosum62, verbose = True)
#print linear_space_alignement(v, w, indel = 5, scoring = blosum62)

#v = 'PLEASANTLY'
#w = 'MEANLY'

fname = 'rosalind_ba5l.txt'
lines = list(l.strip() for l in open(fname))
v = lines[0].strip()
w = lines[1].strip()

(a,b,c) = linear_space_alignement(v,w)
print int(a)
print b
print c