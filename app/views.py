from . import app
import time
import requests

calls_to_make = [
    "http://localhost:4567/125/https://google.com",
    "http://localhost:4567/75/https://google.com",
    "http://localhost:4567/100/https://google.com",
    "http://localhost:4567/200/https://google.com",
    "http://localhost:4567/500/https://google.com",
]


@app.route("/")
def main():
    return "Hello World!"


@app.route("/sync")
def sync_call():
    start_time = time.perf_counter()
    print(f"STARTING AT: {start_time} s")

    for i, url in enumerate(calls_to_make):
        print(f"EXECUTING NO. {i+1}: {url}")
        requests.get(url)

    stop_time = time.perf_counter()
    print(f"STOPPING AT: {stop_time} s")

    duration = stop_time - start_time
    print(f"DONE WITH DURATION: {duration:0.2f} s")

    return {"duration": duration}
