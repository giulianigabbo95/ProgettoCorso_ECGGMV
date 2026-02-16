import Lavatrice

class TicketRiparazione:
    def __init__(self, id_ticket, elettrodomestico):
        # Attributi privati come richiesto (Regola 1: Incapsulamento)
        self.__id_ticket = id_ticket
        self.__elettrodomestico = elettrodomestico # Oggetto (Lavatrice, Frigo o Forno)
        self.__stato = "aperto"                    # Stato iniziale di default
        self.__note = []                           # Lista vuota per i log della riparazione

    # --- METODI RICHIESTI ---

    def aggiungiNota(self, testo):
        """Aggiunge una stringa alla lista delle note del ticket."""
        self.__note.append(testo)

    def calcolaPreventivo(self, *voci_extra):
        """
        METODO VARIADICO: accetta un numero variabile di costi (float o int).
        Sfrutta il POLIMORFISMO: chiama stima_costo_base() senza sapere 
        se l'oggetto è un Forno, una Lavatrice o un Frigo.
        """
        # 1. Recupera il costo base specifico dell'elettrodomestico (Polimorfismo)
        totale = self.__elettrodomestico.stima_costo_base()
        
        # 2. Somma tutti i parametri extra passati tramite *voci_extra
        # voci_extra viene trattato come una tupla all'interno del metodo
        for costo in voci_extra:
            totale += costo
            
        return totale

    """Getter e setter impostati tramite @property per blindare le variabili e impedire manipolazioni errate"""

    @property
    def stato(self):
        return self.__stato

    @stato.setter
    def stato(self, nuovo_stato):
        stati_validi = ["aperto", "in lavorazione", "chiuso"]
        if nuovo_stato.lower() in stati_validi:
            self.__stato = nuovo_stato.lower()
        else:
            print(f"Errore: Stato '{nuovo_stato}' non valido.")

    @property
    def note(self):
        # Restituiamo una copia o la lista formattata per proteggere l'originale
        return "\n".join(self.__note) if self.__note else "Nessuna nota presente."

    # Getter per l'elettrodomestico (utile per il metodo statisticheTipo dell'Officina)
    def get_elettrodomestico(self):
        return self.__elettrodomestico
    
    def get_id(self):
        return self.__id_ticket
    
    
    def calcolaStatisticheTipo(self):
        for ticket in self.tickets:
            if type(ticket._TicketRiparazione__elettrodomestico) == Lavatrice:
                conta_lavatrici += 1
