import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from datasets import load_from_disk
from langchain.schema import Document

# Load environment variables
load_dotenv()

# Retrieve API keys from environment variables
groq_api_key = os.getenv('GROQ_API_KEY')
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

def vector_embedding(dataset_dir):
    """
    Creates vector embeddings for documents in the given directory.
    
    Args:
        dataset_dir (str): Path to the directory containing dataset files.
    
    Returns:
        FAISS: The FAISS vector store.
    """
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    
    # Verify directory existence
    if not os.path.exists(dataset_dir):
        raise ValueError(f"The directory {dataset_dir} does not exist.")
    
    print(f"Loading documents from {dataset_dir}...")
    
    # Load existing dataset
    dataset = load_from_disk(dataset_dir)
    print(f"Dataset loaded from {dataset_dir}.")
    
    # Convert the dataset to Document objects
    documents = [Document(page_content=doc['text']) for doc in dataset]
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    final_documents = text_splitter.split_documents(documents)
    
    vectors = FAISS.from_documents(final_documents, embeddings)
    return vectors

def retrieve_answer(question, book):
    """
    Retrieves an answer to the question based on the selected book's dataset.
    
    Args:
        question (str): The question to answer.
        book (str): The selected book.
    
    Returns:
        str: The answer to the question or an error message.
    """
    dataset_dir = {
        "Deep Learning": "dataset_deep_learning",
        "Introduction to Algorithms": "dataset_introduction_to_algorithms",
        "AI: A Modern Approach": "dataset_ai_modern_approach"
    }.get(book, None)
    
    if not dataset_dir:
        return "Invalid book selection."
    
    try:
        vectors = vector_embedding(dataset_dir)
        
        llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")
        prompt = ChatPromptTemplate.from_template(
            """
            Answer the questions based on the provided context only.
            Please provide the most accurate response based on the question
            <context>
            {context}
            <context>
            Questions:{input}
            """
        )
        
        retriever = vectors.as_retriever()
        document_chain = create_stuff_documents_chain(llm, prompt)
        retrieval_chain = create_retrieval_chain(retriever, document_chain)
        
        # Invoke retrieval chain and handle empty results
        response = retrieval_chain.invoke({'input': question})
        if 'answer' not in response or not response['answer']:
            raise ValueError("No answer found in the response.")
        return response['answer']
    except ValueError as ve:
        return f"ValueError: {ve}"
    except Exception as e:
        return f"An error occurred during retrieval: {e}"

# Example usage (comment out or remove in production)
if __name__ == "__main__":
    question = "What is the main topic of Deep Learning?"
    book = "Deep Learning"
    answer = retrieve_answer(question, book)
    print("Answer:", answer)
