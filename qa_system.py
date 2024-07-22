# from langchain_groq import ChatGroq
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain_core.prompts import ChatPromptTemplate
# import os
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# groq_api_key = os.getenv('GROQ_API_KEY')
# google_api_key = os.getenv('GOOGLE_API_KEY')

# os.environ["GOOGLE_API_KEY"] = google_api_key

# def qa_system(question, context):
#     llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")

#     prompt = ChatPromptTemplate.from_template("""
#     Answer the questions based on the provided context only.
#     Please provide the most accurate response based on the question.
#     <context>
#     {context}
#     <context>
#     Question: {input}
#     """)

#     chain = prompt.chain
#     result = chain.run(context=context, input=question)
#     return result['output']
