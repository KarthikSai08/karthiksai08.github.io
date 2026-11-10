(function () {
  var root = document.documentElement;
  var calm = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  var steps = document.querySelectorAll("#trace li");
  if (calm) { steps.forEach(function (s) { s.classList.add("on"); }); }
  else if (steps.length) {
    var i = 0;
    setInterval(function () {
      if (i < steps.length) { steps[i].classList.add("on"); i++; }
      else { steps.forEach(function (s) { s.classList.remove("on"); }); i = 0; }
    }, 1100);
  }

  var btn = document.getElementById("theme");
  var meta = document.querySelector('meta[name="theme-color"]');
  var modes = ["auto", "light", "dark"];
  var mq = window.matchMedia("(prefers-color-scheme: dark)");
  function current() { return root.dataset.theme || "auto"; }
  function paint() {
    var m = current();
    btn.textContent = m.charAt(0).toUpperCase() + m.slice(1);
    var dark = m === "dark" || (m === "auto" && mq.matches);
    if (meta) meta.setAttribute("content", dark ? "#2b2f3d" : "#e5eaf5");
  }
  btn.addEventListener("click", function () {
    var next = modes[(modes.indexOf(current()) + 1) % modes.length];
    if (next === "auto") root.removeAttribute("data-theme"); else root.dataset.theme = next;
    try { next === "auto" ? localStorage.removeItem("theme") : localStorage.setItem("theme", next); } catch (e) {}
    paint();
  });
  if (mq.addEventListener) mq.addEventListener("change", paint);
  paint();

  var secs = document.querySelectorAll("section[data-tone]");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) root.dataset.tone = e.target.dataset.tone;
      });
    }, { rootMargin: "-40% 0px -50% 0px" });
    secs.forEach(function (s) { io.observe(s); });
  }

  var bar = document.getElementById("bar");
  function prog() {
    var h = document.documentElement.scrollHeight - window.innerHeight;
    bar.style.transform = "scaleX(" + (h > 0 ? Math.min(1, window.scrollY / h) : 0) + ")";
  }
  window.addEventListener("scroll", prog, { passive: true }); prog();

  var cp = document.getElementById("copy");
  if (cp) cp.addEventListener("click", function () {
    var done = function () { cp.textContent = "Copied!"; setTimeout(function () { cp.textContent = "Copy email"; }, 1800); };
    if (navigator.clipboard) navigator.clipboard.writeText(cp.dataset.email).then(done, function () { location.href = "mailto:" + cp.dataset.email; });
    else location.href = "mailto:" + cp.dataset.email;
  });

  if (!calm && "IntersectionObserver" in window) {
    var rv = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add("in");
        var el = e.target; setTimeout(function () { el.classList.remove("rv", "in"); }, 800);
        rv.unobserve(el);
      });
    }, { threshold: 0.12 });
    document.querySelectorAll(".card,.why-card,.stats,.job,.skill-group,.edu-item").forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.top > window.innerHeight) { el.classList.add("rv"); rv.observe(el); }
    });
  }
})();
