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
        print('History:', history)

        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=300,
            temperature=1,
            system=system_message,
            messages=history
        )

        reply = response.content[0].text
        #print(response)

        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()

#This is different from chatgpt because it is a lot slower and harder to work with, it also has no UI
#Which also makes it harder to work with.

''' Reflection lab 1:
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

'''lab 2:
Input tokens = what you send in.
Output tokens = what the AI sends back.
Both are billed and measured in small text chunks called tokens.

Temperature controls the creativity of the AI's responses. A higher temperature (2) makes the output more random and creative, 
while a lower temperature (0) makes it so it answers exactly the same way.

The API needs the full history evrytime to go back and look at the previous messages to understand the context of the conversation.

Reflection lab 2:
1. tokens are like writing down an essay, the more words you write the more power you use.

2. if we delete - history.append({'role': 'user', 'content': user_input}) - the AI recives no context of what the user said,
 so it will not be able to answer correctly. and the input tokens will not be counted because the AI will not know what the user said from before.
 - what really happend - the AI was not able to answer correctly because it has no context of what the user said,
  and the input tokens were not counted because the AI did not know what the user said from before.
 if we delete - history.append({'role': 'assistant', 'content': reply}) - the AI will forget what it said and will not be able to answer correctly,
and the output tokens will not be counted because the AI will not know what it said from before.
if we delete - print('History so far:', history) - the AI will not act differently because Print statements are just for debugging visibility — 
they don't affect the program's logic or the AI's behavior. 
Only code that changes data (like .append()) or gets passed into the API call actually matters.
- what what really happened - the AI did not act differently because print statements are just for debugging visibility —
they don't affect the program's logic or the AI's behavior.

 3. i did not have any bugs in this lab!!
'''