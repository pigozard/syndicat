# 08 — Droit syndical

**URL Jimdo :** `/droit-syndical`  
**Titre de la page :** `Droit syndical — ce que la CGT fait pour vous · CGT — CH Charles Perrens`  
**Maquette :** `droit-syndical.html`

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
    <h2>⚖️ Droit syndical — ce que la CGT fait pour vous</h2>
  </div>
</div>
```

---

## Widget 2 — Contenu de la fiche

Jimdo : **+ → Élément HTML** → coller → Enregistrer

```html
<div class="wrap wrap--narrow wrap--pb">
  <div class="fei-block anim">
    <p><strong>Vous défendre individuellement :</strong> accompagnement en cas de sanction, d'entretien disciplinaire, de refus de mobilité, d'arrêt de travail contesté ; aide à la rédaction de courriers officiels, recours, demandes administratives ; soutien en cas de harcèlement moral ou sexuel, de souffrance au travail ou de mal-être.</p>
    <p><strong>Vous informer sur vos droits :</strong> explications claires sur vos droits statutaires, votre fiche de paie, vos congés, votre carrière et votre rémunération ; suivi des évolutions réglementaires ; réunions d'information syndicale ; mise en lien avec des avocats lors des permanences juridiques du mercredi.</p>
    <p><strong>Agir collectivement :</strong> mobilisation contre les injustices locales, négociation collective sur les conditions de travail, les horaires, les primes, action commune contre des décisions injustes ou arbitraires.</p>
    <p><strong>Vous représenter dans les instances :</strong> CAP (Commission Administrative Paritaire), F3SCT (Formation Spécialisée Santé, Sécurité et Conditions de Travail), CSE (Comité Social d'Établissement) — pour porter votre voix face à l'administration.</p>
    <div class="fei-note">Même sans être syndiqué, vous avez droit à 12 jours de formation syndicale par an pour vous outiller et vous rendre plus fort face à l'institution.</div>
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
