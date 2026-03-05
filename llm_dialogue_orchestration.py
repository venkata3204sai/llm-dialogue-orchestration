from ollama import chat
from ollama import Client
import datetime

client = Client(host='http://localhost:11434')
models = ["llama3.2", "deepseek-r1"]
log_filename = "llm-conversation.txt"



def main():
    with open(log_filename, 'a') as log:
        print("=====Welcome to the LLM Dialogue Orchestration.=====")
        log.write("=====Welcome to the LLM Dialogue Orchestration.=====")
        log.write(f"\nTimestamp Start: {datetime.datetime.now()}")

        question = input("\nHow can i help you?\n> ")
        while True:
            try:
                rounds = int(input("\nHow many rounds (4-12)?\n> "))
                if 4 <= rounds <= 12:
                    break
                else:
                    print("Please choose between 4 and 12.")
            except ValueError:
                print("Enter a valid number.")
        debate = input("\nEnable Debate Mode? (y/n)\n> ").lower() == 'y'
        mode = True

        for i in range(rounds):
            print("\n\n--------------------")
            print(f"\nROUND {i+1}")
            while True:
                try:
                    choice = int(input(f"\nChoose model:\n1: {models[0]}\n2: {models[1]}\n> "))
                    if choice in [1, 2]:
                        curr_model = models[choice - 1]
                        break
                    else:
                        print("Choose 1 or 2.")
                except ValueError:
                    print("Enter a valid number.")

            response = client.chat(
                model = curr_model,
                messages = [{
                    'role': 'system',
                    'content': 'Strictly provide 2-3 lines responses only.'
                },
                {
                    'role': 'user',
                    'content': question
                }],
                stream = True,
                options = {
                    'temperature': 0.7
                })
            
            full_response = ""
            print(f"\n[{curr_model}]> ", end='')
            for chunk in response:
                print(chunk.message.content, end='', flush=True)
                full_response += chunk.message.content
            
            log.write("\n\n--------------------")
            log.write(f"\nROUND {i+1}")
            log.write(f"\n[Model: {curr_model}]")
            log.write(f"\nPrompt:\n{question}")
            log.write(f"\nResponse:\n{full_response}\n")

            if debate:
                question = f"Argue strongly against this response and expose weaknesses in reasoning: {full_response}"
            else:
                question = f"I asked someone this question: {question}. Their answer was: {full_response}. Propose a sharp follow-up question to continue the discussion." if mode else full_response
            mode = not mode
        
        log.write(f"\n\n\nTimestamp End: {datetime.datetime.now()}")


if __name__ == "__main__":
    main()