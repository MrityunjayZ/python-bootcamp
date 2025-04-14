# 

import requests  # Import the requests library

# Example: Fetch data from a public API
url = "https://jsonplaceholder.typicode.com/posts"  # A sample API
response = requests.get(url)  # Send a GET request

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Convert the response to JSON format
    print(data)  # Print the response data (a list of posts)

    # Access the first post (after successfully retrieving data)
    first_post = data[0]
    print("First Post:", first_post)  # Print the first post

    # Access specific fields
    title = first_post['title']
    print("Title:", title)
    body = first_post['body']
    formatted_body = body.replace('\n', ' ')  # Replace line breaks with space
    print("Body:", formatted_body)

    # Loop through all posts and print titles and bodies
    for post in data:
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}\n")

else:
    print("Failed to retrieve data:", response.status_code)

# 1. JSONPlaceholder (Fake blog data)
import requests
url = "https://jsonplaceholder.typicode.com/comments?postId=1"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
    first_post = data[0]
    print("First post is: ",first_post)
    title = first_post['name']
    body = first_post['body']
    formatted_body = body.replace('\n', '     ')  # Replaces newlines with space
    print('Body',formatted_body)
    
    for post in data:
        print(f'Title: {post['name']}')
        print(f'Body: {post['body']}\n')
else:
    print('Failed to retrive data:',response.status_code)

# 2. Public APIs List (from GitHub) 
# https://api.publicapis.org/entries - url not working
# 3. Cat Facts

import requests
url = "https://catfact.ninja/fact"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)

else:
    print('Failed to retrive data:',response.status_code)

# 4 CoinDesk – Bitcoin Price - network issue
# 5 Bored API

import requests
url = "https://www.boredapi.com/api/activity"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)

else:
    print('Failed to retrive data:',response.status_code) 
# response from above code is: Failed to retrive data: 503

# Mini Project: Random Dog Viewer (API + File Save)

import requests
url = "https://dog.ceo/api/breeds/image/random"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    image_url = data['message']
    print('Random Dog images URL :',image_url)
    with open('random_dog_url.text', 'w') as file:
        file.write(image_url)
    print('URL saved to random_dog_url.txt')

else:
    print('Failed to retrive data:',response.status_code)

