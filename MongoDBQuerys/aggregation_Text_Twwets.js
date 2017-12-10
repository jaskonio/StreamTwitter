db.tweets.aggregate(

	// Pipeline
	[
		// Stage 1
		//{
			//$limit: 1000
		//},

		// Stage 2
		{
			$project: {
			    "_id" : 1,
			  	text: 1,
				user : "$user.screen_name"
			}
		},

		// Stage 3
		{
			$out: "text_Tweets"
		},

	]

	// Created with Studio 3T, the IDE for MongoDB - https://studio3t.com/

);
