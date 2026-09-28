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
