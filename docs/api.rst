.. module:: pwned_passwords_django.api

.. _api:

Using the Pwned Passwords API directly
======================================

If the validator and middleware do not cover your needs, you can also directly
check a password against Pwned Passwords. The following two functions handle
this use case, depending on whether you are writing synchronous or asynchronous
Python:

.. autofunction:: check_password

.. function:: check_password_async(password: str) -> int
   :async:

   Check a password against the Pwned Passwords API and return the count of
   times it appears in breaches in the Pwned Passwords database.

   This is an asynchronous version of :meth:`check_password`, and will use an
   asynchronous HTTP client to make the request to Pwned Passwords.

   :raises TypeError: When the given password value is not a string.

   :raises exceptions.PwnedPasswordsError: When the Pwned Passwords API times out,
      returns an HTTP 4XX or 5XX status code, or when any other error occurs in
      contacting the Pwned Passwords API or checking the password.


Using the client class
----------------------

If you want even finer-grained control over interaction with Pwned Passwords,
there is also a client class -- which is what :func:`check_password` and
:func:`check_password_async` and all other public API of pwned-passwords-django
passes through to -- provided:

.. autoclass:: PwnedPasswords

   You also can subclass and override the following attributes:

   .. attribute:: api_endpoint

      A :class:`str` indicating the API endpoint to request when talking to
      Pwned Passwords. Defaults to the Pwned Passwords v3 API endpoint:
      ``"https://api.pwnedpasswords.com/range/"``.

   .. attribute:: user_agent

      A :class:`str` containing the value to send in the HTTP ``User-Agent``
      header. Defaults to a string listing the versions of
      pwned-passwords-django, Python, and ``httpx``.

   Also, in a subclass you can override the constructor to control how the
   following values are set:

   .. attribute:: add_padding

      A :class:`bool` indicating whether or not to include the optional
      ``Add-Padding`` header to the request, causing Pwned Passwords to add
      `random padding to the size of the response body
      <https://haveibeenpwned.com/API/v3#PwnedPasswordsPadding>`_, as an
      additional security measure. The default value is the value of
      ``settings.PWNED_PASSWORDS["ADD_PADDING"]``, or ``True`` if that setting
      is not provided. See :ref:`the settings documentation <settings>`.

   .. attribute:: request_timeout

      A :class:`float` setting a timeout, in seconds, for communicating with
      Pwned Passwords. The default value is the value of
      ``settings.PWNED_PASSWORDS["API_TIMEOUT"]``, or ``1.0`` (1 second) if
      that setting is not provided. See :ref:`the settings documentation
      <settings>`.
