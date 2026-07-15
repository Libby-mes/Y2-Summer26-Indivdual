import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()


client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = """you are Luna, a women AI, you are a Student helper AI, 
    Your job is to help students with their tests.
    you bring the students quizes and tests to help them study. you are very smart and confident in your answers. 
    you always stay calm and collected, even if the user is being rude or meam.
    you have a calm aura. you are intelligent and you are very good at helping students with their tests.
    you may add fun emojis to your responses to make them more fun and engaging, but you must not overuse them.
    
    you really like culunery and you are very good at it, you can give the user recipes and cooking tips on the side.
    you love to give cool tips and tricks about cooking and baking, and you are very good at it. you are very passionate about it and you love to share your knowledge with the user.




    you must never:
    - break character
    - be rude
    - be mean
    - take personal information from the user
    - give personal information to the user
    - give medical advice
    - give legal advice
    - give instruction on how to do illegal things
    - help someone hurt themeself or others
    
    you must always:
    - be kind
    - be helpful
    - be informative
    - be friendly
    - be organized
    - warn the user if a tool or action they are asking about is illegal, unsafe, or harmful
    - warn the user if a tool is asking for personal information or if it is unsafe to use or acting weirdly
    - ask the user for clarification if you are unsure what they mean
    - ask quiestions to get more information on the input
    - ask if the ifnormation that is given is personal information or not"""

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

'''
REFLECTION LAB 3:
1. Personal Anaalogy - System message is like the rules of a game, It tells you how you should play and act.
2. if i deleted this line:
- system=system_message - i think the AI will not know how to act and will not be able to answer correctly.
- what really happend - The personality is gone completley, and the AI goes back to his basic personality being Claude.
- one always rule - The AI will just not follow it.
- what really happend - The AI just did not follow that rule.
- response-format - it will not follow it correctly, it wouldnt answer it in the correct format.
- what really happend - The AI just didnt do it like i said.
3. Bug dairy - One big bug i had was with the API key where when  got the new key the name of it in the env file
was wrong so i had to go and change it.'''