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


# Development

## Building the Rest API from Swagger

The `un_treaties/rest_api` directory has been automatically created from the `swagger.yaml` file. This should be rebuilt if the swagger-file is changed.

1. Download the swagger-codegen-cli: https://github.com/swagger-api/swagger-codegen/#prerequisites

2. Generate the rest-api:

    ```shell
    $ java -jar swagger-codegen-cli.jar generate -l python-flask -i swagger.yaml -c swagger_config.json -o swagger_build
    ```

     Unfortunately, there seems to be some bug in swagger-codegen-cli (or config
     setting we have not figured out) that causes some code to be put into
     `un_treaties.rest_api` instead of `un_treaties/rest_api`. Also, the command
     generates some files like `setup.py` that we don't want in our
     project. Because of this we save everything in a temporary folder,
     `swagger_build`

3. Move files from `swagger_build` into `un_treaties`. Essentially all files
   inside of `swagger_build/un_treaties/rest_api` and
   `swagger_build/un_treaties.rest_api` should be moved to
   `un_treaties/rest_api`. The files in `swagger_build` outside these
   directories should not be moved.

4. Delete the temporary directory `swagger_build`.
