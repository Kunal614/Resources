require("dotenv").config();
const redis = require("redis");
const { promisify } = require("util");

let client = redis.createClient({
    port: 17051,
    host: "redis-17051.c257.us-east-1-3.ec2.cloud.redislabs.com",
    password: process.env.PASS,
});
const getAsync = promisify(client.get).bind(client);
const express = require("express");
const bodyParser = require("body-parser");

const app = express();
app.use(bodyParser.json());

const { google } = require("googleapis");

const oacth2client = new google.auth.OAuth2(
    process.env.CLIENT_ID,
    process.env.CLIENT_SECRET,
    process.env.REDIRECT_URI
);

oacth2client.setCredentials({ refresh_token: process.env.REFRESH_TOKEN });

const drive = google.drive({
    version: "v3",
    auth: oacth2client,
});

app.get("/getfiles/:id", async(req, res) => {
    try {
        var fileId = req.params.id;

        const info = await getAsync(fileId);

        // if (info) {
        //   res.send(JSON.parse(info));
        //   return;
        // }

        console.log("here");
        const response = await drive.files.list({
            includeRemoved: false,
            spaces: "drive",
            fileId: fileId,
            fields: "nextPageToken, files(id, name, parents, mimeType, modifiedTime)",
            q: `'${fileId}' in parents`,
        });
        let data = [];

        for (fileData of response.data.files) {
            await drive.permissions.create({
                fileId: fileData.id,
                requestBody: {
                    role: "reader",
                    type: "anyone",
                },
            });

            const result = await drive.files.get({
                fileId: fileData.id,
                fields: "thumbnailLink, webViewLink, webContentLink",
            });

            if (Object.keys(result.data).length == 3) {
                data.push({
                    downloadUrl: result.data.webContentLink,
                    onlineViewLink: result.data.webViewLink,
                    thumbnailLink: result.data.thumbnailLink,
                });
            }
        }
        client.set(fileId, JSON.stringify(data));
        res.send(data);
    } catch (error) {
        res.send(error.message);
    }
});

app.get("/updatecache/:id", (req, res) => {
    var fileId = req.params.id;
    client.del(fileId);
    res.send({ success: true });
});

app.listen("3000", () => {
    console.log("server on");
});