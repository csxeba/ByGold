# -*- coding: cp1250 -*-

valaszlista = ['k', 'sz']
valaszlista2 = ['i', 'n']
valaszlista3 = ['sz', 'h']
valaszlista4 = ['p', 'k']
valaszlista5 = ['j', 'l']

flag = 'i'

while flag == 'i':
    print 'Szia, �n egy mesters�ges intelligencia vagyok (vagy mi a szar)'
    print 'Hogy vagy?'
    valasz = raw_input ('K�sz�n�m sz�pen j�l vagyok(k)/Szar� de b�szk�n!(sz) >>> ')
    
    if valasz == valaszlista [0]:
        print 'Az j�!'
        print 'Tal�lkozt�l Kati mam�val, hogy ilyen illedelmes j� gyerek m�dj�ra v�laszolsz?'
        valasz2 = raw_input ('Igen, t�le tanultam! (i)/Nem, nem ismerem �t. (n) >>> ')
        if valasz2 == valaszlista2 [0]:
            print 'Ennek �r�l�k! �n is t�le tanultam. Ismered Mollit?'
            valasz4 = raw_input ('Persze! A cukipofi az Arany J�nos utc�ban! Ki nem ismeri azt az �des pof�j�t?! (p)/Nem... ki az? (k) >>> ')
            if valasz4 == 'p':
                print '�n is ismerem az �desk�t!'
            elif valasz4 == 'k':
                print 'Nem gondoltam volna, hogy van olyan ember aki NEM ismeri...!'
            else:
                raw_input ('Persze! A cukipofi az Arany J�nos utc�ban!Ki nem ismeri azt az �des pof�j�t?!(p)/Nem... ki az? (k) >>> ')
        elif valasz2 == valaszlista2 [1]:
            print 'K�r... pedig �rdemes megismerni.'
        else:
            raw_input ('Igen, t�le tanultam! (i)', 'Nem, nem ismerem �t. (n)')
    elif valasz == valaszlista [1]:
        print 'H�t... vannak az embernek rossz napjai.'
        print 'Mi a baj?'
        valasz3 = raw_input ('Szarnom k�! (sz)/Haggy� m�! (h) >>> ') 
        if valasz3 == valaszlista3 [0]:
            print 'H�t menj el! Vagy m�g arra is lusta vagy?'
            valasz5 = raw_input ('Ja... (j)/ Lehets�ges, b�r nem tudom... (l) >>> ')
            if valasz5 == valaszlista5 [0]:
                print '�n erre nem lenn�k b�szke...'
            elif valasz5 == valaszlista5 [1]:
                print 'J� lenne, ha r�j�nn�l!'
            else:
                raw_input ('Ja... (j)/ Lehets�ges, b�r nem tudom... (l) >>> ')
        elif valasz3 == valaszlista3 [1]:
            print 'Rendben van! Szia!'
        else:
            raw_input ('Szarnom k�! (sz)/Haggy� m�! (h) >>> ') 
    else:
        raw_input ('K�sz�n�m sz�pen j�l vagyok(k)/Szar� de b�szk�n!(sz) >>> ')
        
    print 'M�g egy k�rt?'
    flag = raw_input('(i)gen/(n)em > ')
    flag = flag.lower()
    while flag not in ['i','n']:
        flag = raw_input('(i)gen/(n)em > ')
        flag = flag.lower()

