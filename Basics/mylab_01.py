# -*- coding: utf-8 -*-
"""
@author: Lorenzo Negri
"""

# simple code to generate basic summary statistics from one column data-set file
tempe = []
with open('lab_05.txt') as infile:
    for row in infile:
        tempe.append(float(row.strip()))
ts=sorted(tempe)

print('the mean of the data values is: ',sum(tempe)/len(tempe),'\n',
      'the max value is: ',max(tempe),'\n'
      'the min value is: ',min(tempe),'\n',
      'the median is: ', ts[int(len(tempe)/2)])
