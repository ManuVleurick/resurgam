from domain.vraag import Vraag

class MultipleChoiceVraag(Vraag):

    def __init__(self,vraag,onderwerpen,description,quiz_id,antwoord,choices,image=None):
        Vraag.__init__(self,vraag,onderwerpen,description,quiz_id)
        self.set_antwoord(antwoord)
        self.set_choices(choices)
        self.set_image(image)

    def get_antwoord(self):
        return self.antwoord

    def set_antwoord(self,antwoord):
        if type(antwoord)== str:
            self.antwoord = antwoord
        else:
            raise Exception(f'Antwoord has the wrong type must be str but is {type(antwoord)}')

    def set_choices(self,choices):
        if type(choices) == list:
            self.choices = choices
        else:
            raise Exception(f'Choices has the wrong type must be list but is {type(choices)}')

    def get_choices(self):
        return self.choices

    #optioneel
    def set_image(self,image):
        if (image==None) or (type(image) == str):
            self.image = image
        else:
            raise Exception(f'Image has the wrong type must be None or str but is {type(image)}')

    def get_image(self):
        return self.image

    def to_string(self):
        string = 'Multiple choice vraag\n'
        string += f'{super().to_string()}\n'
        string += f'Antwoord: {self.get_antwoord()}\n'
        string += f'Choices: {self.get_choices()}\n'
        string += f'Image pad: {self.get_image() if not self.get_image()==None else "Geen image meegegeven"}'
        return string
