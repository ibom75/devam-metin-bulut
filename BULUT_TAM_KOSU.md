# TAM KOŞU — bulut oturumu görevi (E-270, 29.09.2026)

Bu depoda GOREV.md'yi oku ve kurallarına AYNEN uy. Eşikleri ve kendi_kontrol.py'yi değiştirme.
(kendi_kontrol.py 29.09'da gerçek kapıyla eşitlendi: DK5 sapkalı harfleri saymaz.)

0. ÖNCE: cikti/devam_metin_bulut_pilot10.jsonl içindeki s2_g69_haya d1 kaydı DK5'ten kalıyor (hece 797 < 800).
   Yalnız o kaydı uzat, kendi_kontrol ile 30/30 yap, commit + push.

1. SIRA: girdi/konular_01.jsonl 58. satırdan başla, dosya bitince konular_02.jsonl, konular_03.jsonl ... sırayla.
   ATLA: bitti_konular.txt'deki anahtarlar, konular_01 satır 1–57 (1–2 ve 48–57 pilotlarda yapıldı;
   3–47 ilk turda başka yerde yapılmış VARSAYILIYOR — üretme).
   Başka çıktılarda (cikti/*.jsonl) zaten GEÇMİŞ kaydı olan konuyu tekrar yazma.

2. PARÇA: her parça 20 konu (60 kayıt) -> cikti/devam_metin_bulut_NN.jsonl (NN = 01, 02, ...; var olan numarayı ezme,
   sıradaki boş numarayı al). Her parçada:
   a) yaz, b) python kendi_kontrol.py cikti/devam_metin_bulut_NN.jsonl girdi/<o parçanın konular_XX.jsonl dosyası>
      (parça iki girdi dosyasına bölünüyorsa her dosya için ayrı koş),
   c) kalanları düzelt, en çok 2 kez yeniden koş,
   d) TESLIM.md'ye bir satır: parça no, konu aralığı, geçen / kalan / eksik (yalnız o parçanın 60 kaydı), saat,
   e) HEMEN commit + push. Push etmeden sonraki parçaya GEÇME (oturum kapanırsa push edilmemiş iş kaybolur).

3. DUR: bu oturumda EN ÇOK 5 PARÇA (100 konu). 5. parçanın push'undan sonra TESLIM.md'ye
   "OTURUM SONU: son konu <anahtar>, sıradaki <anahtar>" yaz, push et ve DUR.
   (İbrahim yeni oturum açıp aynı metni verir; yeni oturum TESLIM.md'deki "sıradaki" konudan devam eder.)

4. Bir parçada kalan 2 düzeltme koşusundan sonra da KALDI ise o kayıtları TESLIM.md'ye "KALDI" diye yaz,
   kapıyı değiştirme, sonraki parçaya geç.

5. Hiçbir çıktıyı başka depoya yazma; yalnız bu depodaki cikti/ ve TESLIM.md.
