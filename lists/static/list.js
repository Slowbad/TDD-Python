SetInputEvents = function() {
	$('input[name="text"]').on('keypress click', function() {
		$('.has-error').hide();
	});
};

SetInputEvents();
