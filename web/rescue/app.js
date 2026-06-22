/* SIG Lodges — guest-rescue page logic. Vanilla JS, no dependencies. */
(function () {
  "use strict";

  /* ---- CONFIG (edit these) -------------------------------------------------
     RESERVATIONS_EMAIL: monitored inbox guests reach.
       TODO: swap to a dedicated alias (e.g. guests@<brand>.com) once created.
     FORM_ENDPOINT: POST URL for the reconfirm form (Formspree / HubSpot form
       endpoint / serverless fn). Leave "" to fall back to a prefilled email. */
  var RESERVATIONS_EMAIL = "macko@stok.com";
  var FORM_ENDPOINT = ""; // e.g. "https://formspree.io/f/xxxx"
  /* ------------------------------------------------------------------------- */

  var $ = function (sel, ctx) { return (ctx || document).querySelector(sel); };
  var $$ = function (sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); };

  // Footer year
  var yearEl = $("#year");
  if (yearEl) yearEl.textContent = String(new Date().getFullYear());

  /* ---- Property selection / accent switching ---- */
  var LODGE_LABEL = { lt: "Lost Trail Lodge", rmp: "Thelma Hut", both: "" };

  function setProperty(key) {
    if (!LODGE_LABEL.hasOwnProperty(key)) key = "both";
    document.body.setAttribute("data-property", key);
    $$(".chip").forEach(function (c) {
      c.setAttribute("aria-pressed", String(c.getAttribute("data-select") === key));
    });
    // Pre-select the form's lodge dropdown when a specific property is chosen
    var lodgeSel = $("#lodge");
    if (lodgeSel && LODGE_LABEL[key]) lodgeSel.value = LODGE_LABEL[key];
    var theme = $('meta[name="theme-color"]');
    if (theme) theme.setAttribute("content", key === "rmp" ? "#294a6b" : "#1f4d3a");
  }

  $$(".chip").forEach(function (chip) {
    chip.addEventListener("click", function () { setProperty(chip.getAttribute("data-select")); });
  });

  /* ---- URL params: ?p=lt|rmp  ?ref=ABC123  ?pay=1 ---- */
  var params = new URLSearchParams(window.location.search);
  var pParam = (params.get("p") || "").toLowerCase();
  if (pParam === "lt" || pParam === "rmp") setProperty(pParam);
  var refParam = params.get("ref");
  if (refParam && $("#ref")) $("#ref").value = refParam;
  if (params.get("pay") === "1") {
    var needlink = $("#needlink");
    if (needlink) needlink.checked = true;
    var balance = $("#balance");
    if (balance) balance.scrollIntoView();
  }

  /* ---- Contact email links (mailto) ---- */
  var emailLink = $("#emailLink");
  if (emailLink) {
    emailLink.textContent = RESERVATIONS_EMAIL;
    emailLink.setAttribute("href", "mailto:" + RESERVATIONS_EMAIL +
      "?subject=" + encodeURIComponent("My reservation (Lost Trail / Thelma Hut)"));
  }
  $$("a.contact-email").forEach(function (a) {
    a.setAttribute("href", "mailto:" + RESERVATIONS_EMAIL +
      "?subject=" + encodeURIComponent("My reservation — need help"));
  });

  /* ---- Reconfirm form ---- */
  var form = $("#confirmForm");
  var statusEl = $("#formStatus");

  function setStatus(msg, kind) {
    if (!statusEl) return;
    statusEl.textContent = msg;
    statusEl.className = "form__status" + (kind ? " " + kind : "");
  }

  function buildMailto(data) {
    var lines = [
      "Reconfirming my reservation.",
      "",
      "Name: " + data.name,
      "Email: " + data.email,
      "Phone: " + (data.phone || "—"),
      "Lodge: " + data.lodge,
      "Check-in: " + (data.checkin || "—"),
      "Booking ref: " + (data.ref || "—"),
      "Needs payment link: " + (data.needlink ? "Yes" : "No"),
      "",
      "Message:",
      data.message || "—"
    ];
    return "mailto:" + RESERVATIONS_EMAIL +
      "?subject=" + encodeURIComponent("Reconfirm reservation — " + data.name) +
      "&body=" + encodeURIComponent(lines.join("\n"));
  }

  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }

      var data = {
        name: $("#name").value.trim(),
        email: $("#email").value.trim(),
        phone: $("#phone").value.trim(),
        lodge: $("#lodge").value,
        checkin: $("#checkin").value,
        ref: $("#ref").value.trim(),
        needlink: $("#needlink").checked,
        message: $("#message").value.trim()
      };

      if (!FORM_ENDPOINT) {
        // No backend configured yet — open a prefilled email so nothing is lost.
        setStatus("Opening your email app to send your reconfirmation…", "ok");
        window.location.href = buildMailto(data);
        return;
      }

      setStatus("Sending…", "");
      var btn = $("button[type=submit]", form);
      if (btn) btn.disabled = true;

      fetch(FORM_ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify(data)
      }).then(function (res) {
        if (!res.ok) throw new Error("Request failed: " + res.status);
        form.reset();
        setStatus("Thank you — your reservation request is in. We'll follow up personally, soon.", "ok");
      }).catch(function () {
        // Fall back to email so the guest is never stuck.
        setStatus("We couldn't submit automatically — opening your email app instead…", "err");
        window.location.href = buildMailto(data);
      }).finally(function () {
        if (btn) btn.disabled = false;
      });
    });
  }
})();
