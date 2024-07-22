from anytree import Node, RenderTree
import re
import os

def create_hierarchical_index(text, title):
    root = Node(title)
    current_node = root

    lines = text.split('\n')
    for line in lines:
        if re.match(r'Chapter \d+:', line):
            current_node = Node(line, parent=root)
        elif re.match(r'Section \d+.\d+:', line):
            current_node = Node(line, parent=current_node)
        else:
            Node(line, parent=current_node)
    return root

# Example usage
text_files = ["Deep_Learning.txt", "Introduction_to_Algorithms.txt", "AI_Modern_Approach.txt"]
index_directories = [
    r"D:\Projects\LLamaIndex\RAG\index_deep_learning",
    r"D:\Projects\LLamaIndex\RAG\index_introduction_to_algorithms",
    r"D:\Projects\LLamaIndex\RAG\index_ai_modern_approach"
]

for text_file, index_directory in zip(text_files, index_directories):
    with open(text_file, "r", encoding="utf-8") as f:
        text = f.read()
    index = create_hierarchical_index(text, f"Index for {text_file}")
    
    # Save index to file
    if not os.path.exists(index_directory):
        os.makedirs(index_directory)
    
    index_file = os.path.join(index_directory, "index.txt")
    with open(index_file, "w", encoding="utf-8") as f:
        for pre, fill, node in RenderTree(index):
            f.write("%s%s\n" % (pre, node.name))
    print(f"Index saved to: {index_file}")
