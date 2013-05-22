$(function(){
	$("#mulai").datetimepicker({
		timeFormat: 'H:m:s',
		dateFormat: 'yy-mm-dd',
		timeText: "Waktu",
		hourText: "Jam",
		showMinute: 0,
		onClose: function( selectedDate ) {
			$("#selesai").datetimepicker( 
				"option", "minDate", selectedDate);

		} 
	});
	$("#selesai").datetimepicker({
		timeFormat: 'H:m:s',
		dateFormat: 'yy-mm-dd',
		timeText: "Waktu",
		hourText: "Jam",
		showMinute: 0,
		onClose: function( selectedDate ) {
			$("#mulai").datetimepicker(
				"option", "maxDate", selectedDate);
		}
	});
});