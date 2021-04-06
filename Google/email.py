Techies={}
mail_add = True
while mail_add:
    enter_name=input("enter the name of the person : ")
    enter_mail=input("enter the email of the person : ")
    Techies[enter_name] = enter_mail
    repeate = input("\ndo yo want to add another email details ? ")
    if repeate == 'no':
        mail_add = False
print(Techies)

