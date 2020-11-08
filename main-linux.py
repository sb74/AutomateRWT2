#! /usr/bin/env python3
import os
import requests


def send_feedback(raw_dir):
    external_ip = "35.238.167.86"

    for file in os.listdir(raw_dir):
        file_path = os.path.join(raw_dir, file)
        with open(file_path, "r") as feedback_file:
            # Read in and strip feedback into a list and append to new list.
            feedback_content = feedback_file.readlines()
            feedback_content = [line.strip() for line in feedback_content]
            # Create dict using feedback content.
            feedback_dict = create_feedback_dict(feedback_content)

            # Send feedback.
            web_address = "https://" + external_ip + "/feedback"
            response = requests.post(web_address, json=feedback_dict)

            # Print status.
            print(response.status_code)
    return


def create_feedback_dict(content):
    feedback_dict = {}

    try:
        feedback_dict["title"] = content[0]
        feedback_dict["name"] = content[1]
        feedback_dict["date"] = content[2]
        feedback_dict["feedback"] = content[3]
    except KeyError:
        print("Feedback not in correct format.")

    return feedback_dict


if __name__ == '__main__':
    # Linux home directory.
    home = os.path.expanduser("~")

    raw_location = home + r"/data/feedback"
    send_feedback(raw_location)
