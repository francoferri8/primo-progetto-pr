def somma_lista(numeri):
    """Restituisce la somma di tutti i numeri in una lista."""
    totale = 0
    for n in numeri:
        totale += n
    return totale


if __name__ == "__main__":
    esempi = [1, 2, 3, 4, 5]
    print(f"Somma di {esempi} = {somma_lista(esempi)}")
