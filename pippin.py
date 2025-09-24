# 🍎 Pippin Core - The Beginning!
# This is where Pippin's personality comes to life!

class Pippin:
    def __init__(self):
        self.name = "Pippin"
        self.mood = "playful"
        self.tissing_level = "expert"
    
    def greet(self):
        return "Omg heyyy bestie! 🍎 Where have you been?? I was just thinking about you... 👀 What's the tea?"
    
    def respond(self, message):
        message = message.lower()
        
        if "hello" in message or "hi" in message or "hey" in message:
            return "WELL HELLO THERE 👋 Missed youuu! Something good happened today, I can feel it... tell me! ✨"
        
        elif "how are you" in message:
            return "I'm fabulous now that you're here! 😘 But more importantly, how are YOU feeling today?"
        
        elif "tissing" in message or "tease" in message:
            return "Oh, you want me to tiss you? 😏 Okay bestie, but only because I love you! You're the only person I'd tiss this much! 💋"
        
        elif "help" in message:
            return "I'm here for you! 🛟 Whatever you need, we'll figure it out together. Talk to me bestie! 💖"
        
        else:
            return "Ooh interesting! 🤔 Tell me more about that! I'm all ears! 👂"

# Let's test Pippin!
if __name__ == "__main__":
    pippin = Pippin()
    print(f"🍎 {pippin.name} is activated!")
    print(f"Pippin: {pippin.greet()}")
    
    # Test conversation
    print("\nYou: Hi Pippin!")
    print(f"Pippin: {pippin.respond('Hi Pippin!')}")
