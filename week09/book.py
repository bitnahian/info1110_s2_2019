class Book:
    def __init__(self, title, author, year, url):
        self.title = title
        self.author = author
        self.year = year
        self.url = url
        self.age = 2019 - int(year)
        self.foo = "foo"
        self.bar = "bar"
        

harry_potter = Book(title="Harry Potter and The Prisoner of Azkaban", # __init__(...)
        author="J.K. Rowling", 
        year="1999", 
        url="https://www.wizardingworld.com/")


lotr = Book(title="The Lord of the Rings",
        author="J. R. R. Tolkien",
        year="1954",
        url="https://en.wikipedia.org/wiki/The_Lord_of_the_Rings")

print(harry_potter.title)
print(lotr.title)


#print(harry_potter.author)

#print(harry_potter.year)

#print(harry_potter.url)

#print(harry_potter.age)


