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