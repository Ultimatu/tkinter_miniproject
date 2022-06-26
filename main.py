from tkinter import *
from tkinter.messagebox import askyesno, askyesnocancel
from tkinter.scrolledtext import ScrolledText
import pygame

pygame.init()


class Main():
    # fonction d'initialisation de la fenetre Tk
    def __init__(self):
        self.root = Tk()
        self.root.geometry("600x400+400+100")
        self.root.resizable(0, 0)
        self.root.title("COQ SARL LITE")
        self.root.iconbitmap(bitmap="assets/icob.ico")
        # mise en place de l'ensemble des variables, des Boutons et des callback
        self.SIDE = 600
        self.ind = -1
        self.with_song = False
        self.conf = True; self.dic = {}
        self.o = ""
        self.f = ""
        self.lab_welcome = Label(
            self.root, text="Bienvenue sur COQ SARL LITE", bg="gold", width=100, font=("helvetica", 20, "bold"))
        self.lab_welcome.pack(anchor="e")
        # Canvas  qui affiche des animation et des logo
        self.cnv = Canvas(self.root, bg="ivory",
                          height=self.SIDE/3, width=self.SIDE)
        self.foto1 = PhotoImage(file="assets/giflab/frame-1.gif")
        self.cn_im = self.cnv.create_image(
            self.SIDE/2, self.SIDE/4, image=self.foto1, tag="photo")
        self.fra = Frame(self.root, bg="blue",
                         width=self.SIDE, height=self.SIDE/3)
        self.fra.pack(fill=X)
        self.menubar = Menu(self.root, tearoff=0,
                            borderwidth=20, border=10, bg="red")
        self.menubar.add_cascade(
            label="ABOUT US", hidemargin=0.8, font=("Helvetica", 25, "bold"), command=lambda: self.about(False))
        self.menubar.add_command(
            command=self.ActivePygame, label="🔊🔕PLAY SONG")
        self.root.config(menu=self.menubar)
        self.close_bouton = Button(self.root, text="Quitter",
                                   command=self.closing, relief="groove", bg="red", width=10, borderwidth=10)
        self.close_bouton.place(relx=0.85, rely=0.9)
        # mise en place des boutons qui permettent à l'utilisateur de s'enregistrer
        self.sign_in = Button(self.fra, text="S'inscrire", bg="white", font=(
            "helvetica", 20, "bold"),  borderwidth=10, command=self.inscription)
        self.sign_in.grid(row=0, column=2, padx=20, pady=10)
        self.login = Button(self.fra, text="Se connecter", bg="white", font=(
            "helvetica", 20, "bold"),  borderwidth=10, command=self.connecter)
        self.login.grid(row=0, column=0, padx=30, pady=10)
        self.fra_si = Frame(self.root, width=600, height=300)
        self.bout_verifie = Label(self.root,
                                  bg="white", fg="red", font=("maven", 20, "bold"), justify="right")
        self.fra_si = Frame(self.root, width=self.SIDE,
                            height=self.SIDE/2, bg="gold")
        self.valider = Button(
            self.root, text="Valider", bg="white", font=("helvetica", 10, "bold"), command=self.valider_inscription)
        self.var_check = StringVar()
        self.frame_num1 = Frame(
            self.root, width=self.SIDE, height=self.SIDE/2, bg="red")
        self.frame_num = Frame(self.root, bg="green",
                               width=self.SIDE, height=self.SIDE/2)
        self.bout_pass = Button(
            self.frame_num1, text="Passer à 10", font=("Matura MT Script Capitals", 15, "bold"), command=self.convers_running, bg="gold", width=15)
        self.reset = Button(self.frame_num1, text="Effacer",
                            bg="red", fg="white", command=self.efface, width= 15)
        self.var = StringVar(self.frame_num1)
        self.varSA = StringVar()
        self.varRes = StringVar()
        self.cnv.pack(fill="both", expand="yes")
        self.ent_save = Entry(self.frame_num, textvariable=self.varSA)
        self.Sva = Button(self.root, text="Sauvegarder",
                          bg="gold", borderwidth=10)
        self.ent_remind = Entry(self.root, textvariable=self.varRes,
                                width=20, font=("Times", 20, "italic"))
        self.got = Button(self.root, text="ENVOYER",
                          bg="gold", borderwidth=10, width=20, height=5, command=self.confirm_birth)
        self.animation()

        self.root.mainloop()

    # une fonction qui active le son
    def ActivePygame(self):
        self.ques = askyesno(
            message="Voulez vous Activer le Nom", title="Activer")
        if self.ques == 1:
            self.with_song = True
        else:
            self.with_song = False

    # une fonction qui crée une animation sur le Canvas
    def animation(self, delay=200):
        self.ind += 1
        if self.ind == 18:
            self.ind = 0
        self.foto1.configure(
            file=f"assets/giflab/frame-{str(self.ind)}.gif")
        self.cn_im = self.cnv.create_image(
            self.SIDE/2, self.SIDE/4, image=self.foto1, tag="photo")
        self.root.after(delay, self.animation)

    # definir la fonction qui permet de s'inscrire
    def back(self):
        self.root.destroy()
        Main()

    # La fonction qui permet de s'inscrire
    def inscription(self):
        self.bout_verifie.place_forget()
        self.cnv.pack_forget()
        self.ent_remind.pack_forget()
        self.got.pack_forget()
        self.retour = Button(self.root, text="⏪Précedent", bg="red",
                             relief="raised", command=self.back, width=10, borderwidth=10)
        self.retour.place(relx=0.001, rely=0.92)
        self.root.config(bg="lightblue")
        # retirer les boutons  conncerter et s'inscrire
        for i in self.fra.winfo_children():
            i.grid_forget()
        self.fra.pack_forget()
        self.bout_verifie.pack_forget()
        # definir les label de Nom d'utilisateur et mot de passe
        self.cnv.pack_forget()
        self.lab_welcome.config(
            font=("maven", 10, "bold"), text="Veuillez remplir les champs suivants")
        self.lab_welcome.pack(anchor=CENTER)
        self.fra_si.pack()
        self.nom = Label(self.fra_si, text="Nom d'utilisateur",
                         bg="white", font=("helvetica", 10, "bold"))
        self.nom.grid(row=1, column=0)
        self.var_pass = StringVar(self.root)
        self.var_nom = StringVar(self.root)
        self.nom_ent = Entry(self.fra_si, textvariable=self.var_nom)
        self.password = Label(
            self.fra_si, text="Mot de passe ", bg="white", font=("helvetica", 10, "bold"))
        self.password.grid(row=2, column=0, padx=20, pady=10)
        self.nom_ent.grid(row=1, column=1, padx=20, pady=10)
        self.pass_ent = Entry(
            self.fra_si, textvariable=self.var_pass, justify="right")
        self.password_confirme = Label(
            self.fra_si, text="confirmer mot de passe ", bg="white", font=("helvetica", 10, "bold"), justify="left")
        self.password_confirme.grid(row=3, column=0, padx=20, pady=10)
        self.var_pass_conf = StringVar(self.root)
        self.var_check = StringVar()
        self.pass_ent_conf = Entry(
            self.fra_si, textvariable=self.var_pass_conf, justify="right")
        self.pass_ent_conf.grid(row=3, column=1, padx=10, pady=10)
        self.see_password = Checkbutton(
            self.fra_si, text="afficher ", bg="black", fg="white", command=self.show_passord, variable=self.var_check,
            offrelief="sunken", offvalue=0, overrelief="flat", )
        self.see_password.grid(row=2, column=2)
        self.pass_ent.grid(row=2, column=1)
        self.birth = Label(
            self.fra_si, text="Date de Naissance", bg="white", font=("helvetica", 10, "bold"))
        self.birth.grid(row=4, column=0, padx=20, pady=10)
        self.var_birth = StringVar(self.fra_si)
        self.birth_ent = Entry(self.fra_si, textvariable=self.var_birth)
        self.birth_ent.grid(row=4, column=1, padx=10, pady=10)
        self.valider.pack()
        self.cnv.pack(fill=X)

    # une fonction qui affiche ou cache le mot de passe

    def show_passord(self):

        if self.var_check.get() == "1":
            self.pass_ent["show"] = ""
        else:
            self.pass_ent["show"] = "*"

    # une fontion qui affiche la de zone réinitialisation
    def password_forgot(self):
        self.valider.pack_forget()
        self.cnv.pack_forget()
        self.fra_si.pack_forget()

        self.ent_remind.pack(fill=X)
        self.ent_remind.focus_set()
        self.got.pack(fill=X)

    # une fonction qui verifie si l'utilisateur à un compte
    def confirm_birth(self):
        self.av = self.ent_remind.get()
        fil = "Users.csv"
        op = open(fil, "r")
        for i in op:
            o = i.split(";")
            u, h = o[2], o[1]
            if u == self.av:
                self.lab_welcome.config(
                    text=f"Votre de passe est {h}", bg="green", font=("dubai", 20, "bold"))
                self.lab_welcome.after(4000, self.connecter)
            else:
                self.lab_welcome.config(text="Date Introuvée, recreer un autre compte si cela persiste",
                                        bg="green", font=("dubai", 20, "bold"))
                a = askyesno(title="retourner vers l'inscription",
                             message="Voulez-vous passer à l'inscription")
                if a == 1:
                    self.inscription()
                else:
                    self.root.after(500, self.password_forgot)

    # La fonction qui valide l'inscription
    def valider_inscription(self):
        fil = "Users.csv"
        self.users = open(file=fil, mode="a")
        self.a, self.b, self.c, self.d = self.nom_ent.get(), self.pass_ent.get(
        ), self.birth_ent.get(), self.pass_ent_conf.get()

        if self.a == "" or self.b == "" or self.c == "" or self.d == "":
            self.cnv.pack_forget()
            self.bout_verifie["text"] = "⛔⛔remplissage incomplet⛔⛔"
            self.root.config(bg="red")
            self.bout_verifie.pack(padx=20, anchor="w")
            self.bout_verifie.after(500, self.inscription)

            self.valider.grid_forget()
            self.var_nom.set(self.a)
            self.var_birth.set(self.c)
            self.var_pass.set(self.b)

            print("c'est fait bro")
        else:
            if self.b == self.d:
                for a in self.fra_si.winfo_children():
                    a.grid_forget()
                self.users.write(self.a + ";" + self.b + ";" + self.c + "\n")
                self.users.close()
                self.lab_welcome.grid_anchor(anchor=CENTER)
                self.lab_welcome.config(
                    text="Validation...", bg="green", font=("helvetica", 50, "bold"))
                print('valider')

                self.lab_welcome.after(500, self.starting)
            else:
                self.bout_verifie["text"] = "⛔⛔ mot de passe different!!!"
                self.cnv.pack_forget()
                self.bout_verifie.place(anchor="center", relx=0.2, rely=0.8)
                self.root.config(bg="red")
                self.bout_verifie.after(500, self.inscription)
                self.var_nom.set(self.a)
                self.var_birth.set(self.c)
                self.var_pass.set(self.b)
                self.pass_ent_conf.focus_set()

    # La fonction qui permert à l'utilisatteur d'entrer ses données pour se connecter
    def connecter(self):
        self.cnv.pack_forget()
        self.ent_remind.pack_forget()
        self.got.pack_forget()
        self.retour = Button(self.root, text="⏪Précedent", bg="red",
                             relief="raised", command=self.back, width=10, borderwidth=10)
        self.retour.place(relx=0.001, rely=0.92)
        self.bout_verifie.place_forget()
        self.fra.pack_forget()
        self.sign_in.grid_forget()
        self.login.grid_forget()
        self.fra_si.pack(fill=X, expand="yes")
        self.lab_welcome.config(
            font=("maven", 20, "bold"), text="Veuillez remplir les champs suivants", bg="lightblue")
        self.nom = Label(self.fra_si, text="Nom d'utilisateur",
                         bg="white", font=("helvetica", 10, "bold"))
        self.nom.grid(row=1, column=0)
        self.var_nom = StringVar(self.fra_si)
        self.var_pass = StringVar(self.fra_si)
        self.nom_ent = Entry(self.fra_si, textvariable=self.var_nom)
        self.nom_ent.grid(row=1, column=1, padx=20, pady=10)
        self.password = Label(
            self.fra_si, text="Mot de passe ", bg="white", font=("helvetica", 10, "bold"), justify="left")
        self.password.grid(row=2, column=0, padx=20, pady=10)
        self.pass_ent = Entry(
            self.fra_si, textvariable=self.var_pass)
        self.pass_ent.grid(row=2, column=1, padx=10, pady=10)
        self.see_password = Checkbutton(
            self.fra_si, text="afficher ", bg="white", variable=self.var_check, command=self.show_passord, offvalue=0, onvalue=1)
        self.see_password.grid(row=2, column=2)
        self.valider.pack()
        self.valider.config(command=self.valider_connexion, bg="green")
        if self.conf == True:
            self.cnv.pack()
        if self.conf == False:
            self.cnv.pack(fill=X, expand="yes")
        self.mot_pass_forg = Button(self.fra_si, text="mot de passe oublier?", font=(
            "maven", 8,  "bold"), bg="white", command=self.password_forgot)
        self.mot_pass_forg.grid(row=3)

    # la fonction qui valide la connexion en verifiant les données
    def valider_connexion(self):
        self.lab_welcome["text"] = "connecting..."
        self.lab_welcome["font"] = ("helvetica", 20)
        nom = str(self.nom_ent.get())
        motDe = str(self.pass_ent.get())
        self.lis = []
        with open("Users.csv", "r") as file:
            for i in file:
                ligne = i.split(";")
                for g in ligne:
                    self.lis.append(g)
                self.o = self.lis[0]
                self.f = self.lis[1]
                if self.o == nom and self.f == motDe:
                    self.root.after(500, self.essaie)
                    self.conf = True
                else:
                    self.root.after(1000, self.essaie)
                    self.root.config(bg="red")
                    self.conf = False
                    self.lab_welcome["text"] = "!!!😬🤔Données Incorrect!!!"
    # foncton qui envoyer un msg à l'utilisateur si les données sont fausses

    def essaie(self):
        self.valider.pack_forget()
        self.fra_si.pack_forget()
        self.cnv.pack_forget()
        if self.conf == False:
            self.essaie1()
        else:
            self.starting()

    # callbck de le fonction qui rédirige vers de menu de connection
    def essaie1(self):
        self.cnv = Canvas(self.root, bg="ivory",
                          height=self.SIDE/3, width=self.SIDE/6)
        self.cnv.pack(fill=X, expand="yes")
        self.connecter()

    # usage de la méthode after pour faire parraitre à une animation
    def starting(self):
        # oublier les boutons de la fenetre pour eviter de coallision
        self.fra_si.after_cancel(10)
        self.fra_si.pack_forget()
        self.valider.pack_forget()
        self.cnv.pack_forget()
        self.Sva.pack_forget()
        self.lab_welcome["text"] = "Starting..."
        self.root.config(bg="lightgreen")
        self.lab_welcome.after(500, self.convertor)

    # Fonction intermediaire qui fait un callback sur la fontion effacer avec  la methode after
    def efface(self):
        self.lab_welcome.config(text="Nettoyage...", font=(
            "maven", 20, "italic"), bg="black", fg="white")
        self.lab_welcome.after(1000, self.effacer)

    # fonction qui Effacer les zones d'entrer
    def effacer(self):
        self.var.set("")
        self.ent1["bg"] = "white"
        self.lab_welcome.config(font=(
            "times new roman", 15, "bold"), text="Veuillez entrer le numero")

    # Définir la fonction ''passer'' qui va permettre de saisir les numero de 8 chiffres
    def convertor(self):
        self.retour["text"] = "Logout"
        self.ent_save.pack_forget()
        self.Sva.pack_forget()
        self.lab_welcome.config(bg="Orange", font=(
            "times new roman", 20, "bold"), text="Veuillez entrer le numero")
        self.frame_num1.pack(fill=X, expand="yes")
        self.frame_num1.config(bg="orange")
        self.ent1 = Entry(self.frame_num1, textvariable=self.var, bg="white", relief="groove",
                          borderwidth=10, justify="right", font=("helvetica", 15, "bold"))
        self.ent1.grid(row=0, column=2,
                       padx=10, pady=10, sticky=W)
        self.ent2 = Label(self.frame_num1, text="ID_CIV:+225",
                          border=10, font=("platino", 15, "bold"))
        self.ent2.grid(row=1, column=0, padx=10, pady=10)
        self.prefix = Label(self.frame_num1, text="Préfixe operateur",
                            bg="yellow", font=("maven", 10, "bold"), height=1)
        self.prefix.grid(row=0, column=0, padx=10, pady=10)
        self.num = Label(self.frame_num1, text="Zone de conversion➡️", font=(
            "helvetica", 8, "bold"), relief="groove")
        self.num.grid(row=0, column=1, pady=10)
        self.enregister = Button(
            self.frame_num1, text="Save Contact", bg="gold", border=10, borderwidth=10, command=self.SavIng)
        self.var_search = StringVar(self.frame_num1)
        self.search_ent = Entry(self.frame_num1, textvariable=self.var_search,
                                takefocus=10, border=10, borderwidth=20)
        self.search = Button(self.frame_num1, text="Search", borderwidth=10, relief="raised",
                             border=10, command=self.SearchOn)
        self.search.grid(row=4, column=2, padx=10, pady=10)
        self.see_contact = Button(self.frame_num1, text="Voir la liste ", borderwidth=10,
                                  border=10, command=lambda: self.about(True))
        self.see_contact.grid(row=3, column=1, padx=10, pady=10)
        self.search_ent.grid(row=3, column=2, padx=10, pady=10)
        self.enregister.grid(row=3, column=0, padx=10, pady=10)
        # activer les bouton ''passer à 10 '' et ''effacer'' definient dans la fontion __init___
        self.bout_pass.grid(row=1, column=2, pady=10)
        self.reset.grid(row=1, column=1, pady=10)

    # la fonction qui permet de recuperer le numéro et de  le convertir le numéro à 10
    def passer(self):
        a = str(self.ent1.get())
        # pour les numéros mobiles
        mobile_indicatif_mtn = ["04", "05", "06", "44", "45", "46", "54", "55", "56", "64", "65", "66",
                                "74", "75", "76", "84", "85", "86", "94", "95", "96"]
        mobile_indicatif_org = ["07", "08", "09", "47", "48", "49", "57", "57", "58", "67", "68", "69",
                                "77", "78", "79", "87", "88", "89", "97", "98"]
        mobile_indicatif_mov = ["01", "02", "03", "41",
                                "42", "43", "51", "52", "53", "71", "72", "73"]
        # pour les numéros fixes
        fixe_indicatif_mtn = ["200", "210", "220", "230",
                              "240", "300", "310", "320", "330", "340", "350", "360"]
        fixe_indicatif_org = ["202", "203", "212", "213", "215", "217", "224", "225", "234", "235", "243", "244",
                              "245", "306", "316", "319", "319", "327", "337", "347", "359", "368"]
        fixe_indicatif_mov = ["208", "218", "228", "238"]
        self.all = fixe_indicatif_mov + fixe_indicatif_org + fixe_indicatif_mtn + \
            mobile_indicatif_mov + mobile_indicatif_mtn + mobile_indicatif_org
        # verfier que le numéro entrer est correcte et existe
        if len(a) == 8:
            # convertir les numéros mobiles à 10 chiffres
            for i in mobile_indicatif_mtn:
                # prendre les 02 premiers chiffres du numéro et verifier à quel opérateur il appartient
                if i == a[0:2]:
                    # retourner le numero à 10 chiffres
                    self.var.set("05" + a)
                    self.ent1["bg"] = "green"
                    self.lab_welcome.config(
                        text="Le Numéro est un MOBILE MTN, Save Now", bg="blue")
                    # jouer un son qui donne des informations à l'utilisateur sur le numéro
                    if self.with_song == True:
                        mon_audio = pygame.mixer.Sound("assets/mtn_son.mp3")
                        mon_audio.play(1)
            for f in mobile_indicatif_org:
                if f == a[0:2]:
                    self.var.set("07" + a)
                    self.ent1["bg"] = "green"
                    self.lab_welcome.config(
                        text="Le Numéro est un MOBILE ORANGE, Save Now", bg="blue")
                    if self.with_song == True:
                        mon_audio = pygame.mixer.Sound(
                            "assets/orange_son.mp3")
                        mon_audio.play(1)
            for g in mobile_indicatif_mov:
                if g == a[0:2]:
                    self.var.set("01" + a)
                    self.ent1["bg"] = "green"
                    self.lab_welcome.config(
                        text="Le Numéro est un MOBILE MOOV, Save Now", bg="blue")
                    if self.with_song == True:
                        mon_audio = pygame.mixer.Sound(
                            "assets/moov_son.mp3")
                        mon_audio.play(1)

            # convertir les numeros fixe à 10 chiffres
            for o in fixe_indicatif_mtn:

                # si les 3 premiers chiffres du numéro corresponde à ceux d'un opérateur fixe, ajouter le prefixe
                if o == a[0:3]:
                    self.var.set("25" + a)
                    self.ent1["bg"] = "green"
                    if self.with_song == True:
                        mon_audio = pygame.mixer.Sound("assets/mtn_son.mp3")
                        mon_audio.play(1)
                    self.lab_welcome.config(
                        text="Le Numéro est un fixe ORANGE, Save Now", bg="blue")
            for j in fixe_indicatif_org:
                if j == a[0:3]:
                    self.var.set("27" + a)
                    self.ent1["bg"] = "green"
                    if self.with_song == True:
                        mon_audio = pygame.mixer.Sound(
                            "assets/orange_son.mp3")
                        mon_audio.play(1)
            for k in fixe_indicatif_mov:
                if k == a[0:3]:
                    self.var.set("21" + a)
                    self.ent1["bg"] = "green"
                    self.lab_welcome.config(
                        text="Le Numéro est un fixe MOOV, Save Now", bg="blue")
                    if self.with_song == True:
                        mon_audio = pygame.mixer.Sound(
                            "./assets/moov_son.mp3")
                        mon_audio.play(1)
            for m in self.all:
                if a[0:2] != m:
                    self.lab_welcome.config(
                        text="Ce numero n'est pas ivoirien", bg="Yellow")

        elif len(a) == 10:
            self.lab_welcome.config(
                text="le Numéro est déja 10 chiffres", bg="red")
            self.var.set(a)

        elif (len(a) < 8 or len(a) > 8) and len(a) != 0:
            # quand la taille du numero n'atteint pas 8 chiffres , activer le bouton de message d'erreur
            self.lab_welcome.config(font=(
                "times new roman", 20, "bold"), text="Verifiez la taille du numero")

            if self.with_song == True:
                mon_audio = pygame.mixer.Sound("assets/avertissement.mp3")
                mon_audio.play(1)
        elif len(a) == 0:
            # au cas où l'utilisateur envoie un champ vide, activer de le message d'erreur
            
            self.lab_welcome["text"] = "!!!Aucun numéro saisi!!!\nveuillez entré un numero"
            self.root.after(1000, self.convertor)

    # la focntion callback de la fonction --passer--, style animation
    def convers_running(self):
        self.lab_welcome["text"] = "En cours de conversion.🖥️🖥️.."
        self.lab_welcome.after(1000, self.passer)

    # La fonction qui permet de passer à la zone de sauvegarde
    def SavIng(self):
        self.ak = self.var.get()
        self.varSA = StringVar()
        self.ent_save = Entry(self.root, textvariable=self.varSA,
                              width=20, font=("Times", 20, "italic"))
        self.Sva = Button(self.root, text="Sauvegarder",
                          bg="gold", borderwidth=10, width=20, height=5, command=self.Saved)
        # si le numéro actuelle est correct
        if len(self.ak) == 10 and self.ak[0:2] in self.all:
            self.frame_num1.pack_forget()
            self.lab_welcome["text"] = "Entrez le Nom du Contact"
            self.ent_save.pack(fill=X)
            self.ent_save.focus_set()
            self.Sva.pack(fill=X)
        elif len(self.ak) == 0:
            self.lab_welcome["text"] = "Vous n'avez pas entrer de numero"
            self.root.after(1000, self.convertor)
        else:
            self.lab_welcome["text"] = "Taille du Numero different de 10 chiffres"
            self.root.after(3000, self.convertor)

    # la fonction qui sauvegarde le contact et son nom
    def Saved(self):
        d = open("ContactFile.csv", "a")
        con_na = self.varSA.get()
        self.dic = {con_na: self.ak}
        if len(con_na) != 0:
            d.write(con_na+";"+self.ak+"\n")
            d.close()
            self.lab_welcome["text"] = "✅✅😍Contact Saved☑️✅✅✅"
            self.lab_welcome["bg"] = "green"
            self.root.after(1000, self.starting)
            self.var.set("")
        else:
            self.lab_welcome["text"] = "Vous n'avez de pas entrez de nom"
            d.close()

    # La fonction qui permet de rechercher un éléments dans la liste
    def SearchOn(self):
        cont = self.var_search.get()
        a = open("ContactFile.csv", "r")
        for i in a:
            o = i.split(";")
            u, h = o[0], o[1]
            if u == cont:
                self.lab_welcome.config(text=f"Le Numero de {u} est:")
                self.var.set(h)
                self.ab = self.ent1.config(
                    bg="gold")
                self.root.after(3000, self.convertor)

            else:
                self.lab_welcome.config(
                    text="ce contact n'existe pas!!!")
                self.root.after(1000, self.convertor)
        a.close()

    # cette fonction  la liste de contact ou des informations sur l'application selon de le bouton
    def about(self, val):
        if val == True:
            doc = open("ContactFile.csv","r")

        else:
            doc = open("./assets/about.txt", "r")
        a = ""
        for line in doc: a = a + line
            
        self.toplev = Toplevel()
        self.toplev.geometry("600x400+400+100")
        self.toplev.resizable(0, 0)
        self.fralev = Frame(self.toplev, bg="black",
                            width=self.SIDE, height=self.SIDE)
        self.fralev.pack(fill="both", expand="True", side=LEFT)
        scroll = ScrolledText(self.fralev, font="Dubai")
        scroll.pack(side="right", fill=Y)
        scroll.insert(INSERT, a)
        scroll.config(state="disabled")
        bout = Button(self.toplev, text="Fermer", borderwidth=10, command=self.toplev.quit,
                      bg="red", border=10, font=("terminal", 10, "italic"))
        bout.place(relx=0.9, rely=0.9)
        

    # fonction qui ferme la fenetre si l'utilisateur réponds par oui
    def closing(self):
        sur = askyesnocancel(
            message="Voulez-vous fermer l'application", title="confirmer votre choix")
        if sur == 1:
            self.root.destroy()


# appel de la class
if __name__ == "__main__":
    Main()
