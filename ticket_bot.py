import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options
import webbrowser
import os
import random
import pyfiglet
from termcolor import colored
import time
import webbrowser
import time
import pyfiglet
from termcolor import colored
from tkinter import *
from PIL import Image, ImageTk
import threading


class TicketPurchaseBot:
    def __init__(self, email, password, names, billets, bloc_index=1):
        self.email = email
        self.password = password
        self.names = names
        self.billets = billets
        self.bloc_index = bloc_index
        self.url_login = "https://www.cseaubay.com/com/login?clear="
        self.url_page = "https://www.cseaubay.com/com/page/1401"

        # Chrome options (headless mode disabled for debugging)
        options = Options()
        options.headless = False
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(service=Service(executable_path="chromedriver.exe"), options=options)

    def wait(self, seconds=1):
        time.sleep(seconds)

    def log(self, message):
        print(f"[LOG] {message}")

    def login(self):
        self.driver.get(self.url_login)
        self.driver.find_element(By.ID, "authentication_login").send_keys(self.email)
        self.driver.find_element(By.ID, "authentication_password").send_keys(self.password + Keys.ENTER)
        self.log("Connexion effectuée")

    def go_to_reservation_page(self):
        self.driver.get(self.url_page)
        self.accept_cookies()
        self.log("Arrivé sur la page de réservation")

    def accept_cookies(self):
        try:
            btn = self.driver.find_element(By.CLASS_NAME, "accept-btn-handler")
            self.driver.execute_script("arguments[0].click();", btn)
            self.log("Cookies acceptés")
            self.wait()
        except NoSuchElementException:
            self.log("Pas de pop-in cookies")

    def wait_for_button_and_click(self):
        xpath = f'(//div[@id="contentPresta2"])[' + str(
            self.bloc_index) + ']//a[contains(@class, "boutonRond") and contains(translate(text(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "je commande")]'
        while True:
            try:
                btn = self.driver.find_element(By.XPATH, xpath)
                self.driver.execute_script("arguments[0].click();", btn)
                self.log("Bouton \"Je commande\" cliqué")
                break
            except NoSuchElementException:
                self.log("Bouton non trouvé, recharge de la page...")
                self.wait(0.5)
                self.driver.get(self.url_page)

    def fill_names(self):
        try:
            nom1, nom2 = self.names
            self.driver.find_element(By.NAME, "val_rep_coll0").send_keys(nom1)
            self.driver.find_element(By.NAME, "val_rep_coll1").send_keys(nom2)
            self.log("Champs prénoms remplis")
        except NoSuchElementException:
            self.log("Erreur : champs noms/prénoms introuvables")

    def add_billets_subventionnes(self):
        try:
            for _ in range(self.billets):
                btn = self.driver.find_element(By.XPATH,
                                               "//div[@id='zoneForm_qte_subv_OD11777_0']//button[contains(@onclick, 'plus')]")
                self.driver.execute_script("arguments[0].click();", btn)
                self.wait(0.5)
            self.log(f"Ajouté {self.billets} billets subventionnés")
        except NoSuchElementException:
            self.log("Erreur : bouton ajout billet subventionné introuvable")

    def click_valider_question(self):
        try:
            btn = self.driver.find_element(By.NAME, "b_valider_x")
            self.driver.execute_script("arguments[0].click();", btn)
            self.log("Validation intermédiaire confirmée")
        except NoSuchElementException:
            self.log("Bouton \"valider la question\" introuvable")

    def click_valider_operation(self):
        try:
            btn = self.driver.find_element(By.NAME, "b_confirm_x")
            self.driver.execute_script("arguments[0].click();", btn)
            self.log("Validation finale envoyée")
        except NoSuchElementException:
            self.log("Bouton \"valider l'opération\" introuvable")
    
    def click_valider_paiement(self):
        try:
            btn = self.driver.find_element(By.NAME, "b_valider")
            self.driver.execute_script("arguments[0].click();", btn)
            self.log("Validation de paiement finale envoyée")
        except NoSuchElementException:
            self.log("Bouton \"valider l'opération de paiement\" introuvable")
    
    def click_aller_paiement(self):
        try:
            btn = self.driver.find_element(By.NAME, "b_continuer_recapitulatif")
            self.driver.execute_script("arguments[0].click();", btn)
            self.log("Validation de paiement finale envoyée")
        except NoSuchElementException:
            self.log("Bouton \"valider l'opération de paiement\" introuvable")

    def quit(self):
        self.log("Fermeture du navigateur dans 10 secondes")
        self.wait(500)
        self.driver.quit()

    def run(self):
        self.login()
        self.go_to_reservation_page()
        self.wait_for_button_and_click()
        self.fill_names()
        self.add_billets_subventionnes()
        self.click_valider_question()
        self.click_valider_operation()
        self.click_valider_paiement()
        self.click_aller_paiement()
        self.quit()


