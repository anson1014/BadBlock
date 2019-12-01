const map = {"bitch": "beep", "fuck": "yo"}
// fill this map with your python map
checkWord = function(word){
   if(map.hasOwnProperty(word)){
      //Your replace code here
      console.log(map[word]);
   }
}
checkWord("bitch");
checkWord("yo");
checkWord("fuck");
