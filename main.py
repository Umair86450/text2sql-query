import streamlit as st
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain_core.runnables import Runnable

# Step 1: Define your prompt
template = """
You are an expert SQL generator. Convert the user's request into a syntactically correct SQL query.

User Question:
{question}

SQL Query:
"""

prompt = PromptTemplate.from_template(template)

# Step 2: Load lightweight LLM via Ollama
llm = Ollama(model="phi3")  # You can change to another local model: llama3, mistral, etc.

# Step 3: Create runnable chain
sql_chain: Runnable = prompt | llm

# Step 4: Streamlit UI
st.set_page_config(page_title="🧠 Natural Language to SQL Generator", layout="centered")
st.title("🧠 Natural Language to SQL Generator")

st.markdown("Enter a question in plain English and get the SQL query.")

# User input
user_input = st.text_area("Ask in natural language:", height=150)

# When user clicks the generate button
if st.button("Generate SQL"):
    if user_input.strip() == "":
        st.warning("Please enter a question to generate SQL.")
    else:
        with st.spinner("Generating SQL..."):
            result = sql_chain.invoke({"question": user_input})
            st.success("✅ SQL Query Generated:")
            st.code(result.strip(), language="sql")
