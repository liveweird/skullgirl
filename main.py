import json
import streamlit as st


def read_input(file_name="./input.json"):
    with open(file_name, "r") as file:
        data = json.load(file)
    return data


def pick_word(json_data):
    words = json_data["words"]
    import random
    word = random.choice(words)
    st.session_state['word'] = word


def compare_words(word1, word2):
    # remove whitespace from both words
    word1 = word1.strip()
    word2 = word2.strip()
    # compare two words, case insensitive, return True if equal
    return word1.lower() == word2.lower()

def translate(to_be_translated):
    import requests

    API_TOKEN = "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"
    API_URL = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-pl-en"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        data = response.json()
        return data[0]["translation_text"]

    output = query({
        "inputs": to_be_translated,
    })
    return output


def render_ui():
    st.session_state['points'] = 0
    st.title("Help a Skullgirl prepare for English lessons!")
    st.write("Randomly chosen word: " + st.session_state['word'])
    input_text = st.text_input("Translate this word to English", key="input")
    if st.button("Compare"):
        st.write("Proper translation: " + translate(st.session_state['word']))
        if compare_words(st.session_state['word'], input_text):
            st.write("Correct!")
            st.session_state['points'] += 1
            if st.button("Next word"):
                pick_word(read_file)
        else:
            st.write("Wrong!")
            st.session_state['points'] = 0
            if st.button("Next word"):
                pick_word(read_file)
    st.write("Points: " + str(st.session_state['points']))


if __name__ == '__main__':
    read_file = read_input()
    pick_word(read_file)
    render_ui()
