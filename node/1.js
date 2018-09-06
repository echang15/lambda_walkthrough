const AWS = require('aws-sdk');
const params = {Bucket: 'ec-lamba-test', Key: 'fadetoblack.txt'};
var returndata = "";

exports.handler = (event, context, callback) => {
    var s3 = new AWS.S3({apiVersion: '2006-03-01'});
    
    s3.getObject(params, function(err, data) {
    if (err) console.log(err, err.stack); // an error occurred
     else {
         returndata = Buffer.from(data.Body).toString('utf8');
         const response = {
            statusCode: 200,
            body: returndata
        };
    callback(null, response);
         }// successful response
    });
    
};
