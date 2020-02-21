class Game:

    def __init__(self, name = ""):
        self.name = name
        self.link = ""
        self.dev = ""
        self.publisher = ""
        self.dates = dict()
        self.trailer_link = ""

    def __str__(self):
        return (
            "Name: " + self.name + "\n" + 
            "Link: " + self.link + "\n" + 
            "Dev: " + self.dev +"\n" + 
            "Publisher: " + self.publisher + "\n" + 
            "Dates: " + str(self.dates) + "\n"
            "Tailer link: " + self.trailer_link + "\n"
        )
