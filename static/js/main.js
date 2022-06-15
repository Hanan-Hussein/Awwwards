var nowRate = document.getElementById('nowRate');
nowRate.addEventListener('click', Rate);

function Rate(e) {
    e.preventDefault();
    allrates.style.display='initial';
    nowRate.style.display='none';
}