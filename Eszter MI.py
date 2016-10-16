# -*- coding: cp1250 -*-

valaszlista = ['k', 'sz']
valaszlista2 = ['i', 'n']
valaszlista3 = ['sz', 'h']
valaszlista4 = ['p', 'k']
valaszlista5 = ['j', 'l']

flag = 'i'

while flag == 'i':
    print 'Szia, én egy mesterséges intelligencia vagyok (vagy mi a szar)'
    print 'Hogy vagy?'
    valasz = raw_input ('Köszönöm szépen jól vagyok(k)/Szarú de büszkén!(sz) >>> ')
    
    if valasz == valaszlista [0]:
        print 'Az jó!'
        print 'Találkoztál Kati mamával, hogy ilyen illedelmes jó gyerek módjára válaszolsz?'
        valasz2 = raw_input ('Igen, tőle tanultam! (i)/Nem, nem ismerem Őt. (n) >>> ')
        if valasz2 == valaszlista2 [0]:
            print 'Ennek örülök! Én is tőle tanultam. Ismered Mollit?'
            valasz4 = raw_input ('Persze! A cukipofi az Arany János utcában! Ki nem ismeri azt az édes pofáját?! (p)/Nem... ki az? (k) >>> ')
            if valasz4 == 'p':
                print 'Én is ismerem az édeskét!'
            elif valasz4 == 'k':
                print 'Nem gondoltam volna, hogy van olyan ember aki NEM ismeri...!'
            else:
                raw_input ('Persze! A cukipofi az Arany János utcában!Ki nem ismeri azt az édes pofáját?!(p)/Nem... ki az? (k) >>> ')
        elif valasz2 == valaszlista2 [1]:
            print 'Kár... pedig érdemes megismerni.'
        else:
            raw_input ('Igen, tőle tanultam! (i)', 'Nem, nem ismerem Őt. (n)')
    elif valasz == valaszlista [1]:
        print 'Hát... vannak az embernek rossz napjai.'
        print 'Mi a baj?'
        valasz3 = raw_input ('Szarnom kő! (sz)/Haggyá má! (h) >>> ') 
        if valasz3 == valaszlista3 [0]:
            print 'Hát menj el! Vagy még arra is lusta vagy?'
            valasz5 = raw_input ('Ja... (j)/ Lehetséges, bár nem tudom... (l) >>> ')
            if valasz5 == valaszlista5 [0]:
                print 'Én erre nem lennék büszke...'
            elif valasz5 == valaszlista5 [1]:
                print 'Jó lenne, ha rájönnél!'
            else:
                raw_input ('Ja... (j)/ Lehetséges, bár nem tudom... (l) >>> ')
        elif valasz3 == valaszlista3 [1]:
            print 'Rendben van! Szia!'
        else:
            raw_input ('Szarnom kő! (sz)/Haggyá má! (h) >>> ') 
    else:
        raw_input ('Köszönöm szépen jól vagyok(k)/Szarú de büszkén!(sz) >>> ')
        
    print 'Még egy kört?'
    flag = raw_input('(i)gen/(n)em > ')
    flag = flag.lower()
    while flag not in ['i','n']:
        flag = raw_input('(i)gen/(n)em > ')
        flag = flag.lower()

