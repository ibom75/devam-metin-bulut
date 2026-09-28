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
