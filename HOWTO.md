# HowTo

## Requirements

You can rebuild the necessary Python environment using `conda`:

`conda env create --file un-py36.txt`

then activate your conda environment:

`conda activate un-py36`

## Crawling the website hosting the UN Treaties

`python get_data.py`


## Download the UN treaties and crawl them offline

`wget -r -l 2 --no-clobber --no-parent https://treaties.un.org/Pages/ParticipationStatus.aspx?clang=_en`

`python get_data.py --files`

