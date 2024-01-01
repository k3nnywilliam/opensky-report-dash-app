import multiprocessing
import os

# Gunicorn configuration

# Address and port on which Gunicorn will listen
bind = '127.0.0.1:8050'

# Number of workers (adjust based on your server's CPU cores)
workers = multiprocessing.cpu_count() * 2 + 1

# Worker class for handling requests
worker_class = 'gevent'

# Define log files for Gunicorn access and error logs
accesslog = '/outputs/access.log'
errorlog = '/outputs/error.log'


# Timeout for handling requests
timeout = 30

# Maximum requests a worker will process before restarting
max_requests = 1000

# Log level
loglevel = 'info'

# Define handling of static files (CSS, JS, images)
# Adjust the path based on your Dash app's directory structure
def on_starting(server):
    server.log.info("Starting Gunicorn server...")
    os.chdir('/app/app')  # Change directory to where your app is located
    server.log.info("Changed directory to app folder.")
    
# Define function to handle preloading application code
def on_reload(server):
    server.log.info("Reloading Gunicorn server...")

# Define post-worker-initialization function
def post_worker_init(worker):
    worker.log.info("Worker spawned (pid: %s)", worker.pid)
    
# Define post-worker-exit function
def post_worker_exit(worker, exit_code):
    worker.log.info("Worker exited (pid: %s)", worker.pid)

def worker_abort(worker):
    worker.log.error("Worker aborted (pid: %s)", worker.pid)
    # Perform actions for handling worker abortion
