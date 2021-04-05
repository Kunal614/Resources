require("dotenv").config();

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

app.post("/getfiles", async (req, res) => {
  try {
    var fileId = req.body.id;
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
    res.send(data);
  } catch (error) {
    res.send(error.message);
  }
});

app.listen("3000", () => {
  console.log("server on");
});
