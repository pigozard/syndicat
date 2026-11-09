# 16 — L'équipe

**URL Jimdo :** `/equipe`  
**Titre de la page :** `Qui sommes-nous · CGT — CH Charles Perrens`  
**Maquette :** `equipe.html`

**Fichiers à uploader avant de coller :** `[IMG:equipe-01-valerie]`, `[IMG:equipe-02-marie]`, `[IMG:equipe-03-florent]`, `[IMG:equipe-04-mel]`, `[IMG:equipe-05-loetitia]`, `[IMG:equipe-06-christophe]`, `[IMG:equipe-07-nadege]`, `[IMG:equipe-08-carole]`, `[IMG:equipe-09-nancy]`, `[IMG:equipe-10-marina]`, `[IMG:equipe-11-benjamin]`, `[IMG:equipe-12-judicael]`, `[IMG:equipe-13-titouan]`, `[IMG:equipe-14-thelma]`, `[IMG:logo-cgt-perrens]`

| # | Widget |
|---|---|
| 0 | Navigation |
| 1 | En-tête de page |
| 2 | Histoire et valeurs |
| 3 | Titre « L'équipe » |
| 4 | Le bureau |
| 5 | La Commission exécutive |
| 6 | Bandeau d'aide |

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
      <a href="/droits" data-nav="droits">Vos droits</a>
      <a href="/equipe" data-nav="equipe" class="active">L'équipe</a>
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
    <div class="droits-hero-kicker">La section syndicale</div>
    <h2>Qui sommes-nous</h2>
    <p>Notre histoire, nos valeurs, et l'équipe qui vous représente au quotidien au CH Charles Perrens.</p>
  </div>
