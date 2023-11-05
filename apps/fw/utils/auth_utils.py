from apps.fw.models.user_model import FwUser


def get_property_user_by_email(email, property):
    user = FwUser.objects.filter(email=email).first()

    if user:
        return getattr(user, property)
    else:
        return False


def check_and_get_user(username, password):
    if not username or not password:
        return False

    if "@" in username:
        return get_property_user_by_email(username, "dni")

    elif username.isdigit():
        return username

    else:
        return False
