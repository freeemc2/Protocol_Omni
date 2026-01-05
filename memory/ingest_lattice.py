import chromadb
import os

# --- DRAGONSEYE MASTER PATH ---
MASTER_PATH = r"H:\Dragon Brain\Protocol_Omni_Sovereign"
MEMORY_PATH = os.path.join(MASTER_PATH, "omni_memory")

def populate_brain():
    print(f"[STEEL] Writing to Master Memory: {MEMORY_PATH}")
    
    # 1. Initialize the Master Memory bank
    client = chromadb.PersistentClient(path=MEMORY_PATH)
    collection = client.get_or_create_collection(name="lattice_nodes")
    
    # 2. Your Verified Node Data
    verified_nodes = [
        {"ip": "192.168.87.22", "type": "Scout", "status": "ONLINE"},
        {"ip": "192.168.87.24", "type": "Bridge", "status": "ONLINE"},
        {"ip": "192.168.87.28", "type": "Core", "status": "ONLINE"}
    ]

    for node in verified_nodes:
        metadata = {
            "type": node["type"],
            "status": node["status"],
            "egt_gain": 1.324,
            "harmonic": 79.44
        }
        
        # We use upsert so it updates if they already exist
        collection.upsert(
            documents=[f"Node {node['ip']} linked to Protocol Omni."],
            metadatas=[metadata],
            ids=[node["ip"]]
        )
        print(f"[STEEL] Node {node['ip']} Locked.")

if __name__ == "__main__":
    populate_brain()
