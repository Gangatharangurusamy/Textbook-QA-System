import streamlit as st
import os
from retrieval import retrieve_answer  # Import the retrieve_answer function

# Define directories for each book
dataset_directories = {
    "Deep Learning": r"D:\Projects\LLamaIndex\RAG\dataset_deep_learning",
    "Introduction to Algorithms": r"D:\Projects\LLamaIndex\RAG\dataset_introduction_to_algorithms",
    "AI: A Modern Approach": r"D:\Projects\LLamaIndex\RAG\dataset_ai_modern_approach"
}

# Book selection
book = st.selectbox("Select a Book", list(dataset_directories.keys()))

if book:
    st.write(f"Selected book: {book}")

    # Ask a Question
    question = st.text_input("Enter your question:")
    
    if st.button("Get Answer"):
        if question:
            try:
                # Load the dataset and index for the selected book
                answer = retrieve_answer(question, book)
                st.write(f"Answer: {answer}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a question.")
