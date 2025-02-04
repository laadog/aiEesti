from docx import Document
import os
from LanguageModel import LanguageModel

class Section:
    def __init__(self, filename: str, content: str):
        self.filename = filename
        self.content = content

class Database:
    def __init__(self, data_folder: str, language_model: LanguageModel):
        self.sections = list()
        self.folder = data_folder
        self.language_model = language_model
        self.files = self._get_files()
        self.sections = list()
        self.__populate_database()

    def _get_files(self):
        return [os.path.join(self.folder, f) for f in os.listdir(self.folder) if f.endswith(".docx")]

    def __populate_database(self):
        for file in self.files:
            self.__parseFile__(file)

    def __parseFile__(self, file: str):
        doc = Document(file)
        filename = os.path.basename(file)
        for paragraph in doc.paragraphs:
            self.sections.append(Section(filename, paragraph.text))

    def update(self, input):
        doc = Document(input)
        updates = list()

        for paragraph in doc.paragraphs:
            current_update = None

            original = paragraph.text
            current = (original, input)

            if original == "":
                continue

            for possible_replacement in self.sections:
                if self.language_model.determine_change(os.path.basename(input), original, current[0], current[1], possible_replacement.filename, possible_replacement.content):
                    paragraph.text = possible_replacement.content
                    current = (possible_replacement.content)
                    current_update = f"Changed section '{original.splitlines()[0]}' to '{possible_replacement.content.splitlines()[0]}' from {possible_replacement.filename}"
            updates.append(current_update)

        doc.save(f"UPDATED_{os.path.basename(input)}")

        with open(f"changelog_{os.path.basename(input)}.txt", "w") as changelog:
            changelog.write("\n".join(updates))