</div>
```

---

## Widget 2 — Histoire et valeurs

Jimdo : **+ → Élément HTML** → coller → Enregistrer

```html
<div class="wrap wrap--narrow wrap--pb-sm">
  <div class="fei-block anim">
    <h3>📖 La CGT expliquée, de 1895 à aujourd'hui</h3>
    <p>Congés payés, Sécurité sociale, salaire minimum : rien de tout cela n'est tombé du ciel. Ce sont des conquêtes syndicales. Découvrez 130 ans de luttes, pourquoi il existe plusieurs syndicats, et pourquoi la psychiatrie est un combat syndical.</p>
    <a href="/histoire" class="droit-link">Lire l'histoire de la CGT →</a>
  </div>
  <div class="fei-block anim anim-d1">
    <h3>🤝 Nos valeurs</h3>
    <p>[TEXTE À COMPLÉTER — ce qui distingue l'approche de la section : défense individuelle systématique, priorité donnée aux conditions de travail en psychiatrie, indépendance vis-à-vis de la direction, fonctionnement collectif.]</p>
  </div>
</div>
```

---

## Widget 3 — Titre « L'équipe »

Jimdo : **+ → Élément HTML** → coller → Enregistrer

```html
<div class="droits-hero droits-hero--small">
  <div class="droits-hero-inner"><h2>L'équipe</h2><p>Vos représentants CGT au CH Charles Perrens.</p></div>
</div>
```

---

## Widget 4 — Le bureau

Jimdo : **+ → Élément HTML** → coller → Enregistrer

```html
<div class="wrap">
  <div class="sec-head"><div class="sec-title">Le bureau</div></div>
</div>
<div class="bureau-grid bureau-grid--spaced">
  <div class="bureau-card anim"><div class="bureau-photo"><img src="[IMG:equipe-01-valerie]" alt="Portrait de Valérie" loading="lazy"></div><div class="bureau-info"><h4>Valérie</h4><div class="bureau-role">Secrétaire</div><p>Aide-soignante du pool</p><p class="bureau-meta">À Perrens depuis 1992</p><p class="bureau-meta">Membre du CSE, de la F3SCT, administratrice au CGOS</p></div></div>
  <div class="bureau-card anim anim-d1"><div class="bureau-photo"><img src="[IMG:equipe-02-marie]" alt="Portrait de Marie" loading="lazy"></div><div class="bureau-info"><h4>Marie</h4><div class="bureau-role">Secrétaire adjointe</div><p>Infirmière coordinatrice en ETP à l'UTEP</p><p class="bureau-meta">À Perrens depuis 2017</p><p class="bureau-meta">Membre de la F3SCT, de la Commission exécutive, de l'USD et de la commission de contrôle de la SSTI 33</p></div></div>
  <div class="bureau-card anim anim-d2"><div class="bureau-photo"><img src="[IMG:equipe-03-florent]" alt="Portrait de Florent" loading="lazy"></div><div class="bureau-info"><h4>Florent</h4><div class="bureau-role">Responsable de la politique financière</div><p>Aide-soignant sur C2</p><p class="bureau-meta">À Perrens depuis 16 ans, à la CGT depuis 8 ans</p></div></div>
  <div class="bureau-card anim anim-d3"><div class="bureau-photo"><img src="[IMG:equipe-04-mel]" alt="Portrait de Mel" loading="lazy"></div><div class="bureau-info"><h4>Mel</h4><div class="bureau-role">Adjoint à la politique financière</div><p>Responsable du parc auto/vélo</p><p class="bureau-meta">À Perrens depuis 2015</p></div></div>
</div>
```

---

## Widget 5 — La Commission exécutive

Jimdo : **+ → Élément HTML** → coller → Enregistrer

```html
<div class="wrap">
  <div class="sec-head"><div class="sec-title">La Commission exécutive</div></div>
</div>
<div class="bureau-grid">
  <div class="bureau-card anim"><div class="bureau-photo"><img src="[IMG:equipe-05-loetitia]" alt="Portrait de Loetitia" loading="lazy"></div><div class="bureau-info"><h4>Loetitia</h4><div class="bureau-role">Commission exécutive</div><p>Cadre de santé IDE (Cellule stage &amp; Analyse des pratiques)</p><p class="bureau-meta">À Perrens depuis 1997</p></div></div>
  <div class="bureau-card anim anim-d1"><div class="bureau-photo"><img src="[IMG:equipe-06-christophe]" alt="Portrait de Christophe" loading="lazy"></div><div class="bureau-info"><h4>Christophe</h4><div class="bureau-role">Commission exécutive</div><p>Ouvrier professionnel qualifié (Espaces verts)</p><p class="bureau-meta">À Perrens depuis 1982</p></div></div>
  <div class="bureau-card anim anim-d2"><div class="bureau-photo"><img src="[IMG:equipe-07-nadege]" alt="Portrait de Nadège" loading="lazy"></div><div class="bureau-info"><h4>Nadège</h4><div class="bureau-role">Commission exécutive</div><p>Agent de sécurité au standard</p><p class="bureau-meta">À Perrens depuis 2000</p></div></div>
  <div class="bureau-card anim anim-d3"><div class="bureau-photo"><img src="[IMG:equipe-08-carole]" alt="Portrait de Carole" loading="lazy"></div><div class="bureau-info"><h4>Carole</h4><div class="bureau-role">Commission exécutive</div><p>Infirmière à la DU, coordinatrice JLD</p><p class="bureau-meta">À Perrens depuis 2004</p></div></div>
  <div class="bureau-card anim"><div class="bureau-photo"><img src="[IMG:equipe-09-nancy]" alt="Portrait de Nancy" loading="lazy"></div><div class="bureau-info"><h4>Nancy</h4><div class="bureau-role">Commission exécutive</div><p>Aide-soignante à SUAB (Pôle UNIVA)</p><p class="bureau-meta">À Perrens depuis 2002</p><p class="bureau-meta">Membre de la F3SCT, de l'USD, formatrice syndicale</p></div></div>
  <div class="bureau-card anim anim-d1"><div class="bureau-photo"><img src="[IMG:equipe-10-marina]" alt="Portrait de Marina" loading="lazy"></div><div class="bureau-info"><h4>Marina</h4><div class="bureau-role">Commission exécutive</div><p>Responsable des Services intérieurs (déchets et nuisibles, transformation écologique)</p><p class="bureau-meta">À Perrens depuis 1996</p></div></div>
  <div class="bureau-card anim anim-d2"><div class="bureau-photo"><img src="[IMG:equipe-11-benjamin]" alt="Portrait de Benjamin" loading="lazy"></div><div class="bureau-info"><h4>Benjamin</h4><div class="bureau-role">Commission exécutive</div><p>Régulateur des transports sanitaires</p><p class="bureau-meta">À Perrens depuis 2010</p></div></div>
  <div class="bureau-card anim anim-d3"><div class="bureau-photo"><img src="[IMG:equipe-12-judicael]" alt="Portrait de Judicaël" loading="lazy"></div><div class="bureau-info"><h4>Judicaël</h4><div class="bureau-role">Commission exécutive</div><p>Aide-soignant à la MAS</p><p class="bureau-meta">À Perrens depuis 2011</p></div></div>
  <div class="bureau-card anim"><div class="bureau-photo"><img src="[IMG:equipe-13-titouan]" alt="Portrait de Titouan" loading="lazy"></div><div class="bureau-info"><h4>Titouan</h4><div class="bureau-role">Commission exécutive</div><p>Infirmier au SECOP</p><p class="bureau-meta">À Perrens depuis 2016</p></div></div>
  <div class="bureau-card anim anim-d1"><div class="bureau-photo"><img src="[IMG:equipe-14-thelma]" alt="Portrait de Thelma" loading="lazy"></div><div class="bureau-info"><h4>Thelma</h4><div class="bureau-role">Commission exécutive</div><p>Infirmière à la post-urgence mineurs (PUMA)</p><p class="bureau-meta">À Perrens depuis 2023</p><p class="bureau-meta">Nouvelle recrue de la Commission exécutive</p></div></div>
</div>
```

---

## Widget 6 — Bandeau d'aide

Jimdo : **+ → Élément HTML** → coller → Enregistrer

```html
<div class="cta-band">
  <h3>Si vous avez besoin d'aide, <span>notre porte vous est toujours ouverte</span> !</h3>
  <p>Syndiqué ou non, notre porte vous est toujours ouverte.<br>
  <a href="mailto:cgt@ch-perrens.fr">cgt@ch-perrens.fr</a> · 05.56.56.35.65 · 07.68.03.34.15 · <a href="https://facebook.com/CGT.Perrens" target="_blank" rel="noopener">Facebook.com/CGT.Perrens</a> · <a href="https://instagram.com/cgt.perrens" target="_blank" rel="noopener">@cgt.perrens</a></p>
</div>
```
