const express = require("express");
const router = express.Router();

const {
  getPoses,
  setPoses,
  updatePose,
  deletePose,
} = require("../controllers/PoseController");

router.route("/").get(getPoses).post(setPoses);
router.route("/:id").put(updatePose).delete(deletePose);

module.exports = router;

// Line 11 can be written as
// router.get("/", getPoses);
// router.post("/", setPoses);
// Line 12 can be written as
// router.put("/:id", updatePose);
// router.delete("/:id", deletePose);
