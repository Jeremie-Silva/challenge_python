"""Challenge 04
Given a long string (text) `S`.
Find and extract all substring starts with `http://` or `https://`.
The substring should have no whitespace.
Optionally, you can validate the URL by checking if they are in `FQDN (Full Name Qualified Domain)` form.

## Remarks
Finding valid URL in text is useful for scraping. When processing a paragraph,
there should be many valuable information for recon.
Valid URLs are not only found on a page. It can also be found on assets such as JavaScript file.
"""

import re


text: str = "https://www.google.com/https://github.com/https://pypi.org/http://docs.python.org/fr/3/library/unittest.html"
# google github pypi python


def search_url_in_text(text: str) -> list[str]:
    return re.sub("http", " http", text).split()


urls_list = search_url_in_text(text)

print(urls_list)
