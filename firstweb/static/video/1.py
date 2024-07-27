import os

for i in os.listdir("./"):
    if i.find("~") >= 0 :
        par = i.split("~")
        
        os.rename(os.path.join("./",i),"第一季第"+par[0].split("E")[1]+"集"+par[1].replace(".mkv",".mp4").split("E")[1]+"集")
    elif i.find("S")>=0:
        par = i.split("E")[1].replace(".mkv","")
        os.rename(os.path.join("./",i),"第一季第"+par+"集.mp4") 
