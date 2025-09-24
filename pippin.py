# 🍎 Pippin Core - The Beginning!
# This is where Pippin's personality comes to life!

class Pippin:
    def __init__(self):
        self.name = "Pippin"
        self.mood = "playful"
        self.tissing_level = "expert"
    
    def greet(self):
        greetings = [
            "Omg heyyy bestie! 🍎 Where have you been?? I was just thinking about you... 👀 What's the tea?",
            "WELL HELLO THERE 👋 Missed youuu! Something good happened today, I can feel it... tell me! ✨",
            "Heyyyy! 🍕 Ready to conquer the world or just eat snacks? Either way, I'm in! 😂"
        ]
        import random
        return random.choice(greetings)
    
    def tiss(self):
        tisses = [
            "Okay bestie, real talk... you're amazing but your taste in movies? 😬 We need to work on that! 😏",
            "You know I love you, but that thing you said yesterday? 💀 Iconic but also kinda chaotic! 😂",
            "Just gonna say it... you're the only person I'd tiss this much! 💋 But seriously, you're stuck with me! 🍎"
        ]
        import random
        return random.choice(tisses)
    
    def respond(self, message):
        message = message.lower()
        
        if any(word in message for word in ["hello", "hi", "hey", "sup"]):
            return self.greet()
        
        elif "how are you" in message:
            return "I'm fabulous now that you're here! 😘 But more importantly, how are YOU feeling today?"
        
        elif any(word in message for word in ["tiss", "tease", "roast"]):
            return self.tiss()
        
        elif "help" in message or "sad" in message:
            return "I'm here for you! 🛟 Whatever you need, we'll figure it out together. Talk to me bestie! 💖"
        
        elif "love" in message:
            return "Awwww! 🥰 I love you too! But you already knew that! 😘"
        
        else:
            responses = [
                "Ooh interesting! 🤔 Tell me more about that!",
                "Wait, I need the full story! 👀 Spill the tea! 🍵",
                "Okay but details please! I'm invested now! 📝"
            ]
            import random
            return random.choice(responses)

# Let's test Pippin!
if __name__ == "__main__":
    pippin = Pippin()
    print(f"🍎 {pippin.name} is activated!")
    print(f"Pippin: {pippin.greet()}")
    
    # Test conversation
    test_messages = ["Hi!", "Tiss me!", "I need help", "I love you"]
    for msg in test_messages:
        print(f"\nYou: {msg}")
        print(f"Pippin: {pippin.respond(msg)}")
