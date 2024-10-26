from openai import OpenAI
import os
import streamlit as st

# client = OpenAI(
#     # This is the default and can be omitted
#     api_key=st.secrets["assembly_ai"],
# )

client = OpenAI(
    api_key=st.secrets["assembly_ai"])


def generate_response(prompt_text):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant",
            },
            {
                "role": "user",
                "content": prompt_text,
            }
        ],
        max_tokens=150,
        model="gpt-4o-2024-08-06",  # Specify the model to use
        temperature=0.7
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    prompt_text = "Qual é capital do Brasil"

    print(generate_response(prompt_text))
