from domain.vraag import Vraag

class DragDropVraag(Vraag):

    def __init__(self,vraag,onderwerpen,description,quiz_id,antwoorden,choices,image=None):
        Vraag.__init__(self,vraag,onderwerpen,description,quiz_id)
        self.set_antwoorden(antwoorden)
        self.set_choices(choices)
        self.set_image(image)

    def get_antwoorden(self):
        return self.antwoorden

    def set_antwoorden(self,antwoorden):
        if type(antwoorden)== list:
            self.antwoorden = antwoorden
        else:
            raise Exception(f'antwoorden has the wrong type must be list but is {type(antwoorden)}')

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
        string += f'Antwoorden: {self.get_antwoorden()}\n'
        string += f'Choices: {self.get_choices()}\n'
        string += f'Image pad: {self.get_image() if not self.get_image()==None else "Geen image meegegeven"}'
        return string
