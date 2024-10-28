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
    const db = client.db("employee");
    const collection = db.collection("employes");

    // a. Afficher toutes les collections de la base
    const collections = await db.listCollections().toArray();
    console.log(
      "Collections:",
      collections.map((col) => col.name)
    );

    // b. Afficher tous les documents de la base
    const allDocuments = await collection.find().toArray();
    console.log("All Documents:", allDocuments);

    // c. Compter le nombre de documents de la collection employes
    const count = await collection.countDocuments();
    console.log("Number of Documents in employes:", count);

    // d. Insérer de deux manières différentes deux employés
    await collection.insertOne({ nom: "Dupont", prenom: "Jean", prime: 1000 });
    await collection.insertOne({
      nom: "Martin",
      prenom: "Paul",
      anciennete: 5,
    });

    // e. Afficher la liste des employés dont le prénom est David
    const employeesNamedDavid = await collection
      .find({ prenom: "David" })
      .toArray();
    console.log("Employees named David:", employeesNamedDavid);

    // f. Afficher la liste des employés dont le prénom commence ou se termine par D
    const employeesWithD = await collection
      .find({ prenom: { $regex: /^D|D$/ } })
      .toArray();
    console.log(
      "Employees with prenom starting or ending with D:",
      employeesWithD
    );

    // g. Afficher la liste des personnes dont le prénom commence par D et contient exactement 5 lettres
    const employeesWith5LetterD = await collection
      .find({ prenom: { $regex: /^D.{4}$/ } })
      .toArray();
    console.log(
      "Employees with prenom starting with D and 5 letters:",
      employeesWith5LetterD
    );

    // h. Afficher la liste des personnes dont le prénom commence et se termine par une voyelle
    const employeesWithVowel = await collection
      .find({ prenom: { $regex: /^[aeiouAEIOU].*[aeiouAEIOU]$/ } })
      .toArray();
    console.log(
      "Employees with prenom starting and ending with a vowel:",
      employeesWithVowel
    );

    // i. Afficher la liste des personnes dont le prénom commence et se termine par une même lettre
    const employeesWithSameLetter = await collection
      .find({ prenom: { $regex: /^(.).*\1$/ } })
      .toArray();
    console.log(
      "Employees with prenom starting and ending with the same letter:",
      employeesWithSameLetter
    );

    // j. Afficher le nom et prénom de chaque employé ayant une ancienneté > 10
    const seniorEmployees = await collection
      .find({ anciennete: { $gt: 10 } }, { projection: { nom: 1, prenom: 1 } })
      .toArray();
    console.log("Senior Employees (anciennete > 10):", seniorEmployees);

    // k. Afficher les nom et adresse complète des employés ayant un attribut rue dans l’objet adresse
    const employeesWithRue = await collection
      .find(
        { "adresse.rue": { $exists: true } },
        { projection: { nom: 1, adresse: 1 } }
      )
      .toArray();
    console.log("Employees with rue in adresse:", employeesWithRue);

    // l. Incrémenter de 200 la prime des employés ayant déjà le champ prime
    await collection.updateMany(
      { prime: { $exists: true } },
      { $inc: { prime: 200 } }
    );

    // m. Afficher les trois premières personnes ayant la plus grande valeur d’ancienneté
    const top3Seniority = await collection
      .find()
      .sort({ anciennete: -1 })
      .limit(3)
      .toArray();
    console.log("Top 3 employees by anciennete:", top3Seniority);

    // n. Regrouper les personnes dont la ville de résidence est Toulouse (afficher nom, prénom et ancienneté)
    const toulouseEmployees = await collection
      .find(
        { "adresse.ville": "Toulouse" },
        { projection: { nom: 1, prenom: 1, anciennete: 1 } }
      )
      .toArray();
    console.log("Employees in Toulouse:", toulouseEmployees);

    // o. Afficher les personnes dont le prénom commence par M et la ville de résidence est soit Foix soit Bordeaux
    const specificEmployees = await collection
      .find({
        prenom: { $regex: /^M/ },
        "adresse.ville": { $in: ["Foix", "Bordeaux"] },
      })
      .toArray();
    console.log(
      "Employees with prenom starting with M and living in Foix or Bordeaux:",
      specificEmployees
    );

    // p. Mettre à jour l’adresse de Dominique Mani
    await collection.updateOne(
      { nom: "Mani", prenom: "Dominique" },
      {
        $set: {
          adresse: { numero: 20, ville: "Marseille", codepostal: "13015" },
        },
      }
    );

    // q. Attribuer une prime de 1 500 à tous les employés n’ayant pas de prime et dont la ville de résidence est différente de Toulouse, Bordeaux et Paris
    await collection.updateMany(
      {
        prime: { $exists: false },
        "adresse.ville": { $nin: ["Toulouse", "Bordeaux", "Paris"] },
      },
      { $set: { prime: 1500 } }
    );

    // r. Remplacer le champ tel par un tableau téléphone
    await collection.updateMany({ tel: { $exists: true } }, [
      { $set: { telephone: ["$tel"] } },
      { $unset: "tel" },
    ]);

    // s. Créer un champ prime pour les documents qui n’en disposent pas et de l’affecter à 100 * nombre de caractère du nom de la ville
    await collection.updateMany({ prime: { $exists: false } }, [
      {
        $set: { prime: { $multiply: [{ $strLenCP: "$adresse.ville" }, 100] } },
      },
    ]);

    // t. Créer un champ mail
    await collection.updateMany({ telephone: { $exists: false } }, [
      {
        $set: { mail: { $concat: ["$nom", ".", "$prenom", "@formation.fr"] } },
      },
    ]);
    await collection.updateMany({ telephone: { $exists: true } }, [
      {
        $set: { mail: { $concat: ["$prenom", ".", "$nom", "@formation.fr"] } },
      },
    ]);

    // u. Calculer et afficher la somme de l’ancienneté pour les employés disposant du même prénom
    const sumAnciennete = await collection
      .aggregate([
        {
          $group: { _id: "$prenom", totalAnciennete: { $sum: "$anciennete" } },
        },
      ])
      .toArray();
    console.log("Sum of anciennete by prenom:", sumAnciennete);
  } catch (err) {
    console.error(err);
  } finally {
    await client.close();
  }
}

run().catch(console.dir);
