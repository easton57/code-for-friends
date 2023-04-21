import requests
import datetime
import sys

def rest_request():
    # set the base URL for the API
    url = "https://test.com:8080"

    # create a dictionary of headers to use with the REST API requests
    headers = {"Authorization": "api key"}
    
    # construct the XML payload for disabling the saved search
    disable_payload = {'disabled': '1'}

    # construct the XML payload for enabling the saved search
    enable_payload = {'disabled': '0'}

    # construct the REST API URLs for disabling and enabling the saved search
    disable_url = f"{url}/servicesNS/nobody/-/saved/searches/test"

    # send the REST API request to disable the saved search
    response = requests.post(disable_url, headers=headers, data=disable_payload, verify=False)

    # check if the request was successful
    if response.status_code == 200:

        # print a message indicating that the saved search was disabled
        print(f"The saved search '{i}' has been disabled.")

    else:

        # print an error message if the request was not successful
        print(f"Error: Failed to disable the saved search '{i}'.")


if __name__ == "__main__":
    rest_request()
    sys.exit()