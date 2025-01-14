import os
import ast

class CodePatternAnalyzer(ast.NodeVisitor):
    """
    Analyze Python code for patterns representing emergent behavior (Entities) and rule-based agents (Agents).
    """
    def __init__(self):
        self.has_entity = False
        self.has_agent = False

    def visit_ClassDef(self, node):
        # Check for Entity patterns (e.g., dynamic state updates, interaction loops)
        if any(base.id.lower() == "emergententity" for base in node.bases if isinstance(base, ast.Name)):
            self.has_entity = True

        # Check for Agent patterns (e.g., rule-based processing, predefined actions)
        if any(base.id.lower() == "agent" for base in node.bases if isinstance(base, ast.Name)):
            self.has_agent = True

        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        # Detect dynamic interactions for Entities
        if any(keyword in node.name.lower() for keyword in ["interact", "dynamic", "state"]):
            self.has_entity = True

        # Detect explicit rules or task handling for Agents
        if any(keyword in node.name.lower() for keyword in ["process", "task", "action"]):
            self.has_agent = True

        self.generic_visit(node)


def analyze_file(file_path):
    """
    Analyze a Python file for patterns of Entities and Agents.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read())
        analyzer = CodePatternAnalyzer()
        analyzer.visit(tree)
        return analyzer.has_entity, analyzer.has_agent
    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")
        return False, False


def scan_python_files():
    """
    Scan Python files in the current directory (and subdirectories) for patterns of Entities and Agents.
    """
    entity_only_files = []
    agent_only_files = []
    both_files = []
    scanned_files = 0

    # Get the current working directory
    current_directory = os.getcwd()

    # Walk through the folder structure
    for root, _, files in os.walk(current_directory):
        for file in files:
            if file.endswith(".py"):
                scanned_files += 1
                file_path = os.path.join(root, file)

                has_entity, has_agent = analyze_file(file_path)

                if has_entity and has_agent:
                    both_files.append(file_path)
                elif has_entity:
                    entity_only_files.append(file_path)
                elif has_agent:
                    agent_only_files.append(file_path)

    # Print final results
    print("### Scan Results ###")
    print(f"Current Directory: {current_directory}")
    print(f"Total Python files scanned: {scanned_files}")
    print()

    print(f"Files with Entities only: {len(entity_only_files)}")
    for file in entity_only_files:
        print(f"  - {file}")

    print(f"\nFiles with Agents only: {len(agent_only_files)}")
    for file in agent_only_files:
        print(f"  - {file}")

    print(f"\nFiles with both Entities and Agents: {len(both_files)}")
    for file in both_files:
        print(f"  - {file}")


# Main script entry point
if __name__ == "__main__":
    print("Scanning Python files in the current directory and subdirectories...")
    scan_python_files()