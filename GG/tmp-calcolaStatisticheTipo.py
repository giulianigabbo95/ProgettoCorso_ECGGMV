import Lavatrice

def calcolaStatisticheTipo(self):
    for ticket in self.tickets:
        if type(ticket._TicketRiparazione__elettrodomestico) == Lavatrice:
            conta_lavatrici += 1