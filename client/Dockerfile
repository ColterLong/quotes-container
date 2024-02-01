# https://stackoverflow.com/questions/56497356/how-to-proxy-vue-client-to-express-server-running-in-docker-containers
# build stage
FROM node:21.6-alpine3.19 as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# production stage
FROM nginx:1.25.3-alpine3.18 as production-stage
COPY ./nginx.conf /etc/nginx/nginx.conf
ARG API_URL
RUN sed -i "s/API_URL/$API_URL/g" /etc/nginx/nginx.conf
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]