# ===============================
#   CONFIGURAZIONE E COSTANZI
# ===============================

REGEX_TUTTI_CARATTERI = r'.'           # Tutti i caratteri (usare con re.DOTALL)
REGEX_SENZA_SPAZI = r'\S'              # Caratteri esclusi gli spazi
REGEX_SOLO_LETTERE = r'[a-zA-ZÀ-ÿ]'   # Solo lettere, incluse accentate
REGEX_PAROLE = r'\w+'                  # Parole (lettere, numeri, underscore)
REGEX_PAROLE_LETTERE = r'[a-zA-ZÀ-ÿ]+' # Parole composte solo da lettere
REGEX_FRASI = r'[^.!?]+[.!?]+'         # Frasi terminate da . ! ?


URL: str = "https://raw.githubusercontent.com/marikaseri2000/lezione3/refs/heads/pippo/esercizi_pome/quizzettone/domanda-1.txt?token=GHSAT0AAAAAADQG2YFISBCO2LJLOV7W5YDC2JZLGPQ"
