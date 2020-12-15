# engeto_text_analyser
engeto first project
creating .gitignore
###================Zadani=================
1. Na začátku přivítá uživatele. 
2. Vyžádá si od uživatele přihlašovací jméno a heslo. 
3. Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů.

_Registrováni jsou následující uživatelé:_
USER |   PASSWORD  |
-----------------------
| bob  |     123     |
| ann  |    pass123  |
| mike | password123 |
| liz  |    pass123  |

Pokud se ti tento úkol bude zdát složitý, prověř, jestli zadané údaje jsou mezi registrovanými, ale neřeš spojení uživatel - heslo.

4. Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS - ošetřit validitu vstupů!!!

5. Pro vybraný text spočítá následující statistiky:
- počet slov,
- počet slov začínajících velkým písmenem,
- počet slov psaných velkými písmeny,
- počet slov psaných malými písmeny,
- počet čísel (ne cifer!).

6. Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. Například takto: 
 1 * 1
 2 *********** 11
 3 *************** 15
 4 ********* 9
 5 ********** 10
 
_V textu, ze kterého byl vytvořen tento graf, je tedy pouze 1 jednopísmené slovo, 11 slov složených ze dvou písmen, a tak dále._

7. Program spočítá součet všech čísel (ne cifer!) v textu. Výsledkem tohoto součtu v následujícím textu by teby bylo číslo 8500:

###### **OUTPUT**
----------------------------------------
Welcome to the app. Please log in:
USERNAME: bob
PASSWORD: 123
----------------------------------------
We have 3 texts to be analyzed.
Enter a number btw. 1 and 3 to select: 2
----------------------------------------
There are 62 words in the selected text.
There are 10 titlecase words
There are 0 uppercase words
There are 51 lowercase words
There are 1 numeric strings
----------------------------------------
 2 ******* 7
 3 ***************** 17
 4 ********* 9
 5 ********** 10
 6 ******* 7
 7 *** 3
 8 ** 2
 9 ***** 5
10 * 1
13 * 1
----------------------------------------
If we summed all the numbers in this text we would get: 300.0
----------------------------------------

====END===