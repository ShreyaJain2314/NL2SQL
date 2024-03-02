# Text-to-SQL

This code is a Python script that generates SQL queries based on user input using Streamlit and the OpenAI API. Here's a breakdown of its components and functionality:

Imports: The script imports necessary libraries such as Faker for generating fake data, pandas for data manipulation, Streamlit for building the web application, and OpenAI for utilizing the GPT-3 language model.

Data Preparation: Fake data is generated for various tables like Customers, Categories, Suppliers, Products, and Orders. Each table's schema, including column names, data types, and descriptions, is defined and stored in pandas DataFrames.

Streamlit UI: The Streamlit UI is set up. It includes a text area where users can input their query and a button to trigger the generation of SQL queries.

SQL Query Generation: The main functionality lies in the generate_sql_query() function. This function takes the user's input query, combines it with a system prompt containing JSON schemas of the tables, and sends it to the OpenAI API for completion. The response from OpenAI, which contains the generated SQL query, is then extracted and returned.

Button Trigger: When the user clicks the "Generate SQL Query" button, the input query is passed to the generate_sql_query() function, and the resulting SQL query is displayed in a code block using Streamlit's st.code() function.

Overall, this script demonstrates how to leverage the OpenAI API to generate SQL queries based on user input within a Streamlit web application.




