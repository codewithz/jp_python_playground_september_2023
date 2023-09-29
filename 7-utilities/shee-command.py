import os,subprocess
import sys

os.system("dir")

os.system("md test")

print("-"*40)

# os.system("cd test")
print("-"*40)
# os.system("get-service")

print("-"*40)
# p=subprocess.Popen(["powershell.exe","E:\\Local d\\Zartab\\Trainings\\2023\\B-15 JP Morgan Python September 2023\\Python_Playground\\JP_Python_Background\\6-object-orientation\\hello.ps1"],stdout=sys.stdout)
p=subprocess.Popen(["powershell.exe","E:\\hello.ps1"],stdout=sys.stdout)

p.communicate()



#
# list_files=subprocess.Popen("dir",shell=True)
#
# print(list_files)