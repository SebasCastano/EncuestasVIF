from django.contrib.auth.models import User
user = User.objects.create_user('sistemas', 'castano.sebastian@correounivalle.edu.co', 'sistemasadmin')
user.save()