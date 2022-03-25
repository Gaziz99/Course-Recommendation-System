(function($) {

	"use strict";

	var fullHeight = function() {

		$('.js-fullheight').css('height', $(window).height());
		$(window).resize(function(){
			$('.js-fullheight').css('height', $(window).height());
		});

	};
	fullHeight();

	var carousel = function() {
		$('.featured-carousel').owlCarousel({
	    loop:true,
	    autoplay: true,
	    margin:30,
	    animateOut: 'fadeOut',
	    animateIn: 'fadeIn',
	    nav:true,
	    dots: true,
	    autoplayHoverPause: false,
	    items: 1,
	    navText : ["<span class='ion-ios-arrow-back'></span>","<span class='ion-ios-arrow-forward'></span>"],
	    responsive:{
	      0:{
	        items:1
	      },
	      600:{
	        items:2
	      },
	      1000:{
	        items:3
	      }
	    }
		});

	};
	carousel();

})(jQuery);



var allStars = document.querySelectorAll('*[id^="star"]');

//var form = document.querySelectorAll('*[id^="form"]')


//console.log(form)

const csrf = document.getElementsByName('csrfmiddlewaretoken')

const handleSelect = (selection, rate) => {
	
	
	const star = document.getElementById(selection);
	const otherStarIds = [1,2,3,4,5].map((num) => {
		const idParts = selection.split('.');
		const otherId = `${idParts[0]}.${num}.${idParts[2]}.${idParts[3]}`;
		return otherId;
	}).filter((id) => id !== selection);
	const otherStar1 = document.getElementById(otherStarIds[0]);
	const otherStar2 = document.getElementById(otherStarIds[1]);
	const otherStar3 = document.getElementById(otherStarIds[2]);
	const otherStar4 = document.getElementById(otherStarIds[3]);
	
	switch(rate){
		case '1':{
			star.classList.add('checked')
			otherStar1.classList.remove('checked')
			otherStar2.classList.remove('checked')
			otherStar3.classList.remove('checked')
			otherStar4.classList.remove('checked')
			return
		}
		case '2':{
			star.classList.add('checked')
			otherStar1.classList.add('checked')
			otherStar2.classList.remove('checked')
			otherStar3.classList.remove('checked')
			otherStar4.classList.remove('checked')
			return
		}
		case '3':{
			star.classList.add('checked')
			otherStar1.classList.add('checked')
			otherStar2.classList.add('checked')
			otherStar3.classList.remove('checked')
			otherStar4.classList.remove('checked')
			return
		}
		case '4':{
			star.classList.add('checked')
			otherStar1.classList.add('checked')
			otherStar2.classList.add('checked')
			otherStar3.classList.add('checked')
			otherStar4.classList.remove('checked')
			return
		}
		
		case '5':{
			star.classList.add('checked')
			otherStar1.classList.add('checked')
			otherStar2.classList.add('checked')
			otherStar3.classList.add('checked')
			otherStar4.classList.add('checked')
			return
		}
		case '0':{
			star.classList.remove('checked')
			otherStar1.classList.remove('checked')
			otherStar2.classList.remove('checked')
			otherStar3.classList.remove('checked')
			otherStar4.classList.remove('checked')
			return
		}
	}
}




if (allStars){


	allStars.forEach(item=> item.addEventListener('mouseover', (event)=>{
		const id = event.target.id;

		const rate = id.split('.')[1]
	
		handleSelect(id, rate)
		

	}))

	

	allStars.forEach(item=> item.addEventListener('click', (event)=>{
		
		const val = event.target.id.split('.')[1];

		const course_id = event.target.id.split('.')[2];
		
		const user_id = event.target.id.split('.')[3];
	

		var form = document.getElementById(course_id)

		form.addEventListener('submit',e=>{
			
			e.preventDefault()
			
		

			
		//	const user_id = e.target.id.split('.')[1];

		//	console.log(course_id,user_id)

			const val_num = +val

		//	console.log(val_num)

			$.ajax({
				type: 'POST',
				url: '/rate',
				data:{
					'csrfmiddlewaretoken':csrf[0].value,
					'course_id':course_id,
					'user_id':user_id,
					'val_num':val_num,
				},
				success: function(response){
					console.log(response)
				},
				error: function(error){
					console.log(error)
				}
			})
		})
	}))
}
