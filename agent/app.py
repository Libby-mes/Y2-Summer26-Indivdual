import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()


client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = "Your name is Chloe. You are a young woman who knows everything about makeup and hair care, you know a bit about technology but when you answer it you sound a bit dumb."
    history = []

    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})

        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )

        reply = response.content[0].text
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()

#This is different from chatgpt because it is a lot slower and harder to work with, it also has no UI
#Which also makes it harder to work with.

''' Reflection:
1. It's like walking into the middle of a movie without seeing the earlier scenes. 
Every conversation makes sense because of what happened before, 
so if you only saw the last minute, you'd miss why the characters are saying what they are. 
That's why the agent needs the entire conversation each time, 
it doesn't remember the previous "scenes" on its own.

2.load_dotenv() - i think it wll not start, because it needs to laod the .env file to get the API key.
- what really happened - it gave me an error that the API key was not found.
temperature=0.7 - i think it will make the responses more random.
- what really happened - in my spesific case i didnt notice it change that much, but it did make the responses a bit more random.
break - i think if we delete this line it will keep running even if we type exit.
-what really happened - for me it didnt even  run because there was an if statment with nothing below it, 
but if i added a pass statement it would keep running even if we type exit.

3. i remember the biggest bug i had today was that i forgot to add the .env file to the .gitignore file,
 so when i pushed it to github it was almost public and anyone could see my API key. but thankfully the repository was not aloowing it,
 it said it was aggaint the rules and it was not allowing me to push it.'''