#mmr is a MAXIMAL MARGINAL RELEVANCE its core philosophy is that we pick up the results that are not relevant to the query but also different from each other

#so by the help of it we tend to use less results and make it high relevance as a result because we are basically optimising the no of results as eliminating the copied oneee

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

from langchain_community.vectorstores import FAISS


# Sample documents
docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]


# Initialize OpenAI embeddings
embedding_model = OpenAIEmbeddings()

# Step 2: Create the FAISS vector store from documents
vectorstore = FAISS.from_documents(
    documents=docs,
    embedding=embedding_model
)

# Enable MMR in the retriever
retriever = vectorstore.as_retriever(
    search_type="mmr",                   # <-- This enables MMR
    search_kwargs={"k": 3, "lambda_mult": 0.5}  # k = top results, lambda_mult = relevance-diversity balance
)

#if we set lambda_mult into 1 we get to be as similarity search but if we search for the k little less we get to unleash its mmr type response where it pick the diversify result onlyyyy


