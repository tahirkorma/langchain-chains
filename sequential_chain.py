from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template = "Generate a detailed report on the {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = "Generate a 5 pointer summary from the following text \n{text}",
    input_variables=['text']
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

#chain graph
chain.get_graph().print_ascii()

result = chain.invoke({'topic': 'corruption in india'})

print(result)

chain.get_graph().print_ascii()