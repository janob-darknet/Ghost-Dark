
baseurl = input("url: ")

from bs4 import BeautifulSoup
import os
from urllib.request import urlretrieve
from urllib.request import urlretrieve
import urllib.request
import cssutils
import logging
from time import sleep




def report(count, size, total):
        progress = [0, 0]       
        progress[0] = count * size
        if progress[0] - progress[1] > 1000000:
            progress[1] = progress[0]
            print("Yuklanmoqda {:,}/{:,} ...".format(progress[1], total))

print ("Serverga ulanmoqda...")
cssutils.log.setLevel(logging.CRITICAL)
directory = ''

opener = urllib.request.build_opener()
#defining headers as some servers mandiate it
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),
                        ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
                        ('Connection', 'keep-alive')
                    ]
urllib.request.install_opener(opener)
html_doc = urllib.request.urlopen(baseurl).read()

print ("Ulanish yakunlandi!")
try :
        soup = BeautifulSoup(html_doc, 'html.parser')
        f = open( 'index.html', 'w' )
        f.write(str(soup))
        f.close()
        print ("Telegram: @janob_darknet")
        #Get All Images
       # print ("Jarayon ")
      #  print ("Step 1: Getting all images.")
        a = soup.find_all('img')
        for i in range(len(a)):
            try:
                if(a[i].get('data-src')):
                    directory = a[i]['data-src']
                elif(a[i].get('src')):
                    directory = a[i]['src']
                else:
     #               continue
        #        print ('\t[+]Getting img = '+str(directory))
         #       if "data:image" in directory:
     #               print("-------Skipped for ---------",directory)
                    continue
                if not os.path.exists(os.path.dirname(directory)):
           #         print ("    [DIR]Creating directory")
                    os.makedirs(os.path.dirname(directory))
                testfile, headers = urlretrieve(baseurl+directory, directory, reporthook=report)
            except Exception as e:
               d = ""
      #  print ('==============Done getting images!==============')
        #Get all Css
  #      print ("Step 2: Getting all CSS.")
        a = soup.find_all('link')
        for i in range(len(a)):
            try:
                directory =  a[i]['href']
                if(".css" not in directory):
                 #   print("-------Skipped for ---------",directory)
#                    continue
              #  if "http" in directory or "https" in directory:
#                    print ("------Skipped for ----- ",directory)
                    continue
             #   print ('\t[+]Getting CSS = '+str(directory))
                if "/" not in directory:
                        print ("\tKatalog yo'q. Fayl saqlanmoqda",directory)
                elif not os.path.exists(os.path.dirname(directory)):
                 #   print ("    [DIR]Creating directory")
                    os.makedirs(os.path.dirname(directory))
                testfile, headers = urlretrieve(baseurl+directory, directory, reporthook=report)   
                urls = list( cssutils.getUrls(cssutils.parseFile(directory)))
                if "fontawesome" in directory:
                    continue
                if(len(urls)!=0):
                    for link in urls:
                        try:
                            if "http" in directory or "https" in link or "data:image/" in link:
                              #  print ("------Skipped for ----- ",link)
                                continue
                            while("../" in link):
                                if("assets" in link):
                                    link = link[3:]
                                else:
                                    link = "assets/"+link[3:]
                       #     print ('\t\t[+]Getting CSS-Image = '+str(link))
                            if "/" not in link:
                                    print ("\t\tKatalog yo'q. Fayl saqlanmoqda",link)
                            elif not os.path.exists(os.path.dirname(link)):
                                print ("Katalog yaratilmoqda")
                                os.makedirs(os.path.dirname(link))
                            testfile, headers = urlretrieve(baseurl+link, link, reporthook=report)
                        except Exception as e:
                             d = ""
            except Exception as e:
                 d = ""


        #Get all JS
        a = soup.find_all('script')
        for i in range(len(a)):
            try:
                if(a[i].get('src')):
                    directory=a[i]['src']
                else:
               #     continue
#                if "http" in directory or "https" in directory:
#                    print ("------Skipped for ----- ",directory)
                    continue
           #     print ('\t[+]Getting JS = '+str(directory))
                if not os.path.exists(os.path.dirname(directory)):
               #     print ("    [DIR]Creating directory")
                    os.makedirs(os.path.dirname(directory))
                testfile, headers = urlretrieve(baseurl+directory, directory, reporthook=report)
            except Exception as e:
                 d = ""
#        print ('==============Done getting JS Files!==============')
#        print ('Script Executed successfully!')
 #       os.system("clear")
#        print("Succes !")
        
        os.system("python main.py")
except Exception as e:
    print ("Exception occurred = ",e)