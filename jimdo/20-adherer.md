# 20 — Adhérer

**URL Jimdo :** `/adherer`  
**Titre de la page :** `Adhérer à la CGT · CGT — CH Charles Perrens`  
**Maquette :** `adherer.html`

**Fichiers à uploader avant de coller :** `[IMG:logo-cgt-perrens]`

| # | Widget |
|---|---|
| 0 | Navigation |
| 1 | En-tête de page |
| 2 | Formulaire d'adhésion |
| 3 | Barème des cotisations |
| 4 | Bandeau d'aide |

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
  <div class="droits-hero-inner"><h2>Adhérer à la CGT</h2><p>Rejoignez vos collègues qui font confiance à la CGT CH Charles Perrens.</p></div>
</div>
```

---

## Widget 2 — Formulaire d'adhésion

Jimdo : **+ → Élément HTML** → coller → Enregistrer

```html
<div class="wrap wrap--form wrap--pb">
  <form class="s-card adh-form anim" id="adh-form">
    <div class="adh-title">Bulletin d'adhésion 2026</div>
    <p class="adh-intro">Remplissez ce bulletin : il prépare un email à envoyer au syndicat. <strong>Pensez à joindre votre RIB</strong> pour le prélèvement automatique de vos cotisations.</p>

    <fieldset>
      <legend>Vous</legend>
      <div class="form-grid">
        <label>Nom<input name="Nom" required class="maj" autocomplete="family-name"></label>
        <label>Prénom<input name="Prénom" required class="maj" autocomplete="given-name"></label>
        <label>Date de naissance<input name="Date de naissance" type="date"></label>
        <label class="full">Adresse personnelle<input name="Adresse" class="maj" autocomplete="street-address"></label>
        <label>Code postal<input name="Code postal" inputmode="numeric" autocomplete="postal-code"></label>
        <label>Ville<input name="Ville" class="maj" autocomplete="address-level2"></label>
        <label>Téléphone professionnel<input name="Tél. professionnel" type="tel"></label>
        <label>Téléphone personnel<input name="Tél. personnel" type="tel"></label>
        <label>Portable<input name="Portable" type="tel" autocomplete="tel"></label>
        <label>Email<input name="Email" type="email" required autocomplete="email"></label>
      </div>
      <div class="choice-row"><span>Envoi des documents syndicaux :</span>
        <label><input type="radio" name="Envoi des documents" value="Domicile" checked> Domicile</label>
        <label><input type="radio" name="Envoi des documents" value="Service"> Service</label>
      </div>
    </fieldset>

    <fieldset>
      <legend>Votre poste</legend>
      <div class="form-grid">
        <label>Métier<input name="Métier" class="maj"></label>
        <label>Lieu d'exercice à Charles Perrens<input name="Lieu d'exercice" class="maj"></label>
      </div>
      <div class="choice-row"><span>Catégorie :</span>
        <label><input type="radio" name="Catégorie" value="A"> A</label>
        <label><input type="radio" name="Catégorie" value="B"> B</label>
        <label><input type="radio" name="Catégorie" value="C"> C</label>
      </div>
    </fieldset>

    <fieldset>
      <legend>Indications sur votre fiche de paie</legend>
      <div class="form-grid">
        <label>Indice<input name="Indice" id="adh-indice" type="number" min="1" inputmode="numeric" required></label>
        <label>Grade<input name="Grade" class="maj"></label>
      </div>
      <div class="choice-row"><span>Statut :</span>
        <label><input type="radio" name="Statut" value="CDD"> CDD</label>
        <label><input type="radio" name="Statut" value="CDI"> CDI</label>
        <label><input type="radio" name="Statut" value="Titulaire"> Titulaire</label>
      </div>
      <div class="cotis-result" id="adh-cotis" aria-live="polite">Saisissez votre indice : le montant de votre cotisation s'affiche ici.</div>
      <p class="adh-note">Nous avons besoin de ces renseignements pour utiliser le logiciel de trésorerie de la CGT.</p>
    </fieldset>

    <button type="submit" class="join-btn">Préparer l'email d'adhésion →</button>
    <p class="adh-note">Le bouton ouvre votre messagerie avec un email prêt à l'envoi à <strong>syndicat.cgt@ch-perrens.fr</strong>. Ajoutez votre RIB en pièce jointe, puis envoyez. Si rien ne s'ouvre, écrivez directement à cette adresse ou passez au local CGT.</p>
  </form>
