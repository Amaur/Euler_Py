def FirstFactorial(num): 

  # code goes here
  facto =1
  if (num>1):
     facto=facto*FirstFactorial(num)
     num=num-1
  else:
    return facto
  
  
 
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print (FirstFactorial(8) ) 
