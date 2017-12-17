import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-tweets',
  templateUrl: './tweets.component.html',
  styleUrls: ['./tweets.component.css']
})

export class TweetsComponent {
  tweets;
  limitTweets = 20;
  // host = '192.168.99.100:3000';
   host = 'localhost:3000';
   timestamp_ms;
   time = 0;
   timeInterval = 10000;
  constructor(private http: HttpClient) {
    this.rawTweets();
    setInterval(() => { this.rawTweets(); }, this.timeInterval);

  }

  rawTweets () {
    let time = this.getTimeStampms();
    let url = `http://${this.host}/api/v1/tweetbasics?query={"timestamp_ms":{"$gte":"${time}"}}`;
    this.http.get(url).subscribe(res => {
      console.log(url);
      console.log(typeof(this.tweets));
      console.log(this.tweets);
      if ( typeof(this.tweets) === 'undefined') {
        this.tweets = res;
      }else {
        res.map( x => this.tweets.push(x));
      }
      this.tweets.sort(this.compare).reverse();
      console.log(res);
    });
  }
  compare(a, b) {
    if ( a.timestamp_ms < b.timestamp_ms) {
      return -1;
    }
    if (a.timestamp_ms > b.timestamp_ms) {
      return 1;
    }
    return 0;
  }

  getTimeStampms(){
    let timeStampInMs = window.performance && window.performance.now && window.performance.timing && window.performance.timing.navigationStart ? window.performance.now() + window.performance.timing.navigationStart : Date.now();
    return timeStampInMs;
  }
}

// create array of object
// let userTestStatus: { id: number, name: string }[] = [
