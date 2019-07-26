// $( document ).ready(function() { //required for jQuery to work
//
// //all javascript and jquery code here
//
// }); //required for jQuery to work
//import firebase from 'firebase';
//const firebaseApp = firebase.initializeApp(fbconfig);

function login(){
  var userEmail = document.getElementById("email_field").value;
  var userPass = document.getElementById("password_field").value;


  firebase.auth().signInWithEmailAndPassword(userEmail, userPass).catch(function(error) {
    // Handle Errors here.
    var errorCode = error.code;
    var errorMessage = error.message;

    window.alert("Error : " + errorMessage);
    // ...
  });
}

firebase.auth().onAuthStateChanged(function(user) {
  if (user) {
    // User is signed in.

    document.getElementById("logout_div").style.display = "block";
    document.getElementById("login_div").style.display = "none";

    var user = firebase.auth().currentUser;

    if(user != null){
      var email_id = user.email;
      document.getElementById("user_para").InnerHTML = "Welcome User: " + email_id;
    }
  } else {
    // No user is signed in.
    document.getElementById("logout_div").style.display = "none";
    document.getElementById("login_div").style.display = "block";
  }
});


function logout(){
  firebase.auth().signOut();
  window.alert("You have signed out");
}
