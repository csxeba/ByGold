# -*- coding: cp1250 -*-
## Csin�lunk egy kv�zprogit
#1. k�rd�s
def valaszBekeres(megoldas):
    global jo
    v=raw_input ('>>> ')
    while v not in ['a','A','b','B','c','C']: v = raw_input('>>> ')
    if v.lower() == megoldas:
        print 'J� a v�lasz!'
        jo=jo+1

jo=0
print "Cs�vez�s. Egy kv�zprogicsk�ba cs�ppent�'. Egyszer �rta."
print 'Els� k�rd�s:'
print 'Folytasd a sorozatot: hogyhogyhogy, perszemee, nemhanem...'
print 'A: ... ilyenolyan'
print 'B: ... j�deakk�'
print 'C: ... megtemeg'
valaszBekeres('b')
print 'next kuestion'
print 'Mi Eszter m�v�szneve?'
print 'A: Egyszer'
print 'B: Molly Collie'
print 'C: M. C. Once'
valaszBekeres('c')
print 'K�vi k�rdi'
print 'Folytasd a dalt!\nSzeg�ny asszony vagyok...'
print 'A: ... j�rok, mint gavall�r.'
print 'B: ... nem k�sz�n�k vissza, tov�bbmendeg�l�k.'
print 'C: ... fogyat�kkal �l�k.'
valaszBekeres('c')
print 'K�verny�kova k�rdimeglonella'
print 'Mi Eszter irom�ny�nak c�me?'
print 'A: �da els� Ny�l anyacs�sz�rn�h�z'
print 'B: Ima els� Ny�l anyacs�sz�rn�h�z'
print 'C: �da els� Ny�l anyakir�lyn�h�z'
valaszBekeres('a')
print 'Utcsi k�rdcsi'
print 'Hogy k�sz�n el Csabi amikor felmegy aludni?'
print 'A: Joj'
print 'B: Jazig'
print 'C: Heil'
valaszBekeres('b')
print "�rdemjegyed G�rol�gi�b�l:", jo
a = ['Egy v�lasz sem j�...','EL�GTELEN!!!','el�gs�ges...',
 'k�zepes...','j�...','jeles!'][jo]
print a
