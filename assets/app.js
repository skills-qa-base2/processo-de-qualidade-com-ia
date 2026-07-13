(function () {
  // ---------- Theme toggle (in-memory only, no storage) ----------
  var themeBtn = document.querySelector("[data-theme-toggle]");
  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      var html = document.documentElement;
      var current = html.getAttribute("data-theme");
      if (current === "dark") {
        html.removeAttribute("data-theme");
        themeBtn.textContent = "◐ escuro";
      } else {
        html.setAttribute("data-theme", "dark");
        themeBtn.textContent = "◑ claro";
      }
    });
  }

  // ---------- Mobile sidebar toggle ----------
  var menuBtn = document.querySelector("[data-menu-toggle]");
  var sidebar = document.querySelector(".sidebar");
  if (menuBtn && sidebar) {
    menuBtn.addEventListener("click", function () {
      sidebar.classList.toggle("open");
    });
    document.addEventListener("click", function (e) {
      if (window.innerWidth > 900) return;
      if (sidebar.classList.contains("open") && !sidebar.contains(e.target) && e.target !== menuBtn) {
        sidebar.classList.remove("open");
      }
    });
  }

  // ---------- Search ----------
  var input = document.querySelector("[data-search-input]");
  var resultsBox = document.querySelector("[data-search-results]");
  if (input && resultsBox && window.SKILLS_SEARCH_INDEX) {
    var base = input.getAttribute("data-base") || "";

    function render(items) {
      if (!items.length) {
        resultsBox.innerHTML = '<div class="search-empty">Nenhum resultado encontrado.</div>';
        resultsBox.classList.add("active");
        return;
      }
      resultsBox.innerHTML = items
        .slice(0, 12)
        .map(function (item) {
          return (
            '<a href="' + base + item.url + '">' +
            '<div class="r-title">' + item.title + '</div>' +
            '<div class="r-desc">' + item.desc + '</div>' +
            '</a>'
          );
        })
        .join("");
      resultsBox.classList.add("active");
    }

    input.addEventListener("input", function () {
      var q = input.value.trim().toLowerCase();
      if (!q) {
        resultsBox.classList.remove("active");
        resultsBox.innerHTML = "";
        return;
      }
      var matches = window.SKILLS_SEARCH_INDEX.filter(function (item) {
        return (
          item.title.toLowerCase().indexOf(q) !== -1 ||
          item.desc.toLowerCase().indexOf(q) !== -1 ||
          item.command.toLowerCase().indexOf(q) !== -1 ||
          item.category.toLowerCase().indexOf(q) !== -1
        );
      });
      render(matches);
    });

    input.addEventListener("focus", function () {
      if (input.value.trim()) resultsBox.classList.add("active");
    });

    document.addEventListener("click", function (e) {
      if (!resultsBox.contains(e.target) && e.target !== input) {
        resultsBox.classList.remove("active");
      }
    });
  }
})();
