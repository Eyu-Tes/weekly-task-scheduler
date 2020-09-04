const buttonLeft = document.getElementById('slideLeft');
const buttonRight = document.getElementById('slideRight');

buttonLeft.addEventListener('click', function(){
    let slider = document.getElementById('slider');
    slider.scrollLeft -= 180;
    if (slider.scrollLeft == 0) {
        buttonLeft.style.visibility = 'hidden';
    }
    buttonRight.style.visibility = 'visible';
})

buttonRight.addEventListener('click', function(){
    let slider = document.getElementById('slider');
    let previousScrollLeft = slider.scrollLeft;
    slider.scrollLeft += 180;
    if (previousScrollLeft == 0){
        if (slider.scrollLeft < previousScrollLeft+180) {
            buttonRight.style.visibility = 'hidden';
        }
    } 
    else if (slider.scrollLeft <= previousScrollLeft+180) {
        buttonRight.style.visibility = 'hidden';
    }
    buttonLeft.style.visibility = 'visible';
})