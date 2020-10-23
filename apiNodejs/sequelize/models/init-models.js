var DataTypes = require("sequelize").DataTypes;
var _customers = require("./customers");
var _users = require("./users");

function initModels(sequelize) {
  var customers = _customers(sequelize, DataTypes);
  var users = _users(sequelize, DataTypes);

  return {
    customers,
    users,
  };
}
module.exports = { initModels };
