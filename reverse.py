def reverse_num(n):
    return int(str(n)[::-1]) 

n= int(input("Enter anumber:"))

while True:
    rev= reverse_num(n)
    s=n+rev
    print(f"{n}+{rev}={s}")
    
    if str(s)==str(s)[::-1]:
      print("palindrome reached:",s)
      break
    n=s