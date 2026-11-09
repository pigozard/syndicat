# 07 — RQTH

**URL Jimdo :** `/droit-rqth`  
**Titre de la page :** `RQTH · CGT — CH Charles Perrens`  
**Maquette :** `droit-rqth.html`

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
    <h2>♿ RQTH</h2>
  </div>
</div>
```

---

## Widget 2 — Contenu de la fiche

Jimdo : **+ → Élément HTML** → coller → Enregistrer

```html
<div class="wrap wrap--narrow wrap--pb">
  <div class="fei-block anim">
    <h3>La RQTH : préserver sa santé et éviter l'inaptitude</h3>
    <p><strong>Définition :</strong> la Reconnaissance en Qualité de Travailleur Handicapé est une démarche <strong>personnelle et administrative</strong> réalisée par l'agent auprès de la MDPH (Maison Départementale des Personnes Handicapées) de son département de résidence.</p>
    <p><strong>La RQTH permet de :</strong> bénéficier d'une surveillance médicale particulière ; bénéficier de conditions de travail adaptées (aménagement de l'organisation de travail, achat de matériel adapté...) ; sécuriser son parcours professionnel et l'anticiper en cas d'évolution de son état de santé. La visite médicale auprès du médecin du travail permet de clarifier les besoins spécifiques des agents.</p>
    <p><strong>Comment l'obtenir ?</strong> Complétez le dossier RQTH disponible sur le site de la MDPH du département de votre domicile ; faites compléter par votre médecin traitant ou le spécialiste en charge de votre suivi médical le Cerfa 13788*01 ; transmettez le dossier accompagné des pièces médicales nécessaires à la MDPH.</p>
    <p><strong>Et pour l'employeur ?</strong> Ses devoirs sont de valoriser sa politique handicap et de remplir son obligation d'emploi des travailleurs handicapés. Pour cela, l'employeur bénéficie d'aides auprès du Fonds d'Insertion des personnes Handicapées de la fonction publique pour les aménagements nécessaires à l'agent dans l'exercice de ses missions — car améliorer les aménagements de poste d'un travailleur en situation de handicap permet de travailler sur l'ensemble des conditions de travail de l'équipe.</p>
    <div class="fei-note">Le saviez-vous ? Il n'y a aucune obligation légale pour un agent d'informer son employeur de son état de santé. L'initiative de se déclarer auprès de son employeur revient uniquement à l'agent.</div>
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
