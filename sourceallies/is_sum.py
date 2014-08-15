#!/usr/bin/env python

def isSumPossible( a, N ):
  # Don't keep numbers > N since one of those plus anything is too big already
  b = [ x for x in a if x <= N ]
  if not len(b) > 0:
    b = a

  for i in range(0, len(b)):
    for j in range(i + 1, len(b)):
      if ( b[i] + b[j] == N ):
        return 1

  return 0

  
print isSumPossible( [18,11,21,28,31,38,40,55,60,62], 32 )
#print isSumPossible( [18,11,21,33], 66 )
