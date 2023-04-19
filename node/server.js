//
const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');

http.createServer((req, res) => {
    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8" , (err,body) => {
            res.writehead(200, {"Content-Type": "text/html"});
            res.end(body);
         });
    } else if(req.url.match("/sysinfo")) {
      const myHostname = os.hostname();
      const uptimeInSeconds = os.uptime();
      const totalMemoryInBytes = os.totalmem();
      const freeMemoryInBytes = os.freemem();
      const numberOfCPUs = os.cpus().length;



        const secondsInMinute = 60;
        const secondsInHour = secondsInMinute * 60;
        const secondsInDay = secondsInHour * 24;
        //Days,Hours,MIn,Secs calulation above


        const uptimeInDays = Math.floor(uptimeInSeconds / secondsInDay);
        const uptimeInHours = Math.floor((uptimeInSeconds % secondsInDay) / secondsInHour );
        const uptimeInMinutes = Math.floor((uptimeInSeconds % secondsInHour) / secondsInMinute);
        const uptimeInSecondsMod = uptimeInSeconds % secondsInMinute;


        const totalMemoryInMB = (totalMemoryInBytes / (1024 *1024)).toFixed(2);
        const freeMemoryInMB = (freeMemoryInBytes / (1024 * 1024)).toFixed(2);  

              const html= `
                <! DOCTYPE html> 
                <html>
                  <head>
                    <title>Node JS Response</title>
                  </head>
                  <body>
                    <p>Hostname: ${myHostname}</p>
                    <p>IP: ${ip.address()}</p>
                    <p>Server Uptime: ${uptimeInDays} days, ${uptimeInHours} hours,
                    ${uptimeInMinutes} minutes, ${uptimeInSecondsMod} seconds</p> 
                    <p>Total Memory: ${freeMemoryInMB} MB</p>
                    <p>Free Memory: ${freeMemoryInMB} MB</p>
                    <p>Number of CPUs: ${numberOfCPUs} </p>
                    </body>
                </html>`


        res.writeHead(200,  {"Content-Type" : "text/html"});
        res.end(html);
    } else {
        res.writeHead(404, {"Content-TYpe" : "text/plain"});
        res.end(`404 No File was Found at ${req.url}`);
    }
}).listen(3000);
console.log("Server is listenting on port number 3000");
