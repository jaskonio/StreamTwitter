db.tweets.aggregate(

	// Pipeline
	[
		// Stage 1
		{ $limit: 10},

		// Stage 2
		{
			$project: {
			    "_id" : 1,
			  	text: 1,
				user : "$user.screen_name",
				created_at : "$created_at",
				timestamp_ms : "$timestamp_ms",
				"@timestamp" : "$timestamp"
			}
		},

		// Stage 3
		{
			$out: "tweetbasics"
		},

	]

	// Created with Studio 3T, the IDE for MongoDB - https://studio3t.com/

);
