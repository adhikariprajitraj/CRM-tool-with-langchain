import yaml
from api import huggingface, openai, langchain  # Assuming langchain is the correct module name
from utils import helpers

def load_config(file_path):
    """Load configuration from a YAML file."""
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def main():
    # Load configuration
    config = load_config('config/config.yaml')

    # Initialize API clients or services
    # For example:
    # huggingface_client = huggingface.HuggingFaceClient(api_key=config['huggingface']['api_key'])
    # openai_client = openai.OpenAIClient(api_key=config['openai']['api_key'])
    # langchain_client = langchain.LanguageChainClient(api_key=config['langchain']['api_key'])  # Adjust based on actual usage

    # Sample usage (replace with your actual business logic):
    # query = "sample query from CRM"
    # response = huggingface_client.generate_text(query)
    # processed_response = helpers.process_response(response)
    # ...

    print("CRM Tool initialized!")

if __name__ == "__main__":
    main()
