# Define the data array
data = ['Danawi Liam', 'Tarjaya', 'Daruna', 'Warsoni', 'John Wick', 'Hadi PS', 'Derian Lekso']

# Function to search in the array
def search_name(query):
    results = []
    query = query.lower()  # Convert query to lowercase for case-insensitive search
    for name in data:
        if query in name.lower():  # Check if query matches any part of the name
            results.append(name)
    return results

# Example usage
query = input("Enter name to search: ")
matches = search_name(query)

if matches:
    print("Matching names found:")
    for match in matches:
        print(match)
else:
    print("No matches found.")
