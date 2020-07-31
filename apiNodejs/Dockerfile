FROM node:10

WORKDIR /user/src/app

COPY . .

RUN npm install
RUN npm install -g nodemon

COPY . .

EXPOSE 3000

CMD [ "nodemon", "server.js" ]