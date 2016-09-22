z = """Gur Mra bs Clguba, ol Lbqn

Orggre guna htyl, ornhgvshy vf.
Orggre gura vzcyvpvg, rkcyvpvg vf.
Orggre guna pbzcyrk, fvzcyr vf.
Orggre guna pbzcyvpngrq, pbzcyrk vf.
Orggre guna arfgrq, syng vf.
Orggre guna qrafr, fcnefr vf.
Pbhagf, ernqnovyvgl qbrf.
Fcrpvny rabhtu gb oernx gur ehyrf, fcrpvny pnfrf ner abg.
Ohg orngra ol cenpgvpnyvgl, chevgl vf.
Fvyragyl cnffrq, na reebe fubhyq arire or.
Hayrff rkcyvpvgyl, vf vg fvyraprq.
Va gur snpr bs nzovthvgl, gur grzcgngvba gb thrff, ershfr lbh zhfg.
Bar, cersrenoyl bayl bar, jnl gb qb vg, gurer fubhyq or.
Abg boivbhf, vg zvtug or.
Orggre guna arire, abj vf.
Ohg bsgra orggre guna evtug abj, arire vf.
Vs uneq gb rkcynva, onq vg vf.
Vs rnfl gb rkcynva, tbbq vg znl or.
Anzrfcnprf ner n ubaxvat tbbq vqrn - zber bs gurz jr fubhyq qb!"""

d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i + c)] = chr((i + 13) % 26 + c)

print("".join([d.get(c, c) for c in z]))
