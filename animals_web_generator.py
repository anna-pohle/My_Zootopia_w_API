import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def generate_string_from_json(animals_data):
    animal_info = ""
    for animal in animals_data:
        try:
            name = animal['name']
            animal_info += f"Name: {name}\n"
        except KeyError:
            pass
        try:
            diet = animal['taxonomy']['order']
            animal_info += f"Diet: {diet}\n"
        except KeyError:
            pass
        try:
            location = ", ".join(animal['locations'])
            animal_info += f"Location: {location}\n"
        except KeyError:
            pass
        try:
            type = animal['characteristics']['type']
            animal_info += f"Type: {type}\n"
        except KeyError:
            pass
        animal_info += "\n"
    return(animal_info)

def main():
    animals_data = load_data('animals_data.json')
    website_string = generate_string_from_json(animals_data)

    with open ("animals_template.html", "r") as origin_file:
        html_skeleton = origin_file.read()
    with open("animals.html", "w") as newfile:
        newfile.write(html_skeleton.replace("__REPLACE_ANIMALS_INFO__", website_string))




if __name__ == "__main__":
    main()