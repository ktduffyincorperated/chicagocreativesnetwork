

// .arrow img {
//   width: 5vw;
//   transform: rotate(180deg);}




// why 
// height: 14vh;

$(document).ready(function() {

      function changeText(id) {
          id.innerHTML = "Ooops!";
      }

      $(".typeBox, #menu").hide();

      $(".why").click(function(){
        $(".typeBox").fadeIn("slow");
        $(".bar").fadeOut("slow");
        $(".why").css("height","14vh");
        $(".arrowWhy").addClass("arrowRotate");
      });

      $(".menuIcon").click(function(){
        $(this).addClass("gradientHolder");
         $("#menu").slideToggle();
         $(".barOne").toggleClass("barOneRot");
         $(".barTwo").toggleClass("barTwoRot")
      });


});











// test
    // window.onload = function() {
    //    if (window.jQuery) {
    //       alert('jQuery is loaded');
    //    } else {
    //       alert('jQuery is not loaded');
    //    }
    // }










// $( document ).ready(function() {

//     console.log(test); 

//     // https://codepen.io/GreenSock/pen/gOOZNzQ
// // Rate = Distance over Time r=d/t
// // If we want to define the rate, and 
// // the distance is determined, 
// // time will have to be variable

// // We want to define the rate, and we can 
// // define that statically
// r = 100;
// adjustJank = 4; // Set this to 0 to see the jank I'm talking about ... this just adds to the distance animated to smooth out the seam

// // Get the initial scroll elements and save them for later
// const scrollElems = document.querySelectorAll('.scroll p');

// // Adjust our tween based on the object and distance given
// function adjustTween(obj, d) {
//   // Get the progress of the previous tween if it exists
//   let progress = 0;
//   if(obj.tween) {
//     progress = obj.tween.progress();
//     // Kill the previous tween
//     obj.tween.kill();
//   }
    
//   // r = d/t 
//   // r*t = d
//   // t = d/r
  
//   // Set the proper time
//   var t = d/r;

//   // Create a new tween to animate our text so that it loops
//   // Make sure to save it to the object so we can refer to it later
//   obj.tween = gsap.fromTo(obj.parentElement, {x: 0}, {
//     duration: t,
//     x: "-"+(d+adjustJank), 
//     ease: 'linear',
//     repeat: -1,
//   }).progress(progress); // Set the progress of the new tween to the same value of
//                          // the previous tween (if it exists) before it was killed
                      
// }

// // Set up for what appears to be an seamless stream of text
// // This could go in an init() function
// scrollElems.forEach((obj, i) => {
//   var d = obj.offsetWidth;
//   var parent = obj.parentElement;
//   var clone = obj.cloneNode(true);
//   parent.appendChild(clone);
//   gsap.set(parent.parentElement, {width: d});
  
//   adjustTween(obj, d);
// });

// // Adjust widths and tweens on resize
// window.addEventListener("resize", () => {
//   scrollElems.forEach((obj, i) => {
//     var d = obj.offsetWidth;
//     var parent = obj.parentElement;
//     gsap.set(parent.parentElement, {width: d});
//     adjustTween(obj, d);
//   });
// });


//});