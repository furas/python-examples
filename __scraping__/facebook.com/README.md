
StackOverflow: [https://stackoverflow.com/a/47539575/1832058](https://stackoverflow.com/a/47539575/1832058)

---

There is few problem with this page

- element is inside <iframe> so you have to find <iframe> and switch_to_frame() before you can search element
- <iframe> is in external <iframe> so first you have to find external <iframe> and switch_to_frame() before you start to searching internal <iframe>
- on small monitor element is invisible so Selenium can click it. You have to scroll page to element and then you can click it.
