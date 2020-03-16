import multiprocessing

bind = "0.0.0.0:8080"
worker_class = "gevent"
workers = multiprocessing.cpu_count() * 2 + 1