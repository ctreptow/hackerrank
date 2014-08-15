#!/usr/bin/env python

def is_palindrome(text):
  i = 0
  j = len(text) - 1

  for i in range(0, ( len(text) / 2 ) + 1 ):
    if ( text[i] != text[j] ):
      return False
    j -= 1

  return True

def solve_it( text ):
  operations = 0
  if is_palindrome( text ):
    return operations
  else:
    pass

first_line = raw_input()
testcase_count = int( first_line ) 
    
for test_case in range(0, testcase_count ):
  line = raw_input()
  print line
  print solve_it(line)
                    
print 'aba ', solve_it('aba')                     
print ord('a')
