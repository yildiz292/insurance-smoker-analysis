import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


data= pd.read_csv("insurance.csv")
print(data.isnull().sum())

print(f"Tekrar eden veri sayısı {data.duplicated().sum()}")
print(data.drop_duplicates(inplace=True))

data['smoker'] = data['smoker'].map({'yes' : 1,'no':0})
data['sex'] = data['sex'].map({'male' : 1,'female':0})
print(data.head(3))

#KADIN VE ERKEK SAYILARINA GORE SİGORTA ORTALAMASI BURDA GÖRÜLDÜĞÜ ÜZERE ERKELERİN MASRAFI KADINLARDAN DAHA FAZLA AMA BURDA SORUN ERKEKLERİN MASRAFLI OLMASI DEĞİL ERKLERİN DAHA FAZLA 
#İÇMESİ VE ALTADA ERKEK VE KADINLARIN GRAFİGINI GORUYORUZ 

print(data.groupby('sex')['charges'].mean())
print(data.groupby(['sex', 'smoker']).size())

kadinlar = data[data['sex'] == 1]['charges']
erkekler = data[data['sex'] == 0]['charges']

p_degeri = stats.ttest_ind(kadinlar,erkekler)
print(f"kadın erkek p degeri :{p_degeri}")

sns.barplot(data=data,x="sex",y="charges")
plt.title("CİNSİYETE GÖRE MASRAF GRAFİĞİ")
plt.xticks([0,1],['kadın','erkek'])
plt.show()

#SİGARA HARCAMALARI NORMAL BİR DEGİLIMDA MI BUNU BURDA GORCEZ
sns.histplot(data['charges'],kde=True)
plt.show()
#Harcama verileri üzerinde yapılan Shapiro-Wilk testi sonucunda P-değeri 0.05'ten KÜÇÜK ÇIKMIŞTIR BUNUN SONUCUNDA SİGORTA MALİYETLERİ NORMAL DEGILMAMAKTADIR
deger=stats.shapiro(data['charges'])
print(f"Harcama degeri:{deger}")


#SİGARA İCENLER VE İÇMEYENLER ARASINDA MASRAF FARKI VAR MI
sigaraiçenler = data[data['smoker'] == 1]['charges']
sigaraiçmeyenler = data[data['smoker'] == 0]['charges']

sigaradegeri = stats.ttest_ind(sigaraiçenler,sigaraiçmeyenler)
print(f"SİGRA İÇENLERİN VE İÇMEYENLERİN MASRAF NORMALİ: {sigaradegeri}")
#BURDA SİGARA İÇENLERİN VE İÇMEYENLERİN GRAFIGUNU CİZDİK
sns.boxplot(x='smoker', y='charges', data=data)
plt.title('Sigara Kullanımına Göre Harcama Dağılımı ve Aykırı Değerler')
plt.show()
#BURDA SİGARA İÇENLERİN VE İÇMEYENLERİN KDE GRAFIGUNU CİZDİK
sns.kdeplot(data[data['smoker'] == 0]['charges'],fill=True,color='blue',label='sigara içmeyenler',alpha=0.5)
sns.kdeplot(data[data['smoker'] == 1]['charges'],fill=True,color='red',label='sigara içenler',alpha=0.5)
plt.title("SİGARA İÇEN VE İÇMEYENLERİN GRAFİĞİ")
plt.xlabel("HARCAMA TUTARI")
plt.ylabel("YOĞUNLUK")
plt.show()
#BLGELERE GORE MALIYETE BAKIYORUZ P-değeri 0.032 olarak hesaplanmıştır.  BURDA YASANILAN COGRAFİ BOLGE MALİYET UZERİNDE ETKİLİDİR BU YUZDEN SİRKET PİRİM FİYATLANDIRMASI YAPARKEN BOLGEYİ GOZONUNDE BULUNDURMALIDIR
#GUNEYDOGU DAHA COK
guneydogu = data[data['region'] == 'southwest']['charges']
guneybati = data[data['region'] == 'southeast']['charges']
kuzeydogu= data[data['region'] == 'northwest']['charges']
kuzeybati = data[data['region'] == 'northeast']['charges']

bolgedegeri = stats.f_oneway(guneydogu,guneybati,kuzeydogu,kuzeybati)
print(f"BOLGELERE SİGORTA HARCAMALARI: {bolgedegeri}")
# HANGİ BÖLGE DAHA PAHALI ONU BURDA GÖRÜYORUZ
print(data.groupby('region')['charges'].mean().sort_values(ascending=False))

#BURDA YAŞ,KİLO VE SAĞLIK MALİYETİ ÜZERİNDE BİR ISI HARİTASI GÖRÜYORUZ YAŞ ARTIKÇA SAĞLIK MALİYETİDE ARTIYOR AMA BU BÜYÜK BİR ARTIŞ DEĞİL,
# KİLO VE HARCAMA ARASINDA DA BÜYÜK BİR ETKİ KÜÇÜK YAS VE KİLO ARASINDA Kİ İLİŞKİDE ÇOK DÜŞÜK
sns.heatmap(data[['age','bmi','charges']].corr(),annot=True,cmap='Reds')
plt.title("YAŞ,KİLO VE  SAĞLIK MALİYETİNİN ARALARINDAKİ İLİŞKİ")
plt.show()
#ELDE EDİLEN 257 SAYISI YAS İLE SAGLIK HARCAMALARI ARASINDAKİ İLİŞKİNİN DOGRUSAL OLDUGUNU GOSTERMEKTEDİR YANİ HER YIL BİR YAS ARTIGINDA SİGORTA MALIYETİ 257 ARTMAKTADIR.
model=LinearRegression()
x=data[['age']]
y=data[['charges']]
model.fit(x,y)
artis_miktari = model.coef_[0]
print(f"ARTIS MİKTARI:{artis_miktari}")

