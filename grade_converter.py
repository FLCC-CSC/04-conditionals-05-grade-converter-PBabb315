# FILE NAME - grade_converter.py

# NAME: Patrick Babb
# DATE: 3/1/2026
# BRIEF DESCRIPTION: creating a grade calculator program 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########
def main():
    grade_converter()

def grade_converter():
   
   print('===== Grade Converter =====')
   grade = int(input('Enter the grade (between 0 and 100): '))

   if grade >= 101:
       print('A+')
   elif grade >= 90:
       print('A')
   elif grade >= 80:
      print('B')
   elif grade >= 70:
       print('C')
   elif grade >= 65:
       print('D')
   else:
       print('F')
main()
    









########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Grade Converter =====
Enter a numerical grade (1-100): 101
A+
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): -78
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 64
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 65
D
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 66
D
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is something you would tell a future student to be careful about when
   doing this lab?

To be very careful of the order they write there if elif else statements to avoid a logic error
otherwise the computer will take the first right result and ignore the rest of the comparisons





'''
