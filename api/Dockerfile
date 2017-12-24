FROM node:carbon

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY app/package*.json ./

RUN npm install
# If you are building your code for production
# RUN npm install --only=production

COPY app/* ./

EXPOSE 3000
CMD [ "npm", "start" ]

## create image
## docker build -t Tracking-twiter-api:0.1 .
## docker run --name Tracking-twiter-api -dit -p 3000:3000 --link Tracking-mongo tracking-twiter-api:0.1
## docker logs -f tracking-twiter-api
