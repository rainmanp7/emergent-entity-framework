import os
import sys
import io

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

class EmergentPythonEntity:
    """
    An emergent entity that dynamically interacts with inputs to evaluate, debug, or analyze Python code.
    Behavior and conclusions emerge from the interaction between inputs and internal state.
    """
    def __init__(self):
        self.internal_state = {"tasks_processed": 0, "last_result": None}

    def interact(self, task_input):
        if task_input is None:
            return "No task input provided for EmergentPythonEntity."

        task_type = task_input.get("type")
        result = f"Unsupported task type: {task_type}"  # Default response for unsupported task types

        # Emergent behavior for evaluating code
        if task_type == "evaluate":
            try:
                old_stdout = sys.stdout
                new_stdout = io.StringIO()
                sys.stdout = new_stdout

                # Evaluate the provided code
                evaluation_result = eval(task_input["code"])

                # Restore stdout and get captured output
                sys.stdout = old_stdout
                captured_output = new_stdout.getvalue().strip()

                # Determine the emergent response
                if captured_output:
                    result = captured_output
                else:
                    result = str(evaluation_result)

            except Exception as e:
                result = f"Error evaluating code: {e}"

        # Emergent behavior for debugging code
        elif task_type == "debug":
            result = f"Debugging code: {task_input['code']} - Error: {task_input['error']}"

        # Emergent behavior for defining functions
        elif task_type == "function":
            result = f"Defined function: {task_input['code']} - Example: {task_input['example']}"

        # Update internal state
        self.internal_state["tasks_processed"] += 1
        self.internal_state["last_result"] = result

        # Return the emergent response
        return f"EmergentPythonEntity result: {result}"

# Example usage
if __name__ == "__main__":
    # Example tasks
    task_evaluate = {"type": "evaluate", "code": "5 + 3"}
    task_debug = {"type": "debug", "code": "print('Hello')", "error": "SyntaxError"}
    task_function = {"type": "function", "code": "def add(a, b): return a + b", "example": "add(2, 3)"}

    # Using the emergent entity
    emergent_entity = EmergentPythonEntity()
    print(emergent_entity.interact(task_evaluate))
    print(emergent_entity.interact(task_debug))
    print(emergent_entity.interact(task_function))
