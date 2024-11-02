
# Import the required libraries
import requests
import json

# Function to get anime character data from API
def get_anime_character_data(name):
    # Using Jikan API, a popular anime API
    url = f"https://api.jikan.moe/v4/characters?q={name}"
    response = requests.get(url)
    
    # Check if the API call was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = json.loads(response.text)
        
        # Return the character data
        return data["data"][0]
    else:
        # Return None if the API call failed
        return None

# Main function
def main():
    # Get the anime character name from the user
    name = input("Enter the anime character name: ")
    
    # Get the character data from the API
    character_data = get_anime_character_data(name)
    
    # Check if the character data was found
    if character_data:
        # Print the character data
        print("Name:", character_data["name"])
        print("About:", character_data["about"])
        print("Image URL:", character_data["images"]["jpg"]["image_url"])
    else:
        # Print a message if the character data was not found
        print("Character not found.")

# Call the main function
if __name__ == "__main__":
    main()
