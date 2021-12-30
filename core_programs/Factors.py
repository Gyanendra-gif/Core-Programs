'''
@Author: Gyanendra
@Date: 2021-12-29
@Last Modified by: Gyanendra
@Last Modified time: 2021-12-29 
@Title : Prime Factorization of a Number
'''

"""
Description:
    Function description in depth
Parameter:
      Taking Input From User and Calculate its Prime Factor
Return:
      Prime Factor of a Number
"""
number = int(input('Enter the Number to Check its Prime Factors:' ))
i = 2
while (i<=number):
    if (number%i==0):
        print(i, end=' ')
        number = number/i
    else:
        i += 1


# temp = number
# factors =[]
# while temp != 1:
#     for i in range (2, number):
#         if temp % i == 0:
#             while temp % i == 0:
#                 factors.append(i)
#                 temp = temp/i
#             temp=1

# if len(factors) == 0:
#     print(str(number) + ' is a Prime Number')
# else:
#     print(factors)  
