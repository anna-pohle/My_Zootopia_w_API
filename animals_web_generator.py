import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def main():
    animals_data = load_data('animals_data.json')
    for animal in animals_data:
        try:
            name = animal['name']
            print(f"Name: {name}")
        except KeyError:
            pass
        try:
            diet = animal['taxonomy']['order']
            print(f"Diet: {diet}")
        except KeyError:
            pass
        try:
            location = ", ".join(animal['locations'])
            print(f"Location: {location}")
        except KeyError:
            pass
        try:
            type = animal['characteristics']['type']
            print(f"Type: {type}")
        except KeyError:
            pass
        print("")

if __name__ == "__main__":
    main()