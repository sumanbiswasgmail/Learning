import getpass


def greet(username):
    return f"Hello, {username}!"


if __name__ == "__main__":
    print(greet(getpass.getuser()))
