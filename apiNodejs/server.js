const { Sequelize } = require('sequelize');
const init = require("./app/migration/init-models");
const express = require("express");
const bodyParser = require("body-parser");

const app = express();

// parse requests of content-type: application/json
app.use(bodyParser.json());

// parse requests of content-type: application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: true }));

// simple route
app.get("/", (req, res) => {
  res.json({ message: "Welcome to your api." });
});


require("./app/routes/customers.route.js")(app)

/*TODO for add sequelize connection*/
async function connect() {
  const sequelize = new Sequelize('mydb', 'root', 'root', {
      host: 'localhost',
      port: 3306,
      dialect: 'mysql',
  });
  
  try {
      await sequelize.authenticate();
      console.log('Connection has been established successfully.');
      await init.initModels(sequelize);
      await sequelize.sync({}); //force:true to drop and create
      console.log("All models were synchronized successfully.");
  } catch (error) {
      console.error('Unable to connect to the database:', error);
  }
}

// set port, listen for requests
app.listen(3000, () => {
  console.log("Server is running on port 3000.");
});