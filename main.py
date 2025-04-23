import time

from ticket_bot import TicketPurchaseBot, rickroll_with_gif_and_terminal


def main():
    print("=== Salut pirate on part a la recherche des billets perdus ===")
    # rickroll_with_gif_and_terminal("utils/tentofate-elmo.gif")
    # time.sleep(25)

    pseudo_aubay = input("pseudo aubay de connexion : ").strip()
    password = input("Mot de passe : ").strip()
    nom1 = input("Prénom + nom personne 1 : ").strip()
    nom2 = input("Prénom + nom personne 2 : ").strip()

    bot = TicketPurchaseBot(
        email="mjarnier",
        password='Zomarodejo1?',
        names=("Martin Jarnier", "Jocelyn Jarnier"),
        billets=2,
        bloc_index=3
    )
    bot.run()


if __name__ == "__main__":
    main()
