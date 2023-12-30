# Import necessary libraries
from googlesearch import search  # For performing Google searches
from webbrowser import open  # For opening URLs in the web browser

# Function to perform a Google search


def google_search(query, no_of_results):
    # Perform the search and return results
    result = search(query, num=no_of_results, pause=2, stop=no_of_results)
    return result


if __name__ == "__main__":
    # Get user input for the search query and number of results
    query = input("Enter the Query: ")
    no_of_results = int(input("Enter number of tabs open in browser: "))

    # Perform the search and open each result in the browser
    for i in google_search(query, no_of_results):
        open(i)  # Open each search result URL in the web browser
