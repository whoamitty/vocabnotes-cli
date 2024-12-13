# 1 11-12-2024 mercredi


- [x] Faire une fonction word_target_exists()
    - finalement word_source_and_target_exists()

- [ ] Refaire update_translation() dans translation.py

on veux vérifier si le mot existe  
si non, on ajoute le mot et la traduction  
si oui, on ajoute la traduction  

Pas de besoin de update_translation() + append_translation() + add_translation()
update_translation() suffit



- [ ] Déplacer le code dans un dépo dédier
- [ ] Gérer le chemin vers la base de donnée
- [ ] faire des tests unitaires pour
    def retrieve_word_info(self, word, file_path):
    def word_source_and_target_exists(self, word, file_path):

- [ ] faire un global .gitignore qui exclus les dossiers __pycache et ...


# 2 13-12-2024 vendredi
J'ai ajouté un README.md à vocabnotes-cli  

# Maby later View word statistics
```
$> trans -stats word
```