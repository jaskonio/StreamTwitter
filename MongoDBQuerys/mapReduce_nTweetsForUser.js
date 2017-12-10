
db.tweets.mapReduce(
function(){
  if(this.place){
	emit(this.user.screen_name, 1)
  }
  else{emit("null", 1)}
},
function(key, value){
  return Array.sum(value)
},
{
	out: { replace : "nTweetsForCountry" },
	out: { "inline" : 1},
	//limit:100
}
)
