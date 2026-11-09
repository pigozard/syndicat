# 06 — Autorisations d'absence

**URL Jimdo :** `/droit-absence`  
**Titre de la page :** `Autorisation d'absence spécifique · CGT — CH Charles Perrens`  
**Maquette :** `droit-absence.html`

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
      <div class="logo-mark"><span class="l1">CGT</span><span class="l2">perrens</span></div>
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
    <h2>📅 Autorisation d'absence spécifique</h2>
  </div>
</div>
```

---

## Widget 2 — Contenu de la fiche

Jimdo : **+ → Élément HTML** → coller → Enregistrer

```html
<div class="wrap wrap--narrow wrap--pb">
  <div class="fei-block anim">
    <p>[TEXTE À COMPLÉTER — liste des événements ouvrant droit à autorisation d'absence : événements familiaux (mariage, naissance, décès), examens médicaux, dons du sang, activité syndicale, jury/examens, etc. Préciser les durées et justificatifs à fournir.]</p>
    <div class="fei-note">Un cas particulier n'est pas couvert ici ? Contactez la permanence CGT.</div>
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
