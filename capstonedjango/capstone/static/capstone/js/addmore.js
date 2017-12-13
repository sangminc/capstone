before = 0;
counter = 1;

jQuery(document).ready(function () {
    $("#add-another").click(function() {
    	
    	counter++;
    	before++;
    	
    	//item = $('<div id="select_'+counter+'></div');
    	item = $('<br><select class="btn btn-primary dropdown-toggle my-2" id="select_'+counter.toString()+'" data-target-id='+counter.toString()+' onchange="setNameVal(this)">' + 
    		'<option class="dropdown-item" value="-1">--Choose an option--</option>' +
    		'<option class="dropdown-item" value="1">1. Employee Readiness</option>' +
    		'<option class="dropdown-item" value="2">2. Customer Satisfaction</option>' +
    		'<option class="dropdown-item" value="3">3. Employee Engagement</option>' +
    		'<option class="dropdown-item" value="4">4. Knowledge Management</option>'+
    		'<option class="dropdown-item" value="5">5. Technology and Resource Availability</option>'+
    		'<option class="dropdown-item" value="6">6. Technology and Resource Scalability</option>'+
    		'<option class="dropdown-item" value="7">7. Training</option>'+
    		'<option class="dropdown-item" value="8">8. Leadership</option>'+
    		'<option class="dropdown-item" value="9">9. Productivity</option>'+
    		'</select>'+
    		'<input id="input_'+counter.toString()+'" class="form-control" type=text style="width:60%;" />');
    	item.insertAfter('#input_'+before.toString());
    	$('#counter').val(counter);

    	if (counter >= 9) {
    	$('#add-another').attr("disabled", "disabled");
    	}
    });

    
});


function setNameVal(dom){
	var id = "#select_"+ $(dom).data("target-id");
	var inputid = $(dom).data("target-id");

        if ($('select option[value="' + $(dom).val() + '"]:selected').length > 1)
        {
            $(dom).val(-1).change();
            alert('You have already selected this kpi - please choose another.')
        }
        else
        {
        	//console.log('#'+event.target.id+ ' input');
        	//var id = '#'+event.target.id+ ' input';
        	element = $('#input_'+ inputid);
        	//element = $('#input_'+counter.toString());
        	element.attr('name', 'kpi_'+$(dom).val());
        }

}
