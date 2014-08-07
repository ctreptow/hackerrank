#!/usr/bin/env perl
use warnings;
use strict;

sub get_height {
  my $cycles = shift;
  my $height = 1;

  return $height if ( $cycles == 0 );

  for my $cycle ( 1..$cycles ) {
    if ( $cycle % 2 == 1 ) {
      $height *= 2;
    }
    else {
      $height += 1;
    }
  }

  return $height;
}

print "0 cycles: ", get_height(0), "\n";
print "1 cycles: ", get_height(1), "\n";
print "3 cycles: ", get_height(3), "\n";
print "4 cycles: ", get_height(4), "\n";
