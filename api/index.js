const express = require('express')
const bodyParser = require('body-parser')
const methodOverride = require('method-override')

const mongoose = require('mongoose')
const restify = require('express-restify-mongoose')

const app = express()
const router = express.Router()

app.use(bodyParser.json())
app.use(methodOverride())

mongoose.connect('mongodb://192.168.99.100:27017/Twitter')
// schema Full Tweet
var Tweet = new mongoose.Schema({any: [mongoose.Schema.Types.Mixed] }, {"strict": false })
restify.serve(router, mongoose.model('tweets', Tweet ));

// schema Test_Tweets
var TextTweet = new mongoose.Schema({ text:String, user: String})
// no se aceptan mayusculas en el nombre de las colecciones
// el nombre de las colleciones son plurales, name{s}, vegetale{s}
restify.serve(router, mongoose.model('tweetbasics', TextTweet ));

app.use(router)


app.listen(3000, () => {
  console.log('Express server listening on port 3000')
})