def show_ascii_warning():
    print(colored(pyfiglet.figlet_format("PIRATER"), "red", attrs=["bold"]))
    time.sleep(0.5)
    print(colored(pyfiglet.figlet_format("C'EST MAL"), "yellow", attrs=["bold"]))
    time.sleep(0.5)
    print(colored(pyfiglet.figlet_format("PTOURNIER !"), "green", attrs=["bold"]))
    print(colored("Tu croyais vraiment pouvoir hacker le CSE ? 😂", "cyan"))
    time.sleep(2)


elmo_windows = []

class MyLabel(Label):
    def __init__(self, master, filename):
        im = Image.open(filename)
        seq = []
        try:
            while 1:
                seq.append(im.copy())
                im.seek(len(seq))
        except EOFError:
            pass

        self.delay = im.info.get('duration', 100)
        first = seq[0].convert('RGBA')
        self.frames = [ImageTk.PhotoImage(first)]

        Label.__init__(self, master, image=self.frames[0])
        temp = seq[0]
        for image in seq[1:]:
            temp.paste(image)
            frame = temp.convert('RGBA')
            self.frames.append(ImageTk.PhotoImage(frame))

        self.idx = 0
        self.cancel = self.after(self.delay, self.play)

    def play(self):
        self.config(image=self.frames[self.idx])
        self.idx = (self.idx + 1) % len(self.frames)
        self.cancel = self.after(self.delay, self.play)

def close_all_elmos():
    for win in elmo_windows:
        try:
            win.destroy()
        except:
            pass



def launch_fixed_position_gifs(filename):
    def _start():
        root = Tk()
        root.withdraw()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        positions = [
            (50, 50),  # haut gauche
            (50, screen_height - 550),  # bas gauche
            (screen_width - 550, 50),  # haut droite
            (screen_width - 550, screen_height - 550),  # bas droite
            (screen_width // 2 - 150, 100)  # centre haut
        ]

        for x, y in positions:
            win = Toplevel(root)
            win.title("💥 HACK WARNING 💥")
            win.overrideredirect(True)
            win.geometry(f"+{x}+{y}")
            anim = MyLabel(win, filename)
            anim.pack()
            elmo_windows.append(win)

        control_win = Toplevel(root)
        control_win.geometry("500x80+{}+{}".format(screen_width // 2 - 250, screen_height // 2 - 40))
        control_win.title("🙏 Délivrance")
        btn = Button(control_win, text="SI on a les places je dois une bière à Martin (click)",
                     font=("Arial", 10, "bold"), command=close_all_elmos)
        btn.pack(fill="both", expand=True)
        elmo_windows.append(control_win)

        root.mainloop()

    threading.Thread(target=_start, daemon=True).start()
    time.sleep(2)


def show_ascii_warning_delayed():
    lignes = ["PIRATER", "C'EST MAL", "PTOURNIER !"]
    couleurs = ["red", "yellow", "green"]
    for ligne, couleur in zip(lignes, couleurs):
        print(colored(pyfiglet.figlet_format(ligne), couleur, attrs=["bold"]))
        time.sleep(2)
    print(colored("Tu croyais vraiment pouvoir hacker le CSE ? 😂", "cyan"))
    time.sleep(20)
    print(colored("Bon tkt je t'envoie la suite dans 5 secondes profite un peu de la musique.", "cyan"))


def rickroll_with_gif_and_terminal(gif_file="utils/tentofate-elmo.gif"):
    launch_fixed_position_gifs(gif_file)
    webbrowser.open("https://www.youtube.com/watch?v=x4qGaxZpNS8")
    show_ascii_warning_delayed()
