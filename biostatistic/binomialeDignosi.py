import numpy as np 
import math 
from scipy.stats import binom



'Stiamo analizzando un nuovo esame dignostico.'
'Come requisito si richiede che tale esame sia accurato almeno al 99%.'
'Nella sperimentazione su 100 casi, 95 sono risultati positivi.'
'Possiamo dire che l\'esame è accurato al 99%?'

n_esami = 100
positivi = 95
neativi = 5
prob_diagnosi = 0.99

result = binom.pmf(positivi,n_esami,prob_diagnosi)
print('\n- H0: l\'esame è accurato al 99%\n- H1: l\'esame non è accurato al 99%\n')
print(f'\nLa probabilità di avere un test che abbia un\'accuratezza pari al 99%, e che su 100 esami \
mi restituisca 95 positivi e 5 negativi è pari a {result}, ovvero: {result*100}%')


if result < 0.05:
    print(f'Ho una statistica significativa, quindi rigettiamo ipotesi H0 pertanto l\'esame non ha un\'accuratezza del 99%')
else:
    print(f'Non ho una statistica significativa, quindi non rigettiamo ipotesi H0')

