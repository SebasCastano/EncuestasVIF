from django.contrib.auth.models import User
user = User.objects.create_user('sistemas', 'castano.sebastian@correounivalle.edu.co', 'sistemasadmin')
user.save()
user1 = User.objects.create_user('prueba', 'prueba@correounivalle.edu.co', 'prueba')
user1.save()
from django.contrib.auth.models import User
user2 = User.objects.create_user('764407', 'dlaraque@gmail.com', 'diana764407')
user2.first_name = 'Diana'
user2.last_name = 'Araque'
user2.save()
user3 = User.objects.create_user('519243', 'nathalia.ledesma@correounivalle.edu.co', 'nathalia519243')
user3.first_name = 'Nathalia'
user3.last_name = 'Ledesma'
user3.save()
