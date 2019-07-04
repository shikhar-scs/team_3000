const express = require('express');
const config = require('./config.json');
const bodyParser = require('body-parser');
const path = require('path');
const app = express();
const fs = require('fs');
const fileupload = require('express-fileupload');
const router = require('express').Router();
const http = require('http')


const routes = {
//    login: require('./api/login').route,
//    dashboard: require('./api/dashboard').route,
    python: require('./api/python').route
    // csvfiles: require('./api/csvfiles').route
};

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:true}));

//app.use('/login', routes.login);
//app.use('/dashboard', routes.dashboard);
app.use('/python', routes.python);
// app.use('/csvfiles', routes.csvfiles);


app.use(express.static(path.join(__dirname,'/frontend')));

app.get('/postal',(req,res)=>{
    res.sendFile(path.join(__dirname+'/frontend/index.html'));
});


app.get('/uber',(req,res)=>{
    res.sendFile(path.join(__dirname+'/frontend/uber.html'));
});

//app.get('/home',(req,res)=>{
//    res.sendFile(__dirname+'/frontendWorks/html/uploadFiles.html');
//});

app.use(fileupload());
app.post('/fileupload', (req, res) => {
    // console.log(req);
  if (!req.files)

    return res.status(400).send('No files were uploaded.');

  const sampleFile = req.files.sampleFile;
  const name = sampleFile.name;

  sampleFile.mv(__dirname + '/api/csvFiles/' + name, function(err) {
    if (err)
      return res.status(500).send(err);
    else{
        res.redirect('/python')
    }
  });
});

app.use((req,res)=> res.status(404).send('page not found'));

app.listen( process.env.PORT || config.SERVER.PORT ,
    ()=> {
        console.log("Server started at http://localhost:" +config.SERVER.PORT + "/postal")
        console.log("Server started at http://localhost:" +config.SERVER.PORT + "/uber")});