#BURDA YAS VE SAGLIK MALİYETİ ARASINDAKİ İLİŞKİYİ GÖSTERDİK AMA GÖRÜNDÜĞÜ ÜZERE ARALARINDA %9 CİVARI İLİŞKİ VAR
# BURDAN CIKARDIĞIMIZ SONUÇ İSE YAŞ TEK BAŞINA SAĞLIK ÖAŞİYETLERİ ÜZERİNDE BÜYÜK BİR ETKİYE SAHİP DEĞİL

modelscoru= model.score(x,y)
print(f"MODEL SCORU {modelscoru * 100:.2f}")

#BURADA İSE YAŞ,KİLO VE SİGARANIN SAĞLIK MALİYETİ ÜZERİNDEKİ İLİŞKİYİ GÖRDÜK BURADA YAŞ VE KİLO ETKİLİ AMA SİGARA KADAR DEĞLİ SİGARA BURAYI BÜYÜK BİR ŞEKİLDE ETKİLİYOR
X = data[['age', 'bmi', 'smoker']] 
y = data['charges']
model.fit(X, y)

katsayilar = model.coef_
print(f"Yaş Katsayısı: {katsayilar[0]:.2f}")
print(f"BMI (Kilo) Katsayısı: {katsayilar[1]:.2f}")
print(f"Sigara Katsayısı: {katsayilar[2]:.2f}")
model_scoru = model.score(X, y)
print(f"YENİ MODEL SKORU (R2): %{model_scoru * 100:.2f}")

#BURADA SİGARA İÇEN VE İÇMEYENLER İÇİN GELECEĞE YÖNELİK BİR TAHMİN YAPTIK VE SİGARA İÇENLERİN İÇMEYENLERE GÖRE 24 BİN DAHA FAZLA HARCADIĞINI GÖRÜYORUZ
# BU BÜYÜK BİR FARK BURADAN GELECEGE YONELİK SİGARA BIRKAMA PAKETİ YA DA DAHA FARKLI ÖRNEKLERLE BIRAKMA YOLUNA GİDEBİLİRİZ AMAC GELECEKTE TASSARUFU SAĞLAMAK.
kisi_icmeyen = [[40, 28, 0]] 
kisi_icen = [[40, 28, 1]]    
tahmin_icmeyen = model.predict(kisi_icmeyen)
tahmin_icen = model.predict(kisi_icen)
print("---GELECEK TAHMİNİ---")
print(f"40 yaş, 28 BMI, SİGARA İÇMEYEN tahmini: {tahmin_icmeyen[0]:.2f} $")
print(f"40 yaş, 28 BMI, SİGARA İÇEN tahmini: {tahmin_icen[0]:.2f} $")

#KİLO TEK BAŞINA BİR YERE KADAR İDARE EDER AMA SİGARA İLE BİRLEŞİNCE MASRAFLAR FIRLIYOR.ÖZELLİKLE KİLOSU 30 DAN YUKSEK OLUNCA SAĞLIK SİGORTASININ CEMİNDEN CIKAN PARA ARTIYOR YANİ
sns.scatterplot(data = data, x="bmi",y="charges",hue="smoker")
plt.title("KİLOYA GORE SAGLIK HARCAMALARI")
plt.show()

# ÇOCUK SAYISINA GÖRE ORTALAMA HARCAMALAR
print("Çocuk Sayısına Göre Ortalama Masraf:")
print(data.groupby('children')['charges'].mean().sort_values())

#BURDA COCUK SAYISININ SİGORTA MALİYETİNE ETKİSİNİ GÖRÜYORUZ 2 VE 3 COCUKLU AİLELERİN SAĞLIK SİGORTA MALİYETİ DAHA YÜKSEK 
# AMA GENEL OLARAK BÜYÜK BİR FARK YOK YANİ ÇOCUK SAYISI  SİGORTA MALİYETİ ÜZERİNDE BUYUK BİR ETKİYE SAHİP DEĞİL
plt.figure(figsize=(10,6))
sns.barplot(x='children', y='charges', data=data,hue="children")
plt.title('Çocuk Sayısına Göre Ortalama Sigorta Masrafları', fontsize=15)
plt.show()



# --- DEĞİŞKEN ANALİZİ ---

data_final = pd.get_dummies(data, columns=['region'], drop_first=True)
X_final = data_final.drop('charges', axis=1)
y_final = data_final['charges']

X_train, X_test, y_train, y_test = train_test_split(X_final, y_final, test_size=0.2, random_state=42)
final_model = LinearRegression()
final_model.fit(X_train, y_train)

katsayi_df = pd.DataFrame(final_model.coef_, X_final.columns, columns=['Maliyet Etkisi ($)'])
print("\n--- DEĞİŞKENLERİN CÜZDANA ETKİSİ ---")
print(katsayi_df.sort_values(by='Maliyet Etkisi ($)', ascending=False))

print(f"\nModelin Gerçek Dünya Başarı Skoru: %{final_model.score(X_test, y_test)*100:.2f}")

#En Büyük Risk Sigara içmek, sağlık masraflarını tek başına yaklaşık 23.800 civarı  artırarak açık ara en büyük risk faktörü olmuştur
