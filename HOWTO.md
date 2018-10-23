# HowTo

## Requirements

You can rebuild the necessary Python environment using `conda`:

`conda env create --file un-py36.txt`

then activate your conda environment:

`conda activate un-py36`

## Crawling the website hosting the UN Treaties

`python get_data.py`


### Download the UN treaties and crawl them offline lightning fast!!!

If this seems too slow...

```shell
cd crawler
wget -r -l 2 --no-clobber --no-parent https://treaties.un.org/Pages/ParticipationStatus.aspx?clang=_en
python get_data.py --files
```


## Start the API locally to interact with the data through HTTP request

This API uses Swagger which makes very intuitive REST API, documented and including data validation.

```shell
cd rest_api
python api.py
```

then simply open the link it will generate: [http://localhost:5000](http://localhost:5000) or better, open the UI [http://localhost:5000](http://localhost:5000/api/ui)
