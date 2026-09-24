
function changeLanguage(langCode) {
    document.cookie = `googtrans=/en/${langCode}; path=/;`;
    document.cookie = `googtrans=/en/${langCode}; domain=${window.location.hostname}; path=/;`;
    document.cookie = `googtrans=/en/${langCode}; domain=.${window.location.hostname}; path=/;`;
    localStorage.setItem("site_lang", langCode);
    location.reload();
}

document.addEventListener("DOMContentLoaded", () => {
    const lang = localStorage.getItem("site_lang") || "en";
    const langText = document.getElementById("current-lang-text");
    
    if (lang === "ar") {
        document.body.classList.add("lang-ar");
        document.documentElement.setAttribute("dir", "rtl");
        document.documentElement.setAttribute("lang", "ar");
        if(langText) langText.innerText = "AR";
    } else if (lang === "am") {
        document.body.classList.add("lang-am");
        document.documentElement.setAttribute("lang", "am");
        if(langText) langText.innerText = "AM";
    } else {
        if(langText) langText.innerText = "EN";
    }
});

