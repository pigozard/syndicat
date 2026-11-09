# Migration Jimdo Creator

Les fichiers `NN-*.md` de ce dossier sont **générés** par `python3 outils/build.py`. Ne pas les modifier à la main : corriger la maquette, puis relancer le script.

## Ordre

1. **Images** : uploader dans *Médiathèque* les fichiers listés en tête de chaque `.md` (« Fichiers à uploader »), puis remplacer chaque `[IMG:nom]` par l'URL Jimdo (Cmd+Maj+H dans VS Code sur le dossier `jimdo/`).
2. **CSS** : *Design → Personnaliser → CSS* → tout remplacer par le contenu de `css/site.css`.
3. **Pages** : pour chaque fichier `NN-*.md`, créer la page avec l'URL indiquée, supprimer les éléments par défaut, puis ajouter les widgets dans l'ordre (**+ → Élément HTML** → coller → Enregistrer).
4. **Accueil en dernier.**

## Si l'URL d'une page Jimdo ne correspond pas

Modifier la colonne `jimdo` de la liste `PAGES` dans `outils/build.py`, puis relancer le script : tous les liens sont mis à jour.
