numbers = [1, 2, 4, -6, 7, 8, 100, -125, 11, 123]
names = ["Petr", "Ales", "Honza", "Lenka", "Andrea", "Alice"]
random_codes = ["1-okdsaaa", "0-nFnldd", "0-AA", "0-uwqqq", "2-ZSTh", "0-RKOcsxxx", "1-LwWtss", "0-cdKiddd", "2-KpAAaa",
                "3-sOdSxhcds", "  "]

# 1. pomocí cyklu for vypište čísla ze seznamu numbers, ale přeskočte záporná čísla.
for n in numbers:
    if n < 0:
        continue
    print(n)

# 2. pomocí cyklu while vypište všechna jména, pokud narazíš na jméno 'Alice' cyklus ukonči
i = 0
while i < len(names):
    if names[i] == "Alice":
        break
    print(names[i])
    i += 1

# 3. pomocí list comprehension vytvoř nový list, který bude obsahovat pouze prvky z 'random_codes', které obsahují 0
new_list = [r for r in random_codes if "0" in r]
print(new_list)

# Dobrovolny ukol: Vypis všechny pod-seznamy s alespoň třemi po sobě jdoucími stejnými znaky v seznamu 'random_codes'
for code in random_codes:
    for i in range(len(code) - 2):
        if code[i] == code[i+1] == code[i+2]:
            print("Found:", code)
            break

# Dobrovolny ukol, superkratke reseni studenta:
import re
sub_list = [code for code in random_codes if re.search(r"(.)\1{2,}", code)]
print(sub_list)