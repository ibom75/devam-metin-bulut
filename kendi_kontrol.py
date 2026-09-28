# -*- coding: utf-8 -*-
"""Grok Bot icin KENDI KONTROL — yalniz bicim. Gercek kapi DEGILDIR.

Bu betik, Claude Code'un teslim alirken calistiracagi `devam_grok` kapilarinin
BIR KISMINI taklit eder (ayni esikler). Buradan gecmek URUNE GIRMEK demek
degildir; olgu ve altyazi kapilari burada yoktur. Buradan KALAN kayit ise
teslimde de kesin kalir: once burada duzelt.

Kullanim:  python kendi_kontrol.py cikti/devam_metin_grokbot_01.jsonl girdi/konular_01.jsonl
Yalniz Python standart kutuphanesi.
"""
import collections
import io
import json
import re
import sys

SESLI = set('aeıioöuüAEIİOÖUÜâîûÂÎÛ')
DOLGU = re.compile(
    r'^(haydi|hadi|simdi sira sende|şimdi sıra sende|aferin|bravo|harika|'
    r'cok guzel|çok güzel|devam et|basla|başla|dinle|dikkat|hazir misin|'
    r'hazır mısın|sen de yapabilirsin|kolay degil mi|kolay değil mi|'
    r'birlikte bakalim|birlikte bakalım|goster|göster|soyle bana|söyle bana)\b')
ISLEV = set("""ve ile bu su o bir birlikte icin gibi daha cok az ama fakat ancak hem ya
veya diye kadar sonra once simdi hep her bazi hangi nasil neden nicin evet hayir degil
var yok olur olmaz sen ben biz siz onlar senin benim bizim sizin onun soyle boyle iste
yani de da mi mi mu mu ki ne""".split())
EMOJI = re.compile(u'[\U0001F000-\U0001FAFF←-⇿☀-➿️]')


def tr_kucuk(m):
    """Turkce kucultme. Python 'İ'.lower() -> 'i' + birlesik nokta (U+0307) veriyor ve
    sozcuk bolucu 'İtme'yi 'i' + 'tme' diye kiriyordu (E-270 DK3 olcum hatasi)."""
    return (m or '').replace('İ', 'i').replace('I', 'ı').lower()


def sozcukler(m):
    return re.findall(r'[\wçğıöşüâîû]+', tr_kucuk(m))


def cumleler(m):
    return [c.strip() for c in re.split(r'(?<=[.!?])\s+', (m or '').strip()) if c.strip()]


def icerik(c):
    return [w for w in sozcukler(c) if len(w) > 2 and w not in ISLEV]


def denetle(k, konu):
    s = []
    sahne = [' '.join((x or '').split()) for x in (k.get('sahne') or [])]
    if len(sahne) != 6:
        s.append('sahne sayisi %d (6 olmali)' % len(sahne))
    tum = []
    for i, m in enumerate(sahne, 1):
        c = cumleler(m)
        tum += c
        if len(c) != 4:
            s.append('sahne %d: cumle %d (tam 4)' % (i, len(c)))
        for j, x in enumerate(c, 1):
            n = len(x.split())
            if not 12 <= n <= 20:
                s.append('sahne %d cumle %d: %d sozcuk (12-20)' % (i, j, n))
        if len(sozcukler(m)) < 45:
            s.append('sahne %d: %d sozcuk (en az 45)' % (i, len(sozcukler(m))))
        if EMOJI.search(m):
            s.append('sahne %d: emoji' % i)
        if re.search(r'\[|\]|\{|\}|TODO|XXX|lorem', m, re.I) or re.search(r'^\s*(#|\*|-|\d+\.)', m):
            s.append('sahne %d: yer tutucu / baslik / madde isareti' % i)
    dolgu = [c for c in tum if DOLGU.match(c.lower()) or len(icerik(c)) < 2]
    if tum and 100.0 * len(dolgu) / len(tum) >= 20.0:
        s.append('DK1 dolgu %%%.0f (<20): %s' % (100.0 * len(dolgu) / len(tum), dolgu[:2]))
    say = collections.Counter(c.lower().rstrip('.!?') for c in tum)
    if any(v > 1 for v in say.values()):
        s.append('DK2 ayni cumle iki kez')
    kume = [set(icerik(m)) for m in sahne]
    for a in range(len(kume)):
        for b in range(a + 1, len(kume)):
            if kume[a] and kume[b] and 100.0 * len(kume[a] & kume[b]) / min(len(kume[a]), len(kume[b])) >= 60:
                s.append('DK2 sahne %d ile %d cok benzer (>=%%60)' % (a + 1, b + 1))
    govde = set(w[:5] for w in sozcukler(' '.join(sahne)))
    # E-270 DK3 duzeltmesi: 2-3 harfli konu sozcukleri (Öz, Yaz, Hâl) sayilmiyordu (len > 3).
    # Esik (en az 2 anahtar sozcuk, ilk 5 harf) DEGISMEDI; yalniz sayilan sozcuk kumesi.
    anahtar = [w for w in sozcukler(konu) if len(w) >= 2 and w not in ISLEV]
    if len([w for w in anahtar if w[:5] in govde]) < 2:
        s.append('DK3 konu sozcukleri yetersiz: %s' % anahtar)
    hece = sum(1 for ch in ' '.join(sahne) if ch in SESLI)
    if hece < 800:
        s.append('DK5 hece %d (en az 800)' % hece)
    return s


def main():
    cikti, girdi = sys.argv[1], sys.argv[2]
    konular = {}
    for x in io.open(girdi, encoding='utf-8'):
        if x.strip():
            d = json.loads(x)
            konular[d['anahtar']] = d['konu']
    gorulen, kalan, gecen = set(), 0, 0
    for n, x in enumerate(io.open(cikti, encoding='utf-8'), 1):
        if not x.strip():
            continue
        try:
            k = json.loads(x)
        except ValueError:
            print('satir %d: JSON bozuk' % n)
            kalan += 1
            continue
        fazla = set(k) - {'anahtar', 'tur', 'konu', 'sahne'}
        s = []
        if fazla:
            s.append('fazla alan: %s' % sorted(fazla))
        if k.get('anahtar') not in konular:
            s.append('anahtar girdide yok')
        if k.get('tur') not in ('d1', 'd2', 'd3'):
            s.append('tur d1/d2/d3 degil')
        if k.get('konu') != konular.get(k.get('anahtar')):
            s.append('konu girdidekiyle birebir ayni degil')
        s += denetle(k, konular.get(k.get('anahtar'), ''))
        gorulen.add((k.get('anahtar'), k.get('tur')))
        if s:
            kalan += 1
            print('%s %s: %s' % (k.get('anahtar'), k.get('tur'), ' | '.join(s[:6])))
        else:
            gecen += 1
    eksik = [(a, t) for a in konular for t in ('d1', 'd2', 'd3') if (a, t) not in gorulen]
    print('\ngecen %d · kalan %d · eksik %d (beklenen %d kayit)'
          % (gecen, kalan, len(eksik), 3 * len(konular)))
    for a, t in eksik[:10]:
        print('  eksik: %s %s' % (a, t))
    return 0 if not kalan and not eksik else 1


if __name__ == '__main__':
    sys.exit(main())
