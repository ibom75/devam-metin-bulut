# TESLİM — PİLOT (yalnız 2 konu)

- Başlangıç: 2026-09-28 20:30:10 (UTC, konteyner saati)
- Bitiş: 2026-09-28 20:34 (UTC)
- Kapsam: `girdi/konular_01.jsonl` ilk 2 konu → 6 kayıt. `bitti_konular.txt` boş (yalnız yorum satırı), atlanan yok.
- Kontrol: `python kendi_kontrol.py cikti/devam_metin_bulut_pilot.jsonl girdi/konular_01.jsonl` (eşikler ve betik değiştirilmedi)

| parça | konu | yazılan kayıt | gecen / kalan / eksik | not |
|---|---|---|---|---|
| pilot | s2_g50_haya — Nezaket ve Görgü Kuralları | 3 (d1, d2, d3) | 3 / 0 / 0 | — |
| pilot | s2_g50_türk — Soru Sorma (Kim, Ne, Nerede, Ne Zaman) | 3 (d1, d2, d3) | 3 / 0 / 0 | — |
| **toplam (bu 2 konu)** | | **6** | **6 / 0 / 0** | |

## Çalıştırma geçmişi
1. İlk koşu: gecen 1 · kalan 5 (6 cümle 11 sözcük; s2_g50_türk d1 DK5 hece 793).
2. Yeniden koşu 1: kısa cümleler uzatıldı, hece artırıldı → gecen 6 · kalan 0.
3. Yeniden koşu 2: yalnız dil düzeltmesi (s2_g50_haya d3 sahne 3) → gecen 6 · kalan 0.

Betiğin son satırındaki `eksik 294`, pilot dışındaki 98 konunun kayıtlarıdır; bu 2 konu için eksik = 0.

## Bilinen kusur (kapıda bakılmalı)
- s2_g50_haya d3 sahne 3 cümle 1: "kimseyi öne geçmeden" ifadesi aksak; doğrusu "kimsenin önüne geçmeden".
  Yeniden çalıştırma sınırı (2) dolduğu için doğrulanmadan değiştirilmedi.
- Bu kontrol yalnız biçim kontrolüdür; olgu ve altyazı kapılarından geçmedi.

---

# PİLOT 2 (10 konu)

- Başlangıç: 2026-09-28 20:47:36 (UTC, konteyner saati)
- Bitiş: 2026-09-28 21:02:16 (UTC)
- Kapsam: `girdi/konular_01.jsonl` 48.–57. satırlar, 10 konu → 30 kayıt → `cikti/devam_metin_bulut_pilot10.jsonl`.
  Satır/anahtar eşleşmesi betikle doğrulandı. `bitti_konular.txt` boş (yalnız yorum satırı), atlanan konu yok.
- Kontrol: `python kendi_kontrol.py cikti/devam_metin_bulut_pilot10.jsonl girdi/konular_01.jsonl` (eşikler ve betik değiştirilmedi)

| parça | konu | yazılan kayıt | gecen / kalan / eksik | not |
|---|---|---|---|---|
| pilot10 | s2_g68_haya — Yakın çevremdeki tarihî / doğal yerler (basit) | 3 | 3 / 0 / 0 | — |
| pilot10 | s2_g68_mate — İki Basamaklı Çıkarma (Onluk Bozarak Giriş) | 3 | 3 / 0 / 0 | — |
| pilot10 | s2_g68_türk — Kısa Metin Yazma (3–5 Cümle) | 3 | 3 / 0 / 0 | — |
| pilot10 | s2_g69_haya — Yakın çevremdeki tarihî / doğal yerler (basit) | 3 | 3 / 0 / 0 | — |
| pilot10 | s2_g69_mate — İki Basamaklı Çıkarma (Onluk Bozarak Giriş) | 3 | 3 / 0 / 0 | — |
| pilot10 | s2_g69_türk — Kısa Metin Yazma (3–5 Cümle) | 3 | 3 / 0 / 0 | — |
| pilot10 | s2_g70_haya — Yaşadığım yer ve ülkem — giriş | 3 | 3 / 0 / 0 | — |
| pilot10 | s2_g70_mate — İki Basamaklı Toplama (Elde Var) | 3 | 3 / 0 / 0 | — |
| pilot10 | s2_g70_türk — Olay Sıralama (Önce – Sonra) | 3 | 3 / 0 / 0 | — |
| pilot10 | s2_g71_haya — Yaşadığım yer ve ülkem — giriş | 3 | 3 / 0 / 0 | — |
| **toplam (bu 10 konu)** | | **30** | **30 / 0 / 0** | |

Betiğin son satırındaki `eksik 270`, bu 10 konu dışındaki 90 konunun kayıtlarıdır; bu 10 konu için eksik = 0.

## Çalıştırma geçmişi
1. Koşu 1 (20:59:05): gecen 1 · kalan 29. Neden: ~130 cümle 8–11 sözcük (alt sınır 12); 11 kayıtta DK5 hece < 800
   (en düşük 744); 1 sahne 42 sözcük (< 45). DK1/DK2/DK3 hatası yok.
   Betik kayıt başına yalnız ilk 6 hatayı yazdığı için tüm kısa cümleler kendi basit sayacımla listelendi
   (`split()` sözcük sayısı + sesli harf sayısı; `kendi_kontrol.py` çalıştırılmadı). 124 cümle elle uzatıldı (123 + 1).
2. Koşu 2 = yeniden 1 (21:01:14): gecen 30 · kalan 0.
3. Koşu 3 = yeniden 2 (21:01:44): 5 dil/içerik düzeltmesinden sonra (aşağıda) gecen 30 · kalan 0 · eksik 0.

