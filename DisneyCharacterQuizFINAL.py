# Ask for users name 
print("Hi! Welcome to the Disney Character Quiz!")
name = input("Please type your name: ")
# If left blank, use "friend" 
if name.strip() == "":
    name = "Friend"
# Personalized greeting
print(f"\nHey {name}, I hope you love Disney because this quiz will help you discover the character that best fits you!")
# Which category question
print("\nBefore we get started, choose which type of Disney character you are more interest in:")
print("1. Disney Princesses")
print("2. Disney Princes")
print("3. Disney Animals")
category = input ("Type 1, 2, or 3:")

# Category selection
print(f"\nAwesome choice, {name}! You selected option {category}. Now we can get into the real fun!")

#Dictionary
princesses = {
"Elsa": ["independent", "reserved", "protective"],
"Tiana": ["hardworking", "ambitious", "practical"],
"Ariel": ["curious", "adventurous", "optimistic"],
"Belle": ["intelligent", "kind", "open-minded"]
}

princes = {
"Eric": ["brave", "romantic", "loyal"],
"Charming": ["polite", "traditional", "hopeful"],
"Aladdin": ["resourceful", "playful", "big-hearted"],
"Naveen": ["fun-loving", "charismatic", "easygoing"]

}

animals = {
"Olaf": ["friendly", "silly", "warm-hearted"],
"Simba": ["confident", "playful", "protective"],
"Maximus": ["determined", "loyal", "dutiful"],
"Nemo": ["curious", "brave", "sweet"]
}

princess_questions = [
    { 
        "question": "What motivates you the most?",
        "options": {
            "a": "Protecting the people you love",
            "b": "Achieving your dreams through hard work",
            "c": "Exploring the unknown",
            "d": "Learning and undedrstanding the world"
        },
        "traits": {
            "a": "protective",  #Elsa
            "b": "ambitious",   #Tiana
            "c": "curious",     #Ariel
            "d": "intelligent"   #Belle
        }
    },
    {   "question": "Which environment feels most like home?",
        "options": {
            "a": "A quiet, snowy place",
            "b": "A warm, lively city",
            "c": "The ocean or beach",
            "d": "A cozy library"
        },
        "traits": {
            "a": "reserved",
            "b": "practical",
            "c": "optimistic",
            "d": "open-minded"
        }
    },
    {   "question": "Which quality do you value most in yourself?",
        "options": {
            "a": "Your independence",
            "b": "Your determination",
            "c": "Your sense of adventure",
            "d": "Your kindess and empathy"
        },
        "traits": {
            "a": "independent",
            "b": "ambitious",
            "c": "curious",
            "d": "kind"
        }
    },
    {   "question": "What type of friend are you?",
        "options": {
            "a": "The protective one",
            "b": "The hardworking one",
            "c": "The fun, spontaneous one",
            "d": "The thoughtful, understanding one"
        },
        "traits": {
            "a": "protective",
            "b": "practical",
            "c": "optimistic",
            "d": "open-minded"
        }
    },
    {   "question": "What's your ideal weekend?",
        "options": {
            "a": "Relaxing alone and recharging",
            "b": "Working on a personal goal",
            "c": "Exploring or laarning something new",
            "d": "Reading or learning something new"
        },
        "traits": {
            "a": "reserved",
            "b": "hardworking",
            "c": "adventurous",
            "d": "intelligent"
        }
    },
    {   "question": "How do you handle conflict?",
        "options": {
            "a": "Distance yourself until you cool down",
            "b": "Talk it out calmly and logically",
            "c": "Follow your heart and express your feelings",
            "d": "Try to understand everyone's perspective"
        },
        "traits": {
            "a": "reserved",
            "b": "practical",
            "c": "optimistic",
            "d": "kind"
        }
    },
    {   "question": "Which role fits you best?",
        "options": {
            "a": "The leader",
            "b": "The achiever",
            "c": "The dreamer",
            "d": "The thinker"
        },
        "traits": {
            "a": "independent",
            "b": "ambitious",
            "c": "curious",
            "d": "intelligent"
        }
    }
]

princes_questions = [
    { 
        "question": "What do you look for in an adventure?",
        "options": {
            "a": "A chance to protect someone",
            "b": "A meaninful purpose",
            "c": "A clever challenge",
            "d": "A fun experience"
        },
        "traits": {
            "a": "loyal",         #Eric
            "b": "traditional",     #Charming
            "c": "resourceful",   #Aladdin
            "d": "easygoing"      #Naveen
        }
    },
    { 
        "question": "How do you make decisions?",
        "options": {
            "a": "With your heart",
            "b": "By following tradition",
            "c": "By trusting your instincts",
            "d": "By going with the flow"
        },
        "traits": {
            "a": "romantic",        
            "b": "hopeful",     
            "c": "big-hearted",  
            "d": "charismatic"      
        }
    },
    { 
        "question": "What's your biggest strength?",
        "options": {
            "a": "Your bravery",
            "b": "Your courtesy",
            "c": "Your creativity",
            "d": "Your charm"
        },
        "traits": {
            "a": "brave",        
            "b": "polite",     
            "c": "resourceful",  
            "d": "charismatic"      
        }
    },
    { 
        "question": "How do you treat others?",
        "options": {
            "a": "With loyalty and respect",
            "b": "With politeness and manners",
            "c": "With generosity and heart",
            "d": "With humor and warmth"
        },
        "traits": {
            "a": "loyal",        
            "b": "tradional",     
            "c": "big-hearted",  
            "d": "easygoing"      
        }
    },
   { 
        "question": "What kind of partner would you be?",
        "options": {
            "a": "Protective and devoted",
            "b": "Stable and dependable",
            "c": "Adventurous and supportive",
            "d": "Fun and carefree"
        },
        "traits": {
            "a": "romantic",        
            "b": "hopeful",     
            "c": "resourceful",  
            "d": "charismatic"      
        }
    },
    { 
        "question": "How do you approach meeting someone new?",
        "options": {
            "a": "Show genuine interest in them",
            "b": "Be kind and respectful",
            "c": "Break the ice with humor",
            "d": "Go with what feels the most natural"
        },
        "traits": {
            "a": "loyal",        
            "b": "traditional",     
            "c": "big-hearted",  
            "d": "charismatic"      
        }
    },
    { 
        "question": "How do you show appreciation to others?",
        "options": {
            "a": "By being there when it matters",
            "b": "By honoring traditions or gestures",
            "c": "By doing something thoughtful and unexpected",
            "d": "By making them smile"
        },
        "traits": {
            "a": "loyal",        
            "b": "traditonal",     
            "c": "big-hearted",  
            "d": "charismatic"      
        }
    },
]

