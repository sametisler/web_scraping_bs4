import requests
from bs4 import BeautifulSoup
import pandas as pd



url = "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/Temel-Degerler-Ve-Oranlar.aspx?endeks=01#page-5"

parser = BeautifulSoup(requests.get(url).content, "html.parser")

veriler = []
tablo_id = "temelTBody_Finansal"
tablo = parser.find('tbody', {'id': tablo_id})

if tablo:
    satirlar = tablo.find_all("tr")
    for satir in satirlar:
        # Satırdaki hücreleri alıyoruz
        veri = satir.find_all("td")
        # Verilere erişim burada sağlanır
        bilgi1 = veri[0].text.strip() if len(veri) > 0 else None
        bilgi2 = veri[1].text.strip() if len(veri) > 1 else None
        bilgi3 = veri[2].text.strip() if len(veri) > 2 else None
        bilgi4 = veri[3].text.strip() if len(veri) > 3 else None
        bilgi5 = veri[4].text.strip() if len(veri) > 4 else None
        bilgi6 = veri[5].text.strip() if len(veri) > 5 else None
        bilgi7 = veri[6].text.strip() if len(veri) > 6 else None
        
        veriler.append([bilgi1, bilgi2, bilgi3, bilgi4, bilgi5, bilgi6, bilgi7])
        print(bilgi1, bilgi2, bilgi3, bilgi4, bilgi5, bilgi6, bilgi7)
        
    df = pd.DataFrame(veriler, columns = ["Kod","Kapanış (TL)","F/K","FD/FAVÖK","FD/Satışlar","PD/DD","Son Dönem"])
else:
    print("Tablo bulunamadı.")

print(df)