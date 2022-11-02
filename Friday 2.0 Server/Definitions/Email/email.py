import sendgrid
import os
from sendgrid.helpers.mail import *
from sendgrid import SendGridAPIClient


sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('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'))
from_email = Email("aran0713@hotmail.com")
to_email = To("aran0713@hotmail.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)


