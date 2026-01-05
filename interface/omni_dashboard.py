import tkinter as tk
from tkinter import ttk
import chromadb
import sys
import os

# --- DRAGONSEYE HARD-CODED LATTICE PATH ---
# This ensures no matter where the script is, the brain is found.
MASTER_PATH = r"H:\Dragon Brain\Protocol_Omni_Sovereign"
MEMORY_PATH = os.path.join(MASTER_PATH, "omni_memory")

# Add the root to sys.path so we can import the EGT engine
if MASTER_PATH not in sys.path:
    sys.path.append(MASTER_PATH)

class SovereignHUD:
    def __init__(self, root):
        self.root = root
        self.root.title("DRAGONSEYE | OMNI-HUD v1.1")
        self.root.geometry("800x550")
        self.root.configure(bg="#020202") # Deep black for high contrast
        
        # 1. Connect to the Master Memory Bank
        print(f"[STEEL] Locking onto Memory: {MEMORY_PATH}")
        try:
            self.client = chromadb.PersistentClient(path=MEMORY_PATH)
            self.collection = self.client.get_or_create_collection(name="lattice_nodes")
        except Exception as e:
            print(f"[SHIELD] Memory Lock Failed: {e}")

        self.setup_ui()
        self.refresh_data()

    def setup_ui(self):
        # Neon Cyan Header
        tk.Label(self.root, text="PROTOCOL OMNI: SOVEREIGN LATTICE", 
                 font=("Courier", 24, "bold"), fg="#00f2ff", bg="#020202").pack(pady=25)

        # The Table (Treeview)
        cols = ("IP", "TYPE", "STATUS", "EGT_GAIN")
        self.tree = ttk.Treeview(self.root, columns=cols, show='headings', height=10)
        
        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=150)
        
        # Cyberpunk Styling
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="#0a0a0a", foreground="white", 
                        fieldbackground="#0a0a0a", font=("Courier", 11), rowheight=30)
        style.configure("Treeview.Heading", background="#1a1a1a", foreground="#00f2ff", 
                        font=("Courier", 12, "bold"))
        
        self.tree.pack(padx=30, pady=10, fill="both", expand=True)
        
        # Status Footer
        self.footer = tk.Label(self.root, text="SYNCING WITH 79.44Hz HARMONIC...", 
                              font=("Courier", 10), fg="#00ff41", bg="#020202")
        self.footer.pack(side="bottom", pady=15)

    def refresh_data(self):
        # Clear the old view
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # Pull from the local ChromaDB
        try:
            results = self.collection.get()
            if not results['ids']:
                self.footer.config(text="LATTICE EMPTY | PENDING DATA INGESTION", fg="red")
            else:
                for i in range(len(results['ids'])):
                    ip = results['ids'][i]
                    meta = results['metadatas'][i]
                    self.tree.insert("", "end", values=(ip, meta['type'], meta['status'], f"{meta['egt_gain']}x"))
                self.footer.config(text=f"DRAGONSEYE ONLINE | {len(results['ids'])} NODES VERIFIED", fg="#00ff41")
        except Exception as e:
            self.footer.config(text=f"LATTICE DISCONNECTED: {e}", fg="yellow")

        # Auto-refresh loop
        self.root.after(3000, self.refresh_data)

if __name__ == "__main__":
    root = tk.Tk()
    app = SovereignHUD(root)
    root.mainloop()
