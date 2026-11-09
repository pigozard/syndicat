# 04 — CGOS

**URL Jimdo :** `/droit-cgos`  
**Titre de la page :** `CGOS · CGT — CH Charles Perrens`  
**Maquette :** `droit-cgos.html`

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
    <h2>🎁 CGOS</h2>
  </div>
</div>
```

---

## Widget 2 — Contenu de la fiche

Jimdo : **+ → Élément HTML** → coller → Enregistrer

```html
<div class="wrap wrap--narrow wrap--pb">
  <div class="fei-block anim">
    <h3>Info CGT CGOS — Ouverture du dossier CGOS 2026</h3>
    <p>De la naissance d'un enfant au décès d'un proche, d'une maladie aux prestations vacances, des aides financières aux prestations scolaires, nous avons tous besoin un jour du CGOS. Contractuels, stagiaires et titulaires, nous sommes tous concernés.</p>
    <p><strong>Direction votre espace agent !</strong> www.cgos.info — Avez-vous créé votre espace agent ? L'avez-vous mis à jour pour 2026 ? Savez-vous quelles sont les nouveautés ? Il est très important de faire votre dossier pour ne pas perdre de temps lorsque vous aurez besoin du CGOS. Sans dossier, pas de prestation !</p>
    <p><strong>Pièces à fournir — vous n'avez pas de dossier :</strong> numéro de sécurité sociale, dernier bulletin de paie, adresse mail.</p>
    <p><strong>Pièces à fournir — vous avez déjà un dossier :</strong> avis d'imposition 2025 sur les revenus 2024, certificat de scolarité pour les enfants à partir du secondaire, quittance de loyer s'ils font des études à l'extérieur ou facture d'internat, attestation CAF si garde alternée.</p>
    <div class="fei-note">Nouveau ! Plus de date limite pour la prestation étude — elle sera versée dès que le dossier sera validé.</div>
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
