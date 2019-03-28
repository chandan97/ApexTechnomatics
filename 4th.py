#Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
#Examples:

#Input: 21445 Output: 54421

#Input: 145263 Output: 654321

#Input: 1254859723 Output: 9875543221



number = input("Enter a number: ")
length = len(number)
number = int(number)

nlist = []
for _ in range(0, length):
     
     num = number % 10
     nlist.append(int(num))
     number = number / 10

desc = sorted(nlist, reverse=True)
desc = map(str, desc)
desc = ''.join(desc)
print(desc)


