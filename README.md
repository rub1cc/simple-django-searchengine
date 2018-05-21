# simple-django-searchengine
a simple django search engine built using [django-googlesearch](https://github.com/praekelt/django-googlesearch) app and Google Custom Search Engine

### Preview ###
<p align="center">
<img src="https://raw.githubusercontent.com/farazaulia/simple-django-searchengine/master/tkcbise.gif" alt="demo" />
</p>

# Getting Started
### Initial Setup ###
1. Make a virtualenv ``virtualenv -p python3 env && cd env``
2. Activate the virtualenv ``source bin/activate``
3. Clone this repository ``git clone https://github.com/farazaulia/simple-django-searchengine.git && cd simple-django-searchengine``
4. Install dependecies ``pip install -r requirements.txt``
5. Rename ``tkcbise/example-settings.py`` into ``settings.py``
6. Add your API_KEY and CUSTOM_SEARCH_ID in ``tkcbise/settings.py``
```
GOOGLE_SEARCH_API_KEY = 'YOUR_GOOGLE_API_KEY'
GOOGLE_SEARCH_ENGINE_ID = 'YOU_CUSTOM_SEARCH_ID'
GOOGLE_SEARCH_API_VERSION = 'v1'
GOOGLE_SEARCH_RESULTS_PER_PAGE = 10
GOOGLE_SEARCH_MAX_PAGES = 10
```
5. Run the server ``python manage.py runserver``
6. Open website in browser at ``http://localhost:8000``