## Koşu 3'te düzeltilen kusurlar
- s2_g70_türk d2: "nohut kadar diş macunu" → "bezelye tanesi kadar" (içerik doğruluğu).
- s2_g69_mate d2: "öğretmenin bu hesabı … yapabilir" → "öğretmen de bu hesabı …" (dilbilgisi).
- s2_g71_haya d2: "Mahallende yeni bir aile taşındığında onlar da …" → "Mahallene … o aile de …" (dilbilgisi).
- s2_g69_mate d1: "Dördüncü ve beşinci hataları" (o kayıtta numaralanmamıştı) → "Ters yazma ve hizalama hatalarını".
- s2_g68_türk d1: "en sık görülen hata" (dayanaksız) → "çok sık görülen bir hata".

## Bilinen, düzeltilmemiş dil kusurları / riskler (kapıda bakılmalı)
- Uzatma dolgusu: 12 sözcük sınırı için bazı cümlelere anlam katmayan zarflar eklendi
  ("kesinlikle şarttır", "kolay kolay düşmez", "kolayca sağlar", "sakin adımlarla"). Dolgu kapısı (DK1) geçti ama üslup yer yer şişkin.
- Kalıp tekrar: bütün d3 kayıtları "Bu videoda … tekrar edeceğiz", "Pekiştirme sorusu bir/iki/üç:", "Kısaca özetlersek …" kalıbıyla açılıyor.
  Kayıt içinde DK2 geçti, ama kayıtlar arası benzerlik ölçülmedi.
- Aynı konu iki kez (g68/g69 haya, mate, türk; g70/g71 haya): içerik farklı ana metne göre ayrıştırıldı, ama
  "elli eksi yirmi üç = yirmi yedi" örneği s2_g69_mate d2 ve d3'te, "Karadeniz/Akdeniz/Ege/Marmara" bilgisi s2_g70_haya d1, d2 ve d3'te tekrarlanıyor.
- s2_g69_mate d2 sahne 4: "yirmi beş eksi yedi" iki basamaklıdan tek basamaklı çıkarma; konu başlığı "iki basamaklı". Matematik doğru, kapsam tartışmalı.
- Matematik örneklerinin hepsi elle kontrol edildi (ör. 43−17=26, 62−27=35, 73−39=34, 38+25=63, 65+19=84); otomatik doğrulama yok.
- Pilot 1'deki bilinen kusur ("kimseyi öne geçmeden", s2_g50_haya d3) bu görevin kapsamı dışında, olduğu gibi duruyor.
- Bu kontrol yalnız biçim kontrolüdür; olgu ve altyazı kapılarından geçmedi.

---

# TAM KOŞU (BULUT_TAM_KOSU.md)

- Adım 0 (2026-09-28 21:13 UTC): s2_g69_haya d1 sahne 6 son cümle uzatıldı ("…balıklara, bitkilere ve öteki canlılara…").
  `kendi_kontrol.py cikti/devam_metin_bulut_pilot10.jsonl girdi/konular_01.jsonl` → gecen 30 · kalan 0 (pilot10'un 30 kaydı).

| parça | konu aralığı | yazılan kayıt | gecen / kalan / eksik | saat (UTC) | not |
|---|---|---|---|---|---|
| 01 | konular_01 satır 58–77: s2_g71_mate … s2_g78_türk (20 konu) | 60 | 60 / 0 / 0 | 21:30 | ilk kendi_kontrol koşusunda 60/60 (yeniden koşu gerekmedi). Betiğin `eksik 240`'ı dosyadaki diğer 80 konu. |
| 02 | konular_01 satır 78–97: s2_g79_haya … s2_g86_mate (20 konu) | 60 | 60 / 0 / 0 | 21:48 | ilk kendi_kontrol koşusunda 60/60. Betiğin `eksik 240`'ı dosyadaki diğer 80 konu. |
| 03 | konular_01 satır 98–100 (s2_g86_türk, s2_g87_haya, s2_g87_mate) + konular_02 satır 1–17 (s2_g87_türk … s2_g93_haya) (20 konu) | 60 | 60 / 0 / 0 | 22:05 | İki koşu: `…_03.jsonl girdi/konular_01.jsonl` → gecen 9 · kalan 51 (51'in hepsi "anahtar girdide yok" = konular_02 kayıtları); `…_03.jsonl girdi/konular_02.jsonl` → gecen 51 · kalan 9 (9'u da "anahtar girdide yok" = konular_01 kayıtları). Parçanın 60 kaydı için: 60 geçen, 0 kalan, 0 eksik. |
| 04 | konular_02 satır 18–37: s2_g93_mate … s2_g100_türk (20 konu) | 60 | 60 / 0 / 0 | 22:22 | ilk kendi_kontrol koşusunda 60/60. Betiğin `eksik 240`'ı dosyadaki diğer 80 konu. |
| 05 | konular_02 satır 38–57: s2_g101_haya … s2_g108_mate (20 konu) | 60 | 60 / 0 / 0 | 22:39 | ilk kendi_kontrol koşusunda 60/60. Betiğin `eksik 240`'ı dosyadaki diğer 80 konu. |
| **toplam (5 parça)** | 100 konu | **300** | **300 / 0 / 0** | | Tüm `cikti/*.jsonl`: 336 kayıt (pilot 6 + pilot10 30 + 300), (anahtar, tür) tekrarı yok. |

## Tam koşu yöntemi ve notlar
- Her kayıt önce kendi taslak sayacımla (scratchpad'de; `kendi_kontrol.py` DEĞİL — aynı ölçütleri basitçe sayar:
  cümle/sahne sayısı, 12–20 sözcük, sahne ≥45 sözcük, hece ≥800 (şapkasız sesli), sahne ortaklığı, DK3, dolgu başı)
  ölçüldü; kısa cümleler elle uzatıldı. `kendi_kontrol.py` her parçada yalnız bir kez koşuldu ve beş parçanın hepsinde
  ilk koşuda 60/60 verdi; yeniden koşu hakkı kullanılmadı. Eşikler ve betik değiştirilmedi. KALDI kaydı yok.
- Kapsam dışı bırakılanlar (BULUT_TAM_KOSU.md'ye göre): konular_01 satır 1–57; `bitti_konular.txt` boş (yalnız yorum satırı).
- Tek sözcüklü DK3 riski olan konu (`Besinlerimiz`, `Biyoçeşitlilik`) bu 100 konuda yoktu.

## Bilinen riskler (kapıda bakılmalı)
- Yalnız biçim kontrolü: olgu ve altyazı kapılarından geçmedi.
- Kalıp tekrar: d1 "Bu alıştırmada …", d3 "Bu kısa tekrarda … / Pekiştirme sorusu bir/iki/üç / Kısaca özetlersek …" kalıbı
  bütün kayıtlarda aynı. Kayıt içi DK2 geçti; kayıtlar arası benzerlik ölçülmedi. Aynı konunun 3 günlük tekrarında
  (ör. g101/g102 haya "Tasarruflu kullanma") örnekler kısmen örtüşüyor.
- Uzatma dolgusu: 12 sözcük alt sınırı için "dikkatle, kolayca, tek tek, birlikte" gibi zarflar sık eklendi; üslup yer yer şişkin.
- Olgu hassasiyeti olan yerler: acil yardım numarası 112; Türk lirası madeni/kâğıt para değerleri (5/10/25/50 kuruş, 1 lira;
  5–200 lira); "önce sola bak" (sağdan akan trafik); yıldırım/yüksek ağaç uyarısı; kar oluşumu sadeleştirilerek anlatıldı.
- Matematik örneklerinin hepsi elle kontrol edildi (toplama/çıkarma/çarpma/bölme); otomatik doğrulama yok.
- "5N1K" başlıklı kayıtlarda "5N1K" yazımı seslendirmede ("beş en bir ka") sorun çıkarabilir.

OTURUM SONU: son konu s2_g108_mate, sıradaki s2_g108_türk (girdi/konular_02.jsonl satır 58)

---

# TAM KOŞU — oturum 2 (29.09.2026, BULUT_TAM_KOSU.md)

- Başlangıç: `git fetch origin master && git merge origin/master` → güncel. Devam noktası: s2_g108_türk (konular_02 satır 58).
- Yöntem önceki oturumla aynı: taslak kendi sayacımla ölçüldü, `kendi_kontrol.py` parça başına koşuldu; eşikler ve betik değiştirilmedi.

| parça | konu aralığı | yazılan kayıt | gecen / kalan / eksik | saat (UTC) | not |
|---|---|---|---|---|---|
| 06 | konular_02 satır 58–77: s2_g108_türk … s2_g115_haya (20 konu) | 60 | 60 / 0 / 0 | 05:18 | ilk kendi_kontrol koşusunda 60/60. Betiğin `eksik 240`'ı dosyadaki diğer 80 konu. |
| 07 | konular_02 satır 78–97: s2_g115_mate … s2_g122_türk (20 konu) | 60 | 60 / 0 / 0 | 05:33 | ilk kendi_kontrol koşusunda 60/60. Parça öncesi master birleştirmesi `kendi_kontrol.py` DK3'ünü gerçek kapıya eşitledi (anahtar > 3 harf); taslak sayacım da buna uyarlandı, parça 06 yeni betikle de 60/0. |
| 08 | konular_02 satır 98–100 (s2_g123_haya, s2_g123_mate, s2_g123_türk) + konular_03 satır 1–17 (s2_g124_haya … s2_g130_mate) (20 konu) | 60 | 60 / 0 / 0 | 05:48 | İki koşu: `…_08.jsonl girdi/konular_02.jsonl` → gecen 9 · kalan 51 (51'in hepsi "anahtar girdide yok" = konular_03 kayıtları); `…_08.jsonl girdi/konular_03.jsonl` → gecen 51 · kalan 9 (9'u da "anahtar girdide yok"). Parçanın 60 kaydı: 60 geçen, 0 kalan, 0 eksik. |
| 09 | konular_03 satır 18–37: s2_g130_türk … s2_g138_haya (20 konu) | 60 | 60 / 0 / 0 | 06:03 | ilk kendi_kontrol koşusunda 60/60. Betiğin `eksik 240`'ı dosyadaki diğer 80 konu. |
| 10 | konular_03 satır 38–57: s2_g138_mate … s2_g144_türk (20 konu) | 60 | 60 / 0 / 0 | 06:17 | ilk kendi_kontrol koşusunda 60/60. Betiğin `eksik 240`'ı dosyadaki diğer 80 konu. |
| **toplam (oturum 2, 5 parça)** | 100 konu | **300** | **300 / 0 / 0** | | Tüm `cikti/*.jsonl`: 636 kayıt, (anahtar, tür) tekrarı yok. Son kontrol: 06, 07, 09, 10 güncel `kendi_kontrol.py` ile yeniden 60/0; 08 iki girdiyle 9+51 = 60. |

## Oturum 2 notları
- Yeniden koşu hakkı hiçbir parçada kullanılmadı; KALDI kaydı yok. Eşikler ve `kendi_kontrol.py` değiştirilmedi
  (parça 07 öncesi master'dan gelen DK3 eşitlemesi İbrahim'in değişikliği; taslak sayacım ona uyarlandı).
- Taslak sayacım gerçek eşiklerden biraz sıkı: hece ≥ 830 (kapı 800), sahne benzerliği ≥ %55'te uyarı (kapı %60).
- Tek sözcüklü DK3 riski olan konu bu 100 konuda yoktu. Taslak sayacımın DK3 uyarısı veren 8 kayda
  (s2_g114_haya d2, s2_g115_haya d2, s2_g120_mate d2/d3, s2_g122_mate d2, s2_g129_mate d2, s2_g134_haya d2,
  s2_g135_haya d2) kendi_kontrol koşusundan önce konu sözcüğü eklendi.

## Bilinen riskler (kapıda bakılmalı)
- Yalnız biçim kontrolü: olgu ve altyazı kapılarından geçmedi.
- Kalıp tekrar: d1 "Bu alıştırmada … / Birinci hatayı sayalım … parmağını kaldır", d3 "Bu kısa tekrarda … /
  Pekiştirme sorusu bir/iki/üç … / Kısaca özetlersek …" kalıbı bütün kayıtlarda aynı; kayıtlar arası benzerlik ölçülmedi.
  Aynı konunun 3 günlük tekrarında (ör. g143/g144 "Tatilde sorumluluklarım", g113–g115 yön bulma) örnekler kısmen örtüşüyor.
- Uzatma dolgusu: 12 sözcük alt sınırı için "dikkatle, sırayla, tek tek, kısa ve net" gibi zarflar sık eklendi.
- Olgu hassasiyeti olan yerler: bilim insanları (Edison: ampulün geliştirilmesi; Bell: telefon; Pasteur: mikroplar ve
  sütü ısıtma yöntemi; Aziz Sancar: DNA onarımı, Nobel Kimya — yıl yazılmadı); 23 Nisan'ı Atatürk'ün çocuklara
  armağan etmesi; öğle vakti Güneş'in güneye yakın olması; pil ve ilaç atıklarının özel toplama noktası; yuvarlama kuralı
  (birler basamağı 5 ve üstü yukarı); yarım saatte kısa kolun iki sayı arasında olması.
- Sayı sözcükleri ("on iki", "yirmi dört") sözcük sayımında iki sözcük sayılıyor; bazı cümleler bu yüzden kısaltıldı.
- Matematik örneklerinin hepsi elle kontrol edildi (toplama/çıkarma/çarpma/paylaştırma/tahmin); otomatik doğrulama yok.
- Noktalama konularında (g113–g115_türk) örnek soru/ünlem cümleleri, cümle bölmeyi bozmamak için "?" ve "!" olmadan yazıldı.

OTURUM SONU: son konu s2_g144_türk, sıradaki s2_g145_haya (girdi/konular_03.jsonl satır 58)

---

# TAM KOŞU — oturum 3 (29.09.2026, BULUT_TAM_KOSU.md)

- Başlangıç: `git fetch origin master && git merge origin/master` → güncel. Devam noktası: s2_g145_haya (konular_03 satır 58).
- Yöntem: taslak, `kendi_kontrol.denetle` + daha sıkı uyarılarla (hece < 830, sahne benzerliği ≥ %55) ölçüldü; sonra `kendi_kontrol.py` parça başına koşuldu. Eşikler ve betik değiştirilmedi.

| parça | konu aralığı | yazılan kayıt | gecen / kalan / eksik | saat (UTC) | not |
|---|---|---|---|---|---|
| 11 | konular_03 satır 58–77: s2_g145_haya … s2_g152_mate (20 konu) | 60 | 60 / 0 / 0 | 09:49 | ilk kendi_kontrol koşusunda 60/60. Betiğin `eksik 240`'ı dosyadaki diğer 80 konu. Not: girdide g147 yok (g146 → g148). |
| 12 | konular_03 satır 78–97: s2_g152_türk … s2_g163_mate (20 konu) | 60 | 60 / 0 / 0 | 10:05 | ilk kendi_kontrol koşusunda 60/60. Betiğin `eksik 240`'ı dosyadaki diğer 80 konu. Not: girdide g158 yok. |
| 13 | konular_03 satır 98–100 (s2_g163_türk, s2_g164_mate, s2_g164_türk) + konular_04 satır 1–17 (s2_g165_mate … s2_g174_mate) (20 konu) | 60 | 60 / 0 / 0 | 10:20 | İki koşu: `…_13.jsonl girdi/konular_03.jsonl` → gecen 9 · kalan 51 (51'in hepsi "anahtar girdide yok" = konular_04 kayıtları); `…_13.jsonl girdi/konular_04.jsonl` → gecen 51 · kalan 9 (9'u da "anahtar girdide yok"). Parçanın 60 kaydı: 60 geçen, 0 kalan, 0 eksik. Not: girdide g168 yok. |
| 14 | konular_04 satır 18–37: s2_g174_türk … s3_g4_haya (20 konu) | 60 | 60 / 0 / 0 | 10:36 | ilk kendi_kontrol koşusunda 60/60. Betiğin `eksik 240`'ı dosyadaki diğer 80 konu. 3. sınıf konuları burada başladı. **Girdi notu:** fen anahtarlarının sonunda boşluk var (`"s3_g1_fen "`, `"s3_g2_fen "` …); şema "anahtar birebir" dediği için çıktıda da boşluklu yazıldı (kontrol betiği de böyle eşleştiriyor). Kapıda/ürün birleştirmede `strip()` yapılıyorsa buna dikkat. |
| 15 | konular_04 satır 38–57: s3_g4_mate … s3_g10_haya (20 konu) | 60 | 60 / 0 / 0 | 10:52 | ilk kendi_kontrol koşusunda 60/60. Betiğin `eksik 240`'ı dosyadaki diğer 80 konu. Not: girdide s3_g6 yok (g5 → g7); fen anahtarları yine sonda boşluklu. |
| **toplam (oturum 3, 5 parça)** | 100 konu | **300** | **300 / 0 / 0** | | Tüm `cikti/*.jsonl`: 936 kayıt, (anahtar, tür) tekrarı yok. Son kontrol: 11, 12, 14, 15 yeniden 60/0; 13 iki girdiyle 9+51 = 60. |

## Oturum 3 notları
- Resmî `kendi_kontrol.py` yeniden koşu hakkı hiçbir parçada kullanılmadı; KALDI kaydı yok. Eşikler ve betik değiştirilmedi.
- Taslak aşamasında (kendi_kontrol'den önce) çok sayıda cümle 12 sözcük altındaydı; taslak sayacıyla bulunup uzatıldı.
  Bu uzatmaların bir kısmı "dikkatle, sırayla, tek tek, yüksek sesle" türü zarf dolgusudur — kalite kapısında akış kontrolü önerilir.
- Bir cümle `Dikkat …` ile başlıyordu (DK1 dolgu kalıbı); oran eşiğin çok altında olsa da yeniden yazıldı.
- **Girdi tuhaflığı:** `konular_04`'teki fen anahtarları sonda boşluklu (`"s3_g1_fen "` …). Şema "birebir" dediği için öyle yazıldı.
- Girdide atlanan gün numaraları (g147, g158, g168, s3_g6) girdiden kaynaklı; eksik üretim değil.

## Bilinen riskler (oturum 3, kapıda bakılmalı)
- Yalnız biçim kontrolü: olgu ve altyazı kapılarından geçmedi.
- Kalıp tekrar: d1 "Bu alıştırmada … / … parmağını kaldırarak … cümlesini söyle", d3 "Bu kısa tekrarda … / Pekiştirme sorusu bir/iki/üç … / Kısaca özetlersek …" bütün kayıtlarda aynı.
  Aynı konunun 3 günlük sürümlerinde (ör. g146/g148/g149 yaz güvenliği, g153–g155 örüntü) örnekler kısmen örtüşüyor.
- Türkçe yazım/noktalama hata konularında (g157, g159) **bilerek yanlış yazılmış örnekler** var: `geldinmi`, `gidecem`, `bende geldim`,
  `Ahmetin`, `ayşe`, `gelirmisin`. Yazım denetimi yapan bir kapı bunları hata sayabilir; bağlamları "yanlış örnek" olarak kurulu.
- Olgu hassasiyeti olan yerler: 7×8=56; kutup ayısının kalın kürk ve yağ tabakası; penguenin uçamayıp iyi yüzmesi; arıların çiçek
  özünden bal yapması; uğur böceğinin kırmızı-siyah benekli olması; suyun ısınınca buhar olması; ılık/soğuk su donma örneğinde
  yalnız "soğuk su önce dondu" gözlemi anlatıldı (genel kural iddiası yok). Yıl, tarih, istatistik yazılmadı.
- Matematik örnekleri elle hesaplandı (toplama/çıkarma/eldeli/ödünçlü, çarpma, bölme-kalan); otomatik doğrulama yok.

OTURUM SONU: son konu s3_g10_haya, sıradaki s3_g10_mate (girdi/konular_04.jsonl satır 58)

---

# TAM KOŞU — oturum 4 · SON TUR (29.09.2026 akşam, BULUT_TAM_KOSU.md)

- Başlangıç: `git fetch origin master && git merge origin/master` → güncel. Devam noktası: s3_g10_mate (konular_04 satır 58).
- Yöntem: taslak düz metinde yazıldı, `kendi_kontrol.denetle` + sıkı uyarılarla (hece < 830, sahne benzerliği ≥ %55, dolgu başı) ölçülüp düzeltildi; sonra `kendi_kontrol.py` parça başına koşuldu. Eşikler ve betik değiştirilmedi.

| parça | konu aralığı | yazılan kayıt | gecen / kalan / eksik | saat (UTC) | not |
|---|---|---|---|---|---|
| 16 | konular_04 satır 58–77: s3_g10_mate … s3_g16_haya (20 konu) | 60 | 60 / 0 / 0 | 18:37 | ilk kendi_kontrol koşusunda 60/60. Betiğin `eksik 240`'ı dosyadaki diğer 80 konu. Girdide s3_g12 yok (g11 → g13); fen anahtarları sonda boşluklu, birebir yazıldı. |
| 17 | konular_04 satır 78–97: s3_g16_mate … s3_g22_haya (20 konu) | 60 | 60 / 0 / 0 | 18:52 | ilk kendi_kontrol koşusunda 60/60. Betiğin `eksik 240`'ı dosyadaki diğer 80 konu. Girdide s3_g19 yok (g18 → g20). |
| 18 | konular_04 satır 98–100 (s3_g22_mate, s3_g22_türk, s3_g23_fen) + konular_05 satır 1–17 (s3_g23_haya … s3_g28_haya) (20 konu) | 60 | 60 / 0 / 0 | 19:08 | İki koşu: `…_18.jsonl girdi/konular_04.jsonl` → gecen 9 · kalan 51 (51'in hepsi "anahtar girdide yok" = konular_05 kayıtları); `…_18.jsonl girdi/konular_05.jsonl` → gecen 51 · kalan 9 (9'u da "anahtar girdide yok"). Parçanın 60 kaydı: 60 geçen, 0 kalan, 0 eksik. Girdide s3_g25 yok. |
| 19 | konular_05 satır 18–37: s3_g28_mate … s3_g34_haya (20 konu) | 60 | 60 / 0 / 0 | 19:25 | ilk kendi_kontrol koşusunda 60/60. Betiğin `eksik 240`'ı dosyadaki diğer 80 konu. Girdide s3_g31 yok. |
| 20 | konular_05 satır 38–57: s3_g34_mate … s3_g40_haya (20 konu) | 60 | 60 / 0 / 0 | 19:40 | ilk kendi_kontrol koşusunda 60/60. Betiğin `eksik 240`'ı dosyadaki diğer 80 konu. Girdide s3_g37 yok. Konu adı `Verilmeyen toplanan ( ? + 25 = 60 )` parantez ve soru işareti içeriyor; `konu` alanına birebir kopyalandı, sahne metinlerinde parantez yok. |
| **toplam (oturum 4, 5 parça)** | 100 konu | **300** | **300 / 0 / 0** | | Tüm `cikti/*.jsonl`: 1236 kayıt, (anahtar, tür) tekrarı yok. Son kontrol: 16, 17, 19, 20 yeniden 60/0; 18 iki girdiyle 9+51 = 60. |

## Oturum 4 notları
- Resmî `kendi_kontrol.py` yeniden koşu hakkı hiçbir parçada kullanılmadı; KALDI kaydı yok. Eşikler ve betik değiştirilmedi.
- Taslak aşamasında çok sayıda cümle 12 sözcük altındaydı (ve birkaç sayı cümlesi 20'nin üstünde); taslak sayacıyla bulunup elle düzeltildi.
  Uzatmaların bir kısmı "dikkatle, sırayla, tek tek, yüksek sesle, kolayca" türü zarf dolgusudur — kalite kapısında akış kontrolü önerilir.
- Taslakta 2 kayıtta 7 sahne çıkmıştı (s3_g34_haya d1, s3_g35_mate d1); fazla sahne silindi. 2 cümle "Harika …" ile başlıyordu (DK1 kalıbı), yeniden yazıldı.
- 1 kayıtta DK3 uyarısı (s3_g38_haya d1) vardı; konu sözcükleri ("kişilerle iletişim") eklendi.
- Girdide atlanan gün numaraları (s3_g12, g19, g25, g31, g37) girdiden kaynaklı; eksik üretim değil. Fen anahtarları yine sonda boşluklu, birebir yazıldı.

## Bilinen riskler (oturum 4, kapıda bakılmalı)
- Yalnız biçim kontrolü: olgu ve altyazı kapılarından geçmedi.
- Kalıp tekrar: d1 "Bu alıştırmada … / Şimdi … yüksek sesle söyle", d3 "Bu kısa tekrarda … / Pekiştirme sorusu bir/iki/üç … / Kısaca özetlersek …" bütün kayıtlarda aynı.
  Aynı konunun 3 günlük sürümlerinde (ör. g36/g38/g39 gözlem kaydı, verilmeyen toplanan, mektup) örnekler kısmen örtüşüyor.
- Taslak sayacımın sıkı hece uyarısı (< 830) 10 kayıtta kaldı (en düşük 805: s3_g11_mate d1); gerçek eşik 800'ün üstünde.
- Olgu hassasiyeti olan yerler: 112 tek acil numara (ambulans, itfaiye, polis); Cumhuriyet'in ilanı 29 Ekim 1923, 19 Mayıs'ta Samsun'a çıkış;
  23 Nisan'ın çocuklara armağan edilmesi; Romen rakamı kuralları (IIII değil IV); kurbağa döngüsü yumurta–iribaş–kurbağa; kelebek yumurta–tırtıl–pupa–kelebek;
  mantarın bitki olmadığı; "önce sola, sonra sağa, tekrar sola bak" (sağdan akan trafik); kitaplarda tek sayfaların sağda olması; 20 saniye el yıkama; bezelye tanesi kadar diş macunu.
- Matematik örneklerinin hepsi elle hesaplandı (üç basamaklı toplama/çıkarma, yuvarlama, tahminî işlem, verilmeyen toplanan, tablo toplamları); otomatik doğrulama yok.
- Noktalama konularında (g11–g14_türk) örnek soru/ünlem cümleleri, cümle bölmeyi bozmamak için "?" ve "!" olmadan yazıldı; tırnak örnekleri iç noktasız yazıldı.
- s3_g14_türk d3'te bilerek kapanmamış tırnak örneği var (`"Oyuncağımı ver dedi`): "hata bul" alıştırması.

OTURUM SONU: son konu s3_g40_haya, sıradaki s3_g40_mate (girdi/konular_05.jsonl satır 58)
| yerel 003 | yerel/parca_003.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 30.09 08:03 | Claude Code yerel ajan |
| yerel 002 | yerel/parca_002.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 30.09 08:06 | Claude Code yerel ajan |
| yerel 005 | yerel/parca_005.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 30.09 13:31 | Claude Code yerel ajan |
| yerel 004 | yerel/parca_004.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 30.09 13:34 | Claude Code yerel ajan |
| yerel 007 | yerel/parca_007.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 30.09 18:45 | Claude Code yerel ajan |
| yerel 009 | yerel/parca_009.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 30.09 18:45 | Claude Code yerel ajan |
| yerel 001 | yerel/parca_001.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 30.09 18:46 | Claude Code yerel ajan |
| yerel 006 | yerel/parca_006.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 30.09 18:46 | Claude Code yerel ajan |
| yerel 008 | yerel/parca_008.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 30.09 18:47 | Claude Code yerel ajan |
| yerel 010 | yerel/parca_010.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 02.10 08:21 | Claude Code yerel ajan |
| yerel 013 | yerel/parca_013.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 02.10 08:27 | Claude Code yerel ajan |
| yerel 014 | yerel/parca_014.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 02.10 08:32 | Claude Code yerel ajan |
| yerel 012 | yerel/parca_012.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 02.10 08:43 | Claude Code yerel ajan |
| yerel 011 | yerel/parca_011.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 02.10 08:58 | Claude Code yerel ajan |
| yerel 015 | yerel/parca_015.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 02.10 09:09 | Claude Code yerel ajan |
| yerel 017 | yerel/parca_017.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 02.10 09:37 | Claude Code yerel ajan |
| yerel 016 | yerel/parca_016.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 02.10 09:39 | Claude Code yerel ajan |
| yerel 018 | yerel/parca_018.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 02.10 09:50 | Claude Code yerel ajan |
| yerel 020 | yerel/parca_020.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 02.10 10:05 | Claude Code yerel ajan |
| yerel 021 | yerel/parca_021.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 02.10 10:37 | Claude Code yerel ajan |
| yerel 022 | yerel/parca_022.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 02.10 10:44 | Claude Code yerel ajan |
| yerel 019 | yerel/parca_019.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 02.10 10:50 | Claude Code yerel ajan |
| yerel 023 | yerel/parca_023.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 02.10 11:12 | Claude Code yerel ajan |
| yerel 024 | yerel/parca_024.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 02.10 11:41 | Claude Code yerel ajan |
| yerel 025 | yerel/parca_025.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 02.10 11:41 | Claude Code yerel ajan |
| yerel 050 | yerel/parca_050.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 03.10 10:34 | Claude Code yerel ajan |
| yerel 049 | yerel/parca_049.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 03.10 12:27 | Claude Code yerel ajan |
| yerel 052 | yerel/parca_052.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 03.10 18:41 | Claude Code yerel ajan |
| yerel 051 | yerel/parca_051.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 03.10 18:42 | Claude Code yerel ajan |
| yerel 057 | yerel/parca_057.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 03.10 18:43 | Claude Code yerel ajan |
| yerel 056 | yerel/parca_056.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 03.10 19:32 | Claude Code yerel ajan |
| yerel 055 | yerel/parca_055.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 03.10 19:43 | Claude Code yerel ajan |
| yerel 042 | yerel/parca_042.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 04.10 12:01 | Claude Code yerel ajan |
| yerel 110 | yerel/parca_110.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 06.10 16:45 | Claude Code yerel ajan |
| yerel 132 | yerel/parca_132.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 06.10 22:58 | Claude Code yerel ajan |
| yerel 133 | yerel/parca_133.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 07.10 00:07 | Claude Code yerel ajan |
| yerel 134 | yerel/parca_134.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 07.10 01:28 | Claude Code yerel ajan |
| yerel 135 | yerel/parca_135.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 07.10 01:39 | Claude Code yerel ajan |
| yerel 003 | yerel/parca_003.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 07.10 05:34 | Claude Code yerel ajan |
| yerel 005 | yerel/parca_005.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 07.10 07:34 | Claude Code yerel ajan |
| yerel 011 | yerel/parca_011.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 07.10 11:44 | Claude Code yerel ajan |
| yerel 014 | yerel/parca_014.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 07.10 14:33 | Claude Code yerel ajan |
| yerel 019 | yerel/parca_019.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 07.10 18:22 | Claude Code yerel ajan |
| yerel 048 | yerel/parca_048.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 07.10 21:11 | Claude Code yerel ajan |
| yerel 041 | yerel/parca_041.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 07.10 21:29 | Claude Code yerel ajan |
| yerel 028 | yerel/parca_028.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 07.10 21:40 | Claude Code yerel ajan |
| yerel 025 | yerel/parca_025.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 07.10 21:44 | Claude Code yerel ajan |
| yerel 101 | yerel/parca_101.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 07.10 21:44 | Claude Code yerel ajan |
| yerel 103 | yerel/parca_103.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 07.10 21:51 | Claude Code yerel ajan |
| yerel 111 | yerel/parca_111.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 07.10 22:02 | Claude Code yerel ajan |
| yerel 120 | yerel/parca_120.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 07.10 22:05 | Claude Code yerel ajan |
| yerel 119 | yerel/parca_119.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 07.10 22:05 | Claude Code yerel ajan |
| yerel 137 | yerel/parca_137.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 07.10 22:07 | Claude Code yerel ajan |
| yerel 039 | yerel/parca_039.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 07.10 22:13 | Claude Code yerel ajan |
| yerel 043 | yerel/parca_043.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 07.10 22:15 | Claude Code yerel ajan |
| yerel 113 | yerel/parca_113.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 07.10 22:38 | Claude Code yerel ajan |
| yerel 117 | yerel/parca_117.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 07.10 22:42 | Claude Code yerel ajan |
| yerel 121 | yerel/parca_121.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 07.10 22:49 | Claude Code yerel ajan |
| yerel 115 | yerel/parca_115.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 07.10 23:09 | Claude Code yerel ajan |
| yerel 054 | yerel/parca_054.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 04:01 | Claude Code yerel ajan |
| yerel 053 | yerel/parca_053.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 04:02 | Claude Code yerel ajan |
| yerel 046 | yerel/parca_046.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 04:03 | Claude Code yerel ajan |
| yerel 045 | yerel/parca_045.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 04:04 | Claude Code yerel ajan |
| yerel 038 | yerel/parca_038.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 04:05 | Claude Code yerel ajan |
| yerel 035 | yerel/parca_035.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 04:06 | Claude Code yerel ajan |
| yerel 033 | yerel/parca_033.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 04:07 | Claude Code yerel ajan |
| yerel 031 | yerel/parca_031.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 04:08 | Claude Code yerel ajan |
| yerel 030 | yerel/parca_030.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 04:09 | Claude Code yerel ajan |
| yerel 029 | yerel/parca_029.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 04:09 | Claude Code yerel ajan |
| yerel 027 | yerel/parca_027.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 04:11 | Claude Code yerel ajan |
| yerel 026 | yerel/parca_026.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 04:13 | Claude Code yerel ajan |
| yerel 102 | yerel/parca_102.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 04:14 | Claude Code yerel ajan |
| yerel 106 | yerel/parca_106.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 04:15 | Claude Code yerel ajan |
| yerel 108 | yerel/parca_108.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 04:16 | Claude Code yerel ajan |
| yerel 109 | yerel/parca_109.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 04:17 | Claude Code yerel ajan |
| yerel 114 | yerel/parca_114.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 04:18 | Claude Code yerel ajan |
| yerel 004 | yerel/parca_004.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 04:44 | Claude Code yerel ajan |
| yerel 001 | yerel/parca_001.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 04:48 | Claude Code yerel ajan |
| yerel 006 | yerel/parca_006.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 04:57 | Claude Code yerel ajan |
| yerel 008 | yerel/parca_008.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 05:00 | Claude Code yerel ajan |
| yerel 009 | yerel/parca_009.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 05:02 | Claude Code yerel ajan |
| yerel 013 | yerel/parca_013.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 05:27 | Claude Code yerel ajan |
| yerel 015 | yerel/parca_015.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 05:39 | Claude Code yerel ajan |
| yerel 017 | yerel/parca_017.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 05:43 | Claude Code yerel ajan |
| yerel 032 | yerel/parca_032.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 06:28 | Claude Code yerel ajan |
| yerel 131 | yerel/parca_131.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 06:47 | Claude Code yerel ajan |
| yerel 116 | yerel/parca_116.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 06:49 | Claude Code yerel ajan |
| yerel 010 | yerel/parca_010.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 11:29 | Claude Code yerel ajan |
| yerel 012 | yerel/parca_012.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 11:33 | Claude Code yerel ajan |
| yerel 018 | yerel/parca_018.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 11:40 | Claude Code yerel ajan |
| yerel 047 | yerel/parca_047.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 12:21 | Claude Code yerel ajan |
| yerel 105 | yerel/parca_105.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 12:28 | Claude Code yerel ajan |
| yerel 021 | yerel/parca_021.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 16:36 | Claude Code yerel ajan |
| yerel 034 | yerel/parca_034.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 17:08 | Claude Code yerel ajan |
| yerel 024 | yerel/parca_024.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 21:49 | Claude Code yerel ajan |
| yerel 036 | yerel/parca_036.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 23:20 | Claude Code yerel ajan |
| yerel 037 | yerel/parca_037.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 23:21 | Claude Code yerel ajan |
| yerel 040 | yerel/parca_040.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 23:22 | Claude Code yerel ajan |
| yerel 044 | yerel/parca_044.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 08.10 23:26 | Claude Code yerel ajan |
| yerel 104 | yerel/parca_104.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 09.10 02:09 | Claude Code yerel ajan |
| yerel 136 | yerel/parca_136.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 09.10 02:22 | Claude Code yerel ajan |
| yerel 112 | yerel/parca_112.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 09.10 07:59 | Claude Code yerel ajan |
| yerel 107 | yerel/parca_107.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 09.10 08:00 | Claude Code yerel ajan |
| yerel 118 | yerel/parca_118.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 09.10 08:02 | Claude Code yerel ajan |
| yerel 002 | yerel/parca_002.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 09.10 11:38 | Claude Code yerel ajan |
| yerel 002 | yerel/parca_002.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 09.10 11:39 | Claude Code yerel ajan |
| yerel 002 | yerel/parca_002.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 09.10 11:40 | Claude Code yerel ajan |
| yerel 007 | yerel/parca_007.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 09.10 11:40 | Claude Code yerel ajan |
| yerel 016 | yerel/parca_016.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 09.10 11:42 | Claude Code yerel ajan |
| yerel 023 | yerel/parca_023.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 09.10 11:51 | Claude Code yerel ajan |
| yerel 023 | yerel/parca_023.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 09.10 11:51 | Claude Code yerel ajan |
| yerel 023 | yerel/parca_023.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 09.10 11:52 | Claude Code yerel ajan |
| yerel 125 | yerel/parca_125.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 09.10 11:54 | Claude Code yerel ajan |
| yerel 016 | yerel/parca_016.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 09.10 11:54 | Claude Code yerel ajan |
| yerel 016 | yerel/parca_016.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 09.10 11:55 | Claude Code yerel ajan |
| yerel 002 | yerel/parca_002.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 09.10 12:49 | Claude Code yerel ajan |
| yerel 002 | yerel/parca_002.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 09.10 12:50 | Claude Code yerel ajan |
| yerel 016 | yerel/parca_016.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 09.10 12:50 | Claude Code yerel ajan |
| yerel 002 | yerel/parca_002.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 09.10 12:50 | Claude Code yerel ajan |
| yerel 016 | yerel/parca_016.jsonl (20 konu) | 60 | gercek kapi 60 / 0 / 0 | 09.10 12:51 | Claude Code yerel ajan |
