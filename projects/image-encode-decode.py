import base64
import os, sys
#from janob_darknet import code
janob_darknet = input("""
\033[1;31m
image encode 

1) encode
2) decode
3) delete 
: \033[1;32m""")

#decode

if janob_darknet=="2":
	joylashuv_txt = input("\033[1;31mencoded image file:\033[1;32m ")
	
	file = open(joylashuv_txt, 'rb')
	byte = file.read()
	file.close()
	print("\033[1;31mshifrdan chiqarildi")
	decodeit = open(code.image_name, 'wb')
	decodeit.write(base64.b64decode((byte)))
	decodeit.close()
	
# encode	

elif janob_darknet == "1":
	joylashuv_jpg = input("image: ")
	with open(joylashuv_jpg, "rb") as image2string:
		
		converted_string = base64.b64encode(image2string.read())
		print("\033[1;31mshifrlandi")
			  
	with open(code.txt_name, "wb") as file:
	    file.write(converted_string)
	    
# delete

elif janob_darknet == "3":
	file_for_delete = input("\033[1;31mfile for delete: \033[1;32m")
	os.system("rm -rf "+ file_for_delete)
	print("\033[1;31mfile ochirildi")
else:
	print("\033[1;31mhato(")