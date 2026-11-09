# 13 — Droit de grève

**URL Jimdo :** `/droit-greve`  
**Titre de la page :** `Droit de grève · CGT — CH Charles Perrens`  
**Maquette :** `droit-greve.html`

**Fichiers à uploader avant de coller :** `[IMG:logo-cgt-perrens]`

| # | Widget |
|---|---|
| 0 | Navigation |
| 1 | En-tête de page |
| 2 | Contenu de la fiche |
| 3 | Bandeau d'aide |

---

## Widget 0 — Navigation

Jimdo : **+ → Élément HTML** → coller → Enregistrer

```html
<header class="site-header">
  <div class="header-inner">
    <a class="logo" href="/">
      <img class="logo-img" src="[IMG:logo-cgt-perrens]" alt="Logo CGT Charles Perrens">
      <div class="logo-text"><h1>CGT — CH Charles Perrens</h1><p>Section syndicale · Fonction Publique Hospitalière</p></div>
    </a>
    <nav id="main-nav">
      <a href="/" data-nav="accueil">La CGT</a>
      <a href="/droits" data-nav="droits" class="active">Vos droits</a>
      <a href="/equipe" data-nav="equipe">L'équipe</a>
      <a href="/communiques" data-nav="communiques">Communiqués</a>
      <a href="/contact" data-nav="contact">Contact</a>
      <a href="/contact" class="nav-cta-mobile">Permanence</a>
      <a href="/adherer" class="nav-cta-mobile">Adhérer →</a>
    </nav>
    <div class="header-cta">
      <a href="/contact" class="btn btn-ghost">Permanence</a>
      <a href="/adherer" class="btn btn-red">Adhérer →</a>
    </div>
    <button class="nav-toggle" type="button" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="main-nav">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>
<script>
/* Menu mobile : ouvre / ferme la liste des liens */
(function () {
  var nav = document.getElementById('main-nav');
  var btn = document.querySelector('.nav-toggle');
  if (!nav || !btn) return;
  btn.addEventListener('click', function () {
    var open = nav.classList.toggle('mobile-open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
})();
</script>
```

---

## Widget 1 — En-tête de page

Jimdo : **+ → Élément HTML** → coller → Enregistrer

```html
<div class="droits-hero">
  <div class="droits-hero-inner">
    <a href="/droits" class="back-link">← Retour à Vos droits</a>
    <h2>✊ Droit de grève</h2>
  </div>
</div>
```

---

## Widget 2 — Contenu de la fiche

Jimdo : **+ → Élément HTML** → coller → Enregistrer

```html
<div class="wrap wrap--narrow wrap--pb">
  <div class="fei-block anim">
    <p>Le droit de grève est reconnu par le préambule de la Constitution de 1946. Dans la Fonction Publique Hospitalière, il s'exerce dans un cadre spécifique compte tenu de la continuité du service public — la grève y est un droit, pas une faute, mais elle obéit à des règles de procédure précises.</p>
    <p><strong>Le préavis :</strong> un préavis de grève doit être déposé par une organisation syndicale représentative au moins 5 jours francs avant le déclenchement du mouvement. Il précise les motifs, le lieu, la date, l'heure de début et la durée envisagée. Aucun agent ne peut se mettre en grève avant l'expiration de ce délai. Des négociations doivent s'engager pendant le préavis entre l'autorité administrative et les organisations syndicales — c'est une obligation, pas une option.</p>
    <p><strong>Service minimum, assignation et réquisition :</strong> un service minimum doit être assuré pour garantir la sécurité des patients et la continuité des soins essentiels. Pour l'assurer, la direction peut <em>assigner</em> nommément certains agents à leur poste par décision écrite et individuelle motivée — un agent assigné n'est plus en grève pour les heures concernées et doit travailler ; en cas de désaccord sur la légalité d'une assignation, contactez immédiatement la CGT. La <em>réquisition</em>, plus exceptionnelle, relève d'une décision préfectorale (et non de l'employeur) en cas de menace grave pour l'ordre public ou la santé de la population.</p>
    <p><strong>Retenue sur salaire :</strong> une journée de grève entraîne en principe une retenue correspondant à 1/30e du traitement mensuel (règle du « trentième indivisible »), quelle que soit sa durée dans la journée. Elle doit apparaître clairement sur le bulletin de paie du mois concerné.</p>
    <div class="fei-note">Se déclarer gréviste n'a pas à être justifié : vous n'avez pas à motiver votre participation à un mouvement de grève auprès de votre hiérarchie. Un doute sur une assignation ou une retenue de salaire ? Contactez la permanence CGT.</div>
  </div>
</div>
```

---

## Widget 3 — Bandeau d'aide

Jimdo : **+ → Élément HTML** → coller → Enregistrer

```html
<div class="cta-band">
  <h3>Si vous avez besoin d'aide, <span>notre porte vous est toujours ouverte</span> !</h3>
  <p>Syndiqué ou non, notre porte vous est toujours ouverte.<br>
  <a href="mailto:cgt@ch-perrens.fr">cgt@ch-perrens.fr</a> · 05.56.56.35.65 · 07.68.03.34.15 · <a href="https://facebook.com/CGT.Perrens" target="_blank" rel="noopener">Facebook.com/CGT.Perrens</a> · <a href="https://instagram.com/cgt.perrens" target="_blank" rel="noopener">@cgt.perrens</a></p>
</div>
```
