

let isRecording = false
let mainPhrase = "FBI agent, check your records to answer us                                                           "
let phraseArray = mainPhrase.split("")
let newPhrase =  ""
let secretResponse = []
let answer =""



function showAnswer(){



  answer = answer.replace(".", "")
  document.getElementById("answerHolder").innerHTML = "According to my records here is the answer: " + answerx
  document.getElementById("answerHolder").style.display = "block"
}


function secretText(){


  let nextLetter = phraseArray.shift()
  console.log(nextLetter)
  newPhrase = newPhrase + nextLetter
  document.getElementById('petition').value = newPhrase
}


document.onkeypress = function (e) {
    e = e || window.event
  console.log("typed " + e.key)

  if(document.activeElement.id == "petition"){
   console.log("..... "+ e.key)

   if(e.key == "." && isRecording == false){
     isRecording = true
     console.log("Begin....")
   } else if(e.key == "." && isRecording == true){
     isRecording = false
     console.log("End...")
   }

   if(isRecording == true){
     secretResponse.push(e.key)
     answer = answer+ e.key
     console.log("answer >> " +  answer)
     document.getElementById("answerHolder").innerHTML = answer


   }





  }


};
