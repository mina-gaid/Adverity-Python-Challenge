/*
 * Javascript to show and hide cookie banner using localstorage
 */

/**
 * @description Shows the cookie banner
 */
function showCookieBanner() {
  let cookieBanner = document.getElementById("cookie-banner");
  cookieBanner.style.display = "block";
}

/**
 * @description Hides the Cookie banner and saves the value to localstorage
 */
function hideCookieBanner() {
  localStorage.setItem("cookie_consent_isCookieAccepted", "yes");

  let cookieBanner = document.getElementById("cookie-banner");
  cookieBanner.style.display = "none";
}

/**
 * @description Checks the localstorage and shows Cookie banner based on it.
 */
function initializeCookieBanner() {
  let isCookieAccepted = localStorage.getItem(
    "cookie_consent_isCookieAccepted"
  );
  if (isCookieAccepted === null) {
    localStorage.setItem("cookie_consent_isCookieAccepted", "no");
    showCookieBanner();
  }
  if (isCookieAccepted === "yes") {
    hideCookieBanner();
  }
}

// Assigning values to window object
window.onload = initializeCookieBanner();
window.cookie_consent_hideCookieBanner = hideCookieBanner;
