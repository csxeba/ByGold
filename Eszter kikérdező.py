# -*- coding: cp1250 -*-
valasz = ['Angelica archangelica', 'angelica archangelica',
          'Angelica Archangelica']
jovalasz=0
print 'Ez a program kikérdezi Önt,tisztelt Gór Csabi. Sok szerencsét!'
print 'Latin neveket kell mondania!'
print 'Angyalgyökér?'
a = raw_input ('>>> ')
if a in valasz:
    print 'Rendben van.'
    jovalasz=jovalasz+1
else:
    print 'Sajnos nem jó a válasz!'

valasz1 = ['Anthemis nobilis', 'anthemis nobilis', 'Anthemis Nobilis']
print 'Következő kérdés:'
print 'Római kamilla (római székfű)?'
a = raw_input ('>>> ')
if a in valasz1:
    print 'Gratulálok!'
    jovalasz=jovalasz+1
else:
    print 'Nem jó a kérdésre a válasz!'

valasz2 = ['Artemisia absinthium', 'artemisia absinthium', 'Arthemisia Absinthium']
print 'Következő kérdés:'
print 'Fehér üröm?'
a = raw_input ('>>> ')
if a in valasz2:
    print 'Gratulálok!'
    jovalasz=jovalasz+1
else:
    print 'Nem jó a kérdésre a válasz!'

valasz3 = ['Atropa belladonna', 'atropa belladonna', 'Atropa Belladonna']
print 'Következő kérdés:'
print 'Nadragulya?'
a = raw_input ('>>> ')
if a in valasz3:
    print 'Gratulálok!'
    jovalasz=jovalasz+1
else:
    print 'Nem jó a kérdésre a válasz!'

valasz4 = ['Brassica nigra', 'brassica nigra', 'Brassica Nigra']
print 'Következő kérdés:'
print 'Fekete mustár?'
a = raw_input ('>>> ')
if a in valasz4:
    print 'Gratulálok!'
    jovalasz=jovalasz+1
else:
    print 'Nem jó a kérdésre a válasz!'

valasz5 = ['Calendula officinalis', 'calendula officinalis', 'Calendula Officinalis']
print 'Következő kérdés:'
print 'Körömvirág?'
a = raw_input ('>>> ')
if a in valasz5:
    print 'Gratulálok!'
    jovalasz=jovalasz+1
else:
    print 'Nem jó a kérdésre a válasz!'

valasz6 = ['Capsicum annuum', 'capsicum annuum', 'Capsicum Annuum']
print 'Következő kérdés:'
print 'Paprika'
a = raw_input ('>>> ')
if a in valasz6:
    print 'Gratulálok!'
    jovalasz=jovalasz+1
else:
    print 'Nem jó a kérdésre a válasz!'

valasz7 = ['Carum carvi', 'carum carvi', 'Carum Carvi']
print 'Következő kérdés:'
print 'Konyhakömény?'
a = raw_input ('>>> ')
if a in valasz7:
    print 'Gratulálok!'
    jovalasz=jovalasz+1
else:
    print 'Nem jó a kérdésre a válasz!'

valasz8 = ['Cichorium intybus', 'cichorium inthybus', 'Cichorium Inthybus']
print 'Következő kérdés:'
print 'Mezei katáng?'
a = raw_input ('>>> ')
if a in valasz8:
    print 'Gratulálok!'
    jovalasz=jovalasz+1
else:
    print 'Nem jó a kérdésre a válasz!'

valasz9 = ['Cnicus benedictus', 'cnicus benedictus', 'Cnicus Benedictus']
print 'Következő kérdés:'
print 'Áldott bogáncs?'
a = raw_input ('>>> ')
if a in valasz9:
    print 'Gratulálok!'
    jovalasz=jovalasz+1
else:
    print 'Nem jó a kérdésre a válasz!'
print 'Jó válaszaid száma:' , jovalasz
