from apps.fw.models.user_model import FwUser


def check_and_get_user(username, password):
    if not username or not password:
        return False

    if "@" in username:
        user_finded = FwUser.objects.filter(email=username).first()

        if user_finded:
            return user_finded.dni
        else:
            return False
    elif type(username) is int:
        return username
    else:
        return False
