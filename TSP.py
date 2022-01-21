import os, csv
# import klu
from itertools import permutations
lintasan=""
database="database.csv"
data_salesman = []
data_user = []
tampung_username = []
tampung_password = []

lombok_barat_route=[
    [0,1,2,3,4],
    [1,0,22,26,23],
    [2,22,0,5.8,11],
    [3,26,5.8,0,12],
    [4,23,11,12,0]
   
]

lombok_tengah_route=[
    [0,1,2,3,4],
    [1,0,14.2,25.3,17.7],
    [2,14.2,0,18,7.8],
    [3,25.3,18,0,9.6],
    [4,17.7,7.8,9.6,0]  
]

lombok_utara_route=[
    [0,1,2,3,4,5],
    [1,0,45,32,62,47],
    [2,45,0,27,31,17],
    [3,32,27,0,44,30],
    [4,62,31,44,0,14],
    [5,47,17,30,14,0]
]

lombok_timur_route=[
    [0,1,2,3,4],
    [1,0,51,38,21],
    [2,51,0,16,36],
    [3,38,16,0,25],
    [4,21,36,25,0]
   
]

mataram_route = [
    [0,1,2,3,4],
    [1,0,4.3,6.9,7.8],
    [2,4.3,0,4.7,11],
    [3,6.9,4.7,0,12],
    [4,7.8,11,12,0]
]

try:
    with open("database.csv", "r") as cswrite:
        reader = csv.reader(cswrite, delimiter=",")
        for baris in reader:
            data_salesman.append(baris)
except:
    pass
