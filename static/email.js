(function() {
    // https://dashboard.emailjs.com/admin/integration
    emailjs.init('user_QQaNYH9BQkbKmcH9EGzMG');
})();

function sendEmail(){
    console.log('sendEmail');
    
    emailjs.sendForm('contact_service', 'contact_form', '#main_form')
    .then(function(response) {
       console.log('SUCCESS!', response.status, response.text);
    }, function(error) {
       console.log('FAILED...', error);
    });
}

