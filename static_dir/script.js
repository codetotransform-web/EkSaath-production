
$(document).ready(function() {
    
  
    $("#mobNo").keyup(function() {
      var mob = $("#mobNo").val();
      if (mob.length >= 10) {
        $("#mobNo").prop("disabled", true);
        $("#sendOtp").prop("disabled", false);
      }
    });
  
    $("#otp").keyup(function() {
      var otp = $("#otp").val();
      if (otp.length >= 6) {
        $("#otp").prop("disabled", true);
        $("#verifyOtp").prop("disabled", false);
      }
    });
  
   
  
    $("#verifyOtp").click(function() {
      $("#otpVerification").css({
        visibility: "hidden"
      });
      $("#completeSignUp").css({
        visibility: "visible"
      });
    });
  
    
    
    
    
     
      
  });