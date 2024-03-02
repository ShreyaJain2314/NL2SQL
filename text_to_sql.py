from faker import Faker
import pandas as pd
import streamlit as st

import openai
import os
# Set keys
api_key=<YOUR OPENAI KEY>
# Initialize Faker to generate fake data
fake = Faker()

# Define columns, data types, and descriptions for each table
customers_columns = ['customer_id', 'customer_name', 'address', 'city', 'country']
customers_data_types = {'customer_id': 'Int64', 'customer_name': 'object', 'address': 'object', 'city': 'object', 'country': 'object'}
customers_descriptions = {
    'customer_id': 'customer_id is the primary key (column with unique values) for Customers table.',
    'customer_name': 'The name of the customer',
    'address': 'The address of the customer',
    'city': 'The city where the customer is located',
    'country': 'The country where the customer is located'
}


customers_data = {
    'Column Name': customers_columns,
    'Data Type': [customers_data_types[col] for col in customers_columns],
    'Description': [customers_descriptions.get(col, '') for col in customers_columns]
}

customers=pd.DataFrame(customers_data)

categories_columns = ['category_id', 'category_name', 'description']
categories_data_types = {'category_id': 'Int64', 'category_name': 'object', 'description': 'object'}
categories_descriptions = {
    'category_id': 'category_id is a foreign key (reference column) to the Products table.',
    'category_name': 'The name of the category',
    'description': 'The description of the category'
}

categories_data = {
    'Column Name': categories_columns,
    'Data Type': [categories_data_types[col] for col in categories_columns],
    'Description': [categories_descriptions.get(col, '') for col in categories_columns]
}

categories=pd.DataFrame(categories_data)


suppliers_columns = ['supplier_id', 'supplier_name', 'contact_name', 'address', 'city', 'country', 'phone']
suppliers_data_types = {'supplier_id': 'Int64', 'supplier_name': 'object', 'contact_name': 'object', 'address': 'object', 'city': 'object', 'country': 'object', 'phone': 'object'}
suppliers_descriptions = {
    'supplier_id': 'supplier_id is a foreign key (reference column) to the Orders table.',
    'supplier_name': 'The name of the supplier',
    'contact_name': 'The contact name of the supplier',
    'address': 'The address of the supplier',
    'city': 'The city where the supplier is located',
    'country': 'The country where the supplier is located',
    'phone': 'The phone number of the supplier'
}

suppliers_data = {
    'Column Name': suppliers_columns,
    'Data Type': [suppliers_data_types[col] for col in suppliers_columns],
    'Description': [suppliers_descriptions.get(col, '') for col in suppliers_columns]
}

suppliers=pd.DataFrame(suppliers_data)

suppliers['table_name'] = 'Suppliers'
categories['table_name'] = 'Categories'
customers['table_name'] = 'Customers'

columns = ['product_id', 'product_name','category','category_id']
data_types = {'product_id': 'int64', 'product_name': 'string','category':'string','category_id':'int64'}
descriptions = {
    'product_id': 'product_id is the primary key (column with unique values) for Products table.',
    'product_name': 'The name of the product (consists of only lowercase and uppercase characters)',
    'category' : 'The category or type of product',
    'category_id':'category_id is the primary key (column with unique values) for Products table.',
}

data = {
    'Column Name': columns,
    'Data Type': [data_types[col] for col in columns],
    'Description': [descriptions.get(col, '') for col in columns]
}

# Convert to DataFrame
products = pd.DataFrame(data)

columns1 = ['product_id', 'order_date','unit','supplier_id','customer_id']
data_types1 = {'product_id': 'Int64', 'order_date': 'date','unit':'int64','supplier_id':'int64','customer_id':'int64'}
descriptions1 = {
    'product_id': 'product_id is a foreign key (reference column) to the Products table.',
    'order_date': 'the date on which order was placed',
    'unit' : 'unit is the number of products ordered in order_date.',
    'supplier_id': 'supplier_id is the primary key (column with unique values) for Orders table.',
    'customer_id':'customer_id is a foreign key (reference column) to the Customers table.',
}

data1 = {
    'Column Name': columns1,
    'Data Type': [data_types1[col] for col in columns1],
    'Description': [descriptions1.get(col, '') for col in columns1]
}

# Convert to DataFrame
orders = pd.DataFrame(data1)




import streamlit as st
import pandas as pd
import openai

# Set your OpenAI API key
openai.api_key = api_key

# Function to generate SQL query
def generate_sql_query(user_query):
    # Define the system prompt with the JSON schema
    system_prompt = """
    Given the following JSON schemas representing the tables Products, Orders, Customers, Suppliers, and Categories:
    
    Products:
    {products_json}
    
    Orders:
    {orders_json}
    
    Customers:
    {customers_json}
    
    Suppliers:
    {suppliers_json}
    
    Categories:
    {categories_json}
    
    Write a SQL Query for the user query.
    """.format(
        products_json=products.to_json(orient='records'),
        orders_json=orders.to_json(orient='records'),
        customers_json=customers.to_json(orient='records'),
        suppliers_json=suppliers.to_json(orient='records'),
        categories_json=categories.to_json(orient='records')
    )

    # Combine user query and system prompt
    full_prompt = f"{user_query}\n\n{system_prompt}"

    # Get the completion from OpenAI
    response = openai.Completion.create(
        engine="gpt-35-turbo",  # You can experiment with other engines
        prompt=full_prompt,
        max_tokens=150  # Adjust based on your desired response length
    )

    # Extract the generated SQL query from the response
    generated_sql_query = response['choices'][0]['text']
    
    return generated_sql_query

# Streamlit UI
st.title("SQL Query Generator")

# User input for the query
user_query = st.text_area("Enter your query:")

# Button to generate SQL query
if st.button("Generate SQL Query"):
    if user_query:
        generated_sql_query = generate_sql_query(user_query)
        st.code(generated_sql_query, language='sql')
    else:
        st.warning("Please enter a query.")
