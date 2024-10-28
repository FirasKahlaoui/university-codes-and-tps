const { MongoClient } = require("mongodb");
const exec = require("child_process").exec;

const uri =
  "mongodb://FirasKahlaoui:EmmaLove@127.0.0.1:27017/cinema?authSource=admin";

const client = new MongoClient(uri, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

async function run() {
  try {
    await client.connect();
    exec(
      'mongorestore --username FirasKahlaoui --password EmmaLove --authenticationDatabase admin -d employee "C:\\Users\\Kahla\\OneDrive\\Documents\\TP Security\\university-codes-and-tps\\MongoDB\\TP2\\employes"',
      (error, stdout, stderr) => {
        if (error) {
          console.error(`exec error: ${error}`);
          return;
        }
        console.log(`stdout: ${stdout}`);
        console.error(`stderr: ${stderr}`);
      }
    );
  } catch (err) {
    console.error(err);
  } finally {
    await client.close();
  }
}

run().catch(console.dir);
