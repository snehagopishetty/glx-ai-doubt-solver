# from langchain.chains import RetrievalQA
# # from langchain.llms import OpenAI
# from langchain_openai import OpenAI
# from langchain.prompts import PromptTemplate
# from vectorstore import create_vectorstore
# from langchain_community.llms import Ollama
# import os

# def get_hint(question):
#     vectorstore = create_vectorstore()

#     prompt = PromptTemplate(
#         input_variables=["context", "question"],
#         template="""
#         You are a helpful tutor. Based on the context, give a hint or partial explanation. Do not solve the entire question.

#         Context: {context}
#         Doubt: {question}

#         Hint:
#         """
#     )

#     # chain = RetrievalQA.from_chain_type(
#     #     llm=OpenAI(temperature=0.5, openai_api_key=os.getenv("OPENAI_API_KEY")),
#     #     retriever=vectorstore.as_retriever(),
#     #     chain_type="stuff",
#     #     chain_type_kwargs={"prompt": prompt}
#     # )
#     chain = RetrievalQA.from_chain_type(
#     llm=Ollama(model="llama3", temperature=0.5),  # ✅ Use Ollama
#     retriever=vectorstore.as_retriever(),
#     chain_type="stuff",
#     chain_type_kwargs={"prompt": prompt}
# )

#     return chain.run(question)


    
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI  # ✅ Use OpenRouter-compatible LLM wrapper
from vectorstore import create_vectorstore
import os

def get_hint(question):
    vectorstore = create_vectorstore()

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are a helpful tutor. Based on the context, give a hint or partial explanation. Do not solve the entire question.

Context: {context}
Doubt: {question}

Hint:
"""
    )

    llm = ChatOpenAI(
        model_name="mistralai/mistral-7b-instruct:free",
        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1"
    )

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt}
    )

    return chain.run(question)
