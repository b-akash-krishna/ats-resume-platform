FROM node:18-alpine

WORKDIR /app

COPY package*.json ./

# Install dependencies including devDependencies
RUN npm install --legacy-peer-deps

# Install vite globally
RUN npm install -g vite

COPY . .

EXPOSE 5173

CMD ["vite", "--host", "0.0.0.0"]