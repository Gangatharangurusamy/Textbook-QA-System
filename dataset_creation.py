from datasets import Dataset
import os

def load_text_into_dataset(file_paths, output_dir):
    texts = []
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            texts.append({"text": text})
    
    dataset = Dataset.from_list(texts)
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    dataset.save_to_disk(output_dir)
    
    return dataset

# Example usage
text_files = ["Deep_Learning.txt", "Introduction_to_Algorithms.txt", "AI_Modern_Approach.txt"]
output_directories = [
    r"D:\Projects\LLamaIndex\RAG\dataset_deep_learning",
    r"D:\Projects\LLamaIndex\RAG\dataset_introduction_to_algorithms",
    r"D:\Projects\LLamaIndex\RAG\dataset_ai_modern_approach"
]

for text_file, output_directory in zip(text_files, output_directories):
    dataset = load_text_into_dataset([text_file], output_directory)
    print(f"Dataset saved to: {output_directory}")
