var nowRate = document.getElementById('nowRate');
var vRate = document.getElementById('vRate');
var match = document.getElementById('match_wrapper');

nowRate.addEventListener('click', Rate);
vRate.addEventListener('click', Rater);

function Rate(e) {
    e.preventDefault();
    allrates.style.display = 'initial';
    nowRate.style.display = 'none';
    vRate.style.display = 'initial';
}

function Rater(e) {
    e.preventDefault();
    window.location.reload();
    window.scrollTo(0, document.body.scrollHeight);
}
