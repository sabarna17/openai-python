# Open AI API key
import os
from getpass import getpass
import openai

os.environ['OPENAI_API_KEY'] = 'sdsd'
def testOpenAIKey(openaiapikey):
    openai.api_key = openaiapikey #'sk-YjNP6mLwJjHteurGiWvlXXXXXXXXXXXXXXXXXXXXXXXXX'
    prompt = "What is the calculated value for 6 * 12"
    model = "text-davinci-003"
    try: 
        response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=50)
        generated_text = response.choices[0].text
    except:
        generated_text = 'oops'
    if (generated_text.find('72') < 0):
        print('Your OpenAI API Key is wrong')
        askForOpenAIKey()
    print('Your OpenAI API Key is active')
def askForOpenAIKey():
    openai_api_key = getpass("Enter your OpenAI API key: ")
    os.environ['OPENAI_API_KEY'] = openai_api_key
    print('You have entered: ', openai_api_key)
    testOpenAIKey(openai_api_key)
    if(int(testOpenAIKey(openai_api_key)) > 0):
        askForOpenAIKey()

def checkKey(dic, key):
    if key in dic.keys():
        testOpenAIKey(dic[key])
    else:
        askForOpenAIKey()

checkKey(os.environ, 'OPENAI_API_KEY')
