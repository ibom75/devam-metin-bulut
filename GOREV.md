# GÖREV — DEVAM METİNLERİ (1.607 konu, 4.821 kayıt) · Claude Code bulut oturumu

Kaynak: `GrokBot_GOREV_devam_metin_t160\GOREV.md` (26.09.2026). Kurallar **aynen**; yalnız yollar bu depoya
uyarlandı. Hazırlayan: Claude Code (Eğitim Seti oturumu), 28.09.2026.

> **AÇIK UYARI.** Bu üretim hiçbir kapıdan geçmeden ürüne girmez. Teslimden sonra metinler yerel
> `devam_grok` kapılarından geçirilir. Eşik gevşetilmez. Kapıdan kalan metin ürüne girmez.

## 1. Ne yapılacak
1. **Kapsam:** `girdi/` klasöründeki **1.607 konu**. Her konu için **3 devam videosu metni**, toplam **4.821 kayıt**.
2. **Bitmiş konular:** `bitti_konular.txt` dosyasındaki anahtarlar (satır başına bir anahtar) YAZILMAZ.
   Dosya şu an boş: ilk turun 47 konusu bu bilgisayarda bulunamadı; İbrahim ekleyecek.
3. **Sıra:** Önce **PİLOT**: `girdi/konular_01.jsonl`'in ilk **10** konusu (30 kayıt). Pilot kapı sonucu
   raporlanmadan tam koşuya geçilmez. Sonra parça parça, sınıf → gün sırası.

Girdi satırı: `{"anahtar": "s2_g1_haya", "sinif": "2", "ders": "Hayat Bilgisi", "konu": "...", "ana_metin": "..."}`

## 2. Devam videosu nedir
Çocuk ana anlatımı izledi. Devam videosu farklı anlatım DEĞİL; konuyu **pekiştiren**, ~3 dk yeni video.
| tur | ad | içerik |
|---|---|---|
| `d1` | alıştırma | sayma, eşleme, sözlü cevap |
| `d2` | günlük hayat | evde, mutfakta, sokakta, bahçede karşılığı |
| `d3` | kısa tekrar | ne öğrendik, adım adım tekrar, pekiştirme soruları |

## 3. Biçim — biri bozulursa kayıt ürüne girmez
- Her kayıtta **tam 6 sahne**; her sahnede **tam 4 cümle**; her cümle **12–20 sözcük**.
- Her sahne **en az 45 sözcük**; 6 sahne toplam **en az 800 hece** (sesli harf sayısı).
- Her sahne gerçek bilgi taşır. Aynı cümle iki kez yok; iki sahne aynı sözcüklerle yazılmaz (ortak içerik sözcüğü %60'tan az).
- Konu başlığındaki anahtar sözcüklerden **en az 2'si** metinde geçer (ilk 5 harf).
- Yasak: emoji, başlık, madde işareti, yıldız, köşeli/süslü parantez.
- Yıl, tarih, ölçü, istatistik **uydurma**. Türkçe harfleri doğru kullan: ç ğ ı ö ş ü İ.
- 6–11 yaş çocuğa sıcak, sade dil.
- **DK1 dolgu:** şu sözcüklerle BAŞLAYAN cümle dolgu sayılır: `haydi, hadi, şimdi sıra sende, aferin, bravo,
  harika, çok güzel, devam et, başla, dinle, dikkat, hazır mısın, sen de yapabilirsin, kolay değil mi,
  birlikte bakalım, göster, söyle bana`. Dolgu oranı %20'ye ulaşırsa kayıt kalır. İkiden az içerik sözcüklü cümle de dolgudur.

## 4. Çıktı şeması
Parça başına bir JSONL: `cikti/devam_metin_bulut_NN.jsonl` (pilot: `cikti/devam_metin_bulut_pilot.jsonl`).
Alanlar YALNIZ: `anahtar` (birebir), `tur` (`d1`/`d2`/`d3`), `konu` (birebir), `sahne` (6 metin).
`kalite` ve `sebep` YAZILMAZ. UTF-8, `\n`, `ensure_ascii` kapalı. Örnek: `ornek/ornek_cikti.jsonl`.

## 5. Kendi kontrol — her parçadan sonra
```
python kendi_kontrol.py cikti/devam_metin_bulut_pilot.jsonl girdi/konular_01.jsonl
```
Son satır: `gecen N · kalan N · eksik N`. Kalan kaydı düzelt. Pilotta `eksik` sayısı ilk 10 konu dışındakileri
de sayar; pilot için yalnız ilk 10 konunun 30 kaydını raporla.
Not: bu kopyada DK3 ölçüm hatası düzeltildi (2–3 harfli konu sözcükleri ve büyük İ; `araclar/dk3_sinama.py`,
942/942 geçmiş kayıt aynı sonuç). Tek sözcüklü 6 konu (`Besinlerimiz`, `Biyoçeşitlilik`) DK3'ü yapısal olarak
sağlayamaz: bunları yaz ama kalanlar listesinde ayrıca belirt.

## 6. Teslim
`TESLIM.md`: parça başına bir satır — `parça | konu | yazılan kayıt | gecen / kalan / eksik | not`.
Kısmi teslim kabul; bitmeyen parça "eksik" yazılır.
