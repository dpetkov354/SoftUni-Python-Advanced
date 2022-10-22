from collections import deque

rose = ["r", "o", "s", "e"]
tulip = ["t", "u", "l", "i", "p"]
lotus = ["l", "o", "t", "u", "s"]
daffodil = ["d", "a", "f", "f", "o", "d", "i", "l"]
no_word = False

vowels = deque(map(str, input().split(' ')))
consonants = deque(map(str, input().split(' ')))

while len(vowels) > 0 and len(consonants) > 0:
    vowel_letter = vowels.popleft()
    consonants_letter = consonants.pop()

    if vowel_letter in rose:
        rose.remove(vowel_letter)
    if vowel_letter in tulip:
        tulip.remove(vowel_letter)
    if vowel_letter in lotus:
        lotus.remove(vowel_letter)
    if vowel_letter in daffodil:
        daffodil.remove(vowel_letter)

    if consonants_letter in rose:
        rose.remove(consonants_letter)
    if consonants_letter in tulip:
        tulip.remove(consonants_letter)
    if consonants_letter in lotus:
        lotus.remove(consonants_letter)
    if consonants_letter in daffodil:
        daffodil = list(filter(lambda a: a != consonants_letter, daffodil))

    if len(rose) == 0:
        print("Word found: rose")
        no_word = True
        break
    elif len(tulip) == 0:
        print("Word found: tulip")
        no_word = True
        break
    elif len(lotus) == 0:
        print("Word found: lotus")
        no_word = True
        break
    elif len(daffodil) == 0:
        print("Word found: daffodil")
        no_word = True
        break

if no_word is not True:
    print("Cannot find any word!")
if len(vowels) > 0:
    print(f"Vowels left: {' '.join(vowels)}")
if len(consonants) > 0:
    print(f"Consonants left: {' '.join(consonants)}")

print(rose)
print(tulip)
print(lotus)
print(daffodil)
