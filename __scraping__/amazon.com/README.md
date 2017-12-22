Page uses JavaScript to put big image. But `lxml`/`beautifulsoup` can't run JavaScript.

With `lxml`/`beautifulsoup` you can get only small images on left side using xpath `'//div[@id="altImages"]//img/@src'`.

Some urls you can find in one of `<script>` tag.

Code finds `<script>` with `data["colorImages"] =` and data as JSON string which it converts to Python's dictionary - and then it is easy to get urls to images in many different sizes.
