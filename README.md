# El bosque reanimado [es]
## Entrada para [NaNoGenMo 2022](https://github.com/NaNoGenMo/2022) / [NaNoGenMo 2022](https://github.com/NaNoGenMo/2022) Entry

Partiendo del texto original de «[El bosque animado](https://es.wikipedia.org/wiki/El_bosque_animado)» ([Wenceslao Fernández Flórez](https://es.wikipedia.org/wiki/Wenceslao_Fern%C3%A1ndez_Fl%C3%B3rez), 1943), el programa emplea una técnica de cut-up para recomponer la novela. El programa extrae fragmentos de la novela original y los reordena, sustituyendo cada fragmento por otro elegido al azar que comience por la misma palabra.

El resultado es un texto que conserva el realismo mágico de la novela original pero que descompone la trama dotándola de un caracter más onírico.

Puedes leer el [texto recompuesto](https://github.com/juanalonso/nanogenmo-2022/blob/main/el%20bosque%20reanimado%20-%2080%20columnas.txt) o curiosear el [código](https://github.com/juanalonso/nanogenmo-2022/blob/main/el_bosque_reanimado.py).

### Ejemplos

>El pino, cantando en sordina entre los largos dientes de sus hojas, tenía un papel principal en el coro del bosque y merecía la fama de dominar la onomatopeya. Su propia felicidad, el alborozo pueril de aquella diablura, le movió a decirle al poste:
—¿No quiere usted cantar con nosotros?

---

>Pero de sur a norte había unas pequeñas nubes nítidas, con esto los árboles gozan como niños traviesos.

---

>Como si aquel mar tuviese también su plancton, prefirió de su repertorio una canción burlesca: la tierra amarilla se acumulaba en montones cerca del agujero, todavía lejana, entre una nube zumbadora. Es asombroso, porque aunque el estupor que les produjo tan raro acontecimiento les contuvo brevísimos instantes, creyendo que equivocaba el camino.

---

>—Pero... ¿cómo gritarían las flores, si en verdad era mujer y no un espíritu malo?

---

>El techo se estremecía bajo pisadas frenéticas; su baile consistía en unos pasos menuditos de dirección indecisa, libre de los absorbentes cuidados de ganar la vida y de defenderla.

---

>Como si por la delgadez del aire en aquella mañana recién creada le costase más trabajo sostenerse, todos guardan entonces un silencio profundo, y bajo aquella caricia la fraga ronroneó un poquito, que humeaba dípteros.


### Descripción técnica
#### Proceso de fragmentación
En primer lugar se extraen los fragmentos del texto original, considerando como fragmentos los bloques de palabras entre signos de puntuación. Así, el párrafo

«_La fraga es un tapiz de vida apretado contra las arrugas de la tierra; en sus cuevas se hunde, en sus cerros se eleva, en sus llanos se iguala. Es toda vida: una legua, dos leguas de vida entretejida, cardada, sin agujeros, como una manta fuerte y nueva, de tanto espesor como el que puede medirse desde lo hondo de la guarida del raposo hasta la punta del pino más alto._»

se convierte en esta lista de fragmentos

```
"la fraga es un tapiz de vida apretado contra las arrugas de la tierra"
"en sus cuevas se hunde"
"en sus cerros se eleva"
"en sus llanos se iguala"
"es toda vida"
"una legua"
"dos leguas de vida entretejida"
"cardada"
"sin agujeros"
"como una manta fuerte y nueva"
"de tanto espesor como el que puede medirse desde lo hondo de la guarida del raposo hasta la punta del pino más alto"
```

Además, para mejorar la legibilidad del texto cuando se reconstruya, se extrae la estructura (saltos de línea, puntuación) y la capitalización del mismo. La estructura correspondiente al párrafo anterior sería:

`"<F>; <f>, <f>, <f>. <F>: <f>, <f>, <f>, <f>, <f>, <f>."`

donde `<F>` representa un fragmento que comienza por mayúscula y `<f>` un fragmento que comienza por minúscula.

#### Proceso de recomposición
Una vez extraídos los fragmentos y la estructura del texto original, el programa reordena los fragmentos de forma aleatoria, siempre con la condición de que cada fragmento sustituto comience por la misma palabra que el fragmento al que sustituye.

Por ejemplo, el fragmento «_en sus cuevas se hunde_» se podría sustituír por «_en sus cerros se eleva_» o por «_en sus llanos se iguala_», ya que son fragmentos que también comienzan por «_en_». El fragmento «_dos leguas de vida entretejida_» no variaría ya que en este ejemplo no hay ningún otro fragmento que comience con la palabra «_dos_».
