import numpy as np
import sqlite3
import os
import hashlib
from scipy.sparse import random as sparse_random
from scipy.sparse.linalg import norm
from scipy.sparse import csr_matrix

class HolographicMemory:
    def __init__(self, dimensions=16384):
        self.dimensions = dimensions
        self.memory = {}
        
        # Adjust the path to the data directory
        main_directory = os.path.dirname(os.path.dirname(__file__))  # Navigate up to the main directory
        self.db_path = os.path.join(main_directory, "data", "memory.db")
        
        # Ensure the data directory exists
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        
        self._initialize_db()

    def _initialize_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS memory_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            entity_id TEXT NOT NULL,
            memory_type TEXT NOT NULL,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)
        conn.commit()
        conn.close()

    def dynamic_encode(self, input_vector, output_vector):
        input_hd = self._to_hyperdimensional(input_vector)
        output_hd = self._to_hyperdimensional(output_vector)
        self.memory[tuple(input_hd)] = output_hd
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO memory_entries (entity_id, memory_type, content)
        VALUES (?, ?, ?)
        """, ("default_entity", "dynamic_encode", str(output_hd)))
        conn.commit()
        conn.close()

    def retrieve(self, input_vector):
        input_hd = self._to_hyperdimensional(input_vector)
        return self.memory.get(tuple(input_hd), None)

    def retrieve_all(self):
        return self.memory

    def _to_hyperdimensional(self, vector):
        if isinstance(vector, dict):
            vector = list(vector.values())
        
        # Convert the input vector to a string and hash it to create a deterministic seed
        vector_str = str(vector)
        seed = int(hashlib.sha256(vector_str.encode()).hexdigest(), 16) % (2**32)
        np.random.seed(seed)  # Seed the random number generator for deterministic behavior
        
        # Generate a deterministic hyperdimensional vector
        hd_vector = sparse_random(1, self.dimensions, density=0.1, format='csr', random_state=seed)
        hd_vector = hd_vector / norm(hd_vector)
        return hd_vector.toarray().flatten()

    def apply_noise_reduction(self, vector):
        # Example noise reduction technique
        return vector * 0.9  # Reduce noise by scaling

    def adaptive_compress(self, vector):
        # Example compression technique
        return vector[:self.dimensions // 2]  # Compress to half the dimensions

# Self-execute section for testing
if __name__ == "__main__":
    # Test the HolographicMemory
    memory = HolographicMemory()
    memory.dynamic_encode({"input": "test"}, {"output": "result"})
    print("Retrieved memory:", memory.retrieve({"input": "test"}))