# 02 — Vos droits

**URL Jimdo :** `/droits`  
**Titre de la page :** `Vos droits dans la FPH · CGT — CH Charles Perrens`  
**Maquette :** `droits.html`

| # | Widget |
|---|---|
| 0 | Navigation |
| 1 | En-tête de page |
| 2 | Grille des fiches droits |
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
    <div class="droits-hero-kicker">Ressources syndicales</div>
    <h2>Vos droits dans la FPH</h2>
    <p>Tout ce que vous devez savoir pour défendre votre situation professionnelle à l'hôpital.</p>
  </div>
</div>
```

---

## Widget 2 — Grille des fiches droits

Jimdo : **+ → Élément HTML** → coller → Enregistrer

```html
<div class="droits-grid">
  <div class="droit-card anim"><div class="droit-icon" style="background:#f7e9e6;">🩺</div><h3>Congés maladie</h3><p>CMO : jusqu'à 1 an (3 mois à 90% + 9 mois à demi-traitement). CLM : jusqu'à 3 ans pour pathologies invalidantes (1 an plein traitement + 2 ans à 60%). CLD : jusqu'à 5 ans pour maladies spécifiques (3 ans plein traitement + 2 ans à demi-traitement). Certificat médical à transmettre sous 48h.</p><a href="/droit-conges" class="droit-link">Lire le guide complet →</a></div>
  <div class="droit-card anim anim-d1"><div class="droit-icon" style="background:#e4effe;">🎁</div><h3>CGOS</h3><p>Naissance, décès, maladie, prestations vacances, aides financières, prestations scolaires : contractuels, stagiaires, titulaires, tout le monde est concerné. Créez votre dossier sur www.cgos.info dès votre arrivée — sans dossier, pas de prestation.</p><a href="/droit-cgos" class="droit-link">Direction cgos.info →</a></div>
  <div class="droit-card anim anim-d2"><div class="droit-icon" style="background:#f7e9e6;">🚨</div><h3>Harcèlement</h3><p>Le harcèlement moral est un délit (art. L1152-1) : agissements répétés, dégradation des conditions de travail, atteinte aux droits ou à la santé. Plusieurs démarches possibles — alerter le CSE, l'inspection du travail, saisir les prud'hommes. La CGT écoute, protège, agit à vos côtés.</p><a href="/droit-harcelement" class="droit-link">Agir avec la CGT →</a></div>
  <div class="droit-card anim anim-d3"><div class="droit-icon" style="background:#e6f4e8;">📅</div><h3>Autorisation d'absence spécifique</h3><p>[TEXTE À COMPLÉTER — événements familiaux, syndicaux, examens médicaux : quelles autorisations existent.]</p><a href="/droit-absence" class="droit-link">Voir les cas →</a></div>
  <div class="droit-card anim"><div class="droit-icon" style="background:#f3e8ff;">♿</div><h3>RQTH</h3><p>Surveillance médicale adaptée, aménagements de poste, sécurisation du parcours professionnel. Démarche volontaire auprès de la MDPH de votre département — aucune obligation légale d'en informer votre employeur.</p><a href="/droit-rqth" class="droit-link">Comment l'obtenir →</a></div>
  <div class="droit-card anim anim-d1"><div class="droit-icon" style="background:#fef3e2;">⚖️</div><h3>Droit syndical</h3><p>La CGT vous défend individuellement (sanctions, entretiens disciplinaires, harcèlement), vous représente en CAP, F3SCT, CSE, et vous ouvre l'accès à des formations syndicales — même non syndiqué, vous avez droit à 12 jours de formation par an.</p><a href="/droit-syndical" class="droit-link">Ce que le syndicat fait pour vous →</a></div>
  <div class="droit-card anim anim-d2"><div class="droit-icon" style="background:#e4effe;">💰</div><h3>Grilles de salaires</h3><p>Grilles indiciaires par catégorie (A, B, C), valeur du point d'indice, CTI, primes et indemnités : la Fédération CGT Santé publie chaque année les grilles à jour de la Fonction Publique Hospitalière.</p><a href="/droit-salaires" class="droit-link">Comprendre ma paie →</a></div>
  <div class="droit-card anim anim-d3"><div class="droit-icon" style="background:#fef3e2;">⏱️</div><h3>Temps de travail</h3><p>Durée légale : 35h/semaine, maximum 1607h/an (1476h de nuit). Repos minimum 12h consécutives, 48h max/semaine. En arrêt maladie, un agent ne doit rendre aucune heure et ne génère pas de RTT — le demander est illégal.</p><a href="/droit-travail" class="droit-link">J'ai droit à quoi →</a></div>
  <div class="droit-card anim"><div class="droit-icon" style="background:#fdf1cf;">👵</div><h3>Retraite (CNRACL)</h3><p>Catégorie sédentaire ou active, âge de départ, durée d'assurance, décote/surcote : les agents hospitaliers relèvent de la CNRACL, avec des règles propres à la Fonction Publique Hospitalière. Un simulateur officiel permet d'estimer sa pension.</p><a href="/droit-retraite" class="droit-link">Comprendre ma retraite →</a></div>
  <div class="droit-card anim anim-d1"><div class="droit-icon" style="background:#e4effe;">🏥</div><h3>Mutuelle / Protection sociale complémentaire</h3><p>La réforme de la protection sociale complémentaire (PSC) dans la Fonction Publique Hospitalière change la participation de l'employeur au financement de votre complémentaire santé. Un sujet d'actualité 2026-2027 à suivre de près.</p><a href="/droit-mutuelle" class="droit-link">Ce qui change →</a></div>
  <div class="droit-card anim anim-d2"><div class="droit-icon" style="background:#f7e9e6;">✊</div><h3>Droit de grève</h3><p>Préavis, service minimum, assignation vs réquisition, retenue sur salaire : un droit constitutionnel encadré dans la Fonction Publique Hospitalière compte tenu de la continuité du service public.</p><a href="/droit-greve" class="droit-link">Ce qu'il faut savoir →</a></div>
  <div class="droit-card anim anim-d3"><div class="droit-icon" style="background:#e6f4e8;">📋</div><h3>Événements indésirables</h3><p>Pourquoi et comment signaler un événement indésirable, lié aux soins ou non — une démarche qui protège autant les patients que l'équipe.</p><a href="/droit-fei" class="droit-link">Comment déclarer →</a></div>
  <div class="droit-card anim"><div class="droit-icon" style="background:#f3e8ff;">🗳️</div><h3>Élections professionnelles</h3><p>Le vote au CH Charles Perrens se tient du 3 au 10 décembre 2026. Ce qu'il détermine (CSE, CAP), le calendrier du cycle électoral, et pourquoi voter CGT.</p><a href="/droit-elections" class="droit-link">Tout savoir →</a></div>
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
