
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function () {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.maxHeight) {
            content.style.maxHeight = null;
        } else {
            content.style.maxHeight = content.scrollHeight *2 + "px";
        }
    });
}

let selectList = document.getElementsByClassName('select-dropdown');

for (let j = 0; j < selectList.length; j++) {
    j.setAttribute('disabled', true);
}