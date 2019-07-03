const router = require('express').Router();
const path = require('path');

router.get('/', (req,res) => {
//    res.sendFile(path.join(__dirname,'../frontendWorks/html/uploadFiles.html'));

    vision()
        .then((result)=>{
            res.send(result)
        })

});

function vision(fileType = 0) {
    return new Promise((res, rej) => {
        const spawn = require('child_process').spawn;
        var py;
        py = spawn('python3', [path.join(__dirname, 'pythonScripts/script.py')]);

        py.stdout.on('data', function (data) {
            info = data.toString();
            res(info)
        });

        py.stderr.on('data', (data) => {
            console.log(data.toString());
            console.log("Error occured!");
        });
        py.stdin.end();
    })

}

module.exports.route = router;
