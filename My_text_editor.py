#Text with newline as input:
text_with_newlines = """Ein Ereignisblock wird in deinem Programm mit einem
Ereignis
(Schlüsselwort) eingeleitet, wie zum Beispiel
LOAD-OF-PROGRAM oder START-OF-SELECTION.
Die Reihenfolge, in der du die Ereignisblöcke im Programm
platzierst, ist irrelevant. Also zuerst LOAD-OF-PROGRAM
und dann START-OF-SELECTION oder umgekehrt
spielt keine Rolle. Auch hat ein Ereignisblock nur ein einleitendes
Ereignisschlüsselwort, aber kein beendendes Ereignisschlüsselwort.
Das Ende ergibt sich aus dem nächsten
Ereignisschlüsselwort, aus dem Programmende oder aus Definitionen von Unterprogrammen oder Modulen. Ereignisblöcke können nicht geschachtelt werden.
Ein so im Programm implementiertes Ereignis wird zu einem bestimmten Zeitpunkt in der Programmausführung aufgerufen, zum Beispiel LOAD-OF-PROGRAMM, wenn das Programm geladen wird."""

# Remove newlines
text_without_newlines = text_with_newlines.replace('\n', ' ')

# Print the result as output:
print(text_without_newlines)