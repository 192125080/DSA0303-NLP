import re

def find_dates(text):
    pattern = r'\d{2}/\d{2}/\d{4}'
    dates = re.findall(pattern, text)
    return dates

def find_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    emails = re.findall(pattern, text, re.IGNORECASE)
    return emails

def main():
    sample_text = """
    John Doe was born on 25/12/1985. His email is john.doe@example.com.
    Jane Doe's birthday is on 03/09/1990. You can reach her at jane_doe@gmail.com.
    """

    print("Dates found:")
    dates = find_dates(sample_text)
    for date in dates:
        print(date)

    print("\nEmails found:")
    emails = find_emails(sample_text)
    for email in emails:
        print(email)

if __name__ == "__main__":
    main()
