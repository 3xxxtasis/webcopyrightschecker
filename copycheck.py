import requests

def check_copyright(url):
    # Make a request to the website
    response = requests.get(url)

    # Check the response status code
    if response.status_code != 200:
        print("Error: Could not access website.")
        return

    # Check the content of the website for any potential copyright violations
    content = response.text
    if "copyright" in content:
        print("Warning: Possible copyright violation detected.")
    else:
        print("No copyright violations detected.")

url = input("Enter the URL of the website to check: ")
check_copyright(url)
