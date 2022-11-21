#El bosque reanimado [es]
#Entrada para NaNoGenMo 2022 / NaNoGenMo 2022 Entry


# Partiendo del texto original de "El bosque animado" (Wenceslao Fernández 
# Flórez, 1943), el programa emplea una técnica de cut-up para recomponer la 
# novela. El programa extrae fragmentos de la novela original y los reordena, 
# sustituyendo cada fragmento por otro elegido al azar que comience por la misma 
# palabra.
#
# El resultado es un texto que conserva el realismo mágico de la novela original
# pero que descompone la trama dotándola de un caracter más onírico.

# Descripción técnica
# Proceso de fragmentación
# En primer lugar se extraen los fragmentos del texto original, considerando
# como fragmentos los bloques de palabras entre signos de puntuación. Así, el 
# párrafo
# 
# "La fraga es un tapiz de vida apretado contra las arrugas de la tierra; en sus
# cuevas se hunde, en sus cerros se eleva, en sus llanos se iguala. Es toda 
# vida: una legua, dos leguas de vida entretejida, cardada, sin agujeros, como 
# una manta fuerte y nueva, de tanto espesor como el que puede medirse desde lo 
# hondo de la guarida del raposo hasta la punta del pino más alto."
# 
# se convierte en esta lista de fragmentos
# 
# "la fraga es un tapiz de vida apretado contra las arrugas de la tierra"
# "en sus cuevas se hunde"
# "en sus cerros se eleva"
# "en sus llanos se iguala"
# "es toda vida"
# "una legua"
# "dos leguas de vida entretejida"
# "cardada"
# "sin agujeros"
# "como una manta fuerte y nueva"
# "de tanto espesor como el que puede medirse desde lo hondo de la guarida del 
#  raposo hasta la punta del pino más alto"
#
# Además, para mejorar la legibilidad del texto cuando se reconstruya, se extrae
# la estructura (saltos de línea, puntuación) y la capitalización del mismo. La 
# estructura del párrafo anterior sería:
#
# "<F>; <f>, <f>, <f>. <F>: <f>, <f>, <f>, <f>, <f>, <f>."
#
# donde <F> representa un fragmento que comienza por mayúscula y <f> un 
# fragmento que comienza por minúscula.
# 
# Proceso de recomposición
# Una vez extraídos los fragmentos y la estructura del texto original, el 
# programa reordena los fragmentos de forma aleatoria, siempre con la condición 
# de que cada fragmento sustituto comience por la misma palabra que el 
# fragmento al que sustituye.
#
# Por ejemplo, el fragmento "en sus cuevas se hunde" se podría sustituír por
# "en sus cerros se eleva" o por "en sus llanos se iguala", ya que son los 
# únicos fragmentos que comienzan por "en". El fragmento "dos leguas de vida 
# entretejida" no variaría ya que en este ejemplo no hay ningún otro fragmento 
# que comience con la palabra "dos".




import random
import re

random.seed()

base = "el bosque animado - full.txt"

with open(base, 'r') as file:
    original_text = file.read()


def extract_fragments_layout(text):

    regex = r"[a-záéíóúüñ][a-záéíóúüñ ]*[a-záéíóúüñ]|[a-záéíóúüñ]"
    layout = re.sub(regex, '<f>', text, 0, re.MULTILINE | re.IGNORECASE)

    matches = re.finditer(regex, text, re.MULTILINE | re.IGNORECASE)
    fragments = []
    caps = []
    for index, match in enumerate(matches):
        caps.append(match.group()[0].isupper())
        fragments.append(match.group())

    return fragments, layout, caps


def restore_text(fragments, layout):

    matches = re.finditer(pattern='<f>', string=layout)
    pos = []
    for m in matches:
        pos.insert(0, (m.start(), m.end()))
    assert len(pos) == len(fragments)

    for (start, end) in pos:
        fragment = fragments.pop()
        isCaps = caps.pop()
        if isCaps:
            fragment = fragment[0].upper() + fragment[1:]
        else:
            fragment = fragment[0].lower() + fragment[1:]
        layout = layout[:start] + fragment + layout[end:]

    return layout


fragments, layout, caps = extract_fragments_layout(original_text)


# Misma palabra inicial
def misma_palabra_inicial(fragments):

    pool = fragments[:]

    for f in range(len(fragments)):

        if (f+1)%100 == 0:
            print(f"{f+1}/{len(fragments)}")

        fragment_index = []

        # Esto se puede optimizar muchísimo
        for p in range(len(pool)):
            if pool[p] != '' and pool[p].lower().split()[0] == fragments[f].lower().split()[0]:
                fragment_index.append(p)

        if len(fragment_index) == 0:
            print("ERROR: No hay fragmentos que empiecen igual")
        else:
            if len(fragment_index) > 1:
                if f in fragment_index:
                    fragment_index.remove(f)
            index = random.randint(0, len(fragment_index) - 1)
            fragments[f] = pool[fragment_index[index]]
            pool[fragment_index[index]] = ""

    return fragments


fragments = misma_palabra_inicial(fragments)
restored_text = restore_text(fragments, layout)
print(restored_text)


with open("el bosque reanimado.txt", "w") as file:
    file.write(restored_text)
