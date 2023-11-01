import gradio as gr


def translate(input):
    import requests

    API_TOKEN = "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"
    API_URL = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-pl-en"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        data = response.json()
        return data[0]["translation_text"]

    output = query({
        "inputs": input,
    })
    return output


app = gr.Interface(fn=translate, inputs="text", outputs="text", title="Help a Skullgirl prepare for English lessons!")

if __name__ == '__main__':
    app.launch(show_api=False)
