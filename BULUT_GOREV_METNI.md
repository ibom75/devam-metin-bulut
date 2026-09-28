Bu depoda GOREV.md'yi oku ve kurallarına AYNEN uy. Eşikleri ve kendi_kontrol.py'yi değiştirme.

1. PİLOT: girdi/konular_01.jsonl'in ilk 10 konusu için d1, d2, d3 yaz (30 kayıt) → cikti/devam_metin_bulut_pilot.jsonl.
   bitti_konular.txt'deki anahtarları atla.
2. Çalıştır: python kendi_kontrol.py cikti/devam_metin_bulut_pilot.jsonl girdi/konular_01.jsonl
3. Kalan kayıtları düzelt, yeniden çalıştır. Pilot sonucunu SAYIYLA TESLIM.md'ye yaz (gecen / kalan / eksik,
   yalnız 10 konunun 30 kaydı için) ve dur. Tam koşuya İbrahim onay verince geç.
4. Tam koşuda parça parça ilerle (cikti/devam_metin_bulut_NN.jsonl), her parçadan sonra kendi_kontrol ve TESLIM.md satırı.
5. Hiçbir çıktıyı ana ürün deposuna yazma; yalnız bu depodaki cikti/ klasörü. Commit + push bu depoya.
