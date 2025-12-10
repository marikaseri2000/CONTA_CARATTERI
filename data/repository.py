# ===============================
#   Repository
# =============================== 
#funzione che ci fa accedere al fil nel nostro file system

def get_file_content(file_path: str) -> str:
    """Restituisce un oggetto TextIO con il contenuto del file specificato"""
    if not file_path:
        raise ValueError("Il file path non può essere vuoto!")
    try:
        with open(file_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError ("Il file non esiste")