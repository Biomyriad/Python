function loadCssValues(value) {
    var r = document.querySelector(':root');
    var rs = getComputedStyle(r);

    for (const [key, val] of Object.entries(value)) {
        var prop = rs.getPropertyValue(key);
        if(prop != "" && (val != "" || val != null)) {
            r.style.setProperty(key, val);
        }
        console.log(key, val);
    }
}
