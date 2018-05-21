from django.views.generic import TemplateView
from django.shortcuts import render
#from apiclient.discovery import build
from googleapiclient.discovery import build
from .utils import SearchResults
from . import *


class SearchView(TemplateView):
    template_name = "googlesearch/result.html"

    def get_context_data(self, **kwargs):

        context = super(SearchView, self).get_context_data(**kwargs)

        service = build("customsearch", GOOGLE_SEARCH_API_VERSION,
                        developerKey=GOOGLE_SEARCH_API_KEY)

        # add a "try" block to see if googleapiclient throws a 400 error
        try:
            results = service.cse().list(
                q=self.request.GET.get('q', ''),
                start=self.page_to_index(),
                num=GOOGLE_SEARCH_RESULTS_PER_PAGE,
                cx=GOOGLE_SEARCH_ENGINE_ID,
            ).execute()

            results = SearchResults(results)
            pages = self.calculate_pages()

        # if googleapiclient raises an error, we need to catch it here
        except:

            # run the search again starting with a defined page 1 instead of the "user" defined
            results = service.cse().list(
                q=self.request.GET.get('q', ''),
                start=1,
                num=GOOGLE_SEARCH_RESULTS_PER_PAGE,
                cx=GOOGLE_SEARCH_ENGINE_ID,
            ).execute()

            # set some default values used for the context below
            page = 1

            # previous, current, next pages
            pages = [0, 1, 2]

            results = SearchResults(results)

        """ Set some defaults """
        context.update({
            'items': [],
            'total_results': 0,
            'current_page': 0,
            'prev_page': 0,
            'next_page': 0,
            'search_terms': self.request.GET.get('q', ''),
            'error': results
        })

        """ Now parse the results and send back some
            useful data """

        context.update({
            'items': results.items,
            'total_results': results.total_results,
            'current_page': pages[1],
            'prev_page': pages[0],
            'next_page': pages[2],
            'search_terms': results.search_terms,
        })

        return context

    def calculate_pages(self):
        """ Returns a tuple consisting of
            the previous page, the current page,
            and the next page """

        current_page = int(self.request.GET.get('p', 1))
        return (current_page - 1, current_page, current_page + 1)

    def page_to_index(self, page=None):
        """ Converts a page to the start index """

        if page is None:
            page = self.request.GET.get('p', 1)

        return int(page) * int(GOOGLE_SEARCH_RESULTS_PER_PAGE) + 1 - int(GOOGLE_SEARCH_RESULTS_PER_PAGE)


def index(request):
    return render(request, 'googlesearch/index.html')
