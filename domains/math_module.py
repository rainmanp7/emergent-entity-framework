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

class EmergentMathEntity:
    """
    An emergent entity that dynamically processes math-related tasks.
    Behavior arises from task input and its internal logic.
    """
    def __init__(self):
        self.internal_state = {"tasks_processed": 0, "last_operation": None}

    def interact(self, task_input):
        if task_input is None:
            return "No task input provided for EmergentMathEntity."

        # Extract input details
        task_type = task_input.get("type", "unknown type")
        a = task_input.get("a", 0)
        b = task_input.get("b", 0)

        # Emergent behavior based on task type
        if task_type == "addition":
            result = a + b
            operation = "addition"
        elif task_type == "subtraction":
            result = a - b
            operation = "subtraction"
        elif task_type == "multiplication":
            result = a * b
            operation = "multiplication"
        elif task_type == "division":
            if b == 0:
                return "Error: Division by zero."
            result = a / b
            operation = "division"
        else:
            return f"Unsupported task type: {task_type}"

        # Update internal state
        self.internal_state["tasks_processed"] += 1
        self.internal_state["last_operation"] = operation

        # Return emergent response
        return f"EmergentMathEntity result: {result}"

# Example usage
if __name__ == "__main__":
    # Example tasks
    task_add = {"type": "addition", "a": 5, "b": 3}
    task_sub = {"type": "subtraction", "a": 10, "b": 4}
    task_mul = {"type": "multiplication", "a": 6, "b": 7}
    task_div = {"type": "division", "a": 8, "b": 2}
    task_div_zero = {"type": "division", "a": 8, "b": 0}
    task_unknown = {"type": "modulus", "a": 8, "b": 2}

    # Using the emergent entity
    emergent_entity = EmergentMathEntity()
    print(emergent_entity.interact(task_add))
    print(emergent_entity.interact(task_sub))
    print(emergent_entity.interact(task_mul))
    print(emergent_entity.interact(task_div))
    print(emergent_entity.interact(task_div_zero))
    print(emergent_entity.interact(task_unknown))
