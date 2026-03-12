from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

def build_vector_store(text_data):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts([text_data], embeddings)
    return vectorstore

def create_qa_chain(vectorstore):
    llm = ChatOpenAI(temperature=0)
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever()
    )
    return qa
