import requests
import random

# Define the book data locally
books_data = [
    {"name": "HR. Abu Daud", "id": "abu-daud", "available": 4419},
    {"name": "HR. Ahmad", "id": "ahmad", "available": 4305},
    {"name": "HR. Bukhari", "id": "bukhari", "available": 6638},
    {"name": "HR. Darimi", "id": "darimi", "available": 2949},
    {"name": "HR. Ibnu Majah", "id": "ibnu-majah", "available": 4285},
    {"name": "HR. Malik", "id": "malik", "available": 1587},
    {"name": "HR. Muslim", "id": "muslim", "available": 4930},
    {"name": "HR. Nasai", "id": "nasai", "available": 5364},
    {"name": "HR. Tirmidzi", "id": "tirmidzi", "available": 3625}
]

api_url = "https://api.hadith.gading.dev"

def fetch_random_arabic_hadith():
    errors = []

    try:
        # Choose a random book from the locally defined data
        chosen_book = random.choice(books_data)

        # Extract information for the chosen book
        random_book_id = chosen_book["id"]
        max_range = chosen_book["available"]

        # Choose a random hadith number within the available range
        if max_range > 0:
            random_hadith_number = random.randint(1, max_range)

            # Generate the request structure
            request_structure = f"{api_url}/books/{random_book_id}?range={random_hadith_number}-{random_hadith_number}"

            # Get the random hadith
            response = requests.get(request_structure)
            response_json = response.json()

            if response_json:
                # Extract the "arab" content
                arabic_content = response_json['data']['hadiths'][0]['arab']
                rawi = response_json['data']['name']
                number = response_json['data']['hadiths'][0]['number']
                
                
                content =[]
                content.append(arabic_content)
                content.append(rawi)
                content.append(number)
                
                return content

            else:
                errors.append(f"Failed to retrieve a random Arabic hadith. Response: {response_json}")
                return  errors
        else:
            errors.append(f"The selected book {random_book_id} has no available hadiths.")
            return errors

    except requests.exceptions.RequestException as e:
        errors.append(f"Error: {e}")
        return errors


