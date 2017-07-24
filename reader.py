import subprocess

class Reader:
    def __init__(self):
        self.language = 'pl'
        self.voice = 'm7'

    def set_language(self, lang):
        self.language = lang

    def get_language(self):
        return self.language
    
    def read(self, message):
        command = 'espeak -v {language} "{message}"'.format(
            language=self.language,
            voice = self.voice,
            message = message)
        subprocess.Popen(command, shell=True)
        return True

