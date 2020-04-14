from post_office import mail


def send_mail_using_post_office(to_user, subject, message, from_user='syskart@yandex.com'):
    to_user = [to_user]
    mail.send(
        to_user,  # List of email addresses also accepted
        from_user,
        subject=subject,
        message=message,
        html_message='Hi <strong>there</strong>!',
        priority='now',
    )