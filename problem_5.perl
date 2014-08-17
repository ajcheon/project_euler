#Perl
 my $result = 2;
 foreach (3..20){
     $result = lcd($result,$_);
    }
   
print $result;

sub lcd {
    ($m,$n) = @_;
    $gcd = gcd($m,$n);
    return $m*$n/$gcd;
}
    
sub gcd {
    my($a,$b) = @_;
    return $a if $b == 0;
    if($b > $a){
        gcd($b,$a);
    }else{
   $a = $a % $b;
   gcd($b,$a);
   }
}