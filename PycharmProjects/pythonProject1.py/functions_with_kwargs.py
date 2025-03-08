def greeting(**kwargs):
    """
    This Function is to send message
    :param kwargs:
    :return:
    """
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")


# Calling the function
greeting(message="My name is Benedine Okeke", Age= "I am 35 years old", Country="I am from Nigeria.")




def special_greeting(message, *names):
    """
    This Function is to send message to different persons
    :param message:
    :param names:
    :return:
    """
