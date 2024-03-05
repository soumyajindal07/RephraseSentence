from fastapi import FastAPI
import openai
import os

app = FastAPI()

@app.get("/CMSAI/IsAPIKeyAvailable")
def isAPIKeyAvailable():
    if 'REPHRASE_API_KEY' in os.environ:
        return("API key is set in environment variable.")        
    else:
        print("API key is not set in environment variable.")   


@app.post("/CMSAI/RephraseUsingGPT3")
def rephraseSentenceUsingGPT3(input:str):
    api_key = os.getenv('REPHRASE_API_KEY')    
    openai.api_key = api_key

    # Define the prompt for the API request
    prompt = f"Rewrite the following sentence in a different way:\n\"{input}\""

    # Define the parameters for the API request
    parameters = {
    "max_tokens": 50,  # Adjust the max_tokens parameter according to your preference
    "temperature": 0.7, 
    "n": 2,  # TODO: This needs to be changed/updated 
    }

    client = openai.Client(api_key=api_key)

    # Make the request to the OpenAI API
    response = client.completions.create(model ="gpt-3.5-turbo-instruct", prompt = prompt, **parameters)

    # Capture the response which is the base of rephrased sentences
    rephrased_sentence = response.choices[0].text.strip()
    return rephrased_sentence