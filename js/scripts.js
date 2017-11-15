$(document).ready(function() {
	
	$('#map').usmap({
	    'stateStyles': {fill: '#f2f2f2', stroke: '#fff'},
	    'stateHoverStyles': {fill: 'red'},
	    'clickState': {
	      'NY' : function(event, data) {
	        $('#alert p b').text('New York');
	      }
	    }
	});
	$('.sec-5 input[value="1"]').click(function(){
		$("#car-1").attr("src","images/traveling_over.png");
		$("#car-2").attr("src","images/working.png");
		$("#car-3").attr("src","images/commuting.png");
		$("#car-4").attr("src","images/racing.png");
		$("#car-5").attr("src","images/leisure.png");
	});
	$('.sec-5 input[value="2"]').click(function(){
		$("#car-1").attr("src","images/traveling.png");
		$("#car-2").attr("src","images/working_over.png");
		$("#car-3").attr("src","images/commuting.png");
		$("#car-4").attr("src","images/racing.png");
		$("#car-5").attr("src","images/leisure.png");
	});
	$('.sec-5 input[value="3"]').click(function(){
		$("#car-1").attr("src","images/traveling.png");
		$("#car-2").attr("src","images/working.png");
		$("#car-3").attr("src","images/commuting_over.png");
		$("#car-4").attr("src","images/racing.png");
		$("#car-5").attr("src","images/leisure.png");
	});
	$('.sec-5 input[value="4"]').click(function(){
		$("#car-1").attr("src","images/traveling.png");
		$("#car-2").attr("src","images/working.png");
		$("#car-3").attr("src","images/commuting.png");
		$("#car-4").attr("src","images/racing_over.png");
		$("#car-5").attr("src","images/leisure.png");
	});
	$('.sec-5 input[value="5"]').click(function(){
		$("#car-1").attr("src","images/traveling.png");
		$("#car-2").attr("src","images/working.png");
		$("#car-3").attr("src","images/commuting.png");
		$("#car-4").attr("src","images/racing.png");
		$("#car-5").attr("src","images/leisure_over.png");
	});

	$('#n-1').click(function(){
		$('.sec-1').addClass('display-n');
		$('.sec-2').removeClass('display-n');
	});
	$('#n-2').click(function(){
	    $('.sec-2').addClass('display-n');
        $('.sec-3').removeClass('display-n');
		$.ajaxSetup({
            contentType: "application/json; charset=utf-8"
        });
        var driving_style = document.getElementById('driving_style').value;
        var data = JSON.stringify({
            driving_style: `${driving_style}`
        });
        $.ajax({
            url: '/driving_style',
            type: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            data: data,
            success: function(response){
                alert(response.age)
            }
        })
	});
	$('#n-3').click(function(){
		$('.sec-3').addClass('display-n');
		$('.sec-4').removeClass('display-n');
	});
	$('#n-4').click(function(){
		$('.sec-4').addClass('display-n');
		$('.sec-5').removeClass('display-n');
	});
});
window.onload = function() {
  var input = document.querySelector('input[type=range]'),
    style_el = document.createElement('style'),
    styles = [],
    track_sel = ['::-webkit-slider-runnable-track'];
  document.body.appendChild(style_el);

  styles.push('');

  input.addEventListener('input', function() {
    var min = this.min || 0,
      max = this.max || 100,
      c_style, u, edge_w, val, str = '';

    this.setAttribute('value', this.value);

    val = this.value + '% 100%';
    str += 'input[type="range"]' + track_sel[0] + '{background-size:' + val + '}';

    styles[0] = str;
    style_el.textContent = styles.join('');
  }, false);
}

 /*
     * Replace all SVG images with inline SVG
     */
        jQuery('img.svg').each(function(){
            var $img = jQuery(this);
            var imgID = $img.attr('id');
            var imgClass = $img.attr('class');
            var imgURL = $img.attr('src');

            jQuery.get(imgURL, function(data) {
                // Get the SVG tag, ignore the rest
                var $svg = jQuery(data).find('svg');

                // Add replaced image's ID to the new SVG
                if(typeof imgID !== 'undefined') {
                    $svg = $svg.attr('id', imgID);
                }
                // Add replaced image's classes to the new SVG
                if(typeof imgClass !== 'undefined') {
                    $svg = $svg.attr('class', imgClass+' replaced-svg');
                }

                // Remove any invalid XML tags as per http://validator.w3.org
                $svg = $svg.removeAttr('xmlns:a');

                // Replace image with new SVG
                $img.replaceWith($svg);

            }, 'xml');

        });