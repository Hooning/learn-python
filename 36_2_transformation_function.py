# Task
# Cleans email addresses and splits them into structured data
# (username and domain).

email_addresses = [
    "test@example.com",
    "user@domain.com",
    "admin@website.org"
]


def clean_and_split_email(email):
    username, domain = email.strip().lower().split("@")

    return {
        "username": username,
        "domain": domain
    }


for email in email_addresses:
    cleaned_email = clean_and_split_email(email)
    print(cleaned_email)
