const router = require('express').Router();
const path = require('path');
const usersdb = require('../mongo/mongomodel').models.users

router.get('/', (req,res) => {
    res.sendFile(path.join(__dirname,'../frontendWorks/html/signIn.html'));
});

router.get('/signUp', (req,res) => {
    res.sendFile(path.join(__dirname,'../frontendWorks/html/signUp.html'));
});

router.post('/signin', (req, res) => {
    usersdb.signInVerify({
        username : req.body.username
    })
        .then((data) => {
            console.log(data)
            if(data.pw === req.body.pw){
                res.send({
                    data: data
                })
                console.log('User Logged In')
            }
        })
        .catch((err) => {
            console.error(err)
        })
})

router.post('/signup', (req, res) => {
    usersdb.createNew({
        username : req.body.username,
        pw : req.body.pw,
        email : req.body.email
    })
        .then(() => {
            res.send({data:'done'});
            console.log('User Created Successfully')
        })
        .catch((err) => {
            console.error(err)
        })
})

module.exports.route = router;