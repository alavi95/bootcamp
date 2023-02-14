import os
import openai

# Let's have OpenAI keep returning outputs until we're happy with them.
#   Setting the value for temperature in the definition creates a default value for it s
#   so if users choose not to pass through a value for temperature it will default to whatever 
#   is in the definition.
def get_output(prompt, temperature=.4): # Setting the value for temperature in the definition creates a default value for it so if users choose not to pass through a value for temperature it will default to whatever is in the definition.
    openai_key = os.environ.get("OPENAI_KEY")
    openai.api_key = openai_key # Here is how we pass through our API credentials. This is one way in which some APIs accept credentials, other examples are using a parameter (like we have for model, prompt, temperature, or max_tokens), and another is through the endpoint like we did with Polygon.io
    # Our max tokens are set to 100. For larger outputs consider increasing this value.
    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=temperature, max_tokens=100)
    return response["choices"][0]["text"] # Since the response includes other data like tokens used, we need to parse out the response to get the actual value we're looking for (as is the case with most APIs). 


# Here we have a loop so it keeps prompting the user for a response on whether or not they're happy with the generated text
def keep_trying_gpt(prompt):
    while True:
        # Notice here we don't define the temperature, so it will default to 0.4
        gpt_response = get_output(prompt)
        print(gpt_response)
        user_response = input("\n\nIs the AI generated text sufficient? (Y/N) ")
        if user_response == "Y":
            break
    return gpt_response



# Try it for yourselves:
keep_trying_gpt("If Amazon made a new leadership principle, what would it be?")