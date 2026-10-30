import tkinter as tk
import os
import math

class UltimateVillainVault:
    def __init__(self, root):
        self.root = root
        self.root.title("The Devilish Birthday Vault 🖤")
        self.root.geometry("480x760")
        self.root.configure(bg="#08080a")  # Deep space void back-glow
        self.root.resizable(False, False)

        # Main active viewport container frame
        self.viewport = tk.Frame(self.root, bg="#08080a")
        self.viewport.pack(fill="both", expand=True)

        # Target verification metrics
        self.correct_name = "acquillyne mbithe"
        self.correct_pin = "3010"
        self.entered_pin = ""
        
        # Track bounce animation frames and loops
        self.animation_angle = 0
        self.bouncing_widgets = {}
        self.typing_job = None

        # Dictionary containing custom dark typewriter text contents for each object
        self.vault_contents = {
            "letter": (
                "Before the journey...\n\n"
                "To: Birthday Queen, Acquillyne\n\n"
                "Hey. I know it’s been a minute. Our chat log looks like a ghost town, and my end of things "
                "has been pretty much radio silent for a while. Honestly, I’ve always been a creature of the dark, "
                "lurking in the shadows while our old conversations faded away into nothing. But there’s no way "
                "I’m letting this day slip past in the dark.\n\n"
                "Happy birthday, Acquillyne.\n\n"
                "You are a literal masterpiece of God's creation, born into this twisted world on this exact day. "
                "I hope you enjoy every second of today, especially since you are finally becoming legal in our country. "
                "Welcome to the next level of the game. It’s a whole new phase of life, but with that brilliant mind of yours, "
                "I already know you’re going to conquer it and extract way more than you even think you deserve.\n\n"
                "I wanted to send this because, despite the silence, I still love and cherish you. You were the only one "
                "who was completely true to me back in high school. When I was entirely lost, drowning in my own ignorance "
                "and stupidity, you were the one person who could look straight through my lies. You saw exactly who I was "
                "behind the mask.\n\n"
                "I love you, and my jealousy... 👁️👁️\n"
                "...yeah, it’s still very real. I love you so much, you brilliant creature.\n\n"
                "Even though my soul belongs to the dark, my wish for you is different. May light, joy, and pure happiness "
                "fill all your paths as you step into this fresh chapter. Keep shining, keep growing in the love of God, "
                "and never stop evolving.\n\n"
                "Happy birthday, dear. Stay spooky."
            ),
            "pumpkin": (
                "I know your birthday is on 30th but i hate being common so we celebrate yours on 31st haha ... "
                "now listen to this...\n\n"
                "The damp, suffocating air of the woods swallowed Acquillyne’s headlights. She had wandered "
                "way too far down this pitch-black labyrinth, chasing the phantom of a man she used to trust. Adrian had "
                "taken a sharp turn into these trees hours ago, leaving behind a trail of psychological slaughter.\n\n"
                "It wasn’t just a heartbreak; it was an execution.\n\n"
                "She had dug into his secrets, unearthing a sickening cache of letters between Adrian and her worst enemy. "
                "The pages detailed grotesque plots against her—schemes to kidnap her, to drug her into compliance, to deport her "
                "to a sanitarium where corrupt doctors would surgically tear her memories apart. This malice came from the very "
                "man who carried her heart. He knew he was her first. He knew she possessed a volatile, sleeping dark side, "
                "yet he chose to wake it up entirely. Now, the monster inside her was wide awake.\n\n"
                "Acquillyne scanned the choking density of the interior woods. It felt as though the night itself was trying "
                "to cover up his sins, burying him in shadows. But nobody hides forever.\n\n"
                "She sat paralyzed in her car, chest heaving, breathing heavily as she tried to force the blinding rage into something "
                "analytical. Suddenly, a jagged, unnatural shape whipped past her driver-side window, running violently into the dark. "
                "Simultaneously, off to the right, a sick, flickering headlight pulsed through the fog.\n\n"
                "Fear had left her. Running away from whatever lurked out there would only invite the hunt, and in this state of mind, "
                "she was more than ready to kill it herself.\n\n"
                "She shifted into drive, creeping forward as dry branches cracked like breaking bones beneath her tires. Then, she saw it.\n\n"
                "Adrian’s car was crushed, brutally pinned beneath a massive, fallen tree. Before she could even reach for her door handle, "
                "a spark kissed the leaking fuel. The wreckage exploded into a wall of roaring, merciless fire...\n\n"
                "If it were a real situation what would you do my rose... "
            ),
            "axes": (
                "Acquillyne then drives behind and watches the flames as they flare up the dark forest then suddenly the fire "
                "catches all tree around her and she gives a smark and says is it that the world wants us to meet in another "
                "world and settle scores or what is this game called then the creature appears again and smashes her window "
                "opens the door and carries her away out of the car past the fire a distance away near the shore then she puts "
                "acquillyne down and as acq stands there in complete statue motion the creature turns asif to move away and "
                "before it leaves she calls on to it and say wait.. then she asks it what exactly are you and aren't you going "
                "to eat me. the creature looks at her with its wide open black eyes and gives a one big growl then before it "
                "walks it leans onto her and before any reaction police sirens and firefighters could be heard from a distance ... "
                "smoke does make an alarm quite fast  so it lened down pulls acq up and ran to the northern side of the foreste "
                "til the forest grew darker and darker and the colder the forest become the darker it became and the quiter "
                "it sound. From the moment acq faced Adrian side peace and too much silence become so loud to her and it "
                "could have been better if things could just be plotted out loud now betrayal can really never give an alert .\n\n"
                "Now reality struck acquillyne and he grabbed the fox issh horse like but at the same tome human like creature "
                "and said stop .. put me down then she turned and looked at it and asked are you real but ofcourse it was or "
                "maybe her eyes had also chosen the same path of betrayal but then the crature moved away in small steps as "
                "if it had seen acquillyne's dark side and maybe saw something that made it look so scared and afraid.But then "
                "what was it and why off all people chose and fear me from nowhere? she asked herself"
            ),
            "cracked_heart": (
                "The creature’s abyssal eyes widened, tracking Acquillyne as it shrank backward into the brush. "
                "Its towering, unnatural form trembled. The more she advanced, radiating a suffocating mix of blinding "
                "fury and absolute shock, the more the beast whimpered, genuinely terrified of the aura radiating from her.\n\n"
                "She stepped closer, commanding it down with a chilling calm. She reached out and patted its massive head. "
                "\"Maybe monsters aren’t that bad,\" she whispered, her voice dripping with venomous irony. \"Compared to some "
                "idiots I actually thought I had something with... what a phase.\"\n\n"
                "At her touch, the creature let out a soft, submissive growl. It leaned its heavy head into Acquillyne’s "
                "cold, small hands. For a moment, the madness of the burning forest faded. The two of them sat together "
                "under the roots of a towering tree. Staring into the gloom, Acquillyne spilled her darkest poison. She told "
                "the beast about her burning urge to drill into Adrian’s heart—just five millimeters every five seconds—watching "
                "him break, bleed, and die a slow, agonizing death just to soothe her wrath.\n\n"
                "The creature looked down, listening to her malice as if it understood the weight of a broken soul.\n\n"
                "Just as Acquillyne stood up to find her way back to the city, the creature violently collapsed. It began "
                "convulsing on the damp earth, its form shifting unnaturally. Before her eyes, the monstrous appearance receded, "
                "reshaping itself into a severely injured human figure, his back covered in deep, painful lacerations.\n\n"
                "Acquillyne recoiled, taking a few sharp steps back.\n\n"
                "From beneath the dirt, the groaning human creature lifted his head. It was Adrian.\n\n"
                "\"Are you willing to end me?\" he choked out, his voice cracked with agony. \"What if I said every word written "
                "against you on those letters... made me inflict this pain on myself for the damage I'd caused you? What if I said "
            ),
            "bouquet": (
                "happy turning dear acquillyne silver and gold I may lack but time to make you special i have i love you so much"
            ),
            "deed": (
                "My creative skills might not match yours, but you are the literal reason my writing grew from "
                "basic Alice in Wonderland stories into something substantial. It’s not totally perfect yet, but it’s at a "
                "solid 70%, and I am so incredibly grateful to you for that.\n\n"
                "For a while, genuinely thinking I had lost you as a friend completely broke me. Healing from that kind of "
                "silence wasn't easy at all. But you left such a deep mark on my life, and looking back, I'm just so thankful "
                "for the impact you had on me.\n\n"
                "I truly hope you find good, genuine people to surround yourself with. Please stay safe out there. We live in "
                "a pretty dark world now, where people don't even hesitate to do wrong and anything can happen in the blink of "
                "an eye. I pray that God always keeps a protective shield over you and keeps your spirit high and unbroken.\n\n"
                "Oh, and just a fair warning—there is a specific part of your old manuscripts that I am absolutely stealing "
                "for my own book. Consider it a compliment.\n\n"
                "Happy birthday, Acquillyne."
            )
        }
        

        # Step 1: Initialize Identity Screen
        self.setup_name_screen()

    def clear_viewport(self):
        if self.typing_job:
            self.root.after_cancel(self.typing_job)
            self.typing_job = None
        for widget in self.viewport.winfo_children():
            widget.destroy()
        self.bouncing_widgets.clear()

    # 🔒 PHASE 1: Identity Screen
    def setup_name_screen(self):
        self.clear_viewport()
        frame = tk.Frame(self.viewport, bg="#111116", bd=0, highlightthickness=1, highlightbackground="#00d2ff")
        frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=450)

        tk.Label(frame, text="ACCESS REQUISITION 💀", font=("Courier New", 16, "bold"), fg="#00d2ff", bg="#111116").pack(pady=(60, 15))
        tk.Label(frame, text="Identify yourself, mortal.\nSYSTEM LOGGING ACTIVE.", font=("Courier New", 10, "italic"), fg="#7c7c8c", bg="#111116", justify="center").pack(pady=(0, 40))

        tk.Label(frame, text="TARGET FULL NAME", font=("Courier New", 10, "bold"), fg="#aaaaaa", bg="#111116").pack(anchor="w", padx=45)
        self.name_entry = tk.Entry(frame, font=("Helvetica", 12), bg="#1e1e24", fg="#ffffff", bd=0, insertbackground="#00d2ff", justify="center")
        self.name_entry.pack(fill="x", padx=45, pady=(8, 45))

        tk.Button(frame, text="PROCEED TO SECURE CRYPT >>", font=("Courier New", 11, "bold"), fg="#08080a", bg="#00d2ff", activebackground="#00a2cc", activeforeground="#08080a", bd=0, cursor="hand2", padx=10, pady=12, command=self.verify_name).pack(fill="x", padx=45)

    def verify_name(self):
        if self.name_entry.get().strip().lower() == self.correct_name:
            self.setup_pin_screen()
        else:
            self.setup_failed_screen()

    # 🎛️ PHASE 2: Keypad Screen
    def setup_pin_screen(self):
        self.clear_viewport()
        frame = tk.Frame(self.viewport, bg="#111116", bd=0, highlightthickness=1, highlightbackground="#00d2ff")
        frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=580)

        tk.Label(frame, text="ENTER CRYPTIC PIN 🔐", font=("Courier New", 15, "bold"), fg="#00d2ff", bg="#111116").pack(pady=(35, 10))

        # PIN display boxes
        slots_frame = tk.Frame(frame, bg="#111116")
        slots_frame.pack(pady=15)
        self.slots = []
        for i in range(4):
            slot = tk.Label(slots_frame, text="", font=("Courier New", 16, "bold"), bg="#1e1e24", fg="#00d2ff", width=3, height=1, highlightthickness=1, highlightbackground="#2e2e3a")
            slot.pack(side="left", padx=8)
            self.slots.append(slot)

        keypad_frame = tk.Frame(frame, bg="#111116")
        keypad_frame.pack(pady=10)

        buttons = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'X', '0', '✓']
        row, col = 0, 0
        for btn in buttons:
            cmd = lambda x=btn: self.press_key(x)
            if btn == '✓':
                b = tk.Button(keypad_frame, text=btn, font=("Courier New", 14, "bold"), bg="#00cc77", fg="#08080a", activebackground="#00ff99", width=5, height=2, bd=0, cursor="hand2", command=cmd)
            elif btn == 'X':
                b = tk.Button(keypad_frame, text=btn, font=("Courier New", 14, "bold"), bg="#ff3b3b", fg="#ffffff", activebackground="#ff5c5c", width=5, height=2, bd=0, cursor="hand2", command=cmd)
            else:
                b = tk.Button(keypad_frame, text=btn, font=("Courier New", 14, "bold"), bg="#1e1e24", fg="#ffffff", activebackground="#2e2e3a", width=5, height=2, bd=0, cursor="hand2", command=cmd)
            b.grid(row=row, column=col, padx=8, pady=8)
            col += 1
            if col > 2: col = 0; row += 1

    def press_key(self, key):
        if key == 'X':
            self.entered_pin = ""
        elif key == '✓':
            if self.entered_pin == self.correct_pin:
                self.setup_birthday_card()
            else:
                self.setup_failed_screen()
        else:
            if len(self.entered_pin) < 4:
                self.entered_pin += key

        for i in range(4):
            if i < len(self.entered_pin):
                self.slots[i].config(text="●", bg="#142c33", fg="#00d2ff")
            else:
                self.slots[i].config(text="", bg="#1e1e24", fg="#00d2ff")

    # ☠️ PHASE 3: Custom Villainous Failure State
    def setup_failed_screen(self):
        self.clear_viewport()
        self.entered_pin = ""
        frame = tk.Frame(self.viewport, bg="#111116", bd=0, highlightthickness=1, highlightbackground="#ff3b3b")
        frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=520)

        tk.Label(frame, text="WRONG PASSCODE! ☠️", font=("Courier New", 18, "bold"), fg="#ff3b3b", bg="#111116").pack(pady=(45, 15))
        tk.Label(frame, text="💀🪓", font=("Segoe UI", 70), bg="#111116").pack(pady=15)
        tk.Label(frame, text="Pinching you with an axe...\nAnd dragging your soul back to the cells.", font=("Courier New", 11, "italic"), fg="#b5b5c3", bg="#111116", justify="center").pack(pady=20)
        tk.Button(frame, text="TRY AGAIN ⚔️", font=("Courier New", 11, "bold"), fg="#ffffff", bg="#ff3b3b", activebackground="#ff5c5c", activeforeground="#ffffff", bd=0, cursor="hand2", padx=20, pady=10, command=self.setup_name_screen).pack(pady=10)

    # 🖤 PHASE 4: Success Landing Gate
    def setup_birthday_card(self):
        self.clear_viewport()
        frame = tk.Frame(self.viewport, bg="#111116", bd=0, highlightthickness=1, highlightbackground="#00d2ff")
        frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=620)

        tk.Label(frame, text="🐈‍⬛⛓️🐈", font=("Segoe UI", 55), bg="#111116").pack(pady=(40, 10))
        tk.Label(frame, text="Happy Birthday, Queen. 👑", font=("Courier New", 16, "bold"), fg="#00d2ff", bg="#111116").pack(pady=5)
        
        msg = "Acquillyne Mbithe... another year older, another year of plotting world domination. Let's see what loot we have safely hidden away inside our secret archives..."
        tk.Label(frame, text=msg, font=("Courier New", 10), fg="#ffffff", bg="#111116", wraplength=320, justify="center").pack(pady=20)

        tk.Button(frame, text="ENTER SOUL 🌐", font=("Courier New", 11, "bold"), fg="#08080a", bg="#ffffff", activebackground="#dddddd", activeforeground="#08080a", bd=0, cursor="hand2", padx=20, pady=12, command=self.setup_birthday_world).pack(pady=25)

    # 🌐 PHASE 5: Birthday World Grid
    def setup_birthday_world(self):
        self.clear_viewport()

        title_label = tk.Label(self.viewport, text="CHOOSE YOUR SPOILS 🕸️", font=("Courier New", 16, "bold"), fg="#00d2ff", bg="#08080a")
        title_label.pack(pady=(40, 10))
        
        desc_label = tk.Label(self.viewport, text="Select an artifact to examine its contents.", font=("Courier New", 9, "italic"), fg="#7c7c8c", bg="#08080a")
        desc_label.pack(pady=(0, 20))

        grid_frame = tk.Frame(self.viewport, bg="#08080a")
        grid_frame.pack(expand=True, pady=10)

        items_config = [
            {"id": "letter", "icon": "✉️", "label": "The Letter"},
            {"id": "pumpkin", "icon": "🎃", "label": "Grim Pumpkin"},
            {"id": "axes", "icon": "⚔️", "label": "Crossed Axes"},
            {"id": "cracked_heart", "icon": "💔", "label": "Cracked Heart"},
            {"id": "bouquet", "icon": "💐", "label": "Dark Bouquet"},
            {"id": "deed", "icon": "📜", "label": "Title Deed"}
        ]

        row, col = 0, 0
        for config in items_config:
            item_frame = tk.Frame(grid_frame, bg="#111116", highlightthickness=1, highlightbackground="#2e2e3a", width=110, height=120)
            item_frame.grid_propagate(False)
            item_frame.grid(row=row, column=col, padx=12, pady=12)

            icon_lbl = tk.Label(item_frame, text=config["icon"], font=("Segoe UI", 32), bg="#111116", fg="#ffffff")
            icon_lbl.pack(pady=(15, 2))
            
            self.bouncing_widgets[icon_lbl] = (0, col * 30)

            text_btn = tk.Button(item_frame, text=config["label"], font=("Courier New", 9, "bold"), fg="#00d2ff", bg="#111116", activebackground="#1e1e24", activeforeground="#00d2ff", bd=0, cursor="hand2", command=lambda key=config["id"]: self.view_artifact(key))
            text_btn.pack(fill="x", side="bottom", pady=8)

            col += 1
            if col > 2: col = 0; row += 1
        for config in items_config:
            item_frame = tk.Frame(grid_frame, bg="#111116", highlightthickness=1, highlightbackground="#2e2e3a", width=110, height=120)
            item_frame.grid_propagate(False)
            item_frame.grid(row=row, column=col, padx=12, pady=12)

            icon_lbl = tk.Label(item_frame, text=config["icon"], font=("Segoe UI", 32), bg="#111116", fg="#ffffff")
            icon_lbl.pack(pady=(15, 2))
            
            self.bouncing_widgets[icon_lbl] = (0, col * 30)

            text_btn = tk.Button(item_frame, text=config["label"], font=("Courier New", 9, "bold"), fg="#00d2ff", bg="#111116", activebackground="#1e1e24", activeforeground="#00d2ff", bd=0, cursor="hand2", command=lambda key=config["id"]: self.view_artifact(key))
            text_btn.pack(fill="x", side="bottom", pady=8)

            col += 1
            if col > 2: col = 0; row += 1

        self.animate_bounce()

    def animate_bounce(self):
        if not self.bouncing_widgets:
            return
        self.animation_angle += 0.2
        for lbl, (base_y, offset) in list(self.bouncing_widgets.items()):
            try:
                displacement = int(math.sin(self.animation_angle + offset) * 6)
                lbl.pack_configure(pady=(15 + displacement, 2))
            except:
                pass
        self.root.after(40, self.animate_bounce)

    # 📜 PHASE 6: Typewriter Reading Portal View
    def view_artifact(self, key):
        self.clear_viewport()

        # FULLSCREEN OVERLAY MODE FOR FLOWER BOUQUET
        if key == "bouquet":
            display_card = tk.Frame(self.viewport, bg="#050508")
            display_card.pack(fill="both", expand=True)

            # Left and Right Fullscreen background flower columns
            left_roses = tk.Label(display_card, text="🌹\n🖤\n🌹\n🖤\n🌹\n🖤\n🌹\n🖤\n🌹\n🖤\n🌹", font=("Segoe UI", 20), bg="#050508", fg="#ff2a55", justify="center")
            left_roses.place(relx=0.08, rely=0.5, anchor="w")

            right_roses = tk.Label(display_card, text="🖤\n🌹\n🖤\n🌹\n🖤\n🌹\n🖤\n🌹\n🖤\n🌹\n🖤", font=("Segoe UI", 20), bg="#050508", fg="#ff2a55", justify="center")
            right_roses.place(relx=0.92, rely=0.5, anchor="e")

            # Centered Text Viewport Card Layer
            self.msg_display = tk.Label(display_card, text="", font=("Courier New", 12, "bold"), fg="#ffffff", bg="#050508", wraplength=260, justify="center", anchor="center")
            self.msg_display.place(relx=0.5, rely=0.45, anchor="center", width=280, height=480)

            back_btn = tk.Button(display_card, text="a devilish way to write lets proceed", font=("Courier New", 10, "italic", "underline"), fg="#7c7c8c", bg="#050508", activebackground="#050508", activeforeground="#00d2ff", bd=0, cursor="hand2", command=self.setup_birthday_world)
            back_btn.place(relx=0.5, rely=0.92, anchor="center")

        # STANDARD MODAL CARD VIEW MODE FOR ALL OTHER ITEMS
        else:
            display_card = tk.Frame(self.viewport, bg="#111116", bd=0, highlightthickness=1, highlightbackground="#00d2ff")
            display_card.place(relx=0.5, rely=0.5, anchor="center", width=420, height=620)

            if key == "pumpkin":
                glow_frame = tk.Frame(display_card, bg="#1a1105", highlightthickness=1, highlightbackground="#ff7700")
                glow_frame.place(relx=0.48, rely=0.45, anchor="center", width=380, height=440)
                
                self.msg_display = tk.Label(glow_frame, text="", font=("Courier New", 10, "bold"), fg="#ffaa00", bg="#1a1105", wraplength=350, justify="left", anchor="nw")
                self.msg_display.place(relx=0.5, rely=0.5, anchor="center", width=360, height=410)
            else:
                self.msg_display = tk.Label(display_card, text="", font=("Courier New", 10), fg="#ffffff", bg="#111116", wraplength=360, justify="left", anchor="nw")
                self.msg_display.place(relx=0.48, rely=0.45, anchor="center", width=360, height=440)

            back_btn = tk.Button(display_card, text="a devilish way to write lets proceed", font=("Courier New", 10, "italic", "underline"), fg="#7c7c8c", bg="#111116", activebackground="#111116", activeforeground="#00d2ff", bd=0, cursor="hand2", command=self.setup_birthday_world)
            back_btn.place(relx=0.5, rely=0.94, anchor="center")

        # Initialize Typewriter Output Loop
        text_content = self.vault_contents.get(key, "Secure data slot vacant.")
        self.type_counter = 0
        self.run_typewriter(text_content)

    def run_typewriter(self, full_text):
        if self.type_counter <= len(full_text):
            current_substring = full_text[:self.type_counter]
            self.msg_display.config(text=current_substring)
            self.type_counter += 1
            # 12 milliseconds between character renders
            self.typing_job = self.root.after(12, lambda: self.run_typewriter(full_text))

if __name__ == "__main__":
    root = tk.Tk()
    app = UltimateVillainVault(root)
    root.mainloop()
p