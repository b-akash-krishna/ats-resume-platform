FROM node:18-alpine

WORKDIR /app

# Copy root-level package files
COPY package*.json ./

# Install dependencies ignoring peer conflicts
RUN npm install --legacy-peer-deps

# Copy the rest of the project (since your frontend is in root)
COPY . .

# Expose the port
EXPOSE 3000

# Run Vite dev server accessible to host
CMD ["npm", "run", "dev", "--", "--host"]
