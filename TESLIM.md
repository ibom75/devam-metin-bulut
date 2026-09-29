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
