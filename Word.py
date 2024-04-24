class Word:
    def __init__(self, name = None, level = None, type_word = None):
        self.name = name
        self.level = level
        self.type_word = type_word

    def __str__(self):
        return f"[name: '{self.name}', level: '{self.level}', type: '{self.type_word}']"
    
    def __dict__(self):
        return {
            "name": self.name,
            "level": self.level,
            "type_word": self.type_word
        }
