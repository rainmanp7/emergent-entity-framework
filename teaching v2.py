from core.db_manager import DBManager
from core.holographic_memory import HolographicMemory
from core.meta_entity_core import EmergentMetaEntity
from core.entity_core import EmergentEntityCore
from domains.math_module import EmergentMathEntity
from domains.english_module import EmergentEnglishEntity
from domains.python_module import EmergentPythonEntity
from domains.science_module import EmergentScienceEntity

def bootstrap():
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

    # Initial knowledge tasks (teaching base concepts)
    meta_task = {
        'math': [
            {"type": "addition", "a": 5, "b": 10},
            {"type": "subtraction", "a": 20, "b": 7},
            {"type": "multiplication", "a": 6, "b": 8},
            {"type": "division", "a": 50, "b": 5}
        ],
        'english': [
            {"type": "vocabulary", "word": "ephemeral", "definition": "lasting for a very short time"},
            {"type": "vocabulary", "word": "altruism", "definition": "selfless concern for others"},
            {"type": "grammar", "rule": "subject-verb agreement", "example": "The cat (singular) eats. The cats (plural) eat."},
            {"type": "grammar", "rule": "past tense", "example": "walk -> walked, run -> ran"}
        ],
        'python': [
            {"type": "evaluate", "code": "print(2 + 2)"},
            {"type": "evaluate", "code": "print(10 * 3)"},
            {"type": "debug", "code": "x = 5\nprint(x + y)", "error": "NameError: name 'y' is not defined"},
            {"type": "function", "code": "def add(a, b):\n    return a + b", "example": "add(3, 4) returns 7"}
        ],
        'science': [
            {"type": "biology", "question": "What is photosynthesis?", "answer": "The process by which plants convert sunlight into energy."},
            {"type": "chemistry", "question": "What is H2O?", "answer": "The chemical formula for water."},
            {"type": "physics", "question": "What is gravity?", "answer": "The force that attracts objects toward the center of the Earth."},
            {"type": "astronomy", "question": "What is a black hole?", "answer": "A region of spacetime where gravity is so strong that nothing can escape."}
        ]
    }

    # Distribute tasks and learn from the input
    for domain, tasks in meta_task.items():
        for task in tasks:
            meta_entity.distribute_tasks({domain: task})

    print("Bootstrap completed. Entities have been taught.")

if __name__ == "__main__":
    bootstrap()