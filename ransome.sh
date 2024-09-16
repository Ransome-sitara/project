x#!/bin/bash
#Arithmetic
echo "welcome my dear friend "
name="daniel"
age="80"
location="manful hub"
echo "my name is $name an i am $age years old,and my location is $location"
man=${location:3:3}
echo $man
echo ${!cap[*]}
mult=$((4*4))
echo $mult
time=$(expr 25/5)
echo $time

array=(one two three)
echo ${array[*]}
array[2]="four five six"
echo  ${array[*]}


array=(ten eleven and nine )
echo ${array[@]}
array[2]="two  three"
echo ${array[*]}

declare -a array2=(good bad evil)
declare -a array3=(sweet salty sour)
echo "lets display ${array2[*]} and ${array3[*]}"


echo ${!cap[*]}
mult=$((4*4))
echo $mult
declare -A cap
cap=([goods]="ransome"[price]="30"[places]="uyo")
echo ${!cap[*]}
 cap[goods]="golds"
echo ${cap[goods]}


echo ${!cap[*]}
mult=$((3*5))
echo ${!cap[*]}



































