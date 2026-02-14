# Security Best Practices Implemented

1. DEBUG set to False in production.
2. Enabled SECURE_BROWSER_XSS_FILTER to protect against XSS.
3. Enabled X_FRAME_OPTIONS = 'DENY' to prevent clickjacking.
4. Enabled SECURE_CONTENT_TYPE_NOSNIFF.
5. Enforced HTTPS cookies via CSRF_COOKIE_SECURE and SESSION_COOKIE_SECURE.
6. All forms include {% csrf_token %}.
7. Used Django ORM to prevent SQL injection.
8. Implemented Content Security Policy using django-csp.
