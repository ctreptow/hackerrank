#!/usr/bin/env python

def count_differences( N, K ):
  count = 0
  # Don't keep numbers < N since one of those minus anything is too small already
  b = [ x for x in a if x >= N ]
  if not len(b) > 0:
    b = a

  for i in range(0, len(b)):
    for j in range(i + 1, len(b)):
      if ( ( b[i] - b[j] == N ) or ( b[j] - b[i] == N ) ):
        count += 1

  return count

  
first_line = raw_input()
n, k = (int(x) for x in first_line.split())
    
second_line = raw_input()
numbers = [ int(x) for x in second_line.split() ]

print count_differences( numbers, k )
                    
                     
