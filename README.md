# AES-ENCRYPTION-DECRYPTION
aes encryption/decryption for text and files python and c++ (for all os)

python is needed

        pip install -r requirements.txt

you can use crypto.py wihout .exe file 
        
        usage:
                python crypto.py -k <16,24,32 key> decrypt or encrypt -f file.location -o o_file.location
                python crypto.py -k <0000000000000000 - this is the key> <decrypt - mode> -d <directory location>
                python crypto.py -k 0000000000000000 decrypt -disk E:\
                


includes qr code to easily copy passwords or keys and other data to your phone

        QR:
                python qr.py -d <data (mypass)> -n name.png
  

the program can also generate passwords (.exe file)



  if you use a file with the .exe extension
  this will make it easier for you to use the program(.exe file) works only on windows but python work for all os
  you can also use python script without .exe file
  but the .exe file makes it easy to use
  
         supported keys length: 16, 24, 32 
         

![image](https://user-images.githubusercontent.com/79628437/229899928-e225b1b7-4f6f-4430-b540-cb4bb42a1bbd.png)

![image](https://user-images.githubusercontent.com/79628437/229900140-7d38ca29-d0fd-42ca-b7d9-c9a54ac66de5.png)



![image](https://user-images.githubusercontent.com/79628437/229900283-9eabaf7a-cae9-49db-af94-342c8f308484.png)



![image](https://user-images.githubusercontent.com/79628437/230464359-5c87ebfb-dd81-4560-b23e-0d10edd832b9.png)


Encrypt/Decrypt all files in directory:

![image](https://user-images.githubusercontent.com/79628437/230464002-a127f91e-b80f-4fd0-9423-f81a594a3f5e.png)


        python crypto.py -k <0000000000000000 - this is the key> <decrypt - mode> -d <directory location>



        disc encrypt/decrypt
               python crypto.py -k 0000000000000000 decrypt -disk E:\
 
![image](https://user-images.githubusercontent.com/79628437/230614610-e196ab9c-834f-4f80-ac14-148c59b73c36.png)

if something doesn't work for you use Python Virtual Environments
https://pythonbasics.org/virtualenv/
https://www.youtube.com/watch?v=ebeebaumL3M

