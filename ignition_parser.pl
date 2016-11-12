#!/usr/bin/perl -w
use strict;
my $f = 0;
my $ck = 0;
my $b = 0;
my $r = 0;
my $ca = 0;
my $N = 0;

while(<>){
    next if ! /\[ME\]/;
    print if /Card dealt/;
    $N++ if /Card dealt/;
    $f++ if /Folds/;
    $ck++ if /Checks/;
    $b++ if /Bets/;
    $r++ if /Raises/;
    $ca++ if /Calls/;
}

print "$f $ck $b $r $ca $N\n";
print "VPIP ~= " . ($b + $r + $ca) / $N
