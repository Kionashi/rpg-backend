from rest_framework_simplejwt.tokens import RefreshToken

class AuthenticationService():
    # Generate JWT token
    def generate_token(self, user):
        refresh = RefreshToken.for_user(user)
        token = str(refresh.access_token)
        return token  or 'TOKEN NO GENERATED'

