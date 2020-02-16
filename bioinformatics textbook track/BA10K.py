# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 13:18:10 2018

@author: Memphis
"""

import numpy as np

def parse_emission_symbols_states_transition_matrix_emission_matrix(lines):
    emission = lines[0]
    symbols = lines[2].split('\t')
    states = lines[4].split('\t')
    transition_matrix = np.zeros((len(states),len(states)), dtype = np.longfloat)
    for i in range(len(states)):
        transition_matrix[i,:] = map(np.longfloat,lines[i+7].split('\t')[1:len(states)+1])
    emission_matrix = np.zeros((len(states),len(symbols)), dtype = np.longfloat)
    for i in range(len(states)):
        emission_matrix[i,:] = map(np.longfloat,lines[i+9+len(states)].split('\t')[1:len(symbols)+1])
    return emission,symbols,states,transition_matrix,emission_matrix

def print_hmm_profile(transition,emission,alphabet,state_name):
    __emission = np.round(emission,3)
    __transition = np.round(transition,3)
    ret = ''
    #ret += '\t' + '\t'.join(state_name) + '\n'
    ret += '\t' + '\t'.join(state_name) + '\n'
    for i,s in enumerate(state_name) :
         l = s + '\t'
         l += '\t'.join([format("%.3g" % __transition[i,j]) if __transition[i,j] != 1 else '1.0' for j in range(len(state_name))])
         ret += l+ '\n'
    ret += '--------\n'
    ret += '\t' + '\t'.join(alphabet)
    for i,s in enumerate(state_name) :
         l = '\n'+ s + '\t'
         l += '\t'.join([format("%.3g" % __emission[i,j]) if __emission[i,j] != 1 else '1.0' for j in range(len(alphabet))])
         ret += l
    return ret

def hmm_EM_learning(it,x,symbols,states,transition,emission):
    """
    Output: Emission and transition matrices resulting from applying Viterbi learning for j iterations.
    """
    dsymbols = {s: i for (i,s) in enumerate(symbols)}
    dstates = {s: i for (i,s) in enumerate(states)}
    for j in range(it):
#        path = hmm_soft_decoding(x,dsymbols,dstates,transition,emission)
        test = EM_learning(x,symbols,states,transition,emission)
        test.soft_decoding()
        pi2 = test.condit_prob
        pi3 = test.res_prob
        
        (transition,emission) = hmm_parameter_estimation(x,symbols,pi2,pi3,states)
        print print_hmm_profile(transition,emission,symbols,states)
        print '**************************************'
    print 
    return transition,emission


def hmm_parameter_estimation(x,symbols,pi2,pi3,states):

    transition_matrix = np.zeros((len(states),len(states)), dtype = np.longfloat)
    emission_matrix = np.zeros((len(states),len(symbols)), dtype = np.longfloat)
    for i in range(len(x)):
        for j in range(len(states)):
            for k in range(len(symbols)):
    #            print pi2[i][j]
                if x[i] == symbols[k]:
                    emission_matrix[j][k] += pi2[i][j]
    
    for i in range(len(x)-1):
        for j in range(len(states)):
            for k in range(len(states)):
                transition_matrix[j][k] += pi3[i][j][k]
                
    def norm(a):
        b = a[:]
        for i in range(len(a)):
            s = sum(a[i])
            for j in range(len(a[i])):
                b[i][j] = a[i][j]/s
                
        return b
    tnew = norm(transition_matrix)
    enew = norm(emission_matrix)
    return tnew,enew    


import math
import re
class EM_learning:
    """
        Input: A string x, followed by the alphabet from which x was constructed,
        followed by the states States, transition matrix Transition, and emission matrix
        Emission of an HMM (alphabet, States, Transition, Emission).
        Output: An |x| x |States| matrix whose (i, k)-th element holds the conditional probability.
        """
    def __init__(self,x,symbols,states,t,e):
        self.string = x
        self.alphabet  = symbols
        self.state = states
        self.transit_matrix = t
        self.emission_matrix = e
        self.alphabet_index = {} #index {'x'->0,'y'->1,..}
        for i, alphabet in enumerate(self.alphabet):
            self.alphabet_index[alphabet] = i

        self.sink = 0
        self.forward = [ [1.0 for x in range(len(self.state))] for x in range(len(self.string))]
        self.backward = [ [1.0 for x in range(len(self.state))] for x in range(len(self.string))]
        self.condit_prob = [ [1.0 for x in range(len(self.state))] for x in range(len(self.string))]
        self.res_prob  =[ [[1.0 for x in range(len(self.state))] for x in range(len(self.state))] for x in range(len(self.string)-1)]

    def soft_decoding(self):
        """
            return the conditional probability that the HMM was in state k
            at time i given that it emitted string x.
            """
        self.forward_prob()
        self.backward_prob()
        for i in range(len(self.string)):
            for j in range(len(self.state)):
                self.condit_prob[i][j] = self.forward[i][j]*self.backward[i][j]/self.sink

        for i in range(len(self.string)-1):
            for k in range(len(self.state)):
                for l in range(len(self.state)):
                    weight  = self.emission_matrix[l][self.alphabet_index[self.string[i+1]]]*self.transit_matrix[k][l]
                    self.res_prob[i][k][l] = self.forward[i][k]*weight*self.backward[i+1][l]/self.sink
#        for i in self.state:
#            print i,
#        print
#        for prob in self.condit_prob:
#            for j in prob:
#                print round(j,4),
#            print


    def forward_prob(self):
        """
            calculate the forward probability P(forward)_i
            """
        for i in range(len(self.state)):
            self.forward[0][i] = self.emission_matrix[i][self.alphabet_index[self.string[0]]]/(len(self.state))
        for x in range(1, len(self.string)):
            for i in range(len(self.state)):
                emit  = self.emission_matrix[i][self.alphabet_index[self.string[x]]]
                transit = 0
                for j in range(len(self.state)):
                    transit += self.transit_matrix[j][i]*self.forward[x-1][j]
                self.forward[x][i] = transit*emit
        for i in range(len(self.state)):
            self.sink += self.forward[-1][i]


    def backward_prob(self):
        """
            calculate the backward probability P(backward)_i
            """
        for i in range(len(self.state)):
            self.backward[-1][i] = 1.0
        for i in range(1, len(self.string)):
            for k in range(len(self.state)):
                backward = 0
                for l in range(len(self.state)):
                    weight  = self.emission_matrix[l][self.alphabet_index[self.string[-i]]]*self.transit_matrix[k][l]
                    backward += self.backward[-i][l]*weight
                self.backward[-i-1][k] = backward




fname =  'rosalind_ba10k.txt'
with open(fname, "r") as f:
    text = f.read()
    lines = text.split('\n')
    it = int(lines[0])
    x,symbols,states,t,e = parse_emission_symbols_states_transition_matrix_emission_matrix(lines[2:])
#    test = EM_learning(x,symbols,states,t,e)
##    test.soft_decoding()
##    print test.condit_prob
##    print test.res_prob
t,e = hmm_EM_learning(it,x,symbols,states,t,e)
ret = print_hmm_profile(t,e,symbols,states)
print ret
with open(fname+'.out.txt', "w") as f:
    text = f.write(ret)