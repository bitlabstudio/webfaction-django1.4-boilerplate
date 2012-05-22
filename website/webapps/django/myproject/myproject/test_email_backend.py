"""Custom email backend for testing the projet."""
from django.conf import settings
from django.core.mail.backends.smtp import EmailBackend as SmtpEmailBackend
from django.core.mail.message import sanitize_address


class EmailBackend(SmtpEmailBackend):
    """
    Email backend that sends all emails to a defined address, no matter what
    the recepient really is.

    In order to use it, set this in your local_settings.py::

        TEST_EMAIL_BACKEND_RECEPIENTS = (
            ('Name', 'email@gmail.com'),
        )

    """
    def _send(self, email_message):
        """A helper method that does the actual sending."""
        if not email_message.recipients():
            return False
        from_email = sanitize_address(email_message.from_email, email_message.encoding)
        recipients = [sanitize_address(addr, email_message.encoding)
                      for name, addr in settings.TEST_EMAIL_BACKEND_RECEPIENTS]
        try:
            self.connection.sendmail(from_email, recipients,
                    email_message.message().as_string())
        except:
            if not self.fail_silently:
                raise
            return False
        return True
