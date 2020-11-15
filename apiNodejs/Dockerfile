FROM node:10

WORKDIR /user/src/app

# Install image dependencies
RUN npm install -g nodemon

# Install project dependencies
COPY package.json .
COPY package-lock.json .
RUN npm install

# Add project
COPY . .

EXPOSE 3000

CMD [ "nodemon", "server.js" ]
