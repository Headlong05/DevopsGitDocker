FROM node:18

WORKDIR /app

RUN rm -rf node_modules package-lock.json

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "run", "start"]