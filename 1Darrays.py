#1D ARRAY
#7/7/2017


#PSEUDOCODE
#DECLARE ages: ARRAY[0..9] OF INTEGER
ages = [3, 4, 5, 3, 5, 6, 7, 3, 1, 6, 7]#this creates the line code#
#for index in range(9 , -1, -1): #shows the array in reverse order
for index in range(0 to 10):
    print(ages[index])

temp = ages[0]
ages[0] = ages[1]
ages[1] = temp


