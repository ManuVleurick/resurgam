from domain.vraag import Vraag

class InputVraag(Vraag):

    def __init__(self,vraag,onderwerpen,description,quiz_id,antwoord,image=None):
        Vraag.__init__(self,vraag,onderwerpen,description,quiz_id)
        self.set_antwoord(antwoord)
        self.set_image(image)

    def get_antwoord(self):
        return self.antwoord

    def set_antwoord(self,antwoord):
        if type(antwoord)== str:
            self.antwoord = antwoord
        else:
            raise Exception(f'Antwoord has the wrong type must be str but is {type(antwoord)}')

    #optioneel
    def set_image(self,image):
        if (image==None) or (type(image) == str):
            self.image = image
        else:
            raise Exception(f'Image has the wrong type must be None or str but is {type(image)}')

    def get_image(self):
        return self.image

    def to_string(self):
        string = 'Input vraag'
        string += f'{super().to_string()}\n'
        string += f'Antwoord: {self.get_antwoord()}\n'
        string += f'Image pad: {self.get_image() if not self.get_image()==None else "Geen image meegegeven"}'
        return string
