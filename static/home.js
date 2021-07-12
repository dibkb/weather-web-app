// Home Page
gsap.from(".text-col", {duration: 1.2, opacity: 0,x : -180, ease: 'Power0.easeOut',});
gsap.from(".img-col", {duration: 1.8, opacity: 0,x : 180, ease: 'Power1.easeOut',});
gsap.from(".social", {duration: 1.8, opacity: 0,x : 180, ease: Elastic.easeOut.config(1, 0.3),delay: 1.8,});
gsap.to(".social", {opacity: 0});
gsap.from(".login-btn", {duration: 1.2, opacity: 0,y : -160, ease: 'Power4.easeOut',delay: 1.2});




