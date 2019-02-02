var express = require('express');
var app = express();

var PythonShell = require('python-shell');

var run = schedule.scheduleJob('00 * * * *', PythonShell.run('twitterbot.py', function (err) {
  console.log('finished');
}));