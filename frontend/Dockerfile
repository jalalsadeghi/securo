FROM node:20-alpine

WORKDIR /app

COPY ./frontend/src/package.json ./frontend/src/package-lock.json ./

RUN npm install

COPY ./frontend/src ./

RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
