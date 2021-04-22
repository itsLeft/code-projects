"""
Josh S
Email Gathering
Create a script that asks the user for five email addresses and collects the domain names.

Input
Prompt the user five times to enter an email address. 
If the address does not include a "@" before a ".", it is not valid and does not count toward the five addresses.

Output
After each valid email, print just the domain name portion of the address without the extension. 
For example, "myname@gmail.com" should output as "gmail".

Once all five emails have been entered, all valid domain names should be printed again in one line, separated by spaces.
"""


def isvalidemail(email):
    if '@' in email:
        check = email[email.find("@"):]
        return '@' in check and '.' in check and len(check) != 2
    else:
        return False


def emaildomain(email):
    domain = email[email.find("@")+1:]
    return domain[:domain.find(".")]


domains = []
numEmails = 0
while numEmails != 5:
    email = input("Enter an email address: ")
    if isvalidemail(email):
        domains.append(emaildomain(email))
        numEmails += 1
    else:
        print("Please enter a valid email")
print()
for i in range(len(domains)):
    print(f"Domain {i+1}: {domains[i]}")

