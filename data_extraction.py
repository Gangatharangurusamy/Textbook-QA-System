import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path, output_txt_path):
    with fitz.open(pdf_path) as pdf:
        text = ""
        for page_num in range(len(pdf)):
            page = pdf.load_page(page_num)
            text += page.get_text()
    
    with open(output_txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)

# Example usage
if __name__ == "__main__":
    extract_text_from_pdf('Deep_Learning.pdf', 'Deep_Learning.txt')
    extract_text_from_pdf('Introduction_to_Algorithms.pdf', 'Introduction_to_Algorithms.txt')
    extract_text_from_pdf('AI_Modern_Approach.pdf', 'AI_Modern_Approach.txt')
