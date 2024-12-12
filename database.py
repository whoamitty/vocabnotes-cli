from pathlib import Path
import pandas as pd

class WordDatabase:
    def __init__(self, base_dir=None):
        self.base_dir = Path(base_dir) if base_dir else Path(__file__).parent.parent
        self.ensure_directories()

    def ensure_directories(self):
        """Ensure required directories exist"""
        for lang in ['english', 'french']:
            (self.base_dir / lang).mkdir(parents=True, exist_ok=True)

    def get_increment_file_path(self, lang):
        """Get path to word increment file for given language"""
        return self.base_dir / lang / 'word_increment.csv'

    def increment_word_usage(self, word, lang):
        """Increment or initialize word usage counter"""
        inc_file = self.get_increment_file_path(lang)
        

        if not inc_file.exists():
            inc_file.write_text("word,count\n")
            df = pd.DataFrame(columns=['word', 'count'])
            
        else:
            df = pd.read_csv(inc_file)

        if word in df['word'].values:
            df.loc[df['word'] == word, 'count'] += 1
        else:
            new_row = pd.DataFrame({'word': [word], 'count': [1]})
            df = pd.concat([df, new_row], ignore_index=True)

        df.to_csv(inc_file, index=False)





    def get_translation_file(self, from_lang, to_lang):
        """Get path to translation file"""
        filename = f"{from_lang}_to{to_lang}.csv"
        if from_lang == 'english':
            return self.base_dir / 'english' / 'american-english_tofr.csv'
        else:
            return self.base_dir / 'french' / 'french_toen.csv'
