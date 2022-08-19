import tkinter as tk
import random

root = tk.Tk()
root.resizable(False, False)
root.title("Blad, Steen, Schaar")
root.iconphoto(True, tk.PhotoImage(file='/usr/share/bss/icon.png'))

window_width = 600
window_height = 500

# bepaal de schermafmetingen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# bepaal de centerpunten
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# stel het programmascherm in op het center van het scherm
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

q_frame = tk.Frame(root)
r_frame = tk.Frame(root)

img_blad = tk.PhotoImage(file = "/usr/share/bss/blad.png")
img_steen = tk.PhotoImage(file = "/usr/share/bss/steen.png")
img_schaar = tk.PhotoImage(file = "/usr/share/bss/schaar.png")

spel_stats = {
	"aantal": 0,
	"gewonnen": 0,
	"verloren": 0,
	"gelijkstand": 0
}

def calc_stats():
	stat_overzicht = "U heeft in totaal " + str(spel_stats["aantal"]) + " maal gespeeld, waarvan, Gewonnen: " + str(spel_stats["gewonnen"]) + " maal;  Verloren: " + str(spel_stats["verloren"]) + " maal;  Gelijkstand: " + str(spel_stats["gelijkstand"]) + " maal!"
	return stat_overzicht

def computer_keuze():
	opties = ["steen","blad","schaar"]
	computer = random.choice(opties)
	return computer


def speelveld():
	# Opbouw van het speelveld voor de speler keuze
	q_frame.grid_columnconfigure((0, 1, 2), weight=1)

	tk.Label(q_frame, text="Blad Steen Schaar", font=("Ubuntu Bold", 20, "bold"), fg="#085F80").grid(row=0, column=0, columnspan=3)
	tk.Label(q_frame, text="Een spelletje Blad, Steen, Schaar tegen de computer spelen?").grid(row=1, column=0, columnspan=3)
	tk.Label(q_frame, text="Eenvoudig, maak hieronder uw keuze,").grid(row=2, column=0, columnspan=3)
	tk.Label(q_frame, text="terwijl de computer at random zijn eigen keuze maakt.").grid(row=3, column=0, columnspan=3)
	tk.Label(q_frame, text="Blad", font="bold").grid(row=4, column=0, pady=20)
	tk.Label(q_frame, text="Steen", font="bold").grid(row=4, column=1, pady=20)
	tk.Label(q_frame, text="Schaar", font="bold").grid(row=4, column=2, pady=20)
	tk.Button(q_frame, image=img_blad, width=180, height=180, command=lambda: (resultaat(computer_keuze(), "blad"))).grid(row=5, column=0)
	tk.Button(q_frame, image=img_steen, width=180, height=180, command=lambda: (resultaat(computer_keuze(), "steen"))).grid(row=5, column=1, padx=10)
	tk.Button(q_frame, image=img_schaar, width=180, height=180, command=lambda: (resultaat(computer_keuze(), "schaar"))).grid(row=5, column=2)
	tk.Label(q_frame, text=calc_stats(), font=("Ubuntu", 8, "italic"), fg="#404040").grid(row=6, column=0, columnspan=3, sticky="s", pady=20)
	q_frame.pack(fill="y", expand=True)


def clear_frame(type):
	if type == "q":
		for widget in q_frame.winfo_children():
			widget.destroy()
			q_frame.pack_forget()
	else:
		for widget in r_frame.winfo_children():
			widget.destroy()
			r_frame.pack_forget()


def resultaat(computer, speler):
	clear_frame("q")
	r_frame.grid_columnconfigure((0, 1), weight=1)
	spel_stats["aantal"] += 1

	if computer == speler:
		uitkomst = "Gelijkspel"
		winst = 2
		spel_stats["gelijkstand"] += 1
		if speler == "blad":
			t_image = img_blad
		elif speler == "steen":
			t_image = img_steen
		else:
			t_image = img_schaar
	elif speler == "blad":
		s_image = img_blad
		if computer == "steen":
			c_image = img_steen
			uitkomst = "Je hebt gewonnen! Het blad omsluit de steen!"
			winst = 1
			spel_stats["gewonnen"] += 1
		else:
			c_image = img_schaar
			uitkomst = "Je hebt verloren. De schaar snijdt in het blad!"
			winst = 0
			spel_stats["verloren"] += 1
	elif speler == "steen":
		s_image = img_steen
		if computer == "schaar":
			c_image = img_schaar
			uitkomst = "Je hebt gewonnen! De schaar snijdt zich bot op de steen!"
			winst = 1
			spel_stats["gewonnen"] += 1
		else:
			c_image = img_blad
			uitkomst = "Je hebt verloren. Het blad omsluit de steen!"
			winst = 0
			spel_stats["verloren"] += 1
	elif speler == "schaar":
		s_image = img_schaar
		if computer == "blad":
			c_image = img_blad
			uitkomst = "Je hebt gewonnen! De schaar snijdt in het blad!"
			winst = 1
			spel_stats["gewonnen"] += 1
		else:
			c_image = img_steen
			uitkomst = "Je bent verloren. De schaar snijdt zich bot op de steen!"
			winst = 0
			spel_stats["verloren"] += 1

	tk.Label(r_frame, text="Blad Steen Schaar", font=("Ubuntu Bold", 20, "bold"), fg="#085F80").grid(row=0, column=0, columnspan=2)
	if winst == 2:
		tk.Label(r_frame, text=uitkomst, font="bold", fg="blue").grid(row=1, column=0, columnspan=2)
		tk.Label(r_frame, text="Jouw keuze:").grid(row=2, column=0, pady=10)
		tk.Label(r_frame, text="Keuze van de PC:").grid(row=2, column=1, pady=10)
		tk.Label(r_frame, text="Jullie kozen allebei voor " + speler, fg="blue").grid(row=3, column=0, columnspan=2)
		tk.Label(r_frame, image=t_image, width=180, height=180).grid(row=4, column=0, padx=20, pady=10)
		tk.Label(r_frame, image=t_image, width=180, height=180).grid(row=4, column=1, padx=20, pady=10)
	elif winst == 1:
		tk.Label(r_frame, text=uitkomst, font="bold", fg="green").grid(row=1, column=0, columnspan=2)
		tk.Label(r_frame, text="Jouw keuze:").grid(row=2, column=0, pady=10)
		tk.Label(r_frame, text="Keuze van de PC:").grid(row=2, column=1, pady=10)
		tk.Label(r_frame, text=speler).grid(row=3, column=0)
		tk.Label(r_frame, text=computer).grid(row=3, column=1)
		tk.Label(r_frame, image=s_image, width=180, height=180, bg="green").grid(row=4, column=0, padx=20, pady=10)
		tk.Label(r_frame, image=c_image, width=180, height=180, bg="red").grid(row=4, column=1, padx=20, pady=10)
	else:
		tk.Label(r_frame, text=uitkomst, font="bold", fg="red").grid(row=1, column=0, columnspan=2)
		tk.Label(r_frame, text="Jouw keuze:").grid(row=2, column=0, pady=10)
		tk.Label(r_frame, text="Keuze van de PC:").grid(row=2, column=1, pady=10)
		tk.Label(r_frame, text=speler).grid(row=3, column=0)
		tk.Label(r_frame, text=computer).grid(row=3, column=1)
		tk.Label(r_frame, image=s_image, width=180, height=180, bg="red").grid(row=4, column=0, padx=20, pady=10)
		tk.Label(r_frame, image=c_image, width=180, height=180, bg="green").grid(row=4, column=1, padx=20, pady=10)

	tk.Button(r_frame, text="Speel opnieuw", command=lambda: (clear_frame("r"), speelveld())).grid(row=5, column=0, pady=10, sticky="we")
	tk.Button(r_frame, text="Stop spel", command=root.destroy).grid(row=5, column=1, pady=10, sticky="we")

	tk.Label(r_frame, text=calc_stats(), font=("Ubuntu", 8, "italic"), fg="#404040").grid(row=6, column=0, columnspan=2, sticky="s", pady=10)

	r_frame.pack(fill="y", expand=True)

# Programmaverloop
speelveld()

root.mainloop()