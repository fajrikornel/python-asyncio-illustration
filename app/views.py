from . import app, async_helper, util
import time
import requests
import asyncio

calls_to_make = [
    "http://localhost:4567/125/https://images.unsplash.com/photo-1608848461950-0fe51dfc41cb?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8NHx8fGVufDB8fHx8&w=1000&q=80",
    "http://localhost:4567/75/https://images.unsplash.com/photo-1608848461950-0fe51dfc41cb?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8NHx8fGVufDB8fHx8&w=1000&q=80",
    "http://localhost:4567/100/https://images.unsplash.com/photo-1608848461950-0fe51dfc41cb?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8NHx8fGVufDB8fHx8&w=1000&q=80",
    "http://localhost:4567/200/https://images.unsplash.com/photo-1608848461950-0fe51dfc41cb?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8NHx8fGVufDB8fHx8&w=1000&q=80",
    "http://localhost:4567/500/https://images.unsplash.com/photo-1608848461950-0fe51dfc41cb?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8NHx8fGVufDB8fHx8&w=1000&q=80",
]


@app.route("/")
def main():
    return "Hello World!"


@app.route("/sync")
def sync_call():
    start_time = time.perf_counter()
    print(f"STARTING AT: {start_time} s")

    image_list = []
    for i, url in enumerate(calls_to_make):
        print(f"EXECUTING NO. {i+1}: {url}")
        response = requests.get(url)
        image_list.append(response.content)

    util.concatenate_and_save_image("img.png", image_list)

    stop_time = time.perf_counter()
    print(f"STOPPING AT: {stop_time} s")

    duration = stop_time - start_time
    print(f"DONE WITH DURATION: {duration:0.2f} s")

    return {"duration": duration}


@app.route("/async")
def async_call():
    start_time = time.perf_counter()
    print(f"STARTING AT: {start_time} s")

    asyncio.run(async_helper.execute_async_call(calls_to_make))

    stop_time = time.perf_counter()
    print(f"STOPPING AT: {stop_time} s")

    duration = stop_time - start_time
    print(f"DONE WITH DURATION: {duration:0.2f} s")

    return {"duration": duration}
