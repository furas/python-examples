

`children` (similar to `'list_iterator'`) means many items so you get list not single item. It can be even list with one item or empty list but it is still a list. You have to use for loop to use get() with every item on the list or use index [0] to get only first item (if list is not empty)

But in `BeautifulSoup` it gives all elements inside, not only tags (class `Tag`) but also text between tags (class `NavigableString`) which don't have `.get()` method.

This code

    from bs4 import BeautifulSoup

    html = '''
    <ul class="mainview">
        <li>
            <input value="ABCD" class="origianl">
        </li>
    </ul>
    '''

    soup = BeautifulSoup(html, 'html.parser')

    mainview = soup.find(class_="mainview")

    for child in mainview.children:
        print(type(child))

gives

    <class 'bs4.element.NavigableString'>
    <class 'bs4.element.Tag'>
    <class 'bs4.element.NavigableString'>

Better use next `find()` to find single element or `find_all()` to get list of elements.

    from bs4 import BeautifulSoup

    html = '''
    <ul class="mainview">
        <li>
            <input value="ABCD" class="origianl">
        </li>
    </ul>
    '''

    soup = BeautifulSoup(html, 'html.parser')

    mainview = soup.find(class_="mainview")

    child = mainview.find(class_="origianl")

    print(child.get('value'))

---

`children` gives only first level of subitems (`<li>`), but not children in those subitems (`<input>`) so you would have to use inner `for` loop to get `<input>` which is in `<li>`.

    from bs4 import BeautifulSoup
    import bs4

    html = '''
    <ul class="mainview">
        <li>
            <input value="ABCD" class="origianl">
        </li>
    </ul>
    '''

    soup = BeautifulSoup(html, 'html.parser')

    mainview = soup.find(class_="mainview")

    print('--- children ---')
    for child in mainview.children:
        print('>    tag:', child.name)
        print('>   type:', type(child))
        #print('>content:', child)
        if isinstance(child, bs4.element.Tag):
            print('>  value:', child.get('value'))
            print('          --- subchildren ---')
            for subchild in child.children:
                print('          >    tag:', subchild.name)
                print('          >   type:', type(subchild))
                #print('          >content:', subchild)
                if isinstance(subchild, bs4.element.Tag):
                    print('          >  value:', subchild.get('value'))
                print('          -----------')

        print('-----------')

Result:

    --- children ---
    >    tag: None
    >   type: <class 'bs4.element.NavigableString'>
    -----------
    >    tag: li
    >   type: <class 'bs4.element.Tag'>
    >  value: None
              --- subchildren ---
              >    tag: None
              >   type: <class 'bs4.element.NavigableString'>
              -----------
              >    tag: input
              >   type: <class 'bs4.element.Tag'>
              >  value: ABCD
              -----------
              >    tag: None
              >   type: <class 'bs4.element.NavigableString'>
              -----------
    -----------
    >    tag: None
    >   type: <class 'bs4.element.NavigableString'>
    -----------
