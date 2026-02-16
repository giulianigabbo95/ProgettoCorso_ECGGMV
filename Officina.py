import Ticket as TicketRiparazione

class Officina:
    def __init__(self, nome):
        self.nome = nome
        self.tickets = []
        self.__elettrodomestici = []

    def aggiungiElettrodomestico(self, elettrodomestico):
        self.__elettrodomestici.append(elettrodomestico)
        print(f"Aggiunto: {elettrodomestico.descrizione()}")
    
    def aggiungiTicket(self, ticket):
        if type(ticket) == TicketRiparazione:
            self.tickets.append(ticket)
        else:
            print("Errore: oggetto tipo non valido.")
    
    def chiudiTicket(self, id_ticket):
        for ticket in self.tickets:
            if ticket.getId() == id_ticket:
                ticket.setStato("chiuso")
                print("Ticket chiuso.")
                return
        print("Ticket non trovato.")

    def stampaTicketAperti(self):
        for ticket in self.tickets:
            if ticket.getStato() != "chiuso":
                elettro = ticket.getElettrodomestico()
                print(f"ID: {ticket.getId()} | "
                      f"Tipo: {type(elettro).__name__} | "
                      f"Stato: {ticket.getStato()}")

    def totalePreventivo(self):
        totale = 0
        for ticket in self.tickets:
            totale += ticket.getUltimoPreventivo()
        return totale

    def get_nome(self):
        return self.__nome
    
    def get_elettrodomestici(self):
        return self.__elettrodomestici
    
    def __str__(self):
        print 