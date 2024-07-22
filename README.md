# Textbook QA System

This repository contains a Streamlit application for a Question-Answering system using multiple textbooks.

## Overview

The Textbook QA System allows users to select a book from a list of pre-loaded textbooks and ask questions about the content. The system uses a combination of vector embeddings and language models to retrieve and generate accurate answers from the selected book.

## Features

- **Book Selection**: Users can choose from a list of available textbooks.
- **Question Answering**: Users can ask questions based on the selected textbook and get precise answers.
- **Efficient Retrieval**: Utilizes vector embeddings for efficient document retrieval.
- **Language Models**: Integrates with Google Gemini Pro and Groq for generating answers.

## Setup

### Prerequisites

- Python 3.10 or higher
- Virtual environment tool (optional but recommended)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Gangatharangurusamy/Textbook-QA-System.git
    cd yourrepository
    ```

2. **Create a virtual environment and activate it**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    - Create a `.env` file in the root directory.
    - Add your API keys in the `.env` file:
      ```
      GROQ_API_KEY=your_groq_api_key
      GOOGLE_API_KEY=your_google_api_key
      ```

5. **Ensure dataset directories are in place**:
    - Verify that the dataset directories for each book are present and contain the necessary files.
    - Example structure:
      ```
      dataset_deep_learning/
          data-00000-of-00001.arrow
          dataset_info.json
          state.json
      dataset_introduction_to_algorithms/
          data-00000-of-00001.arrow
          dataset_info.json
          state.json
      dataset_ai_modern_approach/
          data-00000-of-00001.arrow
          dataset_info.json
          state.json
      ```

6. **Run the Streamlit application**:
    ```bash
    streamlit run app.py
    ```

## Usage

1. **Select a Book**:
    - Choose a book from the dropdown menu.
    - Available books:
        - Deep Learning
        - Introduction to Algorithms
        - AI: A Modern Approach

2. **Ask a Question**:
    - Enter your question in the input box.
    - Click the "Submit" button to get an answer based on the selected book's content.

## Deployment

### Deploying on Streamlit Cloud

1. **Upload to GitHub**:
    - Ensure all your project files are uploaded to your GitHub repository.

2. **Create an Account on Streamlit**:
    - Go to [Streamlit Cloud](https://streamlit.io/cloud) and create an account if you don't have one.

3. **Deploy the App**:
    - Click on "New app" and connect your GitHub repository.
    - Select the repository and the branch where your code is located.
    - Specify `app.py` as the main file.
    - Click "Deploy".

4. **Access the App**:
    - Once deployed, you will get a URL for your app. Share this URL to allow users to access your application.

### Example Deployment Link

[Access the Textbook QA System here](https://gangaguru-textbook-ques-ans-system.streamlit.app/)

## Project Structure

- `app.py`: Main Streamlit application script.
- `data_extraction.py`: Script to extract text from PDFs and save them in a specific format.
- `retrieval.py`: Script to handle retrieval of answers from the dataset.
- `dataset_deep_learning/`: Directory containing the dataset for the "Deep Learning" book.
- `dataset_introduction_to_algorithms/`: Directory containing the dataset for the "Introduction to Algorithms" book.
- `dataset_ai_modern_approach/`: Directory containing the dataset for the "AI: A Modern Approach" book.
- `requirements.txt`: List of Python dependencies.
- `.env`: File to store environment variables like API keys.

## Dependencies

The project requires the following Python packages, which are listed in the `requirements.txt` file:

- streamlit
- langchain
- langchain_groq
- langchain_google_genai
- google-cloud
- faiss-cpu  # or faiss-gpu if using GPU
- python-dotenv

Install these dependencies using:
```bash
pip install -r requirements.txt
