const menuButton = document.querySelector(".nav-toggle");
const menu = document.querySelector("#menu-principal");

function setMenuState(isOpen) {
  if (!menuButton || !menu) return;

  menu.classList.toggle("is-open", isOpen);
  menuButton.setAttribute("aria-expanded", String(isOpen));

  const icon = menuButton.querySelector(".nav-toggle-icon");
  const text = menuButton.querySelector(".nav-toggle-text");

  if (icon) icon.textContent = isOpen ? "✕" : "☰";
  if (text) text.textContent = isOpen ? "Fechar" : "Menu";
}

if (menuButton && menu) {
  menuButton.addEventListener("click", () => {
    const isOpen = menuButton.getAttribute("aria-expanded") === "true";
    setMenuState(!isOpen);
  });

  menu.addEventListener("click", (event) => {
    if (event.target.closest("a")) setMenuState(false);
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      setMenuState(false);
      menuButton.focus();
    }
  });

  window.addEventListener("resize", () => {
    if (window.innerWidth > 700) setMenuState(false);
  });
}
