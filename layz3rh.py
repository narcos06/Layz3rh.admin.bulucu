
import urllib.request
import os
import time
import sys

print("""====================================

İnstagram :  layz3rh



====================================""")



time.sleep(1)
print("Hoşgeldiniz")

time.sleep(5)

print("====================================")
time.sleep(1)
print("Dikkat ! Patlatılıcak Sitenin Sonunda / İşareti Olmasına dikkat edin")
time.sleep(1)
print("====================================")
url = input("Admin Paneli Bulunacak Siteyi Giriniz: " )

kelimeler = ('administrator','admin.php','admin','admin.html','login.html','login.php','login.php','log.html','login.cfm','admin.js','login.cgi','images','document','log','custom','script','webmaster','account','em','form','forms','groups','commerce','center','js','jsform','formlog','login.js','form.php','form.js','weblogin','CPanel','cPanel','moderator','form.html','form.asp','moderator/form','moderator/form','moderator/admin','moderator/html','moderator/admin.html','moderator/admin1','admin1','login.htm','login/','login.%EXT%','adm/','admin/','admin/account.html','admin/login.html','admin/home.%EXT%','admin/controlpanel.html','admin/controlpanel.htm','admin/cp.%EXT%.','admin/adminLogin.html','admin/admin_login.%EXT%','admin/controlpanel.%EXT%','admin/admin-login.%EXT%','admin-login.%EXT%','admin/account.%EXT%','admin/admin.%EXT%','admin.htm','admin.html','adminitem/','adminitem.%EXT%','adminitems/','adminitems.%EXT%','adminitems/','adminitems.%EXT%','administrator/','administrator/login.%EXT%','administrator.%EXT%','adminLogin/','adminlogin.%EXT%','admin_area/admin.%EXT%','admin_area/','admin_area/login.%EXT%','manager/','manager.%EXT%','letmein/','letmein.%EXT%','superuser/','superuser.%EXT%')

for kelime in kelimeler:
    sonuc =url+kelime
    try:
        openurl=urllib.request.urlopen(sonuc)
        print("============================")
        print("                                             ")
        
        print("Panel Bulundu ===>"+sonuc)
        
        print("================================")
                     

                         
        with open("siteler.txt","a") as file:
            file.write(sonuc+"\n")
    except:
        print("Sonraki Sefere :/ ")
        
        import urllib.request
import os
import time
import sys
