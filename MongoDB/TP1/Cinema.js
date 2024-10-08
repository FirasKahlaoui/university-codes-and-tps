require('dotenv').config();
const { MongoClient } = require('mongodb');

const uri = process.env.MONGODB_URI;
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

async function run() {
  try {
    await client.connect();
    const database = client.db('cinema');
    const collection = database.collection('movies');

    // Create a new collection called movies if it doesn't exist
    await database.createCollection('movies');

    // Insert sample data into the movies collection
    await collection.insertMany([
      {
        title: "Inception",
        director: "Christopher Nolan",
        year: 2010,
        genres: ["Action", "Sci-Fi", "Thriller"]
      },
      {
        title: "The Matrix",
        director: "Lana Wachowski, Lilly Wachowski",
        year: 1999,
        genres: ["Action", "Sci-Fi"]
      },
      {
        title: "Interstellar",
        director: "Christopher Nolan",
        year: 2014,
        genres: ["Adventure", "Drama", "Sci-Fi"]
      }
    ]);

    // Verify the inserted data
    const movies = await collection.find().toArray();
    console.log(movies);
  } finally {
    await client.close();
  }
}

run().catch(console.dir);