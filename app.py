import streamlit as st
import json
import os

# Path to the dictionary data file
data_file = os.path.join("data", "dictionary.json")

# Load dictionary data
def load_data():
    with open(data_file, "r", encoding="utf-8") as f:
        return json.load(f)

# Save dictionary data
def save_data(data):
    with open(data_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Search for a word in the dictionary
def search_word(word, data):
    for entry in data['words']:
        if entry['word'].lower() == word.lower():
            return entry
    return None

# Streamlit UI
st.title("Yoruba Word Dictionary")

# Word search functionality
word = st.text_input("Enter an English word:")
if st.button("Search"):
    data = load_data()
    result = search_word(word, data)
    if result:
        st.write(f"**Word:** {result['word']}")
        st.write(f"**Meaning (Yoruba):** {result['meaning']}")
        st.write(f"**Synonyms (Yoruba):** {', '.join(result['synonyms'])}")
        st.write(f"**Antonyms (Yoruba):** {', '.join(result['antonyms'])}")
    else:
        st.write("Word not found.")

# Adding a new word to the dictionary
st.subheader("Add a New Word")
new_word = st.text_input("Word (English):")
new_meaning = st.text_input("Meaning (Yoruba):")
new_synonyms = st.text_input("Synonyms (Yoruba, comma-separated):")
new_antonyms = st.text_input("Antonyms (Yoruba, comma-separated):")

if st.button("Add Word"):
    data = load_data()
    if search_word(new_word, data):
        st.write("Word already exists.")
    else:
        new_entry = {
            "word": new_word,
            "meaning": new_meaning,
            "synonyms": [syn.strip() for syn in new_synonyms.split(",")],
            "antonyms": [ant.strip() for ant in new_antonyms.split(",")]
        }
        data['words'].append(new_entry)
        save_data(data)
        st.write("Word added successfully.")

