# UN Treaties REST API

## How to run the API

### Installation

* `pip install flask connexion`

### Start the API

* `python api.py`

Then open the local site: [http://localhost:5000/api/ui](http://localhost:5000/api/ui)

## What are the ... things ...  of the API?

* treaties
* chapters
* countries (~participants or should this be 2 different things?)

## What questions on theses treaties and countries can we formulate with a REST API?

### Classic expected questions, centered on a country

* What treaties did it signed?
* What treaties not signed?
* What treaties did it ratified?
* What treaties not ratified?
* What treaties were signed but not ratified?

### Classic expected questions, centered on a treaty

* which countries signed it?
* which countries ratified it?
* which countries signed it but didn't ratify it?

### Classic expected questions, centered on a chapter

* What treaties belong to this chapter?
* ...

### Funny/Painful questions

* **How this country compares to their "ancestral friendly or less friendly rivals"?** (USA/Canada, USA/Russia, Norway/Sweden, Israel/Palestine, France/UK, UK/Ireland, France/Germany, North Korea/South Korea, Iran/Saudi Arabia, Turkey/Greece, China/Japan, India/Pakistan, ...)
    NB. maybe no that funny with the risk of polarizing nations around a critical subject.
* Can we provide a **human-readable summary** of a treaty?
* What treaties this country is among the very few (<5%) **NOT** having signed/ratified it? 
