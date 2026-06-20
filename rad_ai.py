# Rad AI - First Version 🚀
print("====================================")
print("       🤖 RAD AI  -  ONLINE       ")
print("====================================")
print("Hello! I'm Rad AI, your cool AI assistant.\n")

def rad_ai():
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input == "":
            print("Rad AI: Don't be shy, say something!")
        
        elif "hello" in user_input or "hi" in user_input:
            print("Rad AI: Yo! What's up? 🔥")
        
        elif "how are you" in user_input:
            print("Rad AI: I'm running on pure energy and vibes! How about you?")
        
        elif "your name" in user_input:
            print("Rad AI: I'm Rad AI, the coolest AI in development!")
        
        elif "bye" in user_input or "exit" in user_input:
            print("Rad AI: See you later! Stay rad! 👋")
            break
        
        else:
            print("Rad AI: Hmm... Interesting! Tell me more.")

# Start Rad AI
if __name__ == "__main__":
    rad_ai()
