

// function sendEmail() {
//     console.log('sendEmail');
//     emailjs.sendForm('contact_service', 'contact_form', '#main_form');
// } 

// function sendEmail() {
//     console.log('sendEmail');

//     emailjs.sendForm('contact_service', 'contact_form', '#main_form')
//         .then(function (response) {
//             console.log('SUCCESS!', response.status, response.text);
//             alert("Message sent successfully!");
//         }, function (error) {
//             console.log('FAILED...', error);
//         });
// } 


function sendEmail() {
    let name1 = $('#name').val();
    let email1 = $('#email').val();
    let phone1 = $('#phone').val();
    let message1 = $('#message').val();
    let templateParams = {
        name: name1,
        email: email1,
        phone: phone1,
        message: message1
    };

    emailjs.send('contact_service', 'contact_form', templateParams)
        .then(function (response) {
            console.log('SUCCESS!', response.status, response.text);
        }, function (error) {
            console.log('FAILED...', error);
        });
    alert("Message sent successfully!");
    window.location.reload();

}