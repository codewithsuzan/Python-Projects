email=input("Enter your email address: ") #s@g.np,sujan@gmail.com
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha() or email[0].isnumeric():
        if ("@" in email) and (email.count("@")==1):
            if (email[-3]==".") ^ (email[-4]=="."): # one of the case is true than true otherwise false
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i==i.alpha(): 
                        if i==i.upper():
                            j=1
                    elif i==i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("Invalid email address 5")
            else:
                print("Invalid email address 4")
        else:
            print("Invalid email address 3")
    else:
        print("Invalid email address 2")    
else:
    print("Invalid email address 1")        