from datetime import timedelta
from django.contrib.auth.models import User

class MyUserModel(User):
    token_validity_duration = timedelta(days=2)