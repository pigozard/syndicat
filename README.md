# CGT — CH Charles Perrens · maquette

Maquette statique du site de la section CGT, publiée sur **GitHub Pages**, puis migrée sur **Jimdo Creator** par copier-coller.

## Organisation des fichiers

```
├── index.html, droits.html, droit-*.html,   Une page .html = une page Jimdo
│   equipe.html, communiques.html,
│   contact.html, adherer.html
│
├── css/site.css        LE fichier de styles. Identique sur GitHub Pages et sur Jimdo
│                       (à coller entier dans Jimdo : Design → Personnaliser → CSS)
│
├── partials/           Widgets présents sur toutes les pages
│   ├── nav.html        En-tête + menu (+ son petit script menu mobile)
│   └── bandeau-aide.html
│
├── outils/build.py     Recopie les partials dans les pages + régénère jimdo/
├── jimdo/              GÉNÉRÉ — fichiers prêts à coller (ne pas modifier à la main)
└── images/
```

## Les widgets

Dans chaque page, le contenu est découpé en blocs autonomes :

```html
<!-- ===== WIDGET : Fiches droits ===== -->
  … HTML du bloc …
<!-- ===== FIN WIDGET ===== -->
```

Un bloc = un **Élément HTML** dans Jimdo. Chaque bloc ne dépend que de `css/site.css` : pas de script externe ni de `onclick`. Si un bloc a besoin de JavaScript, son `<script>` se trouve à l'intérieur du bloc.

Pour ajouter un communiqué : copier un bloc `WIDGET : Communiqué — …` existant dans `communiques.html`, puis le modifier.

## Règles pour garder la migration facile

- **Pas de `style="…"`** dans le HTML : mettre une classe et l'ajouter à `css/site.css`, dans la bonne section.
- **Liens entre pages** au format `page.html` ou `page.html#ancre` : le script les convertit en URLs Jimdo.
- **Images** dans `images/` : le script les remplace par des repères `[IMG:nom]` à remplacer par l'URL de la Médiathèque Jimdo.
- **Menu et bandeau du bas** : modifier uniquement `partials/`, puis lancer le script.

## Après chaque modification

```bash
python3 outils/build.py
```

Puis vérifier en local (`python3 -m http.server`, puis ouvrir http://localhost:8000) et pousser sur `main`.
