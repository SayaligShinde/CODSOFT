import random
Letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
'z','A','B'	,'C','D','E','F','G','H','I','J','K','L','M','O','P','Q','R','S','T','U','V','W','X','Y','Z']

Digits=['0','1','2','3','4','5','6','7','8','9']

Symbols=['@','#','$','%','&','^','*','(',')','_','~']

print("Welcome to Password Generator!!!")
no_of_letters=int(input("How many letters do you want:\n"))
no_of_digits=int(input(f"How many Digits do you want:\n"))
no_of_symbol=int(input(f"How many Symbols do you want:\n"))

Password_list=[]
for Letter in range(1,no_of_letters+1):
    Password_list.append(random.choice(Letters))
    
for char in range(1,no_of_symbol+1):
    Password_list += random.choice(Symbols)
    
for char in range(1,no_of_digits+1):
    Password_list += random.choice(Digits)
    
print(Password_list)
random.shuffle(Password_list)
print(Password_list)

Password=""
for letter in Password_list:
    Password += letter
    
print(f"\n your Password is:{Password} \n")