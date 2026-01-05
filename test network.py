import chromadb

# Initialize the Sovereign Memory on DRAGONSEYE
client = chromadb.PersistentClient(path="./omni_memory")
collection = client.get_or_create_collection(name="sovereign_logic")

# The 30-Year Rule: Write it down
goal = "Establish a sovereign neural network on DRAGONSEYE."
step = "Verify ChromaDB integration and persistent storage."

collection.add(
    documents=[goal],
    metadatas=[{"step": step, "multiplier": 1.324}],
    ids=["goal_001"]
)

# Take the Step: Retrieve the goal to verify logic
results = collection.query(query_texts=["How do I build a brain?"], n_results=1)

print("--- OMNI-RECALL ---")
print(f"Goal Retrieved: {results['documents'][0][0]}")
print(f"Metadata (EGT): {results['metadatas'][0][0]['multiplier']}x")
print("-------------------")
