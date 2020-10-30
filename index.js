'use strict'

const express = require('express')
const { spawn } = require('child_process')

const app = express()
const PORT = 3000;

app.get('/', (req, res) => {

    var pyData = [];

    const python = spawn('python', ['genCaptcha.py']);
    python.stdout.on('data', data => {
        console.log('Pipe data from python script ...');
        pyData.push(data)
        console.log(pyData)
    });

    python.on('close', (code) => {
        console.log(`child process close all stdio with code ${code}`);
        // send data to browser
        res.send(pyData.join(""))
    });
});

app.listen(PORT, () => {
    console.log(`Server listening on ${PORT}`)
})