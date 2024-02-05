import openai

# optional; defaults to `os.environ['OPENAI_API_KEY']`
openai.api_key = 'sk-hBU3nlZc3UdpT0Hj5d7d8d99A3Bc4736Ac6037C61c26AdA2'

# all client options can be configured just like the `OpenAI` instantiation counterpart
openai.base_url = "https://api.chatgptid.net/v1"
openai.api_base = "https://api.chatgptid.net/v1"
openai.default_headers = {"x-foo": "true"}

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
)
print(completion.choices[0].message.content)

