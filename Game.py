class Game:    

    def __init__(self, name = None):
        self.name = ""
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
            "publisher: " + self.publisher + "\n" + 
            "dates: " + str(self.dates) + "\n"
            "tailer link: " + self.trailer_link + "\n"
        )