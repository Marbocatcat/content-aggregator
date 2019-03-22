from requests_html import HTMLSession

''' Content aggregator using requests_html '''

# Instantiate HTMLSession object
session = HTMLSession()

# Grab links and topics from https://realpython.com


def get_realpython():
    # Start HTMLSession.
    realpython = session.get('https://realpython.com')
    # Link targets that will grab the link and text we need.
    target = 'body > div.container.main-content > div.row > \
    div.col-12.col-md-6.col-lg-4.mb-5 > div.card.border-0 > \
    div.card-body.m-0.p-0.mt-2 > a'

    scraped_object = realpython.html.find(target)

    for index, links in enumerate(scraped_object):
        print(links.absolute_links, links.text)
        if index == 5:
            print('----- Finished ------')
            break


# Grab links and topics from https://inventwithpython.com/blog

def get_inventpython():
    # Start HTML Session.
    inventpython = session.get('https://inventwithpython.com/blog')
    target = '#content > article > h1 > a'

    scraped_object = inventpython.html.find(target)

    for index, links in enumerate(scraped_object):
        print(links.absolute_links, links.text)
        if index == 5:
            print('----- Finished ------')
            break


get_inventpython()
