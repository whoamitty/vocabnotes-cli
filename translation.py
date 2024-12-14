from pathlib import Path
from typing import Optional
from dataclasses import dataclass

@dataclass
class WordInfo:
    """Class to store information about a word in the translation file"""
    exists: bool = False
    line_number: Optional[int] = None
    line_content: Optional[list] = None


class TranslationManager:
    def __init__(self, word_db):
        self.db = word_db


        
    def retrieve_word_info(self, word, file_path):
        """Check if word exists in translation file and return info if found"""        
        
        if not file_path.exists():
            return WordInfo()
        
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for index, line in enumerate(lines):
                parts = [p.strip() for p in line.split(',')]
                if parts and parts[0] == word:
                    return WordInfo(exists=True, line_number=index, line_content=parts)
        return WordInfo()  #À corriger, ou vérifier les cohérences

    def word_source_and_target_exists(self, word, file_path):
        word_info=self.retrieve_word_info(word, file_path)
        if not word_info.exists:
            return False

        elif  word not in  word_info.line_content:
            return False

        else:
            return True
        



# UPDATE

    def update_translation(self, word, translations, file_path):
        """Update translation for a word if it exists without translation"""
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        for i, line in enumerate(lines):
            parts = [p.strip() for p in line.split(',')]
            if parts and parts[0] == word:
                lines[i] = f"{word}, {', '.join(translations)}\n"
                break
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)


    def append_translation(self, word, translations, file_path):
        """Append new translations to existing word"""

        

        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        added_count = 0
        for i, line in enumerate(lines):


            parts = [p.strip() for p in line.split(',')]
            if parts and parts[0] == word:
                existing_translations = set(p.strip() for p in parts[1:] if p.strip())
                new_translations = set(translations)
                unique_new = new_translations - existing_translations
                if unique_new:
                    all_translations = existing_translations.union(new_translations)
                    lines[i] = f"{word}, {', '.join(all_translations)}\n"
                    added_count = len(unique_new)
                break #À corriger c'est l'ajout de traduction foireuse qui change mon ordre
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        return added_count


        
    def add_translation(self, word, translations, from_lang, to_lang):
        """Add or update translation for a word"""
        trans_file = self.db.get_translation_file(from_lang, to_lang)
        exists, info = self.retrieve_word_info(word, trans_file)

        if not exists:
            with open(trans_file, 'a', encoding='utf-8') as f:
                f.write(f"{word}, {', '.join(translations)}\n")
            self.db.increment_word_usage(word, from_lang)
            return "added"
        elif info is not None and len(info) > 2 and info[2]:
            self.update_translation(word, translations, trans_file)
            return "updated"
        else:
            added_count = self.append_translation(word, translations, trans_file)
            return f"appended_{added_count}"



#À corriger