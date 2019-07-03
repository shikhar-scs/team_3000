const router = require('express').Router();
const path = require('path');

router.get('/', (req,res) => {
    res.sendFile(path.join(__dirname,'../frontendWorks/html/dbindex.html'));
});

router.get('/uploadFiles', (req,res) => {
    res.sendFile(path.join(__dirname,'../frontendWorks/html/uploadFiles.html'));
});

router.get('/uploadImages', (req,res) => {
    res.sendFile(path.join(__dirname,'../frontendWorks/html/uploadImages.html'));
});

router.get('/matches', (req,res) => {
    res.sendFile(path.join(__dirname,'../frontendWorks/html/matches.html'));
});

router.get('/classesToday', (req,res) => {
    res.sendFile(path.join(__dirname,'../frontendWorks/html/classesToday.html'));
});


module.exports.route = router;