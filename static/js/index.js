$(document).ready(function() {
    setTimeout(function() {
        $("#myAlert").fadeOut("slow", function() {
            $(this).remove();
        });
        
    }, 5000); // 5000 milliseconds = 5 seconds
   
});

