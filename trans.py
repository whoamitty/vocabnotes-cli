#!/usr/bin/env python3
import click
from database import WordDatabase
from translation import TranslationManager

@click.command()
@click.argument('direction')
@click.argument('word')
@click.argument('translations', nargs=-1)
def trans(direction, word, translations):
    """
    Add translation to the database.
    
    DIRECTION: Translation direction (enfr or fren)
    WORD: Word to translate
    TRANSLATIONS: One or more translations for the word
    """
    if not translations:
        click.echo("Erreur: Au moins une traduction est requise")
        return

    if direction == 'enfr':
        from_lang = 'english'
        to_lang = 'french'
    elif direction == 'fren':
        from_lang = 'french'
        to_lang = 'english'
    else:
        click.echo("Erreur: Direction invalide. Utilisez 'enfr' ou 'fren'")
        return

    db = WordDatabase()
    tm = TranslationManager(db)
    
    result = tm.add_translation(word, translations, from_lang, to_lang)
    
    if result == "added":
        click.echo(f"Traduction ajoutée pour '{word}'")
    elif result == "updated":
        click.echo(f"Traduction mise à jour pour '{word}'")
    elif result.startswith("appended_"):
        added_count = int(result.split("_")[1])
        click.echo(f"{added_count} nouvelle(s) traduction(s) ajoutée(s) pour '{word}'")
    else:
        click.echo(f"Le mot '{word}' existe déjà avec des traductions dans la base de données")

if __name__ == '__main__':
    trans()
