email = input("Input your email: ")


def hide_email(some_email):
    at = some_email.rfind("@")
    hidden_email = some_email[0:2:1] + "*" * len(some_email[2:at:1]) + some_email[at] +\
        "*" * len(some_email[at:at+2:1]) + some_email[at+3:len(some_email):1]
    return hidden_email


print(hide_email(email))
