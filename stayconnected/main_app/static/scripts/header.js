const jobHolder = document.getElementById('job-holder');
const jobDiv = document.getElementById('jobs');
const jobAdd = document.getElementById('job-add');
const jobView = document.getElementById('job-view');


const projectHolder = document.getElementById('project-holder');
const projectDiv = document.getElementById('projects');
const projectAdd = document.getElementById('project-add');
const projectView = document.getElementById('project-view');

const noUser = document.getElementById('no-user-profile-management');

if (!noUser) {
    let jobLinks = document.querySelectorAll('.job-link');
    let projectLinks = document.querySelectorAll('.project-link');

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
        projectHolder.classList.remove('job-holder');
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