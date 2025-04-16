# 🎟️ TicketPurchaseBot – Bot d'achat de billets CSE Aubay

Ce projet Python vous permet de **réserver automatiquement des billets** dès qu'ils deviennent disponibles sur la plateforme du CSE Aubay. Il est conçu pour détecter, remplir et valider le formulaire de réservation en un temps record.

---

## 🚀 Fonctionnalités

- Connexion automatique à votre compte CSE Aubay
- Détection du bouton `Je commande` dès son apparition
- Remplissage automatique des noms pour les billets
- Ajout de billets subventionnés (quantité paramétrable)
- Validation complète de l'opération
- Logs détaillés dans la console
- Mode débogage visuel (navigateur visible)

---

## 🧰 Prérequis

- Python 3.8+
- Google Chrome installé
- [ChromeDriver](https://chromedriver.chromium.org/downloads) (même version que Chrome)

### 📆 Installation des dépendances

pip install -r requirements.txt


## ⚙️ Lancement du bot

1. Placez chromedriver.exe dans le dossier racine du projet.
   
2. Lancez le script :
   main.py

3. Renseignez les informations demandées :
   - Pseudo de connexion
   - Mot de passe
   - Noms des bénéficiaires
