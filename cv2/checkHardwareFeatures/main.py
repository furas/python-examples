#!/usr/bin/env python3

# https://docs.opencv.org/master/dc/dcc/cvdef_8h.html
# https://docs.opencv.org/master/db/de0/group__core__utils.html#ga74405b66c7a701d17cec08a50b8b2802

import cv2

for x in range(300):
    name = cv2.getHardwareFeatureName(x)
    if name:
        print('{:3} | {:5} | {}'.format(x, str(cv2.checkHardwareSupport(x)), name))
        
'''
  1 | True  | MMX
  2 | True  | SSE
  3 | True  | SSE2
  4 | True  | SSE3
  5 | True  | SSSE3
  6 | True  | SSE4.1
  7 | True  | SSE4.2
  8 | True  | POPCNT
  9 | False | FP16
 10 | False | AVX
 11 | False | AVX2
 12 | False | FMA3
 13 | False | AVX512F
 14 | False | AVX512BW
 15 | False | AVX512CD
 16 | False | AVX512DQ
 17 | False | AVX512ER
 18 | False | AVX512IFMA
 19 | False | AVX512PF
 20 | False | AVX512VBMI
 21 | False | AVX512VL
 22 | False | AVX512VBMI2
 23 | False | AVX512VNNI
 24 | False | AVX512BITALG
 25 | False | AVX512VPOPCNTDQ
 26 | False | AVX5124VNNIW
 27 | False | AVX5124FMAPS
100 | False | NEON
150 | False | CPU_MSA
200 | False | VSX
201 | False | VSX3
256 | False | AVX512-SKX
257 | False | AVX512-COMMON
258 | False | AVX512-KNL
259 | False | AVX512-KNM
260 | False | AVX512-CNL
261 | False | AVX512-CLX
262 | False | AVX512-ICL
'''        
