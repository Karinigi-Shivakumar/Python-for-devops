x =-1
reversed_num = 0
if x<0:
    print("not palindrome")
else:
    print("reversed_num",reversed_num)
    temp = x
    print("temp_var",temp)
    while temp != 0:
        digit = temp % 10
        print("dig",digit)
        reversed_num = reversed_num * 10 + digit
        print("reversed_num_wh",reversed_num)
        temp //= 10
        if reversed_num == x:
            print("palindrome")
        else:
            print("not palindrome")

