marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
length = len(marks)
i = 0
less_than50 = 0
more_than50 = 0
while i <length:
       marks=marks[i]
       if marks < 50:
        less_than50 = less_than50 + 1
       else:
        more_than50 = more_than50 + 1
        index = i+ 1
print ("Marks more than 50: " + more_than50)
print ("Marks less than 50: " + less_than50)       