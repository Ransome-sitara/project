#!/bin/bash
echo 1' 2 3'45
echo -n now\is the  time 
printf "%s %s\n"one two three



printf "Enter a number  greater than ten: " 
read number 
if ((number > 10));then 
             printf"%d is too big\n" "$number" >&2
exit 1
else
printf"you entered %d\n""$number"
fi
if((number < 10)); then
printf"%d is too high\n" "$number" >&2
exit 1
else
printf "you enter %d\n" "$number"
fi
