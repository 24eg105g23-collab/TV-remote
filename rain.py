def reverse_num(n):
 return int(str(n)[::-1])
  
n=int(input("Enter a number:"))
rev= reverse_num(n)
s= n+rev
print(f"{n}+{rev}={s}")

if str(s) == str(s)[::-1]:
 print("palindrome:",s)

n=s