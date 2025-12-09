"""
    -dove si trova il testo?
        - il testo viene preso da un file
        - i file vengono mostrati a video dalla console
    - voglio contare i caretteri di un testo
        - con spazi e senza spazi
        - voglio contare anche le parole
        - voglio contare le frasi
        - voglio contare i paragrafi
        - voglio avere il tempo di lettura
        - voglio verificare le ripetizioni della parola e della lettura
    - dove voglio mostrare i risultati?
        -console
        -scriverlo su file
"""

#dobbiamo aprire un canale di comunicazione con uno STREAM

#======================
#   REPOSITORY
#======================

from typing import TextIO

def get_file(file_path:str)->TextIO:
    #Restituisce un oggetto TextIO con il contenuto del file specifico
        return open (file_path, "r") 
#=======================
#   SERVICES
#=======================
def stampa_testo_input(text: TextIO)->None:
    with text as f:
        content=f.read()
        print (content)

def get_testo(text: TextIO)-> str:
    with text as f:
        content=f.read()
        return content

def get_text_len(text:str)->int:
    if text in None:
        print("La stringa vuota")
    print(len(text))

import re
#libreria che ha vari metodi e per analizzare i PATTERN
def get_text_len_no_space(text:str)->int:
    print(len(re.findall(r"\S", text)))

def main() -> None:
    try:
        content: TextIO=get_file("text.txt")
        get_text_len(get_testo(content))
        get_text_len_no_space(get_testo(content))

    except Exception as e:
        print (f"Errore generico: {e}")
    
    finally:
        print("fine try catch")
    
main()