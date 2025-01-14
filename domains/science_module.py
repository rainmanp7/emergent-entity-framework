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

class EmergentScienceEntity:
    """
    An emergent entity that dynamically interacts with science-related inputs.
    Behavior arises from interaction between task inputs and internal state.
    """
    def __init__(self):
        self.internal_state = {"tasks_processed": 0, "last_field": None}

    def interact(self, task_input):
        if task_input is None:
            return "No task input provided for EmergentScienceEntity."

        # Extract input details
        task_type = task_input.get("type", "unknown type")
        question = task_input.get("question", "unknown question")
        answer = task_input.get("answer", "no answer provided")

        # Emergent behavior based on task type
        if task_type in ["biology", "chemistry", "physics", "astronomy"]:
            response = f"Answered {task_type} question: {question} - Answer: {answer}"
        else:
            response = f"Unsupported task type: {task_type}"

        # Update internal state
        self.internal_state["tasks_processed"] += 1
        self.internal_state["last_field"] = task_type

        # Return emergent response
        return f"EmergentScienceEntity result: {response}"

# Example usage
if __name__ == "__main__":
    # Example tasks
    task_biology = {"type": "biology", "question": "What is DNA?", "answer": "DNA is the genetic material of cells."}
    task_chemistry = {"type": "chemistry", "question": "What is H2O?", "answer": "H2O is water."}
    task_physics = {"type": "physics", "question": "What is gravity?", "answer": "Gravity is a force that attracts objects."}
    task_astronomy = {"type": "astronomy", "question": "What is a black hole?", "answer": "A black hole is a region of space where gravity is so strong that nothing can escape."}
    task_unknown = {"type": "geology", "question": "What are rocks?", "answer": "No answer provided."}

    # Using the emergent entity
    emergent_entity = EmergentScienceEntity()
    print(emergent_entity.interact(task_biology))
    print(emergent_entity.interact(task_chemistry))
    print(emergent_entity.interact(task_physics))
    print(emergent_entity.interact(task_astronomy))
    print(emergent_entity.interact(task_unknown))
