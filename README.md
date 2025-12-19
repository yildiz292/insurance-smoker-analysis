 Insurance Smoker Analysis

Bu projede, sağlık sigortası maliyetlerini etkileyen faktörler analiz edilmiştir.  
Çalışmanın ana odağı sigara kullanımının  sigorta harcamaları üzerindeki etkisini ortaya koymaktır.

İstatistiksel testler ve doğrusal regresyon modelleri kullanılarak hangi değişkenlerin maliyetleri ne ölçüde etkilediği incelenmiştir.

 Veri Seti

- Kaynak: Insurance veri seti (CSV)
- Gözlem Sayısı: Bireysel sigorta kayıtları

### Değişkenler


Değişken  Açıklama 
age Sigortalının yaşı 
sex_binary  Cinsiyet (erkek=1, kadın=0) 
 bmi  Vücut Kitle İndeksi 
 num_children Çocuk sayısı 
 smoker_binary  Sigara kullanımı (evet=1, hayır=0) 
region  Yaşanılan bölge 
 insurance_charges Sağlık sigortası harcaması 

---

Veri Ön İşleme

- Eksik veriler kontrol edildi
- Tekrar eden kayıtlar temizlendi
- Kategorik değişkenler sayısal formata dönüştürüldü
- Bölge değişkeni için One-Hot Encoding uygulandı
- Modelleme için veri uygun hale getirildi

---



### Yapılan Analizler

- Cinsiyete göre ortalama sigorta harcamaları
- Sigara içen ve içmeyenlerin maliyet karşılaştırması
- Bölgelere göre maliyet farkları (ANOVA)
- Normal dağılım testi (Shapiro-Wilk)
- Yaş, BMI ve harcama arasındaki korelasyon analizi

### Kullanılan Grafikler

- Bar grafikleri
- Histogram ve KDE
- Boxplot
- Korelasyon ısı haritası
- Scatter plot

---

## İstatistiksel Testler

- **Bağımsız Örneklem t-Testi**
  - Sigara içenler vs içmeyenler
  - Kadın ve erkek maliyet karşılaştırması
- **ANOVA**
  - Bölgelere göre sigorta harcama farkları

Tüm testlerde anlamlılık düzeyi **0.05** olarak alınmıştır.

---

## Modelleme

### Doğrusal Regresyon Modelleri

1. **Tek Değişkenli Model**
   - Yaş → Sigorta Harcaması

2. **Çok Değişkenli Model**
   - Yaş
   - BMI
   - Sigara Kullanımı

3. **Gelişmiş Model**
   - Yaş, BMI, sigara, çocuk sayısı ve bölge değişkenleri

---

## Model Sonuçları

- Yaş ve BMI sigorta maliyetlerini artırmaktadır
- **Sigara kullanımı**, maliyetler üzerinde açık ara en güçlü etkendir
- Sigara içen bireylerin yıllık sigorta maliyeti, içmeyenlere göre yaklaşık **24.000$** daha fazladır
- Çok değişkenli model, tek değişkenli modele göre çok daha yüksek açıklayıcılığa sahiptir (R²)

---

## Sonuç

Bu çalışma, sigara kullanımının sağlık sigortası maliyetlerini ciddi biçimde artırdığını göstermektedir.  
Elde edilen sonuçlar, sigorta şirketlerinin **risk bazlı fiyatlandırma**, **sigara bırakma teşvikleri** ve **önleyici sağlık politikaları** geliştirmesi için önemli içgörüler sunmaktadır.

---

## Kullanılan Teknolojiler

- Python
- Pandas
- NumPy
- Seaborn
- Matplotlib
- SciPy
- Scikit-learn

---

## Proje Amacı

Bu proje, veri analizi, istatistiksel testler ve regresyon modelleme becerilerini göstermek amacıyla hazırlanmıştır.