</div>
<script>
/* Bulletin d'adhésion : calcul de la cotisation + préparation de l'email */
(function () {
  var DEST = 'syndicat.cgt@ch-perrens.fr';
  /* Barème 2026 : [indice minimum, cotisation mensuelle en €] */
  var BAREME = [[520, 12.5], [500, 12], [480, 11.5], [460, 11], [440, 10.5], [420, 10], [400, 9.5], [380, 9], [0, 8.5]];
  var form = document.getElementById('adh-form');
  var indice = document.getElementById('adh-indice');
  var out = document.getElementById('adh-cotis');
  if (!form) return;

  function euros(n) { return n.toLocaleString('fr-FR', { minimumFractionDigits: n % 1 ? 2 : 0 }) + ' €'; }
  function cotisation(i) {
    for (var k = 0; k < BAREME.length; k++) if (i >= BAREME[k][0]) return BAREME[k][1];
  }
  function maj() {
    var i = parseInt(indice.value, 10);
    if (!i) { out.textContent = "Saisissez votre indice : le montant de votre cotisation s'affiche ici."; return null; }
    var m = cotisation(i);
    out.innerHTML = 'Votre cotisation : <strong>' + euros(m) + ' par mois</strong>, soit ' + euros(m * 2) +
      ' prélevés tous les deux mois (' + euros(m * 12) + ' par an).<br>Déductible à 66 % des impôts : coût réel ' + euros(Math.round(m * 12 * 0.34)) + ' par an.';
    return m;
  }
  indice.addEventListener('input', maj);

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var m = maj();
    var lignes = [];
    Array.prototype.forEach.call(form.elements, function (el) {
      if (!el.name || (el.type === 'radio' && !el.checked)) return;
      var v = el.value.trim();
      if (el.classList.contains('maj')) v = v.toUpperCase();
      if (v) lignes.push(el.name + ' : ' + v);
    });
    if (m) lignes.push('Cotisation mensuelle : ' + euros(m));
    var corps = 'Bonjour,\n\nJe souhaite adhérer à la CGT CH Charles Perrens.\n\n' + lignes.join('\n') +
      '\n\nJe joins mon RIB pour le prélèvement automatique de mes cotisations.\n';
    var nom = (form.elements['Nom'].value + ' ' + form.elements['Prénom'].value).trim().toUpperCase();
    window.location.href = 'mailto:' + DEST + '?subject=' + encodeURIComponent('Bulletin d\'adhésion 2026 – ' + nom) +
      '&body=' + encodeURIComponent(corps);
  });
})();
</script>
```

---

## Widget 3 — Barème des cotisations

Jimdo : **+ → Élément HTML** → coller → Enregistrer

```html
<div class="wrap wrap--form wrap--pb">
  <div class="s-card anim anim-d1">
    <div class="s-title">Cotisations 2026</div>
    <div class="table-scroll">
      <table class="cotis-table">
        <thead><tr><th>Indice</th><th>Par mois</th><th>Prélèvement tous les 2 mois</th><th>Par an</th></tr></thead>
        <tbody>
        <tr><td>366</td><td>8,5 €</td><td>17 €</td><td>102 €</td></tr>
        <tr><td>380</td><td>9 €</td><td>18 €</td><td>108 €</td></tr>
        <tr><td>400</td><td>9,5 €</td><td>19 €</td><td>114 €</td></tr>
        <tr><td>420</td><td>10 €</td><td>20 €</td><td>120 €</td></tr>
        <tr><td>440</td><td>10,5 €</td><td>21 €</td><td>126 €</td></tr>
        <tr><td>460</td><td>11 €</td><td>22 €</td><td>132 €</td></tr>
        <tr><td>480</td><td>11,5 €</td><td>23 €</td><td>138 €</td></tr>
        <tr><td>500</td><td>12 €</td><td>24 €</td><td>144 €</td></tr>
        <tr><td>520+</td><td>12,5 €</td><td>25 €</td><td>150 €</td></tr>
        </tbody>
      </table>
    </div>
    <p class="cotis-note">Cotisations déductibles à 66 % de l'impôt sur le revenu.</p>
  </div>
</div>
```

---

## Widget 4 — Bandeau d'aide

Jimdo : **+ → Élément HTML** → coller → Enregistrer

```html
<div class="cta-band">
  <h3>Si vous avez besoin d'aide, <span>notre porte vous est toujours ouverte</span> !</h3>
  <p>Syndiqué ou non, notre porte vous est toujours ouverte.<br>
  <a href="mailto:cgt@ch-perrens.fr">cgt@ch-perrens.fr</a> · 05.56.56.35.65 · 07.68.03.34.15 · <a href="https://facebook.com/CGT.Perrens" target="_blank" rel="noopener">Facebook.com/CGT.Perrens</a> · <a href="https://instagram.com/cgt.perrens" target="_blank" rel="noopener">@cgt.perrens</a></p>
</div>
```
