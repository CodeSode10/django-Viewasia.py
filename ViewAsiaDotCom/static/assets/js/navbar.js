$(document).ready(function () {
    $(window).scroll(function () {
        $('.menu-btn').click(function () {
            $('.navbaar .menu .btns').toggleClass("active");
            $('.menu-btn i').toggleClass("active");
        });
    });
    
});

submitted = () => {
    alert('Contact Form Submitted')
}

uploaded = () => {
    alert('Uploaded ! Wait for approval')
}