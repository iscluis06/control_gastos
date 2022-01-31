from django.core.management import BaseCommand
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class Command(BaseCommand):
    """ Clase de prueba para generacion de comandos, django-rest-framework, ya tiene
    un metodo especifico para crear tokens """
    help = 'Create user token'

    def add_arguments(self, parser):
        parser.add_argument('user', nargs=1, type=str)

    def handle(self, *args, **options):
        try:
            user_name = options['user']
            user = User.objects.get(username=user_name[0])
            user_has_token = Token.objects.filter(user=user)
            if len(user_has_token) == 0:
                token = Token.objects.create(user=user)
                self.stdout.write("Token: {}".format(token.key))
                return
            self.stdout.write("User has already a token")
        except Exception as err:
            self.stdout.write("Error: {}".format(err))