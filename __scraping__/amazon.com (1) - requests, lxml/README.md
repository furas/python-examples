
Date: 2017.12.22

Link: (stackoverflow) [not able to find or print link form amazon using xpath but I am able to do with beautifulsoup](https://stackoverflow.com/a/47935432/1832058)

---

Page uses JavaScript to put big image. But `lxml`/`beautifulsoup` can't run JavaScript.

With `lxml`/`beautifulsoup` you can get only small images on left side using xpath `'//div[@id="altImages"]//img/@src'`.

Some urls you can find in one of `<script>` tag.

Code finds `<script>` with `data["colorImages"] =` and data as JSON string which it converts to Python's dictionary - and then it is easy to get urls to images in many different sizes.
# date: 2017.12.22
# https://stackoverflow.com/a/47935432/1832058
# date: 2017.12.22
# https://stackoverflow.com/a/47935432/1832058
