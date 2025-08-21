import requests

'''
We will set up our API endpoint to connect to ollama for now, this will allow us to get the system up and running we we will switch to the cloud later
'''
url = 'http://localhost:11434/api/generate'

# Call whenever the user sends a prompt
def generate_response(prompt):
    try:
        r = requests.post(url, json={
            "model": "phi4-mini:3.8b",
            "prompt": prompt,
            "stream": False, 
            "think": False,
        })
        
        # Check if the request was successful
        if r.status_code == 200:
            try:
                response_data = r.json()
                if "response" in response_data:
                    return response_data["response"]
                else:
                    return "Response format not as expected."
            except requests.exceptions.JSONDecodeError:
                # Handle case where response isn't valid JSON
                return "Received invalid JSON response from the model."
        else:
            return f"Error: API returned status code {r.status_code}"
            
    except Exception as e:
        return f"An error occurred: {str(e)}"