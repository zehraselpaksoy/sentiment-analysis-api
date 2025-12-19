# Sentiment Analysis API 🐼

Bu proje, FastAPI kullanılarak geliştirilmiş bir web uygulamasıdır ve temel amacı metinlerin duygu analizini yapmaktır. Uygulama, kullanıcıdan aldığı metni inceleyerek **pozitif, negatif veya nötr** olarak sınıflandırır. 

Mevcut sürümde, analiz **kelime listesi tabanlı** çalışmaktadır: İngilizce ve Türkçe için ayrı pozitif ve negatif kelime setleri tanımlanmıştır. Girilen metin, önce küçük harflere çevrilir ve kelime kelime kontrol edilir; pozitif kelime bulunursa puan artırılır, negatif kelime bulunursa puan azaltılır. Sonuçta pozitif, negatif veya nötr bir duygu belirlenir.

Projede ayrıca **istatistik takibi** mevcuttur. Her analiz sonucunda toplam kaç analiz yapıldığı ve her bir duygu kategorisinin kaç kez alındığı güncellenir. `/stats` endpoint’i ile bu istatistikler JSON formatında görüntülenebilir.

Web arayüzü sayesinde kullanıcılar metni doğrudan tarayıcı üzerinden girebilir ve anında sonuçları görebilir. Analiz sonuçları puan ile birlikte gösterilir ve kullanıcı hangi kelimelerin metni pozitif veya negatif etkilediğini görebilir.

Bu proje, basit bir kelime tabanlı analiz mantığını kullanmasına rağmen, ileride daha gelişmiş sistemlere entegre edilebilecek şekilde tasarlanmıştır. Örneğin:

- Transformers tabanlı modeller eklenerek çok dilli ve bağlam anlayan duygu analizi yapılabilir  
- Negasyon, bağlam, cümle yapısı ve emoji analizi eklenerek doğruluk artırılabilir  
- Web arayüzü modern bir frontend framework ile iyileştirilebilir  

Bu yapısıyla proje hem öğrenme amaçlı bir örnek teşkil eder hem de temel bir duygu analizi API’si olarak çalışabilir.
