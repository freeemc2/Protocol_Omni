import chromadb
class MemoryKernel:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="./omni_memory")
        self.collection = self.client.get_or_create_collection("sovereign_history")
    
    def store_goal(self, goal, step):
        # The 30-Year Rule: Write it down + One Step
        self.collection.add(documents=[goal], metadatas=[{"step": step}], ids=[str(hash(goal))])