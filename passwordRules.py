class Rules:

    def __init__(self, username, password):
        """
        Construct the rules for the password
        :param password: the password
        """
        self.username = username
        self.password = password

    def result(self):
        """
        Return if the password follows the following rules:
        1. The password must have length of 12 or greater
        2. The password must not be equal to the username
        3. The password should not have "password" (common sense one)
        4. The password must have a lowercase letter
        5. The password must have an uppercase letter
        6. The password must have a digit
        :return: true if the password follows all the rules
        """
        return self.no_password() and self.username != self.password \
               and self.length() and self.lower() and self.upper() and self.digit()

    def no_password(self):
        """
        Do not have any "password" (capitalized or lowercase)
        :return:
        """
        return "password" not in self.password.lower()

    def length(self):
        """
        Return boolean value depending on the length of the password
        :return: true if password is equal to greater than 12; otherwise, false
        """
        return len(self.password) >= 12

    def lower(self):
        """
        Return boolean value
        :return: true if password have a lowercase letter
        """
        return any(c.islower() for c in self.password)

    def upper(self):
        """
        Return boolean value
        :return: true if password have a uppercase letter
        """
        return any(c.isupper() for c in self.password)

    def digit(self):
        """
        Return a boolean value whether
        :return: true if the password have a digit; otherwise, false
        """
        return any(c.isdigit() for c in self.password)

def main():
    username = input("Enter the username")
    password = input("Enter the password")
    rule = Rules(username, password)
    print(rule.result())


if __name__ == "__main__":
    main()


