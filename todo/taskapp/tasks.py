# Django
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Models
from todo.users.models import User

# Celery
from celery.decorators import task


@task(name='send_confirmation_email', max_retries=3)
def send_confirmation_email(user_pk, password):
    """Manda el email de confirmacion y el token"""
    user = User.objects.get(pk=user_pk)
    subject = 'Bienvenido @{}, ya estas listo para usar ToDoChallenge!'.format(user.username)
    from_email = 'ToDoChallenge <noreply@todochallenge.com>'
    content = render_to_string(
        'emails/users/welcome_user.html',
        {'user': user, 'password': password}
    )
    msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
    msg.attach_alternative(content, "text/html")
    msg.send()
