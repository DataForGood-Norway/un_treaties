# HowTo

## Requirements

It's nice to run inside an environment. If you use conda you can for instance do:

```shell
$ conda create -n un_treaties python
$ conda activate un_treaties
```

## Installation

Install the package:

```
$ python -m pip install -e .
```

Using `-e` installs the package in editable mode, which is nice for development.


## Crawling the website hosting the UN Treaties

Use the command

```shell
$ un_crawl
```

This will crawl the UN Treaties web site and cache the files it downloads
locally in a `un_treaties` directory inside your home directory.

If you need to refresh the cache you can run it with:

`un_crawl --no-cache`


## Start the API locally to interact with the data through HTTP request

This API uses Swagger which makes very intuitive REST API, documented and including data validation.

```shell
$ un_serve
```

then simply open the link it will generate: [http://localhost:5000](http://localhost:5000) or better, open the UI [http://localhost:5000](http://localhost:5000/api/ui)
