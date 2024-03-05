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
print(attractions)
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
print(attractions)