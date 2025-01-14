import json  # Import json for converting dictionaries to strings

class EmergentEntityCore:
    """
    An emergent entity core that dynamically interacts with a domain module,
    database manager, and holographic memory to process tasks and share knowledge.
    """
    def __init__(self, domain_module, db_manager, memory):
        self.components = {
            "domain_module": domain_module,
            "db_manager": db_manager,
            "memory": memory,
        }
        self.state = {
            "domain_name": self._determine_domain(),
            "tasks_processed": 0,
        }

    def _determine_domain(self):
        """
        Dynamically determines the domain of the entity based on the module name.
        """
        module_name = self.components["domain_module"].__class__.__name__.lower()
        if "math" in module_name:
            return "math"
        elif "english" in module_name:
            return "english"
        elif "python" in module_name:
            return "python"
        elif "science" in module_name:
            return "science"
        else:
            return module_name  # Fallback to the original module name

    def get_domain(self):
        """
        Returns the domain name of the entity.
        """
        return self.state["domain_name"]

    def interact(self, task_data):
        """
        Processes a task using the domain module and updates the entity's state.
        """
        if task_data is None:
            return f"No task data provided for {self.state['domain_name']} domain."

        # Process the task using the domain module
        output = self.components["domain_module"].interact(task_data)

        # Encode the task and output in holographic memory
        self.components["memory"].dynamic_encode(task_data, output)

        # Update internal state
        self.state["tasks_processed"] += 1

        # Return the result
        return output

    def collaborate(self, other_entity):
        """
        Shares knowledge with another emergent entity via holographic memory.
        """
        # Retrieve all shared knowledge
        shared_memory = self.components["memory"].retrieve_all()

        # Create a copy of the shared memory to avoid modifying it during iteration
        shared_memory_copy = shared_memory.copy()

        # Dynamically encode the shared memory into the other entity
        for key, value in shared_memory_copy.items():
            other_entity.components["memory"].dynamic_encode(key, value)

        # Inform about the collaboration
        print(
            f"Knowledge shared from {self.state['domain_name']} "
            f"to {other_entity.state['domain_name']}."
        )

# Self-execute section for testing
if __name__ == "__main__":
    # Mocked domain module, database manager, and memory for demonstration
    class MockDomainModule:
        def interact(self, task_data):
            return f"Processed task: {task_data}"

    class MockDBManager:
        pass

    class MockMemory:
        def __init__(self):
            self.data = {}

        def dynamic_encode(self, task, output):
            # Convert the dictionary to a string to make it hashable
            task_key = json.dumps(task, sort_keys=True)  # Use json.dumps for consistent string representation
            self.data[task_key] = output

        def retrieve_all(self):
            return self.data

    # Create two entities for testing
    math_module = MockDomainModule()
    db_manager = MockDBManager()
    holographic_memory = MockMemory()

    entity1 = EmergentEntityCore(math_module, db_manager, holographic_memory)
    entity2 = EmergentEntityCore(math_module, db_manager, holographic_memory)

    # Process a task and share knowledge
    print(entity1.interact({"task": "solve equation", "details": "x + 2 = 4"}))
    entity1.collaborate(entity2)