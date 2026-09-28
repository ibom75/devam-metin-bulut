# -*- coding: utf-8 -*-
"""DK3 duzeltmesi sinamasi (salt okuma).
1. Gercek kapidan GECMIS 942 kayit (araclar/sinama_gecmis_942.jsonl): eski ve yeni kendi_kontrol
   ayni sonucu vermeli (gecen -> gecen).
2. Girdideki 1.607 konu: eski kuralla DK3'u HIC saglanamayan (sayilan anahtar sozcuk < 2) konu
   sayisi, yenisiyle.
3. Bozuk kopya: gecmis bir kaydin konusu alakasiz sozcuklere cevrilir -> yeni betik DK3 KALDI vermeli.
Kullanim: python araclar/dk3_sinama.py"""
import glob
import importlib.util
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
K = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def yukle(ad, yol):
    s = importlib.util.spec_from_file_location(ad, yol)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


eski = yukle('eski', os.path.join(K, 'araclar', 'kendi_kontrol_eski.py'))
yeni = yukle('yeni', os.path.join(K, 'kendi_kontrol.py'))
kay = [json.loads(s) for s in io.open(os.path.join(K, 'araclar', 'sinama_gecmis_942.jsonl'), encoding='utf-8')
       if s.strip()]
esit = farkli = eski_gecen = yeni_gecen = 0
ornek = []
for k in kay:
    a, b = not eski.denetle(k, k.get('konu', '')), not yeni.denetle(k, k.get('konu', ''))
    eski_gecen += a
    yeni_gecen += b
    if a == b:
        esit += 1
    else:
        farkli += 1
        if len(ornek) < 5:
            ornek.append((k['anahtar'], k['tur'], a, b))
print('1) gecmis %d kayit: eski gecen %d · yeni gecen %d · ayni sonuc %d · farkli %d %s'
      % (len(kay), eski_gecen, yeni_gecen, esit, farkli, ornek))
konu = [json.loads(s) for f in sorted(glob.glob(os.path.join(K, 'girdi', '*.jsonl')))
        for s in io.open(f, encoding='utf-8') if s.strip()]


def say(m, t):
    return len([w for w in m.sozcukler(t) if (len(w) > 3 if m is eski else len(w) >= 2) and w not in m.ISLEV])


imk_e = [x['anahtar'] for x in konu if say(eski, x['konu']) < 2]
imk_y = [x['anahtar'] for x in konu if say(yeni, x['konu']) < 2]
kirik = [x['anahtar'] for x in konu if 'İ' in x['konu']]
print('2) girdi %d konu: DK3 saglanamaz (anahtar < 2) eski %d · yeni %d · İ iceren konu %d'
      % (len(konu), len(imk_e), len(imk_y), len(kirik)))
print('   eskide saglanamayan ornek:', [(x['anahtar'], x['konu']) for x in konu if x['anahtar'] in imk_e][:5])
print('   yenide hala saglanamayan:', [(x['anahtar'], x['konu']) for x in konu if x['anahtar'] in imk_y][:10])
g = next(k for k in kay if not yeni.denetle(k, k.get('konu', '')))
boz = dict(g)
boz['konu'] = 'Uzay gemisi ve deniz kaplumbağası'
s = yeni.denetle(boz, boz['konu'])
print('3) bozuk kopya (%s %s, konu alakasiz): %s' % (g['anahtar'], g['tur'],
                                                     'KALDI ' + str([x for x in s if 'DK3' in x]) if s else 'GECTI (HATA)'))
