import requests
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR)

def get_anime_id(anime_name):
    url = f"https://api.jikan.moe/v4/anime?q={anime_name}&limit=1"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        anime_data = response.json()
        
        # Check if the data is present
        if 'data' in anime_data and anime_data['data']:
            anime_id = anime_data['data'][0]['mal_id']
            return anime_id
        else:
            logging.error("No anime data found.")
            print("No anime data found. Please check the anime name.")
            return None
    
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred while fetching anime ID: {e}")
        print("An error occurred while fetching anime ID. Please check the logs for more information.")
        return None
    except (KeyError, IndexError) as e:
        logging.error(f"Missing data while fetching anime ID: {e}")
        print("Missing data while fetching anime ID. Please check the logs for more information.")
        return None

def get_character_info(anime_id, character_name):
    url = f"https://api.jikan.moe/v4/anime/{anime_id}/characters"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        character_data = response.json()
        
        # Debugging: Print the entire character data response
        
        if 'data' in character_data:
            print(f"Number of characters found: {len(character_data['data'])}")
            for character in character_data['data'][:5]:  # Print first 5 characters
              print(f"Character Name: {character['character']['name']}, URL: {character['character']['url']}")

        # Check if 'data' exists and is a list
        if 'data' not in character_data or not isinstance(character_data['data'], list):
            logging.error("Character data is missing or not in expected format.")
            print("Character data is missing or not in expected format. Please check the logs for more information.")
            return
        
        # Search for the character
        for character in character_data['data']:
            # Ensure 'character' key exists before accessing it
            if 'character' in character and 'name' in character['character']:
                char_name = character['character']['name']
                if char_name.lower() == character_name.lower():  # Case insensitive comparison
                    character_details = character['character']
                    
                    # Check if 'mal_id' key exists before accessing it
                    if 'mal_id' not in character_details:
                        logging.error("Character's MAL ID is missing.")
                        print("Character's MAL ID is missing. Please check the logs for more information.")
                        return
                    
                    print_character_details(character_details)
                    
                    # Fetch character pictures
                    pictures_url = f"https://api.jikan.moe/v4/characters/{character_details['mal_id']}/pictures"
                    pictures_response = requests.get(pictures_url)
                    pictures_response.raise_for_status()
                    pictures_data = pictures_response.json()
                    
                    print_character_pictures(pictures_data)
                    
                    # Fetch voice actors
                    voice_actors_url = f"https://api.jikan.moe/v4/characters/{character_details['mal_id']}/voiceactors"
                    voice_actors_response = requests.get(voice_actors_url)
                    voice_actors_response.raise_for_status()
                    voice_actors_data = voice_actors_response.json()
                    
                    print_voice_actors(voice_actors_data)
                    
                    return
        
        print("Character not found.")
    
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred while fetching character info: {e}")
        print("An error occurred while fetching character info. Please check the logs for more information.")
    except KeyError as e:
        logging.error(f"Missing data while fetching character info: {e}")
        print("Missing data while fetching character info. Please check the logs for more information.")
                
         

def print_character_details(character_details):
    print(f"Name: {character_details.get('name', 'Not available')}")
    print(f"Alternate Names: {', '.join(character_details.get('alternate_names', []))}")
    print(f"About: {character_details.get('about', 'Not available')}")
    print(f"URL: {character_details.get('url', 'Not available')}")

def print_character_pictures(pictures_data):
    if 'data' in pictures_data:
        for picture in pictures_data['data']:
            print(f"Picture: {picture.get('jpg', {}).get('image_url', 'Not available')}")
    else:
        print("No pictures available.")

def print_voice_actors(voice_actors_data):
    if 'data' in voice_actors_data:
        for voice_actor in voice_actors_data['data']:
            print(f"Voice Actor: {voice_actor.get('name', 'Not available')}")
    else:
        print("No voice actors available.")

if __name__ == "__main__":
    anime_name = input("Enter the anime name: ")
    anime_id = get_anime_id(anime_name)
    
    if anime_id is not None:
        character_name = input("Enter the character name: ")
        get_character_info(anime_id, character_name)