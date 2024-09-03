# Meteologica Data Analysis Automation 🛰️

Bu proje, Meteologica xtraders platformuna otomatik olarak giriş yapmayı, belirli analiz seçeneklerini seçmeyi, veri analiz raporu oluşturmayı ve bu raporu CSV dosyası olarak indirip proje dizinine kaydetmeyi amaçlar. 
Python ve Selenium kullanarak dinamik veri alma süreçlerini otomatikleştirdim.

## İçindekiler 🚀
- İş Problemi
- Araçlar ve Teknolojiler
- Ön Gereksinimler
- Kurulum
- Yapılandırma
- Kullanım

### İş Problemi

Meteologica platformunda manuel olarak yapılan veri analizleri için gereken tüm adımların otomatik hale getirilmesi. 
Bu adımlar arasında platforma giriş, veri analiz raporlarının oluşturulması, CSV dosyası olarak indirilmesi ve bu dosyaların proje dizinine kaydedilmesi yer alır.

### Araçlar ve Teknolojiler

- Python 3.x: Projenin temel programlama dili.
- Selenium: Web tarayıcı otomasyonu için kullanılır.
- Chrome WebDriver: Google Chrome tarayıcısı ile otomasyon sağlar.
- Datetime: Tarih ve zaman işlemleri için kullanılır.
- Shutil: Dosya işlemleri için kullanılır.

### Ön Gereksinimler
Bu projeye başlamadan önce aşağıdaki araçların kurulu olması gerekiyor.

- Python 3.x
- Google Chrome ve Chrome WebDriver
- Gerekli Python Kütüphaneleri:
- selenium
- datetime
- shutil

### Sonuç

Bu proje, Meteologica xTraders platformunda manuel olarak gerçekleştirilen veri analiz sürecini otomatikleştirerek kullanıcıların zamandan tasarruf etmesini ve veri analiz süreçlerini daha verimli hale getirmesini sağlar. 
Bu otomasyon sayesinde:

- Hızlı ve Etkin Veri Toplama: Platformdaki analiz raporları otomatik olarak oluşturulup indirilebilir, böylece manuel veri toplama süreci ortadan kalkar.
- Dinamik Tarih Seçimi: Otomasyon, her çalıştırıldığında belirlenen tarih aralığında verileri toplar, böylece verilerin sürekli olarak güncel kalması sağlanır.
- Kolay Entegrasyon: İndirilen CSV dosyaları doğrudan proje dizinine kaydedilir ve gerektiğinde veritabanına aktarılabilir, bu da verilerin analiz edilmesi ve işlenmesi için kolay bir entegrasyon sunar.
- Geliştirilebilir Yapı: Proje, ihtiyaç duyulduğunda farklı veri kaynakları veya platformlarla da genişletilebilir.

