



#(Funktionsname: "count_words", Input: Pfad zum Textdokument, Return: Anzahl der Wörter)
def count_words(path):
    content = readFile(path)
    # Definition of word


#(Funktionsname: "count_character", Input: Pfad zum Textdokument, Return: Anzahl der Zeichen)
#def count_character(path):

#(Funktionsname: "count_lines", Input: Pfad zum Textdokument, Return: Anzahl der Zeilen)
def count_lines(path):
    with open(path) as f:
        content = f.readlines()
        return content.count

#(Funktionsname: "count_words_from_line", Input: Pfad zum Textdokument, Startzeile, Return: Anzahl der Wörter)
#def count_words_from_line():
#(Funktionsname: "count_sentences", Input: Pfad zum Textdokument, Return: Anzahl der Sätze)
#def count_sentences():
#(Funktionsname: "count_quotes", Input: Pfad zum Textdokument, Return: Anzahl der Zitate)
#def count_quotes():
#(Funktionsname: "count_character_all", Input: Pfad zum Textdokument, Return: Anzahl der Zeichen)
#def count_character_all():

###################################
# Support Functions
###################################

def readFile(path):
    f = open(path, "r")
    return f.read()

filepath = "../Challenge.md"

count_words(filepath)