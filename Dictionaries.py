""" Keys can only be strings, numbers, or tuples, but values can be any data type."""
#Create an empty Directory product
product = {}
# Create a sample dictionary
release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
print(release_year_dict)

# Get value by keys
print(release_year_dict['Thriller'] )

# Get all the keys in dictionary
print(release_year_dict.keys() )

# Get all the values in dictionary
print(release_year_dict.values() )

# Append value with key into dictionary
release_year_dict['Graduation'] = '2007'
print("Adding Graduation key ",release_year_dict)

# Delete entries by key
del release_year_dict['Thriller']
del release_year_dict['Graduation']
print(" Deleted Thriller and Graduation key ",release_year_dict)

# Verify the key is in the dictionary
print('The Bodyguard' in release_year_dict) #True
