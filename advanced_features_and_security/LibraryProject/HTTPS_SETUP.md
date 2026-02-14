# HTTPS Deployment Configuration

To enable HTTPS in production:

1. Obtain an SSL/TLS certificate (e.g., Let's Encrypt).
2. Configure web server (Nginx or Apache) to use SSL.

Example Nginx configuration:

server {
    listen 443 ssl;
    server_name example.com;

    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}

Redirect HTTP to HTTPS:

server {
    listen 80;
    server_name example.com;
    return 301 https://$host$request_uri;
}
