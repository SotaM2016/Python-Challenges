def sum_digits(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

start = 101
end = 1000
while end > start:
    if start % sum_digits(start) == 0:
        print(start, "is a neat number")
    start += 1