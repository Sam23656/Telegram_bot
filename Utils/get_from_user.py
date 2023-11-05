def get_chat_id(message):
    return message.chat.id


def get_user_name(message):
    return message.from_user.first_name


def get_user_surname(message):
    return message.from_user.last_name
