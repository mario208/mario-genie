
#!/bin/bash



# Check if Python is installed

if ! command -v python3 &> /dev/null

then

    echo "Python is not installed. Installing Python..."

    sudo apt-get update

    sudo apt-get install python3.8

fi



import os
import textwrap
import google.generativeai as genai
import re

# Set the Google API Key (replace with your actual key)
your_api_key = "AIzaSyAFjcMyHH6bwGVAlIo-qGGdx6YrL_HCuXU"
os.environ['GOOGLE_API_KEY'] = your_api_key

# Configure Google Generative AI
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

def to_markdown(text):
    """Converts plain text to Markdown format with bullets.

    Args:
        text: The plain text string to convert.

    Returns:
        A string containing the Markdown formatted text.
    """
    text = text.replace('•', '  *')  # Use two spaces for better formatting
    # Indent each line
    return textwrap.indent(text, '> ', predicate=lambda _: True)

def is_terminal_question(question):
    """Checks if the question is related to the Linux terminal.

    Args:
        question: The input question string.

    Returns:
        A boolean indicating if the question is related to the Linux terminal.
    """
    keywords = [
        'linux', 'terminal', 'command', 'shell', 'bash', 'cli', 'script', 
        'unix', 'kernel', 'sudo', 'root', 'chmod', 'chown', 'apt-get', 
        'yum', 'package', 'install', 'update', 'grep', 'awk', 'sed', 'vi', 'vim', 'nano'
    ]
    return any(re.search(r'\b' + keyword + r'\b', question, re.IGNORECASE) for keyword in keywords)

# List available models that support text generation
print("Available models for text generation:")
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(model.name)

# Load the generative model (replace 'gemini-1.5-pro-latest' if desired)
model_name = 'gemini-1.0-pro'
model = genai.GenerativeModel(model_name)

print("Welcome to the Genie command! You can ask me questions about the Linux terminal.")
while True:
    question = input("Enter your question (or type 'exit' to quit): ")
    if question.lower() == "exit":
        print("Exiting Genie command. Goodbye!")
        break
    
    # Append "in Ubuntu" to the question
    question_with_ubuntu = question + " in Ubuntu"
    
    if is_terminal_question(question_with_ubuntu):
        response = model.generate_content(question_with_ubuntu)
        print("Genie:")
        print(to_markdown(response.text))
    else:
        print("Genie: I'm sorry, I only answer bash specific questions.")



# Check if the Python script contains "CHANGE_TO_YOUR_PRIVATE_KEY"

if [[ $python_script == *"CHANGE_TO_YOUR_PRIVATE_KEY"* ]]; then

    echo "Please go to https://aistudio.google.com/app/apikey and generate a new private API key from Gemini."

    read -p "Enter your private API key: " api_key

    # Replace "CHANGE_TO_YOUR_PRIVATE_KEY" with the user's API key

    python_script=${python_script//"CHANGE_TO_YOUR_PRIVATE_KEY"/$api_key}

fi



# Create a bash script

cat << EOF > geny

#!/bin/bash



python_script="\$(cat << 'EOPYTHON'

$python_script

EOPYTHON

)"

# Run the Python script with all parameters passed to the bash script

python3 -c "\$python_script" "\$@"

EOF



# Make the bash script executable

chmod +x geny



# Move the bash script to /usr/local/bin so it can be executed from anywhere

sudo mv geny /usr/local/bin/

