import random

jokes = [
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "I haven't slept for ten days, because that would be too long.",
    "My therapist says I have a preoccupation with vengeance. We'll see about that.",
    "I used to hate facial hair, but then it grew on me.",
    "Why don't scientists trust atoms? Because they make up everything... and they have trust issues from their childhood.",
    "I bought the world's worst thesaurus yesterday. Not only is it terrible, it's terrible.",
    "I'm reading a book about anti-gravity. It's impossible to put down.",
    "I told my cat a joke about dogs. He didn't laugh... but he also didn't leave the room, so I'm calling it progress.",
    "I invented a new word: Plagiarism!",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    "My wife accused me of being immature. I was so shocked I nearly choked on my Fruit Loops.",
    "I used to be addicted to soap, but I'm clean now.",
    "A photon checks into a hotel. The bellhop asks, 'Can I help you with your luggage?' The photon says, 'No thanks, I'm traveling light.'",
    "I told my girlfriend she drew her eyebrows too high. She seemed surprised.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "I'm terrified of elevators, so I'm going to start taking steps to avoid them.",
    "My friend's bakery burned down last night. Now his business is toast.",
    "I stayed up all night wondering where the sun went, then it dawned on me.",
    "The early bird might get the worm, but the second mouse gets the cheese.",
    "I'm reading a book on the history of glue – can't put it down.",
    "Time flies like an arrow. Fruit flies like a banana.",
    "I wondered why the baseball kept getting bigger. Then it hit me.",
    "A dyslexic man walks into a bra.",
    "I used to be a banker, but I lost interest.",
    "Broken pencils are pointless.",
    "What do you call a dinosaur that crashes his car? Tyrannosaurus Wrecks.",
    "I'm addicted to brake fluid, but I can stop anytime.",
    "Why did the scarecrow win an award? He was outstanding in his field.",
    "I got a job at a bakery because I kneaded dough.",
    "The math teacher called in sick with algebra."
]

def get_random_joke():
    return random.choice(jokes)