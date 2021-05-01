const mongoose = require("mongoose");
const schema = mongoose.Schema({
  access_token:{type:String},
  refresh_token: { type: String },
  time: { type: Date, default: Date.now() },
  expires_in: { type: Number },
},{
  collection:'base_tokenstuff'
});

const model = mongoose.model("token_store", schema);
module.exports = model;
