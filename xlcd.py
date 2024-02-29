import pandas as pd

# Define quotes for each genre
literature_quotes = [
    "The only way out of the labyrinth of suffering is to forgive.",
    "It is better to be hated for what you are than to be loved for what you are not.",
    "All that is gold does not glitter, Not all those who wander are lost.",
    "We accept the love we think we deserve.",
    "It does not do to dwell on dreams and forget to live.",
    "There are darknesses in life and there are lights, and you are one of the lights, the light of all lights.",
    "We are all in the gutter, but some of us are looking at the stars."
]

philosophy_quotes = [
    "The unexamined life is not worth living.",
    "Whereof one cannot speak, thereof one must be silent.",
    "I think, therefore I am.",
    "To be is to be perceived.",
    "In the beginning there was nothing, which exploded.",
    "The only true wisdom is in knowing you know nothing.",
    "Life must be understood backwards; but... it must be lived forward."
]

funny_quotes = [
    "I don't need a hair stylist, my pillow gives me a new hairstyle every morning.",
    "I'm not lazy, I'm on energy saving mode.",
    "I'm not clumsy, I'm just on a mission to find the floor.",
    "My bed is a magical place where I suddenly remember everything I was supposed to do.",
    "I'm not arguing, I'm just explaining why I'm right.",
    "I'm not short, I'm concentrated awesome!",
    "I'm not a complete idiot, some parts are missing."
]

motivational_quotes = [
    "The only way to do great work is to love what you do.",
    "Believe you can and you're halfway there.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "It always seems impossible until it's done.",
    "You are never too old to set another goal or to dream a new dream.",
    "Don't watch the clock; do what it does. Keep going."
]

happy_quotes = [
    "The best way to cheer yourself up is to try to cheer somebody else up.",
    "Happiness is not something ready made. It comes from your own actions.",
    "Count your age by friends, not years. Count your life by smiles, not tears.",
    "The purpose of our lives is to be happy.",
    "Happiness is not by chance, but by choice.",
    "The happiest people don't have the best of everything, they just make the best of everything.",
    "Be happy for this moment. This moment is your life."
]

humour_quotes = [
    "I am so clever that sometimes I don't understand a single word of what I am saying.",
    "Some people never go crazy. What truly horrible lives they must lead.",
    "I intend to live forever, or die trying.",
    "The only mystery in life is why the kamikaze pilots wore helmets.",
    "I'm writing a book. I've got the page numbers done.",
    "When I die, I want to go peacefully like my grandfather did, in his sleep - not screaming, like the passengers in his car.",
    "I asked God for a bike, but I know God doesn't work that way. So I stole a bike and asked for forgiveness."
]

self_improvement_quotes = [
    "You must be the change you wish to see in the world.",
    "No one can make you feel inferior without your consent.",
    "The only limit to our realization of tomorrow will be our doubts of today.",
    "You yourself, as much as anybody in the entire universe, deserve your love and affection.",
    "It is never too late to be what you might have been.",
    "The only person you are destined to become is the person you decide to be.",
    "Don't be pushed around by the fears in your mind. Be led by the dreams in your heart."
]

# Create a DataFrame
quotes_df = pd.DataFrame(columns=["Quote", "Genre"])

# Add quotes to the DataFrame
quotes_df = pd.concat([
    pd.DataFrame({"Quote": literature_quotes, "Genre": "Literature"}),
    pd.DataFrame({"Quote": philosophy_quotes, "Genre": "Philosophy"}),
    pd.DataFrame({"Quote": funny_quotes, "Genre": "Funny"}),
    pd.DataFrame({"Quote": motivational_quotes, "Genre": "Motivational"}),
    pd.DataFrame({"Quote": happy_quotes, "Genre": "Happy"}),
    pd.DataFrame({"Quote": humour_quotes, "Genre": "Humour"}),
    pd.DataFrame({"Quote": self_improvement_quotes, "Genre": "Self-Improvement"})
])

# Save the DataFrame to CSV
quotes_df.to_csv("quotes.csv", index=False)
