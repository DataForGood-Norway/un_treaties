# United Nations Treaties

This package is for crawling and presenting data from the [UN Treaties web site](https://treaties.un.org/).


## Crawling the website hosting the UN Treaties

Use the command

```shell
$ un_crawl
```

This will crawl the UN Treaties web site and cache the files it downloads
locally in a `.un_treaties` directory inside your home directory.

If you need to refresh the cache you can run it with:

`un_crawl --no-cache`


## Run a Rest API locally to interact with the data

To start serving data at [http://localhost:5000](http://localhost:5000), simply do:

```shell
$ un_serve
```

