import os
import sys

def get_root_dir():
    """
    Gets the absolute path to the root directory of the project.

    Returns:
        str: The absolute path to the root directory.
    """
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def add_root_to_path():
    """
    Adds the root directory to the Python path.
    """
    root_dir = get_root_dir()
    sys.path.insert(0, root_dir)

add_root_to_path()

from core.holographic_memory import HolographicMemory

class EmergentEnglishEntity:
    """
    An emergent entity that processes language-related tasks by interacting with inputs
    and evolving its internal state. The behavior emerges dynamically from these interactions.
    """
    def __init__(self):
        self.internal_state = {"tasks_processed": 0, "last_processed": None}

    def interact(self, task_input):
        if task_input is None:
            return "No task input provided for EmergentEnglishEntity."

        task_type = task_input.get("type")
        # Default task result if type is unsupported
        result = f"Unsupported task type: {task_type}"
        
        # Interaction logic for vocabulary tasks
        if task_type == "vocabulary":
            word = task_input.get("word", "unknown word")
            definition = task_input.get("definition", "no definition provided")
            result = f"Processed vocabulary: {word} - {definition}"
        
        # Interaction logic for grammar tasks
        elif task_type == "grammar":
            rule = task_input.get("rule", "unknown rule")
            example = task_input.get("example", "no example provided")
            result = f"Processed grammar rule: {rule} - Example: {example}"

        # Update internal state dynamically
        self.internal_state["tasks_processed"] += 1
        self.internal_state["last_processed"] = result

        # Return the emergent response
        return f"EmergentEnglishEntity result: {result}"

# Example usage
if __name__ == "__main__":
    # Example tasks
    task_vocabulary = {"type": "vocabulary", "word": "empathy", "definition": "the ability to understand and share the feelings of another"}
    task_grammar = {"type": "grammar", "rule": "Subject-Verb Agreement", "example": "She runs every morning."}

    # Using the emergent entity
    emergent_entity = EmergentEnglishEntity()
    print(emergent_entity.interact(task_vocabulary))
    print(emergent_entity.interact(task_grammar))
