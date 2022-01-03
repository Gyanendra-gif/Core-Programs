print('Welcome to Electric Bill Program')
number = int(input('Provide the Electricity Units: '))
while number > 0:
    if number <= 50:
        bill = 0 * number
        print('Electricity Bill is: ', bill)
        break
    elif number <= 150:
        bill = (50 * 0) + (number - 75) * 1
        print('Electricity Bill is: ', bill)
        break
    elif number <= 250:
        bill = ( 50 * 0) + (100 - 50) * 1 + (number - 150) * 3
        print('Electricity Bill is: ', bill)
        break
    elif number > 250:
        bill = ( 50 * 0) + (150 - 100) * 1 + (250 - 150) * 3 + (number - 200) * 5
        print('Electricity Bill is: ', bill)
        break