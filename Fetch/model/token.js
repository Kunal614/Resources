const mongoose = require("mongoose");
const schema = mongoose.Schema({
  refresh_token: { type: String },
  client_id: { type: String },
  client_secret: { type: String },
  date: { type: Date, default: Date.now() },
  expires_in: { type: Number },
});

const model = mongoose.model("token_store", schema);
module.exports = model;
