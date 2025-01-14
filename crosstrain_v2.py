from core.db_manager import DBManager
from core.holographic_memory import HolographicMemory
from core.meta_entity_core import EmergentMetaEntity
from core.entity_core import EmergentEntityCore
from domains.math_module import EmergentMathEntity
from domains.english_module import EmergentEnglishEntity
from domains.python_module import EmergentPythonEntity
from domains.science_module import EmergentScienceEntity

def cross_train():
    # Initialize Holographic Memory
    memory = HolographicMemory()

    # Initialize Database Managers for each domain
    math_db = DBManager("math.db")
    english_db = DBManager("english.db")
    python_db = DBManager("python.db")
    science_db = DBManager("science.db")

    # Create domain modules and entities
    math_module = EmergentMathEntity()
    english_module = EmergentEnglishEntity()
    python_module = EmergentPythonEntity()
    science_module = EmergentScienceEntity()

    # Create Entities for each domain
    math_entity = EmergentEntityCore(math_module, math_db, memory)
    english_entity = EmergentEntityCore(english_module, english_db, memory)
    python_entity = EmergentEntityCore(python_module, python_db, memory)
    science_entity = EmergentEntityCore(science_module, science_db, memory)

    # Create MetaEntityCore with entities
    entities = [math_entity, english_entity, python_entity, science_entity]
    meta_entity = EmergentMetaEntity(entities, math_db)  # Using math_db for task distribution

    # Cross-training task: entities share knowledge across domains
    cross_train_task = {
        'math': [
            {"type": "addition", "a": 15, "b": 20},
            {"type": "subtraction", "a": 100, "b": 45},
            {"type": "multiplication", "a": 12, "b": 12},
            {"type": "division", "a": 144, "b": 12}
        ],
        'english': [
            {"type": "vocabulary", "word": "resilient", "definition": "able to recover quickly from difficulties"},
            {"type": "grammar", "rule": "present continuous", "example": "I am running, She is eating"},
            {"type": "vocabulary", "word": "meticulous", "definition": "showing great attention to detail"},
            {"type": "grammar", "rule": "future tense", "example": "I will go, They will eat"}
        ],
        'python': [
            {"type": "evaluate", "code": "print(5 * 5)"},
            {"type": "debug", "code": "x = 10\ny = 5\nprint(x / z)", "error": "NameError: name 'z' is not defined"},
            {"type": "function", "code": "def multiply(a, b):\n    return a * b", "example": "multiply(6, 7) returns 42"},
            {"type": "evaluate", "code": "print('Hello, World!')"}
        ],
        'science': [
            {"type": "biology", "question": "What is DNA?", "answer": "Deoxyribonucleic acid, the molecule that carries genetic information."},
            {"type": "chemistry", "question": "What is the periodic table?", "answer": "A table of chemical elements arranged by atomic number."},
            {"type": "physics", "question": "What is Newton's first law?", "answer": "An object in motion stays in motion unless acted upon by an external force."},
            {"type": "astronomy", "question": "What is a galaxy?", "answer": "A system of millions or billions of stars, together with gas and dust, held together by gravity."}
        ]
    }

    # Distribute cross-training tasks and have each entity learn from one another
    for domain, tasks in cross_train_task.items():
        for task in tasks:
            meta_entity.distribute_tasks({domain: task})

    print("Cross-training completed. Entities have shared knowledge.")

if __name__ == "__main__":
    cross_train()