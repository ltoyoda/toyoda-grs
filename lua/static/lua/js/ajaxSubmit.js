//File part of poi_list_amir
// Use this file to calculate distances from the study area using forms


$(document).ready(function(){
	var isr = 'No area is selected.';
	$("#checkdata").click(function(){
		var valid = '';
		var buttonId = 'checkdata';
		var field1 = $("#field1").val();
		var field2 = $("#field2").val();
		var field3 = $("#field3").val();
		var field4 = $("#field4").val();
		if ( field1.length < 1 || field2.length < 1 || field3.length < 1 || field4.length < 1 ) {
			valid += '<br />'+isr;
		}
		if ( valid != '' ) {
			$("#response1").fadeIn("slow");
			$("#response1").html("Error:"+valid);
		} else {

			var datastr1 = '&field1=' + field1 + '&field2=' + field2 + '&field3=' + field3 +
			               '&field4=' + field4 + '&buttonId' + buttonId;
			$("#response1").css("display", "block");
			$("#response1").html("Checking data... ");
			$("#response1").fadeIn("slow");

			$.ajax({
				type: "POST",
				url: "HeaderData.php",
				data: datastr1,
				cache: false,
				success: function(html){
					$("#response1").fadeIn("slow");
					$("#response1").html(html);
				}
			});
		}
		return false;
	});
	$("#getweather").click(function(){
		var valid = '';
        var field5 = $("#field1").val();
        var field6 = $("#field2").val();
        var field7 = $("#field3").val();
        var field8 = $("#field4").val();
		var meas_freq = $('input[name=meas_freq]:checked').val();

        var checked_params = 'dummy';
        $('.selector:checked').each(function(){
			checked_params = checked_params+','+$(this).val();
        });

        var sensor_sel = $('input:radio[name=sensor_sel]:checked').val();
        var pass_sel   = $('input:radio[name=pass_sel]:checked').val();


		if ( field5.length < 1 || field6.length < 1 || field7.length < 1 || field8.length < 1 ) {
			valid +=  '<br />'+isr;
        }
        if ( valid != '' ) {
			$("#response2").fadeIn("slow");
            $("#response2").html("Error:"+valid);
		} else {
			var datastr2 = '&field5=' + field5 + '&field6=' + field6 + '&field7=' + field7 +
			               '&field8=' + field8 + '&meas_freq=' + meas_freq + '&checked_params=' +
						    checked_params + '&sensor_sel=' + sensor_sel + '&pass_sel=' + pass_sel;

            $("#response2").css("display", "block");
            $("#response2").html("Please wait...");
            $("#response2").fadeIn("slow");

			$.ajax({
				type: "POST",
				url: "Weather.php",
				data: datastr2,
                cache: false,
                success: function(html){
					$("#response2").fadeIn("slow");
					$("#response2").html(html);
                }
			});
		}
		return false;
    });
	$("#downloadpara").click(function(){
		var valid = '';
		var field5 = $("#field1").val();
		var field6 = $("#field2").val();
		var field7 = $("#field3").val();
		var field8 = $("#field4").val();
        var sensor_sel = $('input:radio[name=sensor_sel]:checked').val();
        var pass_sel   = $('input:radio[name=pass_sel]:checked').val();

		if ( field5.length < 1 || field6.length < 1 || field7.length < 1 || field8.length < 1 ) {
			valid += '<br />'+isr;
		}
		if ( valid != '' ) {
			$("#response3").fadeIn("slow");
			$("#response3").html("Error:"+valid);
		} else {
			var datastr3 = '&field5=' + field5 + '&field6=' + field6 + '&field7=' + field7 +
			               '&field8=' + field8 + '&sensor_sel=' + sensor_sel + '&pass_sel=' + pass_sel;

			$("#response3").css("display", "block");
			$("#response3").html("setting parameters... ");
			$("#response3").fadeIn("slow");

			$.ajax({
				type: "POST",
				url: "Parameter.php",
				data: datastr3,
				cache: false,
				success: function(html){
					$("#response3").fadeIn("slow");
					$("#response3").html(html);
				}
			});
		}
		return false;
	});
});

function displayCheckBox(TextBoxId)
        {
            var objElement = document.getElementById(TextBoxId);
			TextBoxId.style.display = 'block';
			TextBoxId.style.visibility = 'visible';
        }

		function hideCheckBox(TextBoxId)
		{
			var objElement = document.getElementById(TextBoxId);
			TextBoxId.style.display = 'none';
			TextBoxId.style.visibility = 'hidden';
		}

function checkAll(checkEm,TagName) {
    var cbs = document.getElementsByTagName('*');
    for (var i = 0; i < cbs.length; i++) {
        if (cbs[i].type == 'checkbox') {
            if (cbs[i].name == TagName) {
                cbs[i].checked = checkEm;
            }
        }
    }
}
function disableRadio(RadioID,el) {
   i = 0;
   while ( RadioID[i] ) {
      document.getElementById(RadioID[i]).disabled = el;
   i++;
   }
}