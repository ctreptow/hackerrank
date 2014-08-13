#!/usr/bin/env python

def solveIt( freeway_length, widths, entrance_index, exit_index ):
  #bike:  1
  #car:   2
  #truck: 3

  narrowest_width = 3

  for segment in range( 0, freeway_length ):
    if ( segment >= entrance_index and segment <= exit_index ):
      if ( widths[segment] < narrowest_width ):
        narrowest_width = widths[segment]

  return narrowest_width

first_line = raw_input()
freeway_length, testcase_count = (int(x) for x in first_line.split())
    
second_line = raw_input()
widths = [ int(x) for x in second_line.split() ]

for test_case in range(0, testcase_count ):
  line = raw_input()
  entrance_index, exit_index = (int(x) for x in line.split())
  print solveIt(freeway_length, widths, entrance_index, exit_index)
                    
                     
