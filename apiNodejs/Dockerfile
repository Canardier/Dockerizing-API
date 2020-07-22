FROM node:10

WORKDIR /user/src/app

RUN npm init -y --save
RUN npm install express mysql body-parser --save
RUN npm install -g nodemon --save
RUN npm install

COPY . .

EXPOSE 3000

CMD [ "nodemon", "server.js" ]