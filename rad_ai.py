# Rad AI - Powered by Hugging Face 🚀
import requests

print("====================================")
print("       🤖 RAD AI  -  ONLINE       ")
print("====================================")
print("Hello! I'm Rad AI, your cool AI assistant.\n")

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"
API_TOKEN = "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"

def ask_rad_ai(question):
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    
    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json={"inputs": question},
            timeout=10
        )
        
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                if isinstance(result[0], dict) and "generated_text" in result[0]:
                    return result[0]["generated_text"]
                elif isinstance(result[0], str):
                    return result[0]
            return "I'm thinking... Ask me something else!"
        else:
            return "Oops! My brain is loading. Try again in a moment!"
            
    except Exception as e:
        return f"Something went wrong: {str(e)}"

def rad_ai():
    while True:
        user_input = input("You: ").strip()
        
        if user_input == "":
            print("Rad AI: Don't be shy, say something!")
        elif user_input.lower() in ["bye", "exit", "quit"]:
            print("Rad AI: See you later! Stay rad! 👋")
            break
        else:
            print("Rad AI: Thinking... 🤔")
            answer = ask_rad_ai(user_input)
            print(f"Rad AI: {answer}\n")

if __name__ == "__main__":
    rad_ai()
