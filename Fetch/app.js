require("dotenv").config();
const redis = require("redis");
const mongoose = require("mongoose");
const TokenStore = require("./model/token");
const port = process.env.PORT || 3000;
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
const { default: axios } = require("axios");

const oacth2client = new google.auth.OAuth2(
  process.env.CLIENT_ID,
  process.env.CLIENT_SECRET,
  process.env.REDIRECT_URI
);

const drive = google.drive({
  version: "v3",
  auth: oacth2client,
});

async function fetchNewToken(tkn) {
  console.log('generating new token...');
  const token = await axios.post("https://oauth2.googleapis.com/token", {
    client_id: process.env.CLIENT_ID,
    client_secret: process.env.CLIENT_SECRET,
    refresh_token: tkn,
    grant_type: "refresh_token"  
  });

  return token.data;
}

async function checkToken() {
  const data = await TokenStore.findOne({});
  // console.log(data);

  if (!data || Object.keys(data).length === 0) {
    const token = await fetchNewToken(process.env.REFRESH_TOKEN);

    let new_token = new TokenStore({
      client_id: process.env.CLIENT_ID,
      client_secret: process.env.CLIENT_SECRET,
      expires_in: token.expires_in,
      refresh_token: token.access_token,
    });

    await new_token.save();
  } else if (Date.now() - Date.parse(data.date) > data.expires_in * 1000) {
    const token = await fetchNewToken(process.env.REFRESH_TOKEN);
    data.refresh_token = token.access_token;
    data.date = Date.now();
    data.expires_in = token.expires_in;
    await data.save();
    oacth2client.setCredentials({ refresh_token: token.access_token });
  } else {
    oacth2client.setCredentials({ refresh_token: data.refresh_token });
  }
}

app.get("/getfiles/:id", async (req, res) => {
  try {
    var fileId = req.params.id;

    const info = await getAsync(fileId);

    if (info) {
      res.send(JSON.parse(info));
      return;
    }

    console.log("here");
    await checkToken();

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
        fields: "name, webViewLink, webContentLink",
      });

      if (Object.keys(result.data).length == 3) {
        data.push({
          downloadUrl: result.data.webContentLink,
          onlineViewLink: result.data.webViewLink,
          name: result.data.name,
        });
      }
    }
    client.set(fileId, JSON.stringify(data));
    res.send(data);
  } catch (error) {
    res.send(error);
  }
});

app.get("/updatecache/:id", (req, res) => {
  var fileId = req.params.id;
  client.del(fileId);
  res.send({ success: true });
});


mongoose.connect(
  process.env.MONGO_URL,
  {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  },
  (err, res) => {
    if (!err) {
      app.listen(port, () => {
        console.log("server on");
      });
    }
  }
);
