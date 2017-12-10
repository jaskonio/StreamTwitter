
db.tweets.aggregate([
	{
	   $limit: 10
	},
	{
		$project:{
			_id :0,
			"id" : "$user.id",
"friends_count" : "$user.friends_count",
"profile_image_url_https" : "$user.profile_image_url_https",
"profile_background_image_url" : "$user.profile_background_image_url",
"favourites_count" : "$user.favourites_count",
"description" : "$user.description",
"created_at" : "$user.created_at",
"protected" : "$user.protected",
"screen_name" : "$user.screen_name",
"profile_link_color" : "$user.profile_link_color",
"geo_enabled" : "$user.geo_enabled",
"profile_background_color" : "$user.profile_background_color",
"profile_text_color" : "$user.profile_text_color",
"verified" : "$user.verified",
"profile_image_url" : "$user.profile_image_url",
"time_zone" : "$user.time_zone",
"url" : "$user.url",
"followers_count" : "$user.followers_count",
"profile_use_background_image" : "$user.profile_use_background_image",
"name" : "$user.name",
"location" : "$user.location"


		}
	},
	{
	  $out : "user"
	}
])
