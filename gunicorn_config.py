bind = "0.0.0.0:8000"
module = "correkaminos.wsgi:application"

workers = 4  
worker_connections = 1000
threads = 4

certfile = "/etc/letsencrypt/live/correkaminos.com/fullchain.pem"
keyfile = "/etc/letsencrypt/live/correkaminos.com/privkey.pem"