(function () {
  var form = document.getElementById('contact-form');
  if (!form) return;
  var recap = document.getElementById('recap');
  var pre = document.getElementById('recap-text');
  var status = document.getElementById('copy-status');
  var mail = document.getElementById('recap-mail');
  var EMAIL = 'alban.vayer@gmail.com';
  var rules = {
    nom: function (v) { return v.trim().length >= 2 ? '' : 'Indiquez votre nom.'; },
    tel: function (v) {
      return /^(?:(?:\+|00)33|0)[1-9](?:[ .-]?\d{2}){4}$/.test(v.trim()) ? '' : 'Saisissez un numéro français valide, par exemple 06 12 34 56 78.';
    },
    email: function (v) {
      v = v.trim();
      return v === '' || /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v) ? '' : 'Saisissez une adresse e-mail valide, par exemple nom@exemple.fr.';
    },
    projet: function (v) { return v ? '' : 'Choisissez le type de demande.'; },
    message: function (v) { return v.trim().length >= 10 ? '' : 'Décrivez votre demande en quelques mots (10 caractères minimum).'; }
  };
  function check(name) {
    var el = form.elements[name], err = document.getElementById('err-' + name);
    var msg = rules[name](el.value);
    err.textContent = msg;
    if (msg) { el.setAttribute('aria-invalid', 'true'); } else { el.removeAttribute('aria-invalid'); }
    return !msg;
  }
  Object.keys(rules).forEach(function (n) {
    form.elements[n].addEventListener('blur', function () { check(n); });
    form.elements[n].addEventListener('input', function () { if (form.elements[n].getAttribute('aria-invalid')) check(n); });
  });
  function build() {
    var v = function (n) { return form.elements[n].value.trim(); };
    var lines = ['Bonjour Alban Vayer,', '', 'Je vous contacte pour : ' + v('projet') + '.', '', 'Nom : ' + v('nom'), 'Téléphone : ' + v('tel')];
    if (v('email')) lines.push('E-mail : ' + v('email'));
    lines.push('', 'Message : ' + v('message'));
    return lines.join('\n');
  }
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var first = null;
    Object.keys(rules).forEach(function (n) { if (!check(n) && !first) first = form.elements[n]; });
    if (first) { first.focus(); recap.hidden = true; return; }
    var text = build();
    pre.textContent = text;
    mail.href = 'mailto:' + EMAIL + '?subject=' + encodeURIComponent('Demande pour mon jardin') + '&body=' + encodeURIComponent(text);
    status.textContent = '';
    recap.hidden = false;
    recap.focus();
    recap.scrollIntoView({ behavior: 'smooth', block: 'center' });
  });
  document.getElementById('copy-btn').addEventListener('click', function () {
    var text = pre.textContent;
    function fallback() {
      var r = document.createRange(); r.selectNodeContents(pre);
      var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
      status.textContent = 'Copie automatique impossible : le message est sélectionné, faites Ctrl+C.';
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () { status.textContent = 'Message copié.'; }, fallback);
    } else { fallback(); }
  });
  document.getElementById('edit-btn').addEventListener('click', function () {
    recap.hidden = true;
    form.elements.nom.focus();
  });
})();
