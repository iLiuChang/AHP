#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


RI_dict = {1: 0, 2: 0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45}

# 矩阵
A_arr = [[1, 2, 1.0/3, 3],
        [1.0/2, 1, 1.0/3, 2],
        [3, 3, 1, 4],
        [1.0/3, 1.0/2, 1.0/4, 1]]

def main():
    # 矩阵
    A = np.array(A_arr)

    a_sum0 = A.sum(axis=0)
    B = A / a_sum0  
    print('新矩阵:')
    print(B)
    b_sum = B.sum(axis=1)
    print('新矩阵行和: %s' % b_sum)

    
    W = b_sum.sum()
    w_arr = []
    for w in b_sum:
        w_arr.append(w/W)

    print('W: %s' % w_arr)

    AW = []
    for a in A :
        aa = a * w_arr
        AW.append(aa.sum())

    print('AW: %s' % AW)

    result = np.array(AW) / np.array(w_arr)
    print('AW/W: %s' % result)

    row = result.shape[0]
    Max = result.sum()/row
    print('λMax: %s' % Max)

    CI = (Max - row) / (row - 1)
    print('CI: %s' % CI)
    
    CR = CI / RI_dict[row]
    print('CR: %s' % CR)
    
 
if __name__ == '__main__':
    main()



