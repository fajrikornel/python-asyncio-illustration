from . import app, async_helper, util, image_urls
import time
import requests
import asyncio


@app.route("/")
def main():
    return "Hello World!"


@app.route("/sync")
def sync_call():
    start_time = time.perf_counter()
    app.logger.info(f"STARTING AT: {start_time} s")

    image_list = []
    for i, url in enumerate(image_urls):
        app.logger.info(f"EXECUTING NO. {i+1}: {url}")
        response = requests.get(url)
        image_list.append(response.content)

    util.concatenate_and_save_image("img.png", image_list)

    stop_time = time.perf_counter()
    app.logger.info(f"STOPPING AT: {stop_time} s")

    duration = stop_time - start_time
    app.logger.info(f"DONE WITH DURATION: {duration:0.2f} s")

    return {"duration": duration}


@app.route("/async")
def async_call():
    start_time = time.perf_counter()
    app.logger.info(f"STARTING AT: {start_time} s")

    asyncio.run(async_helper.execute_async_call(image_urls))

    stop_time = time.perf_counter()
    app.logger.info(f"STOPPING AT: {stop_time} s")

    duration = stop_time - start_time
    app.logger.info(f"DONE WITH DURATION: {duration:0.2f} s")

    return {"duration": duration}