animal_questions = [
    { 
        "question": "What brings you the most joy?",
        "options": {
            "a": "Sharing moments with others",
            "b": "Feeling confident in what you do",
            "c": "Finishing something important",
            "d": "Discovering something new"
        },
        "traits": {
            "a": "warm-hearted",    #Olaf
            "b": "protective",      #Simba
            "c": "dutiful",         #Maximus
            "d": "curious"          #Nemo
        }
    },
    { 
        "question": "How do you handle a tough day?",
        "options": {
            "a": "Try to stay upbeat",
            "b": "Push through with strength",
            "c": "Stay focused on what needs to be done",
            "d": "Look for something interesting to distract you"
        },
        "traits": {
            "a": "silly",   
            "b": "brave",      
            "c": "determined",         
            "d": "sweet"         
        }
    },
    { 
        "question": "What kind of activities do you enjoy?",
        "options": {
            "a": "Anything that makes people smile",
            "b": "Running around or being active",
            "c": "Helping someone reach a goal",
            "d": "Exploring unfamiliar places"
        },
        "traits": {
            "a": "warm-hearted",   
            "b": "playful",      
            "c": "loyal",         
            "d": "curious"         
        }
    },
    { 
        "question": "How do you respond when someone needs support?",
        "options": {
            "a": "Offer comfort",
            "b": "Stand strong for them",
            "c": "Take responsibility",
            "d": "Stay gentle and patient"
        },
        "traits": {
            "a": "warm-hearted",   
            "b": "protective",      
            "c": "dutiful",         
            "d": "sweet"         
        }
    },
    { 
        "question": "What's your favorite type of moment?",
        "options": {
            "a": "A silly moment with friends",
            "b": "A moment where you feel bold",
            "c": "A moment where you accomplish something",
            "d": "A moment of discovery"
        },
        "traits": {
            "a": "silly",   
            "b": "brave",      
            "c": "dutiful",         
            "d": "curious"         
        }
    },
    {
        "question": "What inner quality feels the most natural to you?",
        "options": {
            "a": "Comforting others",
            "b": "Standing strong in your opinions and beliefs",
            "c": "Taking responsibility without being asked",
            "d": "Seeking out new experiences"
        },
        "traits": {
            "a": "warm-hearted",   
            "b": "brave",      
            "c": "dutiful",         
            "d": "curious"         
        }
    },
    { 
        "question": "How would your best friend describe your natural energy?",
        "options": {
            "a": "Light and uplifting",
            "b": "Bold and fierce",
            "c": "Focused and reliable",
            "d": "Gentle and open"
        },
        "traits": {
            "a": "silly",   
            "b": "protective",      
            "c": "determined",         
            "d": "sweet"         
        }
    },
]

# Function to run the quiz
def run_quiz(questions):
    scores = {}

    for q in questions:
        print("\n" + q["question"])
        for key, text in q["options"].items():
            print(f"{key}) {text}")

        answer = input("Choose a, b, c, or d:").lower()

        while answer not in ["a", "b", "c", "d"]:
            answer = input("please type a, b, c, or d:").lower()
        
        trait = q["traits"][answer]
        scores[trait] = scores.get(trait, 0) + 1

    return scores

# Function to determine best character
def match_character(scores, characters):
    best_character = None
    best_score = -1 

    for character, traits in characters.items():
        score = sum(scores.get(t,0) for t in traits)
        if score > best_score:
            best_score = score
            best_character = character
    
    return best_character 

# Run quiz based on category
if category =="1":
    print("\nGreat! Let's beging the Disney Princess quiz!")
    result_scores = run_quiz(princess_questions)
    final_character = match_character(result_scores, princesses)
elif category =="2":
    print("\nGreat! Let's beging the Disney Prince quiz!")
    result_scores = run_quiz(princes_questions)
    final_character = match_character(result_scores, princes)
elif category =="3":
    print("\nGreat! Let's beging the Disney Animal quiz!")
    result_scores = run_quiz(animal_questions)
    final_character = match_character(result_scores, animals)
else:
    print("Invalid choice. PLease restart the quiz.")
    exit()

# Final result
print(f"\n {name}, your Disney character match is:{final_character}!")
