
txt = '''American Bilbo was great dwarf.
bIlbo worked in Yandex. Yandex and yandex : great cezar bilbo?
Maybe yandex yandex american dwarf??1!#4 12rasdad
fvfsdgfjfdlksj; iuerjfnl lkfhnwe joweufjkl mf ;;; qsadf 
cezar - cezar? And dwarf was dwarf! Dwarf and yandex from american yandex with bilbo
American american AMERIcan me? cezar bilbo
bilbo cezar yandex YANDEX american dwarf and my DWARF 
SDKFJA AND and was AND AND NAD
AND and dwarf!!!!!!!!YEAH!
Super text, yeap?'''
 
punct = ',.!?:;'
ltxt = [w.rstrip(punct).lower() for w in txt.split() if len(w.rstrip(punct)) > 3]
print(*sorted(set(ltxt), key=ltxt.count, reverse=True)[:5], sep='\n')
