# Given a sorted array of strings which is interspersed with empty strings, write a method to find the location of a given string.
#Example: find “ball” in [“at”, “”, “”, “”, “ball”, “”, “”, “car”, “”, “”, “dad”, “”, “”] will return 4
#Example: find “ballcar” in [“at”, “”, “”, “”, “”, “ball”, “car”, “”, “”, “dad”, “”, “”] will return -1






vals = ['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '']
length = len(vals)

word= input("enter the word to find")
for i in range(0, length):
   if vals[i] == word:
      print(i)
      k=1
   else:
       k=0

if(k==0):
 print(-1)
        

   
