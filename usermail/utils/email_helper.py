from post_office import mail

def send_mail_using_post_office(from_user, to_user, subject, message):
	to_user = [to_user]
	mail.send(
	    to_user, # List of email addresses also accepted
	    'rishabhstpl@gmail.com',
	    subject='My email',
	    message='Hi there!',
	    html_message='Hi <strong>there</strong>!',
	    priority='now',
	)