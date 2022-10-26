import json

def vraag_to_json(vraag):
    vraag_json = {
        "vraag_id": vraag.get_vraag_id(),
        "vraag": vraag.get_vraag(),
        "onderwerpen": vraag.get_onderwerpen(),
        "aantal_correct": vraag.get_aantal_correct(),
        "aantal": vraag.get_aantal(),
        "description": vraag.get_description(),
        "quiz_id": vraag.get_quiz_id()
    }

    vraag_klaar = json.dumps(vraag_json)
    return vraag_klaar