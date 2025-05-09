from datetime import datetime

class Client:
    def __init__(self, id, nom, prenom, adresse, telephone):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.telephone = telephone

    def __str__(self):
        return (f"Client(id={self.id}, nom={self.nom}, prenom={self.prenom}, "
                f"adresse={self.adresse}, telephone={self.telephone})")

class Chambre:
    def __init__(self, id, numero, type_chambre, prix):
        self.id = id
        self.numero = numero
        self.type = type_chambre
        self.prix = prix

    def __str__(self):
        return (f"Chambre(id={self.id}, numero={self.numero}, type={self.type}, "
                f"prix={self.prix}€)")

class ChambreSimple(Chambre):
    def __init__(self, id, numero, prix):
        super().__init__(id, numero, "simple", prix)

class ChambreDouble(Chambre):
    def __init__(self, id, numero, prix):
        super().__init__(id, numero, "double", prix)

class ChambreSuite(Chambre):
    def __init__(self, id, numero, prix):
        super().__init__(id, numero, "suite", prix)

class Reservation:
    def __init__(self, id, date_arrivee, date_depart, client_id, chambre_id):
        # dates as datetime objects
        self.id = id
        self.date_arrivee = datetime.strptime(date_arrivee, "%Y-%m-%d").date()
        self.date_depart = datetime.strptime(date_depart, "%Y-%m-%d").date()
        self.client_id = client_id
        self.chambre_id = chambre_id

    def __str__(self):
        return (f"Reservation(id={self.id}, arrival={self.date_arrivee}, departure={self.date_depart}, "
                f"client_id={self.client_id}, chambre_id={self.chambre_id})")

class Hotel:
    def __init__(self):
        self.clients = []
        self.chambres = []
        self.reservations = []

    # Clients
    def ajouter_client(self, client):
        self.clients.append(client)
        print("Client ajouté avec succès.")

    def lister_clients(self):
        if not self.clients:
            print("Aucun client enregistré.")
        for c in self.clients:
            print(c)

    # Chambres
    def ajouter_chambre(self, chambre):
        self.chambres.append(chambre)
        print("Chambre ajoutée avec succès.")

    def lister_chambres(self):
        if not self.chambres:
            print("Aucune chambre disponible.")
        for ch in self.chambres:
            print(ch)

    # Réservations
    def ajouter_reservation(self, reservation):
        # Could add availability check here
        self.reservations.append(reservation)
        print("Réservation ajoutée avec succès.")

    def lister_reservations(self):
        if not self.reservations:
            print("Aucune réservation.")
        for r in self.reservations:
            print(r)

    # Helpers
    def get_client_by_id(self, client_id):
        return next((c for c in self.clients if c.id == client_id), None)

    def get_chambre_by_id(self, chambre_id):
        return next((ch for ch in self.chambres if ch.id == chambre_id), None)


def main():
    hotel = Hotel()
    while True:
        print("\n--- Menu Principal ---")
        print("1. Ajouter un client")
        print("2. Ajouter une chambre")
        print("3. Faire une réservation")
        print("4. Afficher les clients")
        print("5. Afficher les chambres")
        print("6. Afficher les réservations")
        print("7. Quitter")
        choix = input("Sélectionnez une option: ")

        if choix == '1':
            try:
                id = int(input("ID du client: "))
                nom = input("Nom: ")
                prenom = input("Prénom: ")
                adresse = input("Adresse: ")
                telephone = input("Téléphone: ")
                client = Client(id, nom, prenom, adresse, telephone)
                hotel.ajouter_client(client)
            except ValueError:
                print("Erreur: ID invalide.")

        elif choix == '2':
            try:
                id = int(input("ID de la chambre: "))
                numero = int(input("Numéro de chambre: "))
                print("Types disponibles: simple, double, suite")
                t = input("Type: ").strip().lower()
                prix = float(input("Prix (€): "))
                if t == 'simple':
                    chambre = ChambreSimple(id, numero, prix)
                elif t == 'double':
                    chambre = ChambreDouble(id, numero, prix)
                elif t == 'suite':
                    chambre = ChambreSuite(id, numero, prix)
                else:
                    print("Type invalide.")
                    continue
                hotel.ajouter_chambre(chambre)
            except ValueError:
                print("Erreur: valeurs invalides.")

        elif choix == '3':
            try:
                id = int(input("ID de la réservation: "))
                date_arrivee = input("Date d'arrivée (YYYY-MM-DD): ")
                date_depart = input("Date de départ (YYYY-MM-DD): ")
                client_id = int(input("ID du client: "))
                chambre_id = int(input("ID de la chambre: "))
                if not hotel.get_client_by_id(client_id):
                    print("Client introuvable.")
                    continue
                if not hotel.get_chambre_by_id(chambre_id):
                    print("Chambre introuvable.")
                    continue
                reservation = Reservation(id, date_arrivee, date_depart, client_id, chambre_id)
                hotel.ajouter_reservation(reservation)
            except ValueError:
                print("Erreur: valeurs invalides ou format de date incorrect.")

        elif choix == '4':
            hotel.lister_clients()
        elif choix == '5':
            hotel.lister_chambres()
        elif choix == '6':
            hotel.lister_reservations()
        elif choix == '7':
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
