# 🎟️ TicketPurchaseBot – Bot d'achat de billets

Ce projet Python vous permet de **réserver automatiquement des billets** dès qu'ils deviennent disponibles. Il est conçu pour détecter, remplir et valider le formulaire de réservation en un temps record.

---

## 🚀 Fonctionnalités

- Connexion automatique à votre compte
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

creer un envrionnement et installer les depandances avec :
```
pip install -r requirements.txt
```

## ⚙️ Lancement du bot

1. Placez chromedriver.exe dans le dossier racine du projet.

2. Ouvrir un terminal dans le dossier du projet (mieux hors vscode)

3. Activer l'environnement avec :
   ```
   .\nom_env\Scripts\Activate
   ```
   
4. Lancez le script :
   ```
   python main.py
   ```

6. Renseignez les informations demandées dans le terminal:
   - Pseudo de connexion
   - Mot de passe
   - Noms des bénéficiaires
