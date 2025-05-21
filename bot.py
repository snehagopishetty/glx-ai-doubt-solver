from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
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

    chain = RetrievalQA.from_chain_type(
        llm=OpenAI(temperature=0.5, openai_api_key=os.getenv("OPENAI_API_KEY")),
        retriever=vectorstore.as_retriever(),
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt}
    )

    return chain.run(question)
