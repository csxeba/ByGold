# -*- coding: cp1250 -*-
valasz = ['Angelica archangelica', 'angelica archangelica',
          'Angelica Archangelica']
jovalasz=0
print 'Ez a program kik�rdezi �nt,tisztelt G�r Csabi. Sok szerencs�t!'
print 'Latin neveket kell mondania!'
print 'Angyalgy�k�r?'
a = raw_input ('>>> ')
if a in valasz:
    print 'Rendben van.'
    jovalasz=jovalasz+1
else:
    print 'Sajnos nem j� a v�lasz!'

valasz1 = ['Anthemis nobilis', 'anthemis nobilis', 'Anthemis Nobilis']
print 'K�vetkez� k�rd�s:'
print 'R�mai kamilla (r�mai sz�kf�)?'
a = raw_input ('>>> ')
if a in valasz1:
    print 'Gratul�lok!'
    jovalasz=jovalasz+1
else:
    print 'Nem j� a k�rd�sre a v�lasz!'

valasz2 = ['Artemisia absinthium', 'artemisia absinthium', 'Arthemisia Absinthium']
print 'K�vetkez� k�rd�s:'
print 'Feh�r �r�m?'
a = raw_input ('>>> ')
if a in valasz2:
    print 'Gratul�lok!'
    jovalasz=jovalasz+1
else:
    print 'Nem j� a k�rd�sre a v�lasz!'

valasz3 = ['Atropa belladonna', 'atropa belladonna', 'Atropa Belladonna']
print 'K�vetkez� k�rd�s:'
print 'Nadragulya?'
a = raw_input ('>>> ')
if a in valasz3:
    print 'Gratul�lok!'
    jovalasz=jovalasz+1
else:
    print 'Nem j� a k�rd�sre a v�lasz!'

valasz4 = ['Brassica nigra', 'brassica nigra', 'Brassica Nigra']
print 'K�vetkez� k�rd�s:'
print 'Fekete must�r?'
a = raw_input ('>>> ')
if a in valasz4:
    print 'Gratul�lok!'
    jovalasz=jovalasz+1
else:
    print 'Nem j� a k�rd�sre a v�lasz!'

valasz5 = ['Calendula officinalis', 'calendula officinalis', 'Calendula Officinalis']
print 'K�vetkez� k�rd�s:'
print 'K�r�mvir�g?'
a = raw_input ('>>> ')
if a in valasz5:
    print 'Gratul�lok!'
    jovalasz=jovalasz+1
else:
    print 'Nem j� a k�rd�sre a v�lasz!'

valasz6 = ['Capsicum annuum', 'capsicum annuum', 'Capsicum Annuum']
print 'K�vetkez� k�rd�s:'
print 'Paprika'
a = raw_input ('>>> ')
if a in valasz6:
    print 'Gratul�lok!'
    jovalasz=jovalasz+1
else:
    print 'Nem j� a k�rd�sre a v�lasz!'

valasz7 = ['Carum carvi', 'carum carvi', 'Carum Carvi']
print 'K�vetkez� k�rd�s:'
print 'Konyhak�m�ny?'
a = raw_input ('>>> ')
if a in valasz7:
    print 'Gratul�lok!'
    jovalasz=jovalasz+1
else:
    print 'Nem j� a k�rd�sre a v�lasz!'

valasz8 = ['Cichorium intybus', 'cichorium inthybus', 'Cichorium Inthybus']
print 'K�vetkez� k�rd�s:'
print 'Mezei kat�ng?'
a = raw_input ('>>> ')
if a in valasz8:
    print 'Gratul�lok!'
    jovalasz=jovalasz+1
else:
    print 'Nem j� a k�rd�sre a v�lasz!'

valasz9 = ['Cnicus benedictus', 'cnicus benedictus', 'Cnicus Benedictus']
print 'K�vetkez� k�rd�s:'
print '�ldott bog�ncs?'
a = raw_input ('>>> ')
if a in valasz9:
    print 'Gratul�lok!'
    jovalasz=jovalasz+1
else:
    print 'Nem j� a k�rd�sre a v�lasz!'
print 'J� v�laszaid sz�ma:' , jovalasz
