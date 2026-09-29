# TAM KOŞU — bulut oturumu görevi (E-270, 29.09.2026 akşam · SON TUR)

Bu depoda GOREV.md'yi oku ve kurallarına AYNEN uy. Eşikleri ve kendi_kontrol.py'yi değiştirme.
(kendi_kontrol.py 29.09'da gerçek kapıyla eşitlendi: DK5 sapkalı harfleri saymaz.)

**SON TUR (İbrahim kararı 29.09 akşam):** hesapta ~17 USD var; bu tur ~2 USD kalana kadar kullanılır
(önceki "bakiye 15 USD'nin üstünde olmalı" sınırı İbrahim'in kararıyla ~2 USD'ye indirildi).
Hedef ≈ 100 konu / 300 kayıt = 5 parça. Tur YARIM KONU BIRAKMADAN temiz durur (madde 3).

0. HER PARÇADAN ÖNCE: `git fetch origin master && git merge origin/master` (önceki oturumların çıktısı ana dala
   birleştirilir). TESLIM.md'deki EN SON "OTURUM SONU: ... sıradaki <anahtar>" satırından devam et.
   cikti/ altında herhangi bir dosyada kaydı olan konuyu TEKRAR YAZMA.

1. SIRA: TESLIM.md'deki "sıradaki" konudan başla (29.09 akşam itibarıyla **girdi/konular_04.jsonl satır 58,
   s3_g10_mate**), dosya bitince konular_05.jsonl, konular_06.jsonl ... sırayla.
   ATLA: bitti_konular.txt'deki anahtarlar, konular_01 satır 1–57 (1–2 ve 48–57 pilotlarda yapıldı;
   3–47 ilk turda başka yerde yapılmış VARSAYILIYOR — üretme).
   Başka çıktılarda (cikti/*.jsonl) zaten GEÇMİŞ kaydı olan konuyu tekrar yazma.

2. PARÇA: her parça 20 konu (60 kayıt) -> cikti/devam_metin_bulut_NN.jsonl (NN: var olan numarayı ezme,
   sıradaki boş numarayı al; bu turda ilk parça 16). Her parçada:
   a) yaz, b) python kendi_kontrol.py cikti/devam_metin_bulut_NN.jsonl girdi/<o parçanın konular_XX.jsonl dosyası>
      (parça iki girdi dosyasına bölünüyorsa her dosya için ayrı koş),
   c) kalanları düzelt, en çok 2 kez yeniden koş,
   d) TESLIM.md'ye bir satır: parça no, konu aralığı, geçen / kalan / eksik (yalnız o parçanın 60 kaydı), saat,
   e) HEMEN commit + push. Push etmeden sonraki parçaya GEÇME (oturum kapanırsa push edilmemiş iş kaybolur).

3. DUR — TEMİZ BİTİŞ: bu oturumda EN ÇOK 5 PARÇA (100 konu).
   - Bir konunun üç kaydı (d1, d2, d3) BİRLİKTE yazılır; konu yarım bırakılmaz.
   - Bir parça başladıysa 20 konusu bitirilip kontrol edilir ve push edilir; parça ortasında durulmaz.
   - Kullanım/kota uyarısı gelirse YENİ PARÇA BAŞLATMA: elindeki parçayı bitir, push et, OTURUM SONU yaz.
   - Son push'tan sonra TESLIM.md'ye "OTURUM SONU: son konu <anahtar>, sıradaki <anahtar>" yaz, push et ve DUR.

4. Bir parçada kalan 2 düzeltme koşusundan sonra da KALDI ise o kayıtları TESLIM.md'ye "KALDI" diye yaz,
   kapıyı değiştirme, sonraki parçaya geç.

5. Hiçbir çıktıyı başka depoya yazma; yalnız bu depodaki cikti/ ve TESLIM.md.
