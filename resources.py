from tabulate import tabulate


def resources():

    print("Resources Used")
    documentation_articles()
    APIs_used()


def documentation_articles():

    print(f"\nDocumentation and Articles")
    headings = ["Source", "Title"]
    data = [['Free Code Camp', 'Python Requests – How to Interact with Web Services using Python',],
            ['Free NBA API', 'How to Use The Free NBA API with Python, PHP, Ruby and JavaScript'],
            ['Geeks for Geeks', 'Python | ASCII art using pyfiglet module'],
            ['InquirerPy', 'Read the docs'],
            ['PyPI','Requests, Tabulate'],
            ['W3Schools', 'Python Requests Module'],
            ['ZeroMQ', 'Get started']]

    print(tabulate((item for item in data), headings, tablefmt="heavy_grid"))
    print(f"\n")


def APIs_used():

    print(f"\nAPIs")
    headings = ["API", "link"]
    data = [['API-BASKETBALL', 'https://rapidapi.com/api-sports/api/api-basketball'],
            ['Free NBA', 'https://rapidapi.com/theapiguy/api/free-nba'],
            [f"Ball Don't Lie", 'https://app.balldontlie.io/']]

    print(tabulate((item for item in data), headings, tablefmt="heavy_grid"))
    print(f"\n")
