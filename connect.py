import json
from mongoengine import *

class Author(Document):
    fullname = StringField(required=True)
    date_born = StringField(required=True)
    born_location = StringField(required=True)
    bio = StringField(required=True)


class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField(required=True)

def connect_mongodb():
    connect('hw9', host='mongodb+srv://userweb10:567234@cluster0.h9yiutj.mongodb.net/?retryWrites=true&w=majority')

    with open('authors.json') as f:
        authors = json.load(f)

    with open('quotes.json') as f:
        quotes = json.load(f)

    for author in authors:
        Author(**author).save()

    for quote in quotes:
        author_fullname = quote['author']
        author = Author.objects(fullname=author_fullname).first()

        if author:
            quote['author'] = author
            Quote(**quote).save()
        else:
            print(f"Author '{author_fullname}' not found in the database. Quote not saved.")


if __name__ == '__main__':
    connect_mongodb()


