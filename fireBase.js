var fireBase = fireBase || firebase;
var hasInit = false;
var config = {
  apiKey: "AIzaSyAD0WRHdv59LTZS9VfIRs2H5AB3XN6kCHg",
  authDomain: "yogai-cc884.firebaseapp.com",
  projectId: "yogai-cc884",
  storageBucket: "yogai-cc884.appspot.com",
  messagingSenderId: "813527456400",
  appId: "1:813527456400:web:2331953f7beb23955f5615",
  measurementId: "G-QMEKS1L1M4",
};
if (!hasInit) {
  firebase.initializeApp(config);
  hasInit = true;
}
