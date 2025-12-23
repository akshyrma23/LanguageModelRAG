
# Basic examples to compare document and retrieve information by using semantic search
 
# To set the virtual environment
 python -m venv venv

# Install all the dependencies
pip install -r requirements.txt

# Replace API key in the env file with your own API keys
OPENAI_API_KEY = "Your_API_Key" // create an account in open AI and generate an API key
HUGGINGFACEHUB_API_TOKEN =  "Your_API_Key" //  // create an account in hugging face and generate an API key

# To run prompt_ui using streamlit
streamlit run prompt_ui.py