# main tidak perlu dirubah
def main():
    os.system("clear")
    print("="*108)
    print("||"+"Ninjago ".center(104)+"||")
    print("||"+"Selamat Datang di Aplikasi Ninjago".center(104)+"||")
    print("||"+"Silahkan login jika anda telah memiliki akun".center(104)+"||")
    print("||"+"dan Silahkan mendaptar jika belum memiliki akun".center(104)+"||")
    print("="*108)
    print("||"+"[1] Masuk ".ljust(103)+"||")
    print("||"+"[2] Daftar".ljust(103)+"||")
    print("||"+"[3] Keluar".ljust(103)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    pilih = input("Masukan pilihan anda: ")
    if pilih == "1":
        login()
    elif pilih == "2":
        register()
    elif pilih == "3":
        exit()
# lintasan kota mataram /ubah
def menu_lombokTengah():
    os.system("clear")
    global start
    print("||"+"Daftar Menu Kota".center(104)+"||")
    print("="*108)
    print("||"+"0 = Janapria".ljust(104)+"||")
    print("||"+"1 = Kopang".ljust(104)+"||")
    print("||"+"2 = Pringgarata".ljust(104)+"||")
    print("||"+"3 = Batukliang".ljust(104)+"||")
    print("||"+"4 = Praya".ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    start = int(input("Masukan titik awal: "))
    
# lintasan lombok utara
def menu_lombokUtara():
    os.system("clear")
    global start
    print("||"+"Daftar Menu Kota".center(104)+"||")
    print("="*108)
    print("||"+"1 = Bayan".ljust(104)+"||")
    print("||"+"2 = Gangga".ljust(104)+"||")
    print("||"+"3 = Kayangan".ljust(104)+"||")
    print("||"+"4 = Pemenang".ljust(104)+"||")
    print("||"+"5 = Tanjung".ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    start = int(input("Masukan titik awal: "))
  
# Lintasan lmbok Barat
def menu_lombokBarat():
    os.system("clear")
    global start
    print("||"+"Daftar Menu Kota".center(104)+"||")
    print("="*108)
    print("||"+"0 = Narmada".ljust(104)+"||")
    print("||"+"1 = Kediri".ljust(104)+"||")
    print("||"+"2 = Labuapi".ljust(104)+"||")
    print("||"+"3 = Gerung".ljust(104)+"||")
    print("||"+"4 = Lembar".ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    start = int(input("Masukan titik awal: "))
  
# lintasan lombok timur
def menu_lombokTimur():
    os.system("clear")
    global start
    print("||"+"Daftar Menu Kota".center(104)+"||")
    print("="*108)
    print("||"+"0 = Aikmel".ljust(104)+"||")
    print("||"+"1 = Jerowaru".ljust(104)+"||")
    print("||"+"2 = Keruak".ljust(104)+"||")
    print("||"+"3 = Labuhan haji".ljust(104)+"||")
    print("||"+"4 = Masbagik".ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    start = int(input("Masukan titik awal: "))

# lintasan kota mataram 
def menu_kota_mataram():
    os.system("clear")
    global start
    print("||"+"Daftar Menu Kota".center(104)+"||")
    print("="*108)
    print("||"+"0 = Selaparang".ljust(104)+"||")
    print("||"+"1 = Ampenan".ljust(104)+"||")
    print("||"+"2 = Sekarbela".ljust(104)+"||")
    print("||"+"3 = Sandubaya".ljust(104)+"||")
    print("||"+"4 = Cakranegara".ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    start = int(input("Masukan titik awal: "))
 
# dashboar tidak perlu dirubah
def dashboard():
    os.system("clear")
    print("="*108)
    print("||"+"NinjaGo".center(104)+"||")
    print("="*108)
    print("||"+"    [1] = Mulai Route".ljust(104)+"||")
    print("||"+"    [2] = Detail Route".ljust(104)+"||")
    print("||"+"    [0] = Keluar".ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    pilihan = input("Masukan pilihan anda : ")
    if pilihan == '1':
        daftar_kota()
    elif pilihan == '2':
        detail()
        input("Tekan enter untuk kembali")
        dashboard()
    elif pilihan == '0':
        confirm = input("Apakah anda yakin untuk keluar ? [y/n]")
        if confirm == 'y':
            main()
        else:
            dashboard()
    else:
        dashboard()

def dashboard1():
    os.system("clear")
    print("="*108)
    print("||"+"NinjaGo".center(104)+"||")
    print("="*108)
    print("||"+"    [1] = Mulai Route".ljust(104)+"||")
    print("||"+"    [0] = Keluar".ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    pilihan = input("Masukan pilihan anda : ")
    if pilihan == '1':
        daftar_kota()
    elif pilihan == '0':
        confirm = input("Apakah anda yakin untuk keluar ? [y/n]")
        if confirm == 'y':
            main()
        else:
            dashboard1()
    else:
        dashboard1()

# daftar kota tidak perlu dirubah
def daftar_kota():
    os.system("clear")
    print("="*108)
    print("||"+"NinjaGo".center(104)+"||")
    print("="*108)
    print("||"+"    [1] = Mataram".ljust(104)+"||")
    print("||"+"    [2] = lombok Timur".ljust(104)+"||")
    print("||"+"    [3] = lombok Barat".ljust(104)+"||")
    print("||"+"    [4] = lombok Tengah".ljust(104)+"||")
    print("||"+"    [5] = lombok Utara".ljust(104)+"||")
    print("||"+"    [0] = Keluar".ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    pilihan = input("Masukan pilihan anda : ")
    if pilihan == '1':
        menu_kota_mataram()
        tsp(mataram_route, start)
        hasil()
    elif pilihan == '2':
        menu_lombokTimur()
        tsp1(lombok_timur_route, start)
        hasil()
    elif pilihan == '3':
        menu_lombokBarat()
        tsp2(lombok_barat_route, start)
        hasil()
    elif pilihan == '4':
        menu_lombokTengah()
        tsp3(lombok_tengah_route, start)
        hasil()
    elif pilihan == '5':
        menu_lombokUtara()
        tsp4(lombok_utara_route, start)
        hasil()      
    elif pilihan == '0':
        confirm = input("Apakah anda yakin untuk keluar ? [y/n]")
        if confirm == 'y':
            main()
        else:
            dashboard()
    else:
        dashboard()

# mataram
def tsp3(lombok_tengah_route, start):
    global lintasan
    tampung_point = []
    lintasan_tsp = []
    for point in range(len(lombok_tengah_route)):
        if point != start:
            tampung_point.append(point)
    min_cost = 1000000
    tampung_permutasi = permutations(tampung_point)
    for permutasi in tampung_permutasi:
        kota_awal(start)
        lintasan+="-->"
        current_cost = 0
        baris = start
        for kolom in permutasi:
            kota_tengah(kolom)
            current_cost +=lombok_tengah_route[baris][kolom]
            baris = kolom
        kota_awal(start)
        current_cost +=lombok_tengah_route[baris][start]
        lintasa_copy = lintasan
        if current_cost == min_cost:
            lintasan_tsp.append(lintasa_copy)
        elif current_cost < min_cost:
            lintasan_tsp.clear()
            lintasan_tsp.append(lintasa_copy)
        min_cost = min(min_cost, current_cost)
        lintasan = ""
    return min_cost,lintasan, lintasan_tsp

def kota_awal(start):
    global lintasan
    if start == 0:
        lintasan += "Janapria"
    elif start == 1:
        lintasan += "Kopang"
    elif start == 2:
        lintasan += "Pringgarata"
    elif start == 3:
        lintasan += "Batukliang"
    elif start == 4:
        lintasan += "Praya"

def kota_tengah(kolom):
    global lintasan
    if kolom == 0:
        lintasan+="Janapria-->"
    elif kolom == 1:
        lintasan+="Kopang-->"
    elif lintasan == 2:
        lintasan+="Pringgarata-->"
    elif kolom == 3:
        lintasan+="Batukliang-->"
    elif kolom == 4:
        lintasan+="Praya-->"

def hasil():
    cost_bbm = 1000
    pertamax = 4
    jmlh_pertamax = tsp3(lombok_tengah_route, start)[0]/pertamax
    total_biaya = tsp3(lombok_tengah_route, start)[0]/pertamax*cost_bbm
    print("="*108)
    print("||"+"Kesimpulan".center(104)+"||")
    print("="*108)
    print("||"+" Lintasan Terpendek : ", tsp3(lombok_tengah_route, start)[0], "km".ljust(74)+"||")
    print("||"+" Menghabiskan Pertamax : ", jmlh_pertamax, "liter".ljust(72)+"||")
    print("||"+" Total Biaya : ", total_biaya, "liter".ljust(68)+"||")
    for i in range(len(tsp3(lombok_tengah_route, start)[2])):
        print("||"+" Lintasan yang dilalui : ", tsp3(lombok_tengah_route,start)[2][i].ljust(77)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    input("Tekan enter untuk kembali")
    dashboard()

def detail():
    kota = ["Janapria", "Kopang", "Pringgarata", "Batukliang", "Praya"]
    menu_lombokTengah()
    input("Tekan untuk melihat route")
    print("="*108)
    print("||"+"Detail route".center(104)+"||")
    print("="*108)
    for i in range(len(lombok_tengah_route)):
        cost = str(kota[start])+"-->"+str(kota[i])+" = "+str(lombok_tengah_route[start][i])+" km"
        print("||"f' {cost}'.ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)

# lombok utara
def tsp4(lombok_utara_route, start):
    global lintasan
    tampung_point = []
    lintasan_tsp = []
    for point in range(len(lombok_utara_route)):
        if point != start:
            tampung_point.append(point)
    min_cost = 1000000
    tampung_permutasi = permutations(tampung_point)
    for permutasi in tampung_permutasi:
        kota_awal(start)
        lintasan+="-->"
        current_cost = 0
        baris = start
        for kolom in permutasi:
            kota_tengah(kolom)
            current_cost +=lombok_utara_route[baris][kolom]
            baris = kolom
        kota_awal(start)
        current_cost +=lombok_utara_route[baris][start]
        lintasa_copy = lintasan
        if current_cost == min_cost:
            lintasan_tsp.append(lintasa_copy)
        elif current_cost < min_cost:
            lintasan_tsp.clear()
            lintasan_tsp.append(lintasa_copy)
        min_cost = min(min_cost, current_cost)
        lintasan = ""
    return min_cost,lintasan, lintasan_tsp

def kota_awal(start):
    global lintasan
    if start == 0:
        lintasan += "Rumah"
    elif start == 1:
        lintasan += "Bayan"
    elif start == 2:
        lintasan += "Gangga"
    elif start == 3:
        lintasan += "Kayangan"
    elif start == 4:
        lintasan += "Pemenang"
    elif start == 5:
        lintasan += "Tanjung"

def kota_tengah(kolom):
    global lintasan
    if kolom == 0:
        lintasan+="Bayan-->" 
    elif kolom == 1:
        lintasan+="Gangga-->"
    elif lintasan == 2:
        lintasan+="Kayangan-->"
    elif kolom == 3:
        lintasan+="Pemenang-->"
    elif kolom == 4:
        lintasan+="Tanjung-->"
    elif kolom == 5:
        lintasan+="Rumah-->" 
        
def hasil():
    cost_bbm = 1000
    pertamax = 4
    jmlh_pertamax = tsp4(lombok_utara_route, start)[0]/pertamax
    total_biaya = tsp4(lombok_utara_route, start)[0]/pertamax*cost_bbm
    print("="*108)
    print("||"+"Kesimpulan".center(104)+"||")
    print("="*108)
    print("||"+" Lintasan Terpendek : ", tsp4(lombok_utara_route, start)[0], "km".ljust(74)+"||")
    print("||"+" Menghabiskan Pertamax : ", jmlh_pertamax, "liter".ljust(72)+"||")
    print("||"+" Total Biaya : ", total_biaya, "liter".ljust(68)+"||")
    for i in range(len(tsp4(lombok_utara_route, start)[2])):
        print("||"+" Lintasan yang dilalui : ", tsp4(lombok_utara_route,start)[2][i].ljust(77)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    input("Tekan enter untuk kembali")
    dashboard()

def detail():
    kota = ["Bayan", "Gangga", "Kayangan", "Pemenang", "PTanjung"]
    menu_lombokUtara()
    input("Tekan untuk melihat route")
    print("="*108)
    print("||"+"Detail route".center(104)+"||")
    print("="*108)
    for i in range(len(lombok_utara_route)):
        cost = str(kota[start])+"-->"+str(kota[i])+" = "+str(lombok_utara_route[start][i])+" km"
        print("||"f' {cost}'.ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)

# lombok barat
def tsp2(lombok_barat_route, start):
    global lintasan
    tampung_point = []
    lintasan_tsp = []
    for point in range(len(lombok_barat_route)):
        if point != start:
            tampung_point.append(point)
    min_cost = 1000000
    tampung_permutasi = permutations(tampung_point)
    for permutasi in tampung_permutasi:
        kota_awal(start)
        lintasan+="-->"
        current_cost = 0
        baris = start
        for kolom in permutasi:
            kota_tengah(kolom)
            current_cost += lombok_barat_route[baris][kolom]
            baris = kolom
        kota_awal(start)
        current_cost +=lombok_barat_route[baris][start]
        lintasa_copy = lintasan
        if current_cost == min_cost:
            lintasan_tsp.append(lintasa_copy)
        elif current_cost < min_cost:
            lintasan_tsp.clear()
            lintasan_tsp.append(lintasa_copy)
        min_cost = min(min_cost, current_cost)
        lintasan = ""
    return min_cost,lintasan, lintasan_tsp

def kota_awal(start):
    global lintasan
    if start == 0:
        lintasan += "Narmada"
    elif start == 1:
        lintasan += "Kediri"
    elif start == 2:
        lintasan += "Labuapi"
    elif start == 3:
        lintasan += "Gerung"
    elif start == 4:
        lintasan += "Lembar"

def kota_tengah(kolom):
    global lintasan
    if kolom == 0:
        lintasan+="Narmada-->"
    elif kolom == 1:
        lintasan+="Kediri-->"
    elif lintasan == 2:
        lintasan+="Labuapi-->"
    elif kolom == 3:
        lintasan+="Gerung-->"
    elif kolom == 4:
        lintasan+="Lembar-->"

def hasil():
    cost_bbm = 1000
    pertamax = 4
    jmlh_pertamax = tsp2(lombok_barat_route, start)[0]/pertamax
    total_biaya = tsp2(lombok_barat_route, start)[0]/pertamax*cost_bbm
    print("="*108)
    print("||"+"Kesimpulan".center(104)+"||")
    print("="*108)
    print("||"+" Lintasan Terpendek : ", tsp2(lombok_barat_route, start)[0], "km".ljust(74)+"||")
    print("||"+" Menghabiskan Pertamax : ", jmlh_pertamax, "liter".ljust(72)+"||")
    print("||"+" Total Biaya : ", total_biaya, "liter".ljust(68)+"||")
    for i in range(len(tsp2(lombok_barat_route, start)[2])):
        print("||"+" Lintasan yang dilalui : ", tsp2(lombok_barat_route,start)[2][i].ljust(77)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    input("Tekan enter untuk kembali")
    dashboard()

def detail():
    kota = ["Narmada", "Kediri", "Labuapi", "Gerung", "Lembar"]
    menu_lombokBarat()
    input("Tekan untuk melihat route")
    print("="*108)
    print("||"+"Detail route".center(104)+"||")
    print("="*108)
    for i in range(len(lombok_barat_route)):
        cost = str(kota[start])+"-->"+str(kota[i])+" = "+str(lombok_barat_route[start][i])+" km"
        print("||"f' {cost}'.ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)

# lombok timur
def tsp1(lombok_timur_route, start):
    global lintasan
    tampung_point = []
    lintasan_tsp = []
    for point in range(len(lombok_timur_route)):
        if point != start:
            tampung_point.append(point)
    min_cost = 1000000
    tampung_permutasi = permutations(tampung_point)
    for permutasi in tampung_permutasi:
        kota_awal(start)
        lintasan+="-->"
        current_cost = 0
        baris = start
        for kolom in permutasi:
            kota_tengah(kolom)
            current_cost += lombok_timur_route[baris][kolom]
            baris = kolom
        kota_awal(start)
        current_cost +=lombok_timur_route[baris][start]
        lintasa_copy = lintasan
        if current_cost == min_cost:
            lintasan_tsp.append(lintasa_copy)
        elif current_cost < min_cost:
            lintasan_tsp.clear()
            lintasan_tsp.append(lintasa_copy)
        min_cost = min(min_cost, current_cost)
        lintasan = ""
    return min_cost,lintasan, lintasan_tsp

def kota_awal(start):
    global lintasan
    if start == 0:
        lintasan += "Aikmel"
    elif start == 1:
        lintasan += "Jerowaru"
    elif start == 2:
        lintasan += "Keruak"
    elif start == 3:
        lintasan += "Labuhan haji"
    elif start == 4:
        lintasan += "Masbagik"

def kota_tengah(kolom):
    global lintasan
    if kolom == 0:
        lintasan+="Aikmel-->"
    elif kolom == 1:
        lintasan+="Jerowaru-->"
    elif lintasan == 2:
        lintasan+="Keruak-->"
    elif kolom == 3:
        lintasan+="Labuhan haji-->"
    elif kolom == 4:
        lintasan+="Masbagik-->"

def hasil():
    cost_bbm = 1000
    pertamax = 4
    jmlh_pertamax = tsp1(lombok_timur_route, start)[0]/pertamax
    total_biaya = tsp1(lombok_timur_route, start)[0]/pertamax*cost_bbm
    print("="*108)
    print("||"+"Kesimpulan".center(104)+"||")
    print("="*108)
    print("||"+" Lintasan Terpendek : ", tsp1(lombok_timur_route, start)[0], "km".ljust(74)+"||")
    print("||"+" Menghabiskan Pertamax : ", jmlh_pertamax, "liter".ljust(72)+"||")
    print("||"+" Total Biaya : ", total_biaya, "liter".ljust(68)+"||")
    for i in range(len(tsp1(lombok_timur_route, start)[2])):
        print("||"+" Lintasan yang dilalui : ", tsp1(lombok_timur_route,start)[2][i].ljust(77)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    input("Tekan enter untuk kembali")
    dashboard()

def detail():
    kota = ["Aikmel", "Jerowaru", "Keruak", "Labuhan haji", "Masbagik"]
    menu_lombokTimur()
    input("Tekan untuk melihat route")
    print("="*108)
    print("||"+"Detail route".center(104)+"||")
    print("="*108)
    for i in range(len(lombok_timur_route)):
        cost = str(kota[start])+"-->"+str(kota[i])+" = "+str(lombok_timur_route[start][i])+" km"
        print("||"f' {cost}'.ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)

# mataram
def tsp(mataram_route, start):
    global lintasan
    tampung_point = []
    lintasan_tsp = []
    for point in range(len(mataram_route)):
        if point != start:
            tampung_point.append(point)
    min_cost = 1000000
    tampung_permutasi = permutations(tampung_point)
    for permutasi in tampung_permutasi:
        kota_awal(start)
        lintasan+="-->"
        current_cost = 0
        baris = start
        for kolom in permutasi:
            kota_tengah(kolom)
            current_cost += mataram_route[baris][kolom]
            baris = kolom
        kota_awal(start)
        current_cost +=mataram_route[baris][start]
        lintasa_copy = lintasan
        if current_cost == min_cost:
            lintasan_tsp.append(lintasa_copy)
        elif current_cost < min_cost:
            lintasan_tsp.clear()
            lintasan_tsp.append(lintasa_copy)
        min_cost = min(min_cost, current_cost)
        lintasan = ""
    return min_cost,lintasan, lintasan_tsp

def kota_awal(start):
    global lintasan
    if start == 0:
        lintasan += "Selaparang"
    elif start == 1:
        lintasan += "Ampenan"
    elif start == 2:
        lintasan += "Sekarbela"
    elif start == 3:
        lintasan += "Sandubaya"
    elif start == 4:
        lintasan += "Cakranegara"

def kota_tengah(kolom):
    global lintasan
    if kolom == 0:
        lintasan+="Selaparang-->"
    elif kolom == 1:
        lintasan+="Ampenan-->"
    elif lintasan == 2:
        lintasan+="SEkarbela-->"
    elif kolom == 3:
        lintasan+="Sandubaya-->"
    elif kolom == 4:
        lintasan+="Cakranegara-->"

def hasil():
    cost_bbm = 1000
    pertamax = 4
    jmlh_pertamax = tsp(mataram_route, start)[0]/pertamax
    total_biaya = tsp(mataram_route, start)[0]/pertamax*cost_bbm
    print("="*108)
    print("||"+"Kesimpulan".center(104)+"||")
    print("="*108)
    print("||"+" Lintasan Terpendek : ", tsp(mataram_route, start)[0], "km".ljust(74)+"||")
    print("||"+" Menghabiskan Pertamax : ", jmlh_pertamax, "liter".ljust(72)+"||")
    print("||"+" Total Biaya : ", total_biaya, "liter".ljust(68)+"||")
    for i in range(len(tsp(mataram_route, start)[2])):
        print("||"+" Lintasan yang dilalui : ", tsp(mataram_route,start)[2][i].ljust(77)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    input("Tekan enter untuk kembali")
    dashboard()

def detail():
    kota = ["Selaparang", "Ampenan", "Sekarbela", "Sandubaya", "Sandubaya"]
    menu_kota_mataram()
    input("Tekan untuk melihat route")
    print("="*108)
    print("||"+"Detail route".center(104)+"||")
    print("="*108)
    for i in range(len(mataram_route)):
        cost = str(kota[start])+"-->"+str(kota[i])+" = "+str(mataram_route[start][i])+" km"
        print("||"f' {cost}'.ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)



def register():
    os.system("clear")
    errors = 0
    print("="*108)
    print("||"+"NinjaGo".center(104)+"||")
    print("="*108)
    username = input(" Usnername    :")
    password = input(" Password     :")
    if username.isalnum() == False or password.isalnum() == False:
        errors += 1
        print("Username atau password hanya berupa huruf dan angka saja")
    if len(username) < 5 or len(password) < 5:
        errors += 1
        print("Username atau password minimal terdiri dari 6 karakter")
    if username == password:
        errors = 1
        print("Username dan password tidak boleh sama")
    if errors == 0:
        data_salesman.append([username, password])
        with open("database.csv", "a", newline="") as css:
            write = csv.writer(css, delimiter=",")
            for t in data_salesman:
                write.writerow(t)
        print("Akun anda berhasil dibuat, silahkan login1")
    input("Tekan enter untuk kembali")
    main() 

def login():
    os.system("clear")
    print("="*108)
    print("||"+"Ninjago".center(104)+"||")
    print("="*108)
    nama = []
    sandi = []
    with open("database.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        try:
            for row in csv_reader:
                nama.append(row[0])
                sandi.append(row[1])
        except:
            pass
    username = input("Username :")
    password = input("Password :")
    if username in nama:
        index = nama.index(username)
        if password == sandi[index]:
            dashboard1()
        else:
            print("Password anda salah")
    else:
        print("Akun tidak ditemukan")
    input("Enter untuk kembali")
    main()
    

if __name__ == "__main__":
    main()





