$(document).ready(function() {
	$('.spoiler-text').hide();  
	$('html').on('click', '.spoiler', function() {
		$(this).toggleClass("folded").toggleClass("unfolded").next().slideToggle(250);
	});
});