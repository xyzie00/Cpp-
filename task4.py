def check_login(username,password):
    if username== "admin" and password == "1234" :
        return "login successfull"
    else : 
        return "invalid login "
    
try: 
    user_input = input("enter username: ",)
    pass_input = input("enter password: ",)
    if not user_input or not pass_input : 
        raise ValueError("username or passsword cannot be empty. ")
    result = check_login(user_input,pass_input)
    print(result)
except ValueError as e:
    print(f"error : {e}")
except Exception as e:
    print(f"unexpected error : {e}")

