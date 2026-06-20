
KNOWLEDGE_BASE = {
    #greetuser
    "hello"        : "Heya {name}! What's on your mind?",
    "hi"           : "Hiii, {name}! What can I help you with?",
    "hey"          : "Hey, {name}! What's up?",
    "good morning" : "Good morning, {name}! Hope the day's treating you well.",
    "good evening" : "Good evening, {name}! What would you like to talk about?",
    "yo"           : "Yo, {name}! What's poppin'?",

    #Identity
    "who are you"  : "I'm Savvy — a rule-based AI chatbot built by Anna. I'm her first ever project as an intern! I use no neural networks, just pure logic!",
    "what are you" : "I'm a deterministic chatbot. Every response is hard-coded and 100% predictable, therefore we've got zero hallucination risk ;)",
    "your name"    : "I'm Savvy! Enchantè!",

    #AI knowledge
    "what is ai"               : "So, Artificial Intelligence is the field of building systems that can do things that normally require human intelligence. Things like understanding language, recognising images, or making decisions.",
    "what is a chatbot"        : "A chatbot is a program that essentially simulates conversation. Rule-based bots like me use fixed logic whereas ML-based bots learn patterns from data.",
    "what is machine learning" : "Machine Learning is a subset of AI where systems learn from data instead of following presupposed hand-written rules.",
   
    #help
    "help"            : "I can answer questions about AI, crack a joke, or play a game with you!\n\nTry asking:\n  - What is AI?\n  - Who are you?\n  - Tell me a joke\n  - Play a game",
    "what can you do" : "I can chat about AI basics, crack a joke, or play a number guessing game with you. Type 'help' for hints!",

    #basic
    "how are you"  : "Doing pretty good for a chatbot :) How about you?",
    "i am fine"    : "Goody good :D Anything I can help with, {name}?",
    "i am good"    : "So am I! Let me know if you need help with anything",
    "thank you"    : "You're welcome! Happy to help, {name}",
    "thanks"       : "Don't mention it, {name}",

    #jokes
    "tell me a joke" : "What has wheels and flies but isn't an airplane? \nA garbage truck, hahaha 😝",
    "joke"           : "How to say 'no' in India :\ndekhta hoon \nthodi der mein batata hoon \npakka nahi hai abhi \nghar waalon se puchna padega 🤣",
    "another joke"   : "Get ready for some good ol' dad jokes 😌 So. What happens to an impatient Ice-cream? \nIt has a melt-down!",
    "one more"       : "What do you called a sick eagle? \nAn ILLEGAL! 💀",

    #entertainment
    "play a game" : "__GAME_MENU__",
    "game"        : "__GAME_MENU__",
    "lets play"   : "__GAME_MENU__",
    "play game"   : "__GAME_MENU__",

    #byeee
    "bye"     : "See youuu 👋",
    "goodbye" : "Goodbye, {name}!",
    "see you" : "Byee! God bless ya, {name}",
}

EXIT_COMMANDS = {"exit", "quit", "q", "stop"}

FALLBACK = ("Hmmm, well, I am not sure about that one yet - my knowledge base is still growing!\n"
            "Type 'help' to see what I can do, or 'play a game' for some fun.")


TRIVIA_QUESTIONS = [
    {
        "q"      : "What does 'AI' stand for?",
        "choices": ["a) Automated Interface", "b) Artificial Intelligence",
                    "c) Automated Intelligence", "d) Artificial Interface"],
        "answer" : "b",
        "explain": "AI stands for Artificial Intelligence — the simulation of human intelligence by machines."
    },
    {
        "q"      : "Which language is most commonly used for AI development?",
        "choices": ["a) Java", "b) C++", "c) Python", "d) Ruby"],
        "answer" : "c",
        "explain": "Python dominates AI/ML thanks to libraries like TensorFlow, PyTorch, and scikit-learn."
    },
    {
        "q"      : "What type of AI is a rule-based chatbot?",
        "choices": ["a) Machine Learning", "b) Deep Learning",
                    "c) Deterministic / Symbolic AI", "d) Reinforcement Learning"],
        "answer" : "c",
        "explain": "Rule-based chatbots are Deterministic/Symbolic AI — they follow explicitly programmed rules."
    },
    {
        "q"      : "What is a neural network inspired by?",
        "choices": ["a) Computer circuits", "b) The human brain",
                    "c) Decision trees", "d) Spreadsheets"],
        "answer" : "b",
        "explain": "Neural networks are loosely modelled on the structure of neurons in the human brain."
    },
    {
        "q"      : "What does 'ML' stand for in tech?",
        "choices": ["a) Machine Logic", "b) Meta Language",
                    "c) Machine Learning", "d) Model Layer"],
        "answer" : "c",
        "explain": "ML = Machine Learning — a branch of AI where systems learn patterns from data."
    },
]

#sanitisation

def sanitize(raw: str) -> str:
    """Lowercase, strip whitespace, and remove punctuation."""
    import string
    cleaned = raw.lower().strip()
    cleaned = cleaned.translate(str.maketrans("", "", string.punctuation))
    return cleaned

