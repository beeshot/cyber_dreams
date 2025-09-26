import json

# Load your dream journal
with open("dreamjournal.jason", "r") as file:
    dream_data = json.load(file)

# Print all dream titles
for dream in dream_data["dreams"]:
    print(dream["title"])

from collections import Counter

# Count occurrences of symbols
symbol_counter = Counter()

for dream in dream_data["dreams"]:
    symbol_counter.update(dream["symbols"].keys())

print("Most Common Symbols:", symbol_counter.most_common(5))

import json
import matplotlib.pyplot as plt
from collections import Counter

# Load dream journal JSON file
file_path = "dreamjournal.jason"  # Update this with your actual file path

with open(file_path, "r") as file:
    dream_journal = json.load(file)

# Extract symbols from dreams
symbols = []
for dream in dream_journal["dreams"]:
    symbols.extend(dream.get("symbols", []))  # Ensure symbols exist

# Count occurrences of each symbol
symbol_counts = Counter(symbols)

# Visualization
plt.figure(figsize=(10, 5))
plt.bar(symbol_counts.keys(), symbol_counts.values(), color='purple')
plt.xlabel("Dream Symbols")
plt.ylabel("Frequency")
plt.title("Symbol Frequency in Dreams")
plt.xticks(rotation=45, ha="right")
plt.show()

# Extract emotions from dreams
emotions = []
for dream in dream_journal["dreams"]:
    emotions.extend(dream.get("emotions", []))  # Ensure emotions exist

# Count occurrences of each emotion
emotion_counts = Counter(emotions)

# Visualization - Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(emotion_counts.values(), labels=emotion_counts.keys(), autopct="%1.1f%%", colors=plt.cm.Paired.colors)
plt.title("Emotional Themes in Dreams")
plt.show()


