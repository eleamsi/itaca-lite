# Esempio di script
def saluta(nome: str) -> str:
    """Restituisce un saluto."""
    return f"Ciao, {nome}!"

for i in range(3):
    print(saluta("mondo"), i)  # commento con una riga piuttosto lunga che supera la larghezza del riquadro per vedere lo scorrimento
