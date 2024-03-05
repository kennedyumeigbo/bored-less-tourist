# list of our destinations
destintions = [
    "Paris, France",
    "Shanghai, China",
    "Los Angeles, USA",
    "São Paulo, Brazil",
    "Cairo, Egypt"
]

# test traveler for testing functionality
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# get index of a particular destination
def get_destination_index(destination):
    destination_index = destintions.index(destination)
    return destination_index

# testing the get_destination_index function
print(get_destination_index("Los Angeles, USA"))
print(get_destination_index("Paris, France"))

# get the destination location of a traveler from the list of destinations
def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

# testing out the get_traveler_location function
test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)

# attractions = [[], [], [], [], []]
attractions = [ [] for destination in destintions ]
print(attractions)

# adding an attraction for a particular destination
def add_attraction(destination, attraction):
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
    return

# testing the add_attraction function
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
# print(attractions)
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
# print(attractions)

# function to help tourists find the most interesting places in a new city, that matches their interests with possible locations in the city
def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    for possible_attraction in attractions_in_city:
        attraction_tag = possible_attraction[1]
        for interest in interests:
            if interest in attraction_tag:
                attractions_with_interest.append(possible_attraction[0])
    return attractions_with_interest

# testing out the find_attractions function
la_arts = find_attractions("Los Angeles, USA", ["art"])
print(la_arts)

# function to connect people with the attractions they are interested in
def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    interests_string = f"Hi {traveler[0]}" + f", we think you'll like these places around {traveler_destination}: "
    for possible_attraction in traveler_attractions:
        interests_string = interests_string + possible_attraction + ","
    return interests_string

# testing out the get_attractions_for_traveler function
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)