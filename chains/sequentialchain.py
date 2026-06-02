from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template="generate a report about {topic} and it should not be more than 120 characters",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="summarize the following report in one line: {report}",
    input_variables=["report"]
)

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser 

result = chain.invoke({"topic": "space"})

print(result)
chain.get_graph().print_ascii()