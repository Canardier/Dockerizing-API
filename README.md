# API CONTAINERIZING

# START
Go to apiNodejs and run `npm install`<br>

# COMPOSE
Run `docker-compose up --build -d` at the root folder

# SEQUELIZE AUTO
<a>https://github.com/sequelize/sequelize-auto</a>
In the apiNodejs repository use this cmd:<br>
Linux: `sequelize-auto -o "./models" -d mydb -h localhost -u root -p 3360 -x root -e mysql`<br>
WINDOWS: `.\node_modules\.bin\sequelize-auto -o ".\app\migration\" -d mydb -h localhost -u root -p 3360 -x root -e mysql`<br>

# ROUTE
folder coming soon

# SEQUELIZE API
<a>https://sequelize.org/</a>