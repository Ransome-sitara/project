#!/bin/bash
read -p "enter a number"   number
if (($number % 2== 0));
then
echo "$number is an even number"
else (("$number" % 3== 1)); 
echo"$number is an odd number"
fi
