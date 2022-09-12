from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class MoviePagination(PageNumberPagination):
    page_size = 7
    page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 10
    last_page_strings = 'end'

class MovieLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 6