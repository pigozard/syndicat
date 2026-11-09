# 15 — Élections professionnelles

**URL Jimdo :** `/droit-elections`  
**Titre de la page :** `Élections professionnelles · CGT — CH Charles Perrens`  
**Maquette :** `droit-elections.html`

**Fichiers à uploader avant de coller :** `[IMG:logo-cgt-perrens]`

| # | Widget |
|---|---|
| 0 | Navigation |
| 1 | En-tête de page |
| 2 | Contenu de la fiche |
| 3 | Notre liste |
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
    <h2>🗳️ Élections professionnelles</h2>
  </div>
</div>
```

---

## Widget 2 — Contenu de la fiche

Jimdo : **+ → Élément HTML** → coller → Enregistrer

```html
<div class="wrap wrap--narrow wrap--pb">
  <div class="fei-block anim">
    <h3>🗳️ Le vote au CH Charles Perrens : du 3 au 10 décembre 2026</h3>
    <p>Les prochaines élections professionnelles se tiendront <strong>du 3 au 10 décembre 2026</strong>. Elles déterminent qui vous représente pour les 4 prochaines années dans les instances de l'établissement — c'est le moment où votre voix pèse directement sur les décisions qui concernent vos conditions de travail.</p>
    <p><strong>Un vote 100 % électronique</strong>, sur la plateforme Néovote. À partir du <strong>16 novembre 2026</strong>, chaque agent reçoit par courrier son identifiant de vote.</p>
    <p><strong>Votre code de sécurité :</strong> les 6 derniers chiffres de votre IBAN, que vous trouverez sur votre fiche de paie.</p>
    <div class="fei-note">Pas reçu votre courrier Néovote, ou un souci pour vous connecter ? Contactez la permanence CGT : 05 56 56 35 65, du lundi au vendredi de 9h à 17h.</div>
  </div>
  <div class="fei-block anim anim-d1">
    <h3>🏛️ Ce que ces élections déterminent</h3>
    <p><strong>Le CSE (Comité Social d'Établissement) :</strong> instance de représentation du personnel consultée sur l'organisation, les conditions de travail, la gestion et l'évolution de l'établissement. Sa composition et sa formation spécialisée en matière de santé, sécurité et conditions de travail (F3SCT) sont directement issues du résultat des élections.</p>
    <p><strong>La CAP (Commission Administrative Paritaire) :</strong> instance paritaire qui examine les décisions individuelles concernant la carrière des agents (avancement, mobilité, discipline). La représentativité syndicale qui en ressort conditionne le poids de chaque organisation lorsqu'elle défend un agent.</p>
    <p>La représentativité syndicale obtenue lors de ces élections détermine aussi les moyens syndicaux (décharges d'activité, droits de communication) accordés à chaque organisation pour les 4 années suivantes.</p>
  </div>
  <div class="fei-block anim anim-d2">
    <h3>📅 Le cycle électoral, grandes étapes</h3>
    <p>Le calendrier électoral de la Fonction Publique Hospitalière comprend plusieurs étapes encadrées réglementairement, avant le scrutin lui-même : détermination et publication des listes électorales, dépôt des candidatures par les organisations syndicales, période de campagne électorale, puis vote et dépouillement.</p>
    <p><strong>22 octobre 2026 :</strong> dépôt des listes validé.<br>
    <strong>À partir du 16 novembre 2026 :</strong> envoi des identifiants de vote par Néovote.<br>
    <strong>Du 3 au 10 décembre 2026 :</strong> vote électronique.</p>
    <div class="fei-note">[À COMPLÉTER — date du dépouillement et de la publication des résultats.]</div>
  </div>
  <div class="fei-block anim anim-d3">
    <h3>✅ Pourquoi voter CGT</h3>
    <p>Voter CGT, c'est choisir une organisation qui vous défend individuellement au quotidien (entretiens, sanctions, arrêts contestés) autant qu'elle porte des revendications collectives (effectifs, salaires, conditions de travail) — et qui siège dans toutes les instances où se décide votre avenir professionnel.</p>
    <a href="/adherer" class="droit-link">Rejoindre la CGT dès maintenant →</a>
  </div>
</div>
```

---

## Widget 3 — Notre liste

Jimdo : **+ → Élément HTML** → coller → Enregistrer

```html
<div class="wrap wrap--narrow wrap--pb">
  <div class="fei-block anim">
    <h3>✊ La liste CGT : vos 24 candidates et candidats</h3>
    <p>Des collègues de tous les métiers de l'hôpital : soin, technique, administratif, encadrement.</p>
    <ol class="liste-cgt">
      <li><span class="liste-num">1</span><span><strong>Valérie Cuignet</strong><br>Aide-soignante</span></li>
      <li><span class="liste-num">2</span><span><strong>Mel Rousselet</strong><br>Ouvrier principal</span></li>
      <li><span class="liste-num">3</span><span><strong>Marie Ziegler</strong><br>Infirmière</span></li>
      <li><span class="liste-num">4</span><span><strong>Loetitia Icaseta</strong><br>Cadre de santé</span></li>
      <li><span class="liste-num">5</span><span><strong>Nadège Potin</strong><br>ASHQ</span></li>
      <li><span class="liste-num">6</span><span><strong>Titouan Caillot</strong><br>Infirmier</span></li>
      <li><span class="liste-num">7</span><span><strong>Laurent Constantin</strong><br>Encadrant d'unité de soins</span></li>
      <li><span class="liste-num">8</span><span><strong>Thelma Bord-Delvecchio</strong><br>Infirmière</span></li>
      <li><span class="liste-num">9</span><span><strong>Judicaël Le Calloch</strong><br>Aide-soignant</span></li>
      <li><span class="liste-num">10</span><span><strong>Benjamin Couton</strong><br>Ouvrier principal</span></li>
      <li><span class="liste-num">11</span><span><strong>Carole Thomas</strong><br>Infirmière</span></li>
      <li><span class="liste-num">12</span><span><strong>Sophie Bekkali</strong><br>Infirmière</span></li>
      <li><span class="liste-num">13</span><span><strong>Christelle Labarussias</strong><br>Infirmière</span></li>
      <li><span class="liste-num">14</span><span><strong>Jane-Laure Dupiol</strong><br>Éducatrice spécialisée</span></li>
      <li><span class="liste-num">15</span><span><strong>Marina Rodriguez</strong><br>Technicienne supérieure hospitalière</span></li>
      <li><span class="liste-num">16</span><span><strong>Bruno Bouchaud</strong><br>Ambulancier principal</span></li>
      <li><span class="liste-num">17</span><span><strong>Claire Charbonneau</strong><br>Agent des services hospitaliers qualifié</span></li>
      <li><span class="liste-num">18</span><span><strong>Kenza Rigodon</strong><br>Infirmière</span></li>
      <li><span class="liste-num">19</span><span><strong>Christophe Hidalgo</strong><br>Ouvrier principal</span></li>
      <li><span class="liste-num">20</span><span><strong>Nancy Bourdieu-Laplace</strong><br>Aide-soignante</span></li>
      <li><span class="liste-num">21</span><span><strong>Christel Goncalves Da Silva</strong><br>Aide-soignante</span></li>
      <li><span class="liste-num">22</span><span><strong>Gaëlle Charlot</strong><br>Ergothérapeute</span></li>
      <li><span class="liste-num">23</span><span><strong>Christelle Rousset</strong><br>Assistante médico-administrative</span></li>
      <li><span class="liste-num">24</span><span><strong>Awa N Dione</strong><br>Agent des services hospitaliers qualifié</span></li>
    </ol>
    <div class="fei-note">Du 3 au 10 décembre 2026, votez et faites voter CGT, pour que le changement continue !</div>
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
