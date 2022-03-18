import json
import requests
import csv


def delete_profile(filename, profile_names):
    # Open the list of profiles which we want to remove from Multilogin
    with open(filename, 'r') as file:
        # Consider the first row as the row with data
        for_removal = csv.DictReader(file, fieldnames=['profile_name'])
        list_for_removal = list(for_removal)

        # Number of profiles in the list, set the counter
        number_of_profiles = len(list_for_removal)
        print('The number of profiles to remove is {}.'.format(number_of_profiles))
        print('The total number of profiles in Multilogin is {}.'.format(len(profile_names)))
        counter = 0

        for row in list_for_removal:
            for profile in profile_names:
                if profile.get('name') == row['profile_name']:
                    profile_id = profile.get('uuid')
                    response_request = requests.delete(URL + profile_id)
                    # answer = response_request.text
                    print('The profile {} is removed.'.format(profile.get('name')))
                    counter += 1
                    break
            else:
                if profile_names.index(profile) == len(profile_names) - 1:
                    print('The profile {} is not found.'.format(row['profile_name']))
                continue
            continue

        print('{} out of {} have been removed.'.format(counter, number_of_profiles))


# Mutlilogin and other variables
PORT = "30012"
URL = f"http://localhost:{PORT}/api/v2/profile/"
input_file = "remove_profiles.csv"

# Set variables for requests, get all profiles
payload, headers = {}, {}
response = requests.request("GET", URL, headers=headers, data=payload)
all_profiles = json.loads(response.text)

# Run the function
delete_profile(input_file, all_profiles)
