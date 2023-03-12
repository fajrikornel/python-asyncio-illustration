# Python Asyncio Illustration

## Setup

- Make sure virtualenv is available on your PC.
- Create the virtual environment:

```
virtualenv venv
```

- Run `./venv/bin/activate` every time this project is used.
- Install dependencies:

```
pip3 install -r requirements.txt
```

### Optional setup

If you want to use the delay proxy to simulate network delays (as explained below), you need:
- Docker
- Docker Compose

## How to use the app

This app illustrates how asyncio can help boost performance in APIs. This is a simple app that concatenates a list of images into one image vertically.

There are two APIs, `/sync` and `/async`, which as the name suggests:
- `/sync` downloads those image synchronously in a sequential manner
- `/async` downloads the image asynchronously using asyncio.

To run the app, edit the `image_list.txt` file provided with the line-separated list of images online that you want to be concatenated as one image.

Then run the following command:

```
python3 main.py
```

Call the APIs:

```
curl localhost:5000/sync
curl localhost:5000/async
```

You can then observe the difference in delay yourself or inspect the logs for it. The image will be stored on the project root as `img.png`.

### Simulating network delays

Optionally, we can use the Deelay proxy submodule to simulate network delays. To do so, run:

```
docker-compose up -d
```

It will run the Deelay proxy on `localhost:4567`. Then on the `image_list.txt` we can prefix urls we want to simulate a delay for with `http://localhost:4567/{delay_in_ms}/`.

## Credits

Credit to Grzegorz Biesiadecki for his Deelay proxy which is used in this illustration. Link to [GitHub repo here](https://github.com/biesiad/deelay).
