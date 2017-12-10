db.tweets.mapReduce(
function(){
  if(this.place){
	emit(this.place.country, 1)    
  }else{
	emit( "NULL", 1)
  }
},
function(key, value){
  return Array.sum(value)
},
{
	out: { replace : "nTweetsForCountry" }
}
)
