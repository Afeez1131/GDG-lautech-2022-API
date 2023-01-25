import random
import string

from django.core.management import BaseCommand

from api.models import Attendees

digit = string.digits

interest = ['Mobile Development', 'Frontend Development', 'Backend Development', 'UI/UX', 'Devops']
# phone = '081%s' % (''.join(random.choice(digit) for _ in range(8)))
names = ['Lolade Olasunkanmi-fasayo', 'Titi', 'Sulaimon', 'Rotimi', 'Aremu', 'Zainab',
         'Chibuike', 'Afolabi Shade', 'Adeoluwa Buchi', 'Ngozi Muyiwa',
         'Justina Titi', 'Omobolanle Titilayo', 'Atanda']
states = ['Kano State',
          'Katsina State',
          'Kebbi State',
          'Kogi State',
          'Kwara State'
          'Lagos State',
          'Ondo State',
          'Osun State',
          'Oyo State'
          ]


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        count = 0
        while count < 50:
            name = random.choice(names)
            email = name.replace(' ', '') + '@gmail.com'
            phone = '081%s' % (''.join(random.choice(digit) for _ in range(8)))
            at = Attendees.objects.create(name=name, interest=random.choice(interest),
                                          phone=phone, email=email, state=random.choice(states))
            print(at.name, at.email, at.phone, at.interest, at.state, 'created successfully.')
            count += 1
        print('-------------DONE----------------')
