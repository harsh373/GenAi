from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)
model2 = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

prompt1 = PromptTemplate(
    template="generate a short and simple notes from this {text} and it should not be more than 120 characters",
    input_variables=["text"]
)
prompt2 = PromptTemplate(
    template="generate 2 questions from the {text}",
    input_variables=["text"]
)   

prompt3 = PromptTemplate(
    template="merge the notes->{notes} and questions->{questions}",
    input_variables=["notes", "questions"]
)   

parser = StrOutputParser()


/* runnable parallel will run both the chains in parallel and then merge the results using the merge chain */


parallelchain = RunnableParallel(
    {
        "notes": prompt1 | model1 | parser,
        "questions": prompt2 | model2 | parser
    }
)
 
mergechain = prompt3 | model1 | parser

chain = parallelchain | mergechain

text = """The Samsung Galaxy S24 Ultra is a powerful smartphone with a Snapdragon 8 Gen 3 processor, a 5000mAh battery, and a stunning 200MP camera. However, its weight and size may make it uncomfortable for one-handed use, and the price tag is quite high.""" 

result = chain.invoke({"text": text})

print(result)
chain.get_graph().print_ascii() 

