const jobHolder = document.getElementById('job-holder');
const jobDiv = document.getElementById('jobs');
const jobAdd = document.getElementById('job-add');
const jobView = document.getElementById('job-view');


const projectHolder = document.getElementById('project-holder');
const projectDiv = document.getElementById('projects');
const projectAdd = document.getElementById('project-add');
const projectView = document.getElementById('project-view');

const photoHolder = document.getElementById('photo-holder');
const photoDiv = document.getElementById('photos');
const photoAdd = document.getElementById('photo-add');
const photoView = document.getElementById('photo-view');

const noUser = document.getElementById('no-user-profile-management');

if (!noUser) {
    let jobLinks = document.querySelectorAll('.job-link');
    let projectLinks = document.querySelectorAll('.project-link');
    let photoLinks = document.querySelectorAll('.photo-link');

    jobDiv.addEventListener('click', function (event) {
        jobDiv.style.display = 'none';
        jobLinks.forEach(function (job) {
            unfade(job);
        });
        jobHolder.classList.add('holder-clicked');
        jobHolder.classList.remove('job-holder');
    });
    projectDiv.addEventListener('click', function (event) {
        projectDiv.style.display = 'none';
        projectLinks.forEach(function (project) {
            unfade(project);
        });
        projectHolder.classList.add('holder-clicked');
        projectHolder.classList.remove('project-holder');
    });
    photoDiv.addEventListener('click', function (event) {
        photoDiv.style.display = 'none';
        photoLinks.forEach(function (photo) {
            unfade(photo);
        });
        photoHolder.classList.add('holder-clicked');
        photoHolder.classList.remove('photo-holder');
    });
}

const header = document.getElementById('header');

window.onscroll = function () {
    "use strict";
    if (document.body.scrollTop >= 1 || document.documentElement.scrollTop >= 1) {
        header.classList.add('header-colored');
        header.classList.remove('header-transparent');
    }
    else {
        header.classList.add('header-transparent');
        header.classList.remove('header-colored');
    }
}

function unfade(element) {
    let op = 0.1;
    element.style.display = 'block';
    let timer = setInterval(function () {
        if (op >= 1) {
            clearInterval(timer);
        }
        element.style.opacity = op;
        element.style.filter = 'alpha(opacity=' + op * 100 + ")";
        op += op * 0.02;
    }, 10);
}

const inputs = document.querySelectorAll('input');

inputs.forEach(function (a) {
    a.setAttribute('autocomplete', 'off');
});