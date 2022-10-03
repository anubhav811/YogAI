var fireBase = fireBase || firebase;
var hasInit = false;
var config = {
    apiKey: "AIzaSyCvhIPeRcsj_OCr6rUIs3OckE4zi3M2rYU",
    authDomain: "yogaspire-60fc9.firebaseapp.com",
    databaseURL: "https://yogaspire-60fc9.firebaseio.com",
    projectId: "yogaspire-60fc9",
    storageBucket: "yogaspire-60fc9.appspot.com",
    messagingSenderId: "512885104040"
  };
if(!hasInit){
    firebase.initializeApp(config);
    hasInit = true;
}



