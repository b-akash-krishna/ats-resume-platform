FROM node:18-alpine

WORKDIR /app

COPY package*.json ./

# Install dependencies including devDependencies
RUN npm install --legacy-peer-deps

COPY . .

EXPOSE 5173

# Use npx to run local vite
CMD ["./node_modules/.bin/vite", "--host", "0.0.0.0"]
