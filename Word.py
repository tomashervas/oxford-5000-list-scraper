class Word:
    def __init__(self, name = None, level = None, type_word = None, traduction = None, example = None, example_traduction = None):
        self.name = name
        self.level = level
        self.type_word = type_word
        self.traduction = traduction
        self.example = example
        self.example_traduction = example_traduction

    def __str__(self):
        return f"[name: '{self.name}', level: '{self.level}', type: '{self.type_word}', traduction: '{self.traduction}', example: '{self.example}', example_traduction: '{self.example_traduction}']"
    
    def __dict__(self):
        return {
            "name": self.name,
            "level": self.level,
            "type_word": self.type_word,
            "traduction": self.traduction,
            "example": self.example,
            "example_traduction": self.example_traduction
        }
