from googlesearch import search
from urllib.parse import urlparse

def count_websites_with_term(term):
    count = 0
    for url in search(term, stop=10):  # Adjust 'stop' as needed to control the number of results
        count += 1
        parsed_url = urlparse(url)
        print("Website {}: {}".format(count, url))
        print("   Scheme:", parsed_url.scheme)
        print("   Domain:", parsed_url.netloc)
        print("   Path:", parsed_url.path)
        print("   Query Parameters:", parsed_url.query)
        print("   Fragment:", parsed_url.fragment)
        print()
    return count

# Prompt the user to input a term to search for
term = input("Enter the term to search for on the internet: ")

# Count how many websites contain the term
count = count_websites_with_term(term)
print("Number of websites containing the term '{}': {}".format(term, count))
