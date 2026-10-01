# Devam metni envanteri (01.10.2026 gece) — tek yer

Betik: `Araclar\e264\devam_envanter_e270.py`. Her kayıt **gerçek kapıdan** geçirildi (`devam_kalite_kapi`, eşik aynı).
Birleşik dosya: `birlesik/devam_birlesik.jsonl` — her (anahtar, tür) için geçen tek kayıt, `kaynak` alanıyla.
Öncelik: bulut > yerel > grok. **Ürüne yazılmadı** (ürüne alma zincir B kapandıktan sonra).

| Kaynak | Nerede | Konu | Kayıt | Gerçek kapı | Kaynak içi çift |
|---|---|---|---|---|---|
| Claude bulut oturumları | `cikti/devam_metin_bulut_*.jsonl` (+pilot, pilot10) | 412 | 1.236 | **1.236 / 1.236** | 0 |
| Claude normal oturum (alt ajan) | `cikti/devam_metin_yerel_*.jsonl` (+pilot01) | 190 | 570 | **570 / 570** | 0 |
| Grok Build (E-264, `devam_grok.py`, 1.286 oturum ≈ 17,8 saat) | `Araclar\e264\devam_metin_e264.jsonl` | 314 (1. sınıf 178 · 2. sınıf 136) | 942 | **942 / 942** | 0 |
| E-263 eski pilot | `Araclar\e263\devam_metin.jsonl` | 3 | 9 | 0 / 9 (emojili eski biçim) | 0 |
| Yarım (bitmiş sayılmaz) | `yerel_yarim/` | 90 | 270 | 243 / 270 | 0 |

- **Kaynaklar arası çift kayıt:** 9 — hepsi E-263 pilotu ile Grok Build arasında (aynı 3 konu); birleşikte Grok kaydı alındı. Bulut / yerel / Grok arasında çift **0**.
- **Birleşik:** 2.748 kayıt = **916 konu** (üç türü tam): bulut 1.236 · yerel 570 · grok 942.
- **Girdi listesi (1.607 konu, 2.–5. sınıf):** Grok Build'in bitirdiklerinden sonra kalanlarla kuruldu; Grok'un 314 konusu girdide yok, çakışma yok.
- **GERÇEKTEN KALAN:** **960 konu** (yerel iş listesi; 90'ı `yerel_yarim/`'de yarım) **+ 45 konu GrokBot ilk turu** (`konular_01` satır 3–47, `s2_g51`–`s2_g67`; Pazar alınacak, bu işin dışında).
