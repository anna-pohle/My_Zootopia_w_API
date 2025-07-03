import requests


REQUEST_URL = "https://api.api-ninjas.com/v1/animals?name={}"
API_KEY = "pukp8Yg3NDo2oXht0bMqVw==zbvHVk0XgdOz2exE"

def get_animal_data(REQUEST_URL, animal_name):
  """ Gets animal data from the API """
  REQUEST_URL = REQUEST_URL.format(animal_name)
  response = requests.get(REQUEST_URL, headers={'X-Api-Key': API_KEY})
  if response.status_code == requests.codes.ok:
      return response.json()
  else:
      print("Error:", response.status_code, response.text)
      return None


def generate_html_string_from_json(animals_data):
    """
    take json data and transform into html code: information blocks for every animal in the database
    :param animals_data:
    :return: html-string "animal_info"
    """
    website_string = ""
    for animal_obj in animals_data:
        website_string += serialize_animal(animal_obj)
    return website_string


def serialize_animal(animal_obj):
    """
    take one dictionary from the original list from json and turn it into html
    """
    animal_info = ""
    animal_info += "<li class='cards__item'>"
    try:
        name = animal_obj['name']
        animal_info += f"<div class='card__title'> {name}</div>"
    except KeyError:
        pass
    animal_info += "<p class='card__text'>"
    try:
        diet = animal_obj['taxonomy']['order']
        animal_info += f"<strong>Diet:</strong> {diet}<br/>\n"
    except KeyError:
        pass
    try:
        location = ", ".join(animal_obj['locations'])
        animal_info += f"<strong>Location:</strong> {location}<br/>\n"
    except KeyError:
        pass
    try:
        type = animal_obj['characteristics']['type']
        animal_info += f"<strong>Type:</strong> {type}<br/>\n"
    except KeyError:
        pass
    animal_info += "</p></li>"
    return animal_info


def main():
    user_animal = input("Enter a name of an animal:")
    animals_data = get_animal_data(REQUEST_URL, user_animal)
    if animals_data == []:
        website_string = f"<li class='cards__item'><h2>The animal '{user_animal}' doesn't exist :(.</h2></li>"
    else:
        website_string = generate_html_string_from_json(animals_data)

    with open ("animals_template.html", "r") as origin_file:
        html_skeleton = origin_file.read()
    with open("animals.html", "w") as newfile:
        newfile.write(html_skeleton.replace("__REPLACE_ANIMALS_INFO__", website_string))
    print("Website was successfully generated to the file animals.html")


if __name__ == "__main__":
    main()