import numpy as np 
import math 
from scipy.stats import binom


'''
Abbiamo un sospetto che una moneta sia truccata, in modo tale da far uscire croce (C) più spesso di testa (T).
'''

print(' \n- H0: la moneta è bialnciata\n- H1: la moneta è truccata\n')
n_lanci = 10
prob_testa = 0.5
prob_croce = 0.5
n_croce = 8
n_testa = 2
array_lanci = ['T','C','C','C','T','C','C','C','C','C']

'''
Voglio capire se con 10 lanci ho una statistica che sia significativa per decretare se la moneta è truccata o meno.
Si assume pertanto che l'ipotesi h0 sia vera. E si calcola la probabilità di ottenere 8 croci su 10 lanci condizionata a questa ipotesi.
P(Dati In Possesso | H0)
'''

result = binom.pmf(n_croce,n_lanci,prob_croce)
print(f'La probabilità di ottenere 8 croci su 10 lanci è {result}')

if result < 0.05:
    print(f'Ho una statistica significativa, quindi rigettiamo ipotesi H0')
else:
    print(f'Non ho una statistica significativa, quindi non rigettiamo ipotesi H0')

