import zipfile
 
 
def crack_password(password_list, obj):
   
    idx = 0
    with open(password_list, 'rb') as file:
        for line in file:
            for word in line.split():
                try:
                    idx += 1
                    obj.extractall(pwd=word)
                    print("\033[1;32mparol topildi:\033[1;31m ", idx)
                    print("\033[1;32mparol: \033[1;31m", word.decode())
                    return True
                except:
                    continue
    return False
 
 
password_list = input("\033[1;31mpassword list:\033[1;32m ")
 
zip_file = input("\033[1;31mzip file:\033[1;32m ")
 

obj = zipfile.ZipFile(zip_file)
 
cnt = len(list(open(password_list, "rb")))
 
print("\033[1;31mqidiruv", cnt,
      "\033[1;31mparollar royxati ")
 
if crack_password(password_list, obj) == False:
    print("\033[1;31mparol topilmadi !")