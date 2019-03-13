from django.contrib.auth import get_user_model


class CustomAuthBackend():

    def authenticate(self, email=None, password=None, **kwargs):
        user_model = get_user_model()
        if email is None:
            email = kwargs.get(user_model.USERNAME_FIELD)
        try:
            user = user_model._default_manager.get(email=email)
            if user.check_password(password):
                return user
        except user_model.DoesNotExist:
            user_model().set_password(password)

    def get_user(self, user_id):
        user_model = get_user_model()
        try:
            return user_model._default_manager.get(pk=user_id)
        except user_model.DoesNotExist:
            return None
