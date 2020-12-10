$(function() {
	$('a.fancy-formsets-add-row').click(function() {
		var tr = $(this).parents('table').find('tr.extra:first');
		if (tr.length) {
			tr.removeClass("hidden").removeClass("extra");
			tr.find("span.fancy-formsets-delete input")
		      .prop('checked', false);
		    tr.trigger("fancy-formsets-row-added");
		} else {
			$(this).next("span.fancy-formsets-no-more-rows")
			       .removeClass("hidden");
		}		
		return false;
	});
});
