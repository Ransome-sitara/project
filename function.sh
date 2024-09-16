#!/bin/bash
sum (){
for i in $@ ; do
local sum=$@
echo $sum
done
}
read -p "addition: "addition  
echo "$sum"
