function setTheme(themeName) {
    document.body.className = themeName;
    localStorage.setItem("theme", themeName);
}

window.onload = function () {
    let savedTheme = localStorage.getItem("theme");

    if (savedTheme) {
        document.body.className = savedTheme;
    }
}