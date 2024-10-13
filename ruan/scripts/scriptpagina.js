

window.addEventListener('scroll', function() {
    const scrolled = window.scrollY;
    const header = document.querySelector('header');
    header.style.opacity = Math.max(1 - scrolled / 200, 0);
});
class MobileNavbar {
    constructor (mobileMenu, navList ,navLinks) {
        this.mobileMenu = document.querySelector(mobileMenu);
        this.navList = document.querySelector(navList);
        this.navLinks = document.querySelectorAll(navLinks);
        this.activeClass = "active";
        this.handleClick =this.handleClick.bind(this)
    }
    handleClick() {
        this.navList.classList.toggle(this.activeClass);
        this.mobileMenu.classList.toggle(this.activeClass);
        this.animateLinks();
    }
    animateLinks(){
        this.navLinks.forEach((link,index)=>{
            link.style.animation
            ? (link.style.animation="")
            : (link.style.animation= 'navLinkFade 0.5s ease forwards ${index/7 +0.3}s')
        })
    }
   
    addClickEvent(){
        this.mobileMenu.addEventListener("click", this.handleClick);
    }
    init() {
        if(this.mobileMenu) {
            this.addClickEvent();
        }
        return this
    }
}
const mobileNavbar = new MobileNavbar(
    ".mobile-menu",
    ".nav-list",
    ".nav-list li",
);
mobileNavbar.init();