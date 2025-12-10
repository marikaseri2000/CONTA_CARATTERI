# ===============================
#   Services
# =============================== 
import re
from constant import REGEX_SENZA_SPAZI,REGEX_PAROLE_LETTERE, REGEX_FRASI


def get_caratteri_len(text: str)->int:
    if not text:
        return 0
    return  len(text)

def get_text_len_no_space(text: str) -> int:
    """Restirtuisce il numero di caratteri presenti in una stringa, senza contare gli spazi."""
    if not text:
        return 0
    return len(re.findall(REGEX_SENZA_SPAZI, text))

def get_words_numers(text: str)->int:
    """Restituisce il numero di parole in una stringa"""
    if not text:
        return 0
    return len(re.findall(REGEX_PAROLE_LETTERE, text))

def get_phrase_number(text: str)->int:
    """Restituisce il numero di parole in una stringa"""
    if not text:
        return 0
    return len(re.findall(REGEX_FRASI, text))
