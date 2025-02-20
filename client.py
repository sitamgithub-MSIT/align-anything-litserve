import requests

url = "http://localhost:8000/predict"

# Input image path and question for the test
image_path = "images/math.png"
question = "What is the result of this problem?"

# Create the payload for the request
payload = {"image_path": image_path, "question": question}

# Send the request to the server
response = requests.post(url, json=payload)

# Print the JSON response
print(response.json())
