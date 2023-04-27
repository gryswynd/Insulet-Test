import openai
import requests
from bs4 import BeautifulSoup
from googlesearch import search

# Set up OpenAI API
openai.api_key = input("Enter your OpenAI API key: ")

# User input
content_type = input("Enter the type of content: ")
industry = input("Enter the industry: ")
target_language = input("Enter the target language: ")

# Generate content using OpenAI API
def generate_content(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

content_prompt = f"Create {content_type} content for the {industry} industry."
generated_content = generate_content(content_prompt)
print("Generated content:", generated_content)

# Search Google for translation best practices
query = f"transcreation best practices for the {industry} industry into {target_language}"
for url in search(query, num_results=10):
    best_practices_url = url
    break

# Scrape content from the URL
response = requests.get(best_practices_url)
soup = BeautifulSoup(response.text, "html.parser")
best_practices_text = ' '.join([p.text for p in soup.find_all('p')])

# Transcreate content using OpenAI API with best practices context
transcreation_prompt = f"Transcreate the following content into {target_language} Content: {generated_content}.\n\nFollowing these best practices to decide how to transcreate the content: {best_practices_text}"
transcreated_content = generate_content(transcreation_prompt)
print("Transcreated content:", transcreated_content)