#ask user name
def ask_name() -> str:
    """Ask the user for their name once at startup and return a clean,
    capitalised version of it (e.g. 'anna' -> 'Anna')."""
    while True:
        raw = input("Savvy: Heya! Great to have you here. First things first, what would you like me to call you?\nYou: ").strip()
        if raw:
            lower = raw.lower()
            prefixes = ("my name is ", "i am ", "i'm ", "im ", "call me ")
            for p in prefixes:
                if lower.startswith(p):
                    raw = raw[len(p):].strip()
                    break
            name = raw.split()[0] if raw.split() else ""
            if name:
                return name.capitalize()
        print("Savvy: I didn't quite catch that — go ahead and type your name.")
 
#games

GAME_MIN = 1
GAME_MAX = 30


def play_number_game():
    import random
    secret = random.randint(GAME_MIN, GAME_MAX)
    attempts = 0
    print("\nSavvy: Alrighty, {name}, game on! I'm thinking of a number between {GAME_MIN} and {GAME_MAX}.")
    print("       Try to nail it in as few guesses as possible!\n")

    while True:
        raw = input("Your guess: ").strip()
        if raw.lower() in EXIT_COMMANDS or raw.lower() == "quit game":
            print(f"Savvy: Game over! The number was {secret}. Come back anytime! 👾")
            break
        try:
            num = int(raw)
        except ValueError:
            print("Savvy: That's not a number! Try again.")
            continue

        if num < GAME_MIN or num > GAME_MAX:
            print("Savvy: Out of range! Pick a number between {GAME_MIN} and {GAME_MAX}.")
            continue

        attempts += 1
        if num == secret:
            if attempts == 1:
                praise = "Are you a tech-psychic? Incredible! You got it in the first try itself?!"
            elif attempts <= 3:
                praise = f"Amazing - only {attempts} attempts! 🎉"
            elif attempts <= 6:
                praise = f"Nice work - {attempts} attempts! 🙌"
            else:
                praise = f"Got it in {attempts} attempts. We can play again!"
            print(f"Savvy: 🎯 Correct! The number was {secret}. {praise}")
            break
        elif num < secret:
            close = " (You're really close!)" if secret - num <= 3 else ""
            print(f"Savvy: 📈 Higher!{close}")
        else:
            close = " (You're really close!)" if num - secret <= 3 else ""
            print(f"Savvy: 📉 Lower!{close}")


def play_trivia_game():
    import random
    questions = TRIVIA_QUESTIONS.copy()
    random.shuffle(questions)
    score = 0
    total = len(questions)

    print(f"\nSavvy: AI Trivia time! 🧠 {total} questions. Type the letter of your answer.\n")

    for i, q in enumerate(questions, 1):
        print(f"  Q{i}. {q['q']}")
        for choice in q["choices"]:
            print(f"       {choice}")
        answer = input("  Your answer: ").strip().lower()
        answer = answer.translate(str.maketrans("", "", ".)("))  # clean stray punctuation

        if answer == q["answer"]:
            score += 1
            print(f"  Savvy: ✅ Correct! {q['explain']}\n")
        else:
            print(f"  Savvy: ❌ Not quite. The answer was {q['answer'].upper()}. {q['explain']}\n")

    pct = round((score / total) * 100)
    if pct == 100:
        grade = "Perfect score! You're an AI genius! 🏆"
    elif pct >= 71:
        grade = "Great job! Solid AI knowledge. 🎉"
    elif pct >= 43:
        grade = "Not bad! Keep learning and you'll ace it. 📚"
    else:
        grade = "Room to grow — keep exploring AI concepts! 💡"

    print(f"Savvy: Quiz complete! Your score: {score}/{total} ({pct}%) — {grade}")


def show_game_menu():
    print("\nSavvy: Let's play! Pick a game:")
    print("         1️⃣  Number Guessing — I pick a number 1–20, you guess it.")
    print("         2️⃣  AI Trivia Quiz  — 5 questions about AI & tech.")
    print("       Type 1 or 2 (or 'exit' to cancel).\n")

    while True:
        choice = input("Your choice: ").strip()
        if choice == "1":
            play_number_game()
            break
        elif choice == "2":
            play_trivia_game()
            break
        elif choice.lower() in EXIT_COMMANDS:
            print("Savvy: No worries! Come back anytime. 🎮")
            break
        else:
            print("Savvy: Just type 1 or 2!")

#main loop running
            
def run_chatbot():
    print("=" * 55)
    print("  Welcome to Savvy : I'm a rule-based AI Chatbot 😁")
    print("=" * 55)
    
    name = ask_name()
    print(f"\nSavvy : That's a wonderful name! Great to meet you, {name}!")
    print("  Type 'help' for tips. Type 'exit' to quit.")


    while True:
        raw = input(f"\n{name}: ")
        clean = sanitize(raw)

        if not clean:
            print("Savvy: Please type something!")
            continue

        if clean in EXIT_COMMANDS:
            print("Savvy: Session ended. See ya soon, {name}. ")
            break

        response = KNOWLEDGE_BASE.get(clean, FALLBACK)

        if response == "__GAME_MENU__":
            show_game_menu()
        else:
            print(f"Savvy: {response.format(name=name)}")




if __name__ == "__main__":
    run_chatbot()
