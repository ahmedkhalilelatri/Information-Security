function getCookie(name) {
    const cookies = document.cookie.split(";");

    for (let cookie of cookies) {
        cookie = cookie.trim();

        if (cookie.startsWith(name + "=")) {
            return cookie.substring(name.length + 1);
        }
    }

    return null;
}

let analyticsId = getCookie("analytics_id");

if (!analyticsId) {
    analyticsId =
        Math.random().toString(36).substring(2) +
        Date.now().toString(36);

    document.cookie =
        "analytics_id=" +
        analyticsId +
        "; max-age=3600; path=/";
}

console.log("Analytics ID:", analyticsId);

const url =
    "http://analytics.test:9100/collect" +
    "?id=" + encodeURIComponent(analyticsId) +
    "&publisher=" + encodeURIComponent(location.hostname) +
    "&page=" + encodeURIComponent(document.title);

const img = new Image();
img.src = url;