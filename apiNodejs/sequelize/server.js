const { Sequelize } = require('sequelize');
const init = require("../models/init-models");

async function connect() {
    const sequelize = new Sequelize('mydb', 'root', 'root', {
    host: 'localhost',
    port: 3360,
    dialect: 'mysql',
    });

    try {
        await sequelize.authenticate();
            console.log('Connection has been established successfully.');
            await sequelize.sync({ force: true });
                console.log("All models were synchronized successfully.");
        } catch (error) {
            console.error('Unable to connect to the database:', error);
    }
}

connect();