"""
Codewars 5 kyu kata: PaginationHelper
URL: https://www.codewars.com/kata/515bb423de843ea99400000a/python
"""


class PaginationHelper(object):
    def __init__(self, collection, items_per_page):
        self.collection, self.items_per_page = collection, items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        return self.item_count() / self.items_per_page + 1 if self.item_count() % self.items_per_page else 0

    def page_item_count(self, page_index):
        last_page = self.page_count() - 1

        if 0 <= page_index < last_page:
            return self.items_per_page
        elif page_index == last_page:
            return self.item_count() % self.items_per_page
        else:
            return -1

    def page_index(self, item_index):
        return item_index / self.items_per_page if 0 <= item_index < self.item_count() else -1

