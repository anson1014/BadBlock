// const map = {"bitch": "beep", "fuck": "yo"}
// // fill this map with your python map
// checkWord = function(word){
//    if(map.hasOwnProperty(word)){
//       //Your replace code here
//       console.log(map[word]);
//    }
// }
// checkWord("bitch");
// checkWord("yo");
// checkWord("fuck");

var json = require('badwordsjson.json')

let badwordset;

var toReplace = $('body').text()

badWordSetAdder = function(word){
   for (var key in json) {
      badwordset.add(key);
   }
   return badwordset
}

wordReplace = function(word){
   switch (word){
      default: return "BLEEP"
      case "fuck*": return "diddle"
      case "fucker": return "diddler"
      case "fucking": return "diddling"
      case "motherfucker": return "mother flubber"
      case "bitch": return "brat"
      case ("nigger"|"nigga"): return "neighbour"
      case ("dick*"|"penis"): return "male genitalia"
      case ("pussy"|"vagina"|"cunt"): return "female genitalia"
      }
   }

phrase_fix = function(text){
   let words = text.split();
   let badwordset = badWordSetAdder(json);
   
   for (let x in badwordset) {
     let badword = words[x];
     if (badwordset.contains(badword)){
       words[x] = wordReplace(badword);
       let new_text = words.join();
     }
   }
   return new_text;
 }


 document.getElementById("butt").addEventListener("click", phrase_fix(toReplace));

