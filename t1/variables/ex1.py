
#                            Variabler - Övning 1
#
# Denna uppgift handlar om att ändra på några detaljer i en kort berättelse om
# en karaktär. Idén är att lära sig varför variabler är viktiga och hur de
# hjälper programmeraren att hålla reda på data och information.
#

# Dessa nedan kallas för "variabler". De används till att spara data, och att
# sedan återanvända det.
name = "Adbi"
age = 15

# Detta är en kort berättelse om 
story = f"""\
Det här är en berättelse om min vän {name}.
Han är {age} år gammal och kommer från en by inte långt härifrån.
Idag tänker {name} komma till stan för att skaffa en ny bil för sin familj.
Men {name} har ett problem, han glömde plånboken på tåget.

Han behöver ta sig tillbaka till tågstationen och förklara för någon att han
tappat bort viktiga ägodelar på tåget.

Om ett par månader blir Abdi {age + 1} år gammal.
"""


print(story)

is_done = False

def do_once(func) -> bool:
    global is_done

    if not is_done:
        func()
        is_done = True
        return True
    else:
        return False

################################################################################

while True:
    do_once(lambda: print('Moustafa sucks'))
