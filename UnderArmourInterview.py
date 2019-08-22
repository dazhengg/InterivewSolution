# Your last Java code is saved below:
# // Given a string, write a method that compacts consecutive identical values into an output string.  
# // For instance,  "aabcjjkaa" becomes "a2bcj2ka2".  Note that order does matter since we may want to explode 
# // the compacted string back into the orginal string.  Let's assume that there are only lower case alphabetical
# // characters in the string. 


# Count each letter and if it's a "new" letter than reset count to zero. 
#a 2 b a 2 
# aa b aa 

# reset the count to zero. and also check if count == 1 

def compacter(user_string): 
  res = ""
  count = 0 #ab 
  for idx in range(len(user_string) - 1): # aa    
    char = user_string[idx]  # aa b aa  
    count += 1  # = 1  
    if char != user_string[idx + 1]:
      if count > 1:
        res += char + str(count) 
        count = 0
      else:  
        res += char
        count = 0 
    

  count += 1 
  #check for the last with the second last letter, since our loop goes up until the last letter (exclusive boundary)
  if user_string[-1] == user_string[-2] and count > 1:
      res += user_string[-1] + str(count)
  else:
      res += user_string[-1]
    
    
  return res 
    
  
user_string = "aabcjjkajjd" 
ans = compacter(user_string)
print(ans)

  

# import java.io.*;

# class MyCode {
#     public static void main (String[] args) {
#         System.out.println("Hello Java");
#     }
# }