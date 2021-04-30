magic_square = [
    [8, 3, 4],
   [1, 5, 9],
    [6, 7, 2]
]
i=0
sum=0
num=3
while i<num:
    sum=sum+magic_square[i][i]
    i=i+1
print(sum)
i2=0
sum2=0
while i2<num:
  sum2=sum2+magic_square[i][num-i-i]     






    