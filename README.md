



# <p align="center">decomentation 💡</p>

An AI chatbot with Gemini API to assist in your daily usage of linux insated of RTFM 😉

# Installation


## Automated setup

Setuping the app on your machine

  #### pre steps
  
  1. download the repo
  
  ```bash
  git clone https://github.com/keryakosALKOMOS
  ```
  

#### Get your own API key
 3. You will be asked for the api key. to get the key go to : 
  	 1. [Get API key | Google AI Studio](https://aistudio.google.com/app/apikey)
     2. click on `Create API KEY` button
  	 3. generate a new project if needed or select a previous google cloud project.
  	 4. Copy the api key Showen on the popup dialog
  	 
  	Also check the steps on the detailed images below
  <br/><br/><br/><br/>
  
  #### detailed images
    
    1. click on `Create API KEY` button
![1](https://github.com/AmrEL3taaL/mesba7/assets/110328592/8d712415-8f97-4db8-b169-2f984b878e23)
    
    2. generate a new project if needed or select a previous google cloud project.
![2](https://github.com/AmrEL3taaL/mesba7/assets/110328592/fa94f290-a6bc-48e0-bf14-df4d2e6daee0)
    
  
  
  4. A Geny will spawn on your machine granting you infinite number of wishes ;)

## How to use
all you need is to call `geny` and your wishes will be granted ✨

#### examples:

1.
```bash
geny how to create a new directory?
```
###### output
```bash
mkdir directory_name
```
2.
```bash
geny how to list files in a directory?
```
###### output
```txt
ls
```

3.
```bash
geny how to copy files and directories?
```
###### output
```txt
cp [options] source destination
```
4.
```bash
geny What is 5 + 5?
```
###### output
```txt
Your question is off-topic for this assistant. I can only help with questions about Linux bash commands.
```

# <p align="center">Genie 🧞 and the project. </p>

## Manual setup

step by step how to create and the code explanations

1. First of all this is the python main logic code

```py
import os
import textwrap
import google.generativeai as genai

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

# List available models that support text generation
print("Available models for text generation:")
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(model.name)

# Load the generative model (replace 'gemini-1.5-pro-latest' if desired)
model = genai.GenerativeModel('gemini-1.0-pro')

print("Welcome to the Genie command! You can ask me questions about the Linux terminal.")
while True:
    question = input("Enter your question (or type 'exit' to quit): ")
    if question.lower() == "exit":
        print("Exiting Genie command. Goodbye!")
        break
    response = model.generate_content(question)
    print("Genie:")
    print(to_markdown(response.text))

```py
text="Help with any question I ask about Linux bash commands only in very summarized answer with a short example usage and don't add any markdown styling make sure all the output you give is pair text. other wise if my question is off topic please only answer politely by refusing to answer this question. So my questions is : "+" ".join(sys.argv[1:])
```
<br /><br /><br />
2. Now about how to convert the normal python code into a ready to install application for any Debian based Linux disruptions
by copying the above code don't forget to set your own API key [in this step](#get-your-own-api-key)
and set it in a file named `genie.py`
get the path of the file
```bash
pwd ./genie.py
```
copy the output and add `/genie.py` at the end of it
```bash
pwd genie

/home/<usrName>
```
thus the path is : 
`/home/<usrName>/genie.py`
copy it and keep it for the next step.

do the following 
```bash
nano ~/.bashrc
```

this will open a file for you in which go to `last line` in the file and add the following : 
```bash
alias genie='python3 /home/<usrName>/genie.py'
```

Now you are behind one step from the glow!
update the new settings for the system to read by doing : 
```bash
source ~/.bashrc
```
<br />
Now you can use genie just as like as you would use the installed geny from the mesba7

<h1 align="center">that's it 👀</h1>

