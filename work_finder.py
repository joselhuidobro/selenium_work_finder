
#-------------------------------------------------------------------------
from selenium import webdriver

import time
import winsound
from selenium.common.exceptions import NoSuchElementException




PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
#def alarma():
 #   a=1
  #  intentos=0
   # winsound.Beep(800, 500)
   # winsound.Beep(800, 500)
   # winsound.Beep(800, 500)
   # winsound.Beep(800, 500)



def ingresar_contraseña():
    print("Hello fish... lets play a game...")
    print("In the last few months you have been a bitch")
    time.sleep(2)
    print("Tienes 13 segundos para ingresar la contraseña...")
    winsound.Beep(400, 500)

    driver.get("https:xxxxxxxxxxxxxxxxx")
    c = driver.page_source
    # print(c)
    time.sleep(10)
    winsound.Beep(800, 500)


# -----iNICIO --

ingresar_contraseña()
a = 0
intentos=0
primera = 0

while (True):


 if (a== 1):  #  siguiente accion despues de dar el primer click
                intentos = 0
                winsound.Beep(800, 500)
                winsound.Beep(400, 500)




                 # ----------------- Intentar segundo click--------

                try:

                    
                     driver.find_element_by_class_name('.find-work-row').click()

                     a=2
                except NoSuchElementException:

                     print("No pude hacer el segundo click ")
                     a = 0
                     time.sleep(10)

 if (a == 2):  # siguiente accion despues de dar el primer click
                    intentos = 0
                    winsound.Beep(100, 100)
                    print("logre dar el SEGUNDO click Drops de MIC")
                    time.sleep(10000)

 else:
     #0 buscando primer click
     #1 Se dio el primer click
     #2 Se dio el segundo click
   while(a==0):


                 driver.get("xxxxxxxxxxxxxxxxxxxxxxxx")
                 intentos= intentos + 1
                 print("Buscando trabajos, intento No.")
                 print(intentos)


    #---------------------------- primer click----------------------
                 time.sleep(0.4)

                 try:
                         driver.find_element_by_xpath("//p").click()

                 except NoSuchElementException: #sino l puede dar click...
                     a=1

                 time.sleep(2)