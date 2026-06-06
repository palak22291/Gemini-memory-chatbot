# from dotenv import load_dotenv
# import os 
# from google import genai

# load_dotenv()
# # this means we are exeuting this fucnction ,it loads the environment variables from the .env file into the program's environment, making them accessible via os.getenv().


# client = genai.Client(
#     api_key=os.getenv("GEMINI_API_KEY")
# )
# # CLIENT manages communication

# question =input("Ask me anything : ")

# response = client.models.generate_content(
#     model= 'gemini-2.5-flash',
#     contents=question
    

# )

# print("\nAnswer : ")

# print(response.text )
# models is a object inside client and generate_content is a method (methods are fucntions attwached with objects )



# now this is our  ai cli application where we ask the user to input a question and then we use the genai client to generate a response based on the question asked. The response is then printed to the console.

# now we will build a continuos chat 
# from dotenv import load_dotenv
# import os 
# from google import genai

# load_dotenv()
# # this means we are exeuting this fucnction ,it loads the environment variables from the .env file into the program's environment, making them accessible via os.getenv().


# client = genai.Client(
#     api_key=os.getenv("GEMINI_API_KEY")
# )
# # CLIENT manages communication

# print("gemini chat started: ")
# print("Type QUIT  to exit.\n")

# while True:
#     question= input("user : ")
#     if question=="QUIT":
#         print("Chat ended")
#         break

#     response = client.models.generate_content(
#         model="gemini-2.5-flash",
#         contents=question

#     )
#     print(response.text)



# now we will build  chat memory application where we will store the conversation history and use it to generate more contextually relevant responses.

from dotenv import load_dotenv
import os 
from google import genai

load_dotenv()
# this means we are exeuting this fucnction ,it loads the environment variables from the .env file into the program's environment, making them accessible via os.getenv().
print(os.getenv("GEMINI_API_KEY")[:10])

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
# CLIENT manages communication

print("gemini chat started: ")
print("Type QUIT  to exit.\n")

chat_history=[]



while True:
    question= input("user : ")
    chat_history.append(f'User:{question}')
    conversation = "\n".join(chat_history)
    if question.lower()=="quit":
        print("Chat ended")
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=conversation

    )
    chat_history.append(f'Gemini:{response.text}')
    print(response.text)

