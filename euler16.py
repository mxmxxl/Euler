#Q: What is the sum of the digits of the number 21000?

x = str(2**1000)
sum = 0
for i in range(len(x)):
  sum += int(x[i])

print(sum)