import pprint
from . import *


class SearchResults(dict):

    """ This is a wrapper that provides easy
        access to common parameters of the
        very complex search results dictionary

        Takes one argument:

        dict: a dictionary of search results

    """

    items = []
    total_results = 0
    search_terms = ''

    def __init__(self, dict={}):
        super(SearchResults, self).__init__(dict)

        self.total_results = int(
            self.get('searchInformation', {}).get('totalResults', 0))

        self.search_terms = self.get('queries', {}).get(
            'request', [])[0].get('searchTerms', '')

        self.items = self.get('items', [])
