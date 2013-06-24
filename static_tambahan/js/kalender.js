$(function(){
	$("#id_mulai").datetimepicker({
		timeFormat: 'H:m:s',
		dateFormat: 'yy-mm-dd',
		timeText: "Waktu",
		hourText: "Jam",
		showMinute: 0,
		showSecond: 0,
		onClose: function( selectedDate ) {
			$("#id_selesai").datetimepicker( 
				"option", "minDate", selectedDate);

		} 
	});
	$("#id_selesai").datetimepicker({
		timeFormat: 'H:m:s',
		dateFormat: 'yy-mm-dd',
		timeText: "Waktu",
		hourText: "Jam",
		showMinute: 0,
		showSecond: 0,
		onClose: function( selectedDate ) {
			$("#id_mulai").datetimepicker(
				"option", "maxDate", selectedDate);
		}
	});
});