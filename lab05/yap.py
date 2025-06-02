import random

words = {
    "Time": ["One minute ago", "Yesterday", "Last February", "On Christmas", "Last Year", "Once upon a time"],
    "noun": ["rice cake", "cheesecake", "chestnut tree", "hairball", "vacuum cleaner", "hiccup"],
    "verb": ["squeaked", "whistled", "climbed", "laughed", "hiccuped", "shimmied"],
    "adjective": ["colorful", "handsome", "frivolous", "punctual", "flaming", "disinterested"],
    "preposition": ["through", "over", "under", "beyond", "across", "into", "in front of", "behind", "between"],
    "adverb": ["just", "interestingly", "hilariously", "spotily", "frighteningly", "onboxiously"],
    "color": ["pink", "blue", "mauve", "red", "transparent", "forest green", "maroon", "auburn", "sea foam green", "brown"],
    "person’s": ["coach's", "mom's","gardener's","teacher's","motivational speaker's", "comedian's"],
    "place": ["office", "living room", "school", "house", "pool", "car"]
}

templates = ["Time the color noun verb preposition the person’s adjective color noun that was adverb adjective before",
    "The adverb color noun verb preposition the person’s adverb adjective place",
    "Time the person’s place was invaded by the adjective color noun that verb preposition the adverb color place"
    ]


def random_sentence():
        sentence = []
        for token in random.choice(templates).split():
            if token in words:
                sentence.append(random.choice(words[token])) 
            else:
                sentence.append(token)
        return " ".join(sentence) + ". "
        
def random_paragraph(): 
        for _ in range(5):
            print(random_sentence(), end="")
        

random_paragraph()