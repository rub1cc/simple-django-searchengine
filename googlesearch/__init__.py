from django.conf import settings


""" Your GSE API key """
GOOGLE_SEARCH_API_KEY = getattr(settings, 'GOOGLE_SEARCH_API_KEY', None)

""" The ID of the Google Custom Search Engine """
GOOGLE_SEARCH_ENGINE_ID = getattr(settings, 'GOOGLE_SEARCH_ENGINE_ID', None)

""" The API version. Defaults to 'v1' """
GOOGLE_SEARCH_API_VERSION = getattr(
    settings, 'GOOGLE_SEARCH_API_VERSION', 'v1')

""" The number of search results to show per page """
GOOGLE_SEARCH_RESULTS_PER_PAGE = getattr(
    settings, 'GOOGLE_SEARCH_RESULTS_PER_PAGE', 10)

""" The maximum number of pages to display """
GOOGLE_SEARCH_MAX_PAGES = getattr(settings, 'GOOGLE_SEARCH_MAX_PAGES', 10)
