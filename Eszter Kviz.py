# -*- coding: cp1250 -*-
## Csinálunk egy kvízprogit
#1. kérdés
def valaszBekeres(megoldas):
    global jo
    v=raw_input ('>>> ')
    while v not in ['a','A','b','B','c','C']: v = raw_input('>>> ')
    if v.lower() == megoldas:
        print 'Jó a válasz!'
        jo=jo+1

jo=0
print "Csövezés. Egy kvízprogicskába csöppenté'. Egyszer írta."
print 'Első kérdés:'
print 'Folytasd a sorozatot: hogyhogyhogy, perszemee, nemhanem...'
print 'A: ... ilyenolyan'
print 'B: ... jódeakkó'
print 'C: ... megtemeg'
valaszBekeres('b')
print 'next kuestion'
print 'Mi Eszter művészneve?'
print 'A: Egyszer'
print 'B: Molly Collie'
print 'C: M. C. Once'
valaszBekeres('c')
print 'Kövi kérdi'
print 'Folytasd a dalt!\nSzegény asszony vagyok...'
print 'A: ... járok, mint gavallér.'
print 'B: ... nem köszönök vissza, továbbmendegélök.'
print 'C: ... fogyatékkal élök.'
valaszBekeres('c')
print 'Kövernyákova kérdimeglonella'
print 'Mi Eszter irományának címe?'
print 'A: Óda első Nyúl anyacsászárnőhöz'
print 'B: Ima első Nyúl anyacsászárnőhöz'
print 'C: Óda első Nyúl anyakirálynőhöz'
valaszBekeres('a')
print 'Utcsi kérdcsi'
print 'Hogy köszön el Csabi amikor felmegy aludni?'
print 'A: Joj'
print 'B: Jazig'
print 'C: Heil'
valaszBekeres('b')
print "Érdemjegyed Górológiából:", jo
a = ['Egy válasz sem jó...','ELÉGTELEN!!!','elégséges...',
 'közepes...','jó...','jeles!'][jo]
print a
