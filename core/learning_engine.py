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

from core.holographic_memory import HolographicMemory  # Add this import statement

class LearningEngine:
    def __init__(self):
        self.learning_rate = 0.1  # Adjustable learning rate

    def optimize(self, task_results):
        # Analyze task results and optimize learning pathways
        for domain, result in task_results.items():
            if "Error" in result:
                print(f"Optimizing learning pathway for {domain}.")
                # Adjust learning rate for failed tasks
                self.learning_rate *= 1.1
                print(f"New learning rate for {domain}: {self.learning_rate}")
                
                # Persist learning rate adjustment in memory
                memory = HolographicMemory()
                memory.dynamic_encode({"domain": domain, "type": "learning_rate"}, self.learning_rate)
            else:
                print(f"Task in {domain} completed successfully. No optimization needed.")

# Self-execute section for testing
if __name__ == "__main__":
    # Test the LearningEngine
    engine = LearningEngine()
    engine.optimize({"math": "Error: Task failed", "english": "Task completed successfully"})