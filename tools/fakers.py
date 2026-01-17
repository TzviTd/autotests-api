from faker import Faker

class Fake:
    """Random data generation class"""
    def __init__(self, faker: Faker):
        """
        :param faker: Creates a class Faker unit
        """
        self.faker = faker

    def text(self) -> str:
        """
        Generate random text function
        :return: Random text string
        """
        return self.faker.text()

    def uuid4(self) -> str:
        """
        Generate random uuid4 function
        :return: Random uuid4
        """
        return self.faker.uuid4()

    def email(self, domain: str | None = None) -> str:
        """
        Generate random email function
        :param domain: email domain (@domainname.com), if not indicated generated automatically
        :return: Random email
        """
        return self.faker.email(domain=domain)

    def sentence(self) -> str:
        """
        Generates random sentence function
        :return: Random sentence
        """
        return self.faker.sentence()

    def password(self) -> str:
        """
        Generates random password
        :return: Random password
        """
        return self.faker.password()

    def last_name(self) -> str:
        """
        Generates random last name
        :return: Random last name
        """
        return self.faker.last_name()

    def first_name(self) -> str:
        """
        Generates random first name
        :return: Random first name
        """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """
        Generates random middle name
        :return: Random first name that plays the role of a middle name
        """
        return self.faker.first_name()

    def integer(self, start: int = 1, end: int = 100):
        """
        Auxiliar function that generates random number in the given range, including start/end numbers
        :param start: minimal value
        :param end: maximal value
        :return: random number within the given range (default range 1 - 100)
        """
        return self.faker.random_int(start,end)

    def estimated_time(self) -> str:
        """
        Generates estimatedTime value string
        :return: estimatedTime value (e.g. "3 weeks")
        """
        return f"{self.integer(1,10)} weeks"

    def max_score(self) -> int:
        """
        Generates random maximal score value
        :return: Random maxScore
        """
        return self.integer(50, 100)

    def min_score(self) -> int:
        """
        Generates random minimal score value
        :return: Random minScore
        """
        return self.integer(1, 30)

fake = Fake(faker=Faker()) # Creating a variable containing a class Faker unit