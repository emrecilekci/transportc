import requests
import logging

class transportcb:
    def __init__(self, sourceip, destip, user, password):
        self.sourceip = sourceip
        self.destip = destip
        self.user = user
        self.password = password
        self.clusterversion()


    def clusterversion(self):
        urlfordestinaion = f"http://{self.destip}:8091/pools"
        urlforsource = f"http://{self.sourceip}:8091/pools"
        sourceversion = requests.get(url=urlforsource, auth =(self.user,self.password))
        destinationversion = requests.get(url=urlfordestinaion, auth =(self.user,self.password))
        sourceresult = int(str(sourceversion.json()['implementationVersion']).split('.')[0])
        destinationresult = int(str(destinationversion.json()['implementationVersion']).split('.')[0])

        if destinationresult >= sourceresult:
            print("Bilgi: Migrate İşlemi Devam Ediyor . . .")
            self.canmigrated = True
            return True
        else:
            print("Hata : Migrate İşlemi Yapılamaz(Versiyonlar Uygun Değil)")
            self.canmigrated = False
            return False


    def migratefull(self):
        if self.canmigrated == True:
            print("Migration Başladı")
        else:
            print("Hata")
        return True

