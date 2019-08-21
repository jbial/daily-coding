"""
This problem was asked by Microsoft.

Implement a URL shortener with the following methods:

shorten(url), which shortens the url into a six-character alphanumeric string,
such as zLg6wl.

restore(short), which expands the shortened string into the original url.
If no such shortened string exists, return null.

Hint: What if we enter the same URL twice?

Solution:

"""
import string

class Shortener:

    def __init__(self, short_len=6):
        # character alphabet for shortened IDs
        self.alpha = string.ascii_letters + "0123456789"
        self.alpha_map = {char: i for i, char in enumerate(self.alpha)}

        self.alpha_size = len(self.alpha)
        self.url_map = dict()

        # init the ids so that the shortened urls are 6 characters long
        self.id_counter = self.alpha_size ** (short_len - 1) 

        # max amount of ids allowed in database (62 ^ short_len)
        self.max_ids = self.alpha_size ** short_len

    def _id_to_url(self):
        return {self.url_map[k]: k for k in self.url_map}

    def _add_url(self, url):
        if self.id_counter < self.max_ids:
            self.url_map[url] = self.id_counter
            self.id_counter += 1
        else:
            raise ValueError("URL database size exceeded")

    def shorten(self, url):
        if url not in self.url_map:
            self._add_url(url)

        # get the url id from the url database
        url_id = self.url_map[url]
        short_url = ""

        while url_id:
            short_url += self.alpha[url_id % self.alpha_size]
            url_id //= self.alpha_size
        return short_url[::-1]

    def restore(self, short):
        id_map = self._id_to_url()

        url_id = 0
        for i in short:
            url_id = url_id * self.alpha_size + self.alpha_map[i]
        return id_map[url_id]


def main():

    s = Shortener()

    test_urls = [
        "https://explained.ai/matrix-calculus/index.html",
        "https://www.youtube.com/watch?v=MrSN6gdGilo",
        "https://www.youtube.com/watch?v=ChtumoDfZXI",
        "https://arxiv.org/pdf/1705.03122.pdf"
    ]

    short_urls = [s.shorten(url) for url in test_urls]

    if all(url == s.restore(short) for url, short in zip(test_urls, short_urls)):
        print("Passed")
    else:
        print("Failed")


if __name__ == '__main__':
    main()


        



