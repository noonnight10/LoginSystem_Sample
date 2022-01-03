#ID upload
ID = input("Please input your ID. : ")
PW = input("Please input your PW. : ")

#login page
i = 1
m = 1
while m <= 5: #login attempt exceeded
    while i == 1: #if login success
        if m == 6:
            print("Your number of attempts has exceeded 5.")
            break
        a = input("What's your ID? : ")
        if a == ID:
            b = input("What's your PassWord? : ")
            if b == PW: #login successful
                i = i + 1
                print("login successful.")
                break
            else:
                print("login failed. try again.\n==============")
                m = m + 1
        else:
            print("login failed. try again.\n==============")
            m = m + 1
            break

if m == 6: #login attempt exceeded
  print("Your number of attempts has exceeded 5.")