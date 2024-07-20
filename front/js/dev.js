$(document).ready(function () {
    /*var*/
    let aa = 0;
    /*fix*/
    let w = $(window).width();
    if (w < 992) {
        $("#bazsho").addClass('bazsho');
        $(".menu-top").addClass('menu-mobile');
        $(".menu-top").removeClass('menu-top');
        $(".baz").css("display","flex");
    }
    /*resize*/
    $(window).resize(function () {
        let ww = $(window).width();
        if (ww < 992 & aa % 2 !== 0) {
            $("#bazsho").addClass('bazsho');
            $(".menu-top").addClass('menu-mobile');
            $(".menu-top").removeClass('menu-top');
            $(".baz").css("display","flex");
            aa++;
        } else if (ww > 992 & aa % 2 === 0) {
            $("#bazsho").removeClass('bazsho');
            $(".menu-mobile").addClass('menu-top');
            $(".menu-mobile").removeClass('menu-mobile');
            $(".baz").hide();
            aa++
        }
    });
    /*click*/
    $(".baz").click(function () {
        let mm = $(window).width() - 250;
        $(".bazsho").css("width", "250px");
        $(".back-c").css("width", "100%");
    });
    $(".back-c, .arrow-menu").click(function () {
        $(".bazsho").removeAttr("style");
        $(".back-c").css("width", "0");
    });
    /*menu-a*/
    $("li").has('ul').addClass("sub-menu");
    $(".sub-menu>a:first-child").addClass("t");
    $(".menu-mobile>ul>li>a").click(function () {
        $(this).next('ul').slideToggle().toggleClass('open');
        if ($(this).next('ul').hasClass('open')) {
            $(this).removeClass("t");
            $(this).addClass("b");
        } else {
            $(this).removeClass("b");
            $(this).addClass("t");
        }
    });
    $(".menu-mobile>ul>li>ul>li>a").click(function () {
        $(this).next('ul').slideToggle().toggleClass('open');
        if ($(this).next('ul').hasClass('open')) {
            $(this).removeClass("t");
            $(this).addClass("b");
        } else {
            $(this).removeClass("b");
            $(this).addClass("t");
        }
    });
    $(".menu-mobile>ul>li>ul>li>ul>li>a").click(function () {
        $(this).next('ul').slideToggle().toggleClass('open');
        if ($(this).next('ul').hasClass('open')) {
            $(this).removeClass("t");
            $(this).addClass("b");
        } else {
            $(this).removeClass("b");
            $(this).addClass("t");
        }
    });
    $(".menu-mobile a.t").removeAttr("href");
    /**/
    $("#ser").click(function () {
        $(".search-header-box").slideToggle();
    });
    /**/
});
var swiper = new Swiper('.slider-big .swiper-container', {
    slidesPerView: 2.5,
    spaceBetween: 50,
    slidesPerGroup: 1,
    effect: 'coverflow',
    grabCursor: true,
    loop: true,
    centeredSlides: true,
    autoplay: {
        delay: 6000,
        disableOnInteraction: false,
    },
    coverflowEffect: {
        rotate: 0,
        stretch: 0,
        depth: 100,
        modifier: 1,
    },
    pagination: {
        el: '.slider-big .swiper-pagination',
    },
    breakpoints: {
        1024: {
            slidesPerView: 2.5,
            spaceBetween: 40,
        },
        768: {
            slidesPerView: 1.5,
            spaceBetween: 40,
        },
        640: {
            slidesPerView: 1.2,
            spaceBetween: 25,
        },
        320: {
            slidesPerView: 1.5,
            spaceBetween: 20,
        }
    }
});
var swiper = new Swiper('.slider-comment-index .swiper-container', {
    slidesPerView: 3,
    spaceBetween: 25,
    // init: false,
    pagination: {
        el: '.slider-comment-index .swiper-pagination',
        clickable: true,
    },
    breakpoints: {
        1024: {
            slidesPerView: 3,
            spaceBetween: 40,
        },
        768: {
            slidesPerView: 2,
            spaceBetween: 30,
        },
        640: {
            slidesPerView: 1.3,
            spaceBetween: 20,
        },
        320: {
            slidesPerView: 1,
            spaceBetween: 10,
        }
    }
});
// menu button profile
const profileBtn = document.getElementById("profileBtn");
const profileDropdown = document.getElementById("profileDropdown");
const posTitleBox = document.querySelector('.pos-title-box');
const posWrapper = document.querySelector('.pos-wrapper')

profileBtn.addEventListener("click", () =>{
    profileBtn.classList.toggle("active")
    profileDropdown.classList.toggle("active")
});
posTitleBox.addEventListener("click", () =>{
    posWrapper.classList.toggle("active")
})
function priceRang() {
    const priceWrapper = document.querySelector('.price-wrapper');
    priceWrapper.classList.toggle("active");
}
function wraingBtn() {
    const element = document.getElementById("showInfoUser");
    element.classList.toggle("active");
}
function dropDownTab() {
    const dropDownTab = document.querySelector('.min-menu-chat');
    dropDownTab.classList.toggle("active");
}
function openChat(evt, username) {
    var i, singleChatBox, singleChat;
    singleChatBox = document.getElementsByClassName("single-chat-box");
    for (i = 0; i < singleChatBox.length; i++) {
      singleChatBox[i].style.display = "none";
    }
    singleChat = document.getElementsByClassName("single-chat");
    for (i = 0; i < singleChat.length; i++) {
      singleChat[i].className = singleChat[i].className.replace(" active", "");
    }
    document.getElementById(username).style.display = "flex";
    evt.currentTarget.className += " active";
}
