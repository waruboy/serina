$(function(){
	$("#id_awal").datetimepicker({
		timeFormat: 'H:m:s',
		dateFormat: 'yy-mm-dd',
		timeText: "Waktu",
		hourText: "Jam",
		showMinute: 0,
		showSecond: 0,
		onClose: function( selectedDate ) {
			$("#id_akhir").datetimepicker( 
				"option", "minDate", selectedDate);

		} 
	});
	$("#id_akhir").datetimepicker({
		timeFormat: 'H:m:s',
		dateFormat: 'yy-mm-dd',
		timeText: "Waktu",
		hourText: "Jam",
		showMinute: 0,
		showSecond: 0,
		onClose: function( selectedDate ) {
			$("#id_awal").datetimepicker(
				"option", "maxDate", selectedDate);
		}
	});
});