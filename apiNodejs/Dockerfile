FROM node:10

WORKDIR /user/src/app

RUN npm init -y
RUN npm install express mysql body-parser --save

COPY . .

EXPOSE 3000

CMD [ "node", "server.js" ]