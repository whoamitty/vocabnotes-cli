# 1 11-12-2024 mercredi


- [x] Faire une fonction word_target_exists()
    - finalement word_source_and_target_exists()



# 2 13-12-2024 vendredi
- [x] Déplacer le code dans un dépo dédier
- [x] J'ai ajouté un README.md à vocabnotes-cli  
- [x] faire un global .gitignore qui exclus les dossiers __pycache__/ et ...


# later

- [o] Gérer le chemin vers la base de donnée
    - [x] from dotenv import load_dotenv
    - [ ] Il manque le test pour être sûr que  c'est bon



- [ ] Refaire update_translation() dans translation.py

on veux vérifier si le mot existe  
si non, on ajoute le mot et la traduction  
si oui, on ajoute la traduction  

Pas de besoin de update_translation() + append_translation() + add_translation()
update_translation() suffit



- [ ] faire des tests unitaires pour
    def retrieve_word_info(self, word, file_path):
    def word_source_and_target_exists(self, word, file_path):

- [ ] stocker le fichier reflexion autre par


# Maby later View word statistics
```
$> trans -stats word
```