# ===============================
#  UI
# =============================== 

def print_risultato(value:int, spec:str)->None:
    if value is None:
        raise ValueError(f"{value} è obbligatorio (Non può essere None)")
    if not isinstance(value, (int)):
        raise TypeError (f"{value} deve essere un numero")

    print("*"*50)
    print(f"Il numero di {spec} è {value}")
    print("*"*50)