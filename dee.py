#!/bin/python3
#print ("hello word")
#print ("name is daniel emmanuel")
#print ('*' * 10)
#price = 20
#print (price)
#price = 50
#print (price)

#full_name = 'john smith'
#age = 20
#is_new = True
#name  =   input ("what is your name?  ")
#input  ("hello !! " + name)
#input ("welcome on board  " + name)
 #input ("what will you like us to offer you?  " + name)
#age   =  input ("your age? ")
#input   ("you are" + age) 
#print ("if you are ask to state if you are new say 'new'  other  wise say ' not new'")
#is_new_or_not_new  = input ("are you new?  ")
#colour =  input ('whats  your favourite  colour?  ')
#print  (name  + "  your favourite colour is  " + colour)
#print ( name + "  you are  " + is_new_or_not_new)



#birth_year = input ('birth year;')
#age =2024 -  int (birth_year)
#print (age)

#course = 'python for beginners '
#print (course [0:-1])


#price = 1000000
#good_credit_card =  False
#bad_credit_card =  False
#if  good_credit_card:
  #   down_payment = 0.1 * price
   #  print (f"Down payment:${down_payment}")
#elif bad_credit_card:
 #    Down_payment = 0.3 * price 
  #   print (f"Down payment : ${Down_payment}")
#else: 
 #    print ("not eligiblefor the house")



name = input  ("name  ") 
if  len(name) < 3:
     print ('name is less than the maximum character required')
elif len(name) > 50:
     print ('name  is greater than the  maximum character required')
else: 
     print ('this is a very good name')



for numbers in  range (10 + 1):
    if numbers != 8 :
          input('number: ')
    elif  numbers == 8 :
           print ('this is number 8')
else:
            print ("this is the end")
