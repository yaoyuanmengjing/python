#!/usr/bin/env python
#_*_enconding:utf-8 _*_
import os
import subprocess
os.system(r'"C:\CardSystem\CardSystem.exe"')

#os.system(r'"C:\Users\Administrator.USER-20171003KG\Desktop\CardSystem\CardSystem.exe"')
#os.system('TASKKILL /F /IM CardSystem.exe')
print (os.popen('tasklist /FI "IMAGENAME eq CardSystem.exe"').read()  )
print("CardSystem.exe" in os.popen('tasklist /FI "IMAGENAME eq CardSystem.exe"').read()  )
