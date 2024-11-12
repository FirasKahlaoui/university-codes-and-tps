db.blog.find({ author: "Alain Arnaud" }, { title: 1, _id: 0 });

db.blog.find({ likes: { $gt: 10 } });

db.blog.updateOne({ _id: 1 }, { $set: { title: "tutorial MongoDB" } });

db.blog.updateOne({ _id: 1 }, { $addToSet: { tags: "CAP" } });

db.blog.updateOne({ _id: 1 }, { $pull: { tags: "NosqL" } });

db.blog.updateOne(
  { _id: 1, "comments.user": "user1" },
  { $inc: { "comments.$.like": 2 } }
);

db.blog.deleteMany({ title: /MongoDB/ });

db.blog.aggregate([
  { $group: { _id: "$author", count: { $sum: 1 } } },
  { $sort: { count: 1 } }
]);

db.blog.aggregate([
  { $unwind: "$comments" },
  { $group: { _id: "$comments.user", count: { $sum: 1 } } }
]);

db.blog.aggregate([
  { $group: { _id: "$category", documents: { $push: "$title" } } },
  { $out: "DocByCategory" }
]);
