const asyncHandler = require("express-async-handler");

// @desc get all Poses
// @route GET api/Poses
// @access Private
const getPoses = asyncHandler(async (req, res) => {
  res.send({
    message: "Get Poses",
  });
});

// @desc set goal
// @route POST api/Poses
// @access Private
const setPoses = asyncHandler(async (req, res) => {
  if (!req.body.text) {
    res.status(400);
    throw new Error("Please add a text field");
  }
  console.log(req.body);

  res.send({ message: "Set Goal" });
});
// @desc update goal with id
// @route PUT api/Poses/:id
// @access Private
const updateGoal = asynchHandler(async (req, res) => {
  res.send({
    message: `Update Goal for id=${req.params.id}`,
  });
});

// @desc delete goal with id
// @route PUT api/Poses/:id
// @access Private
const deleteGoal = asyncHandler(async (req, res) => {
  res.send({
    message: `Delete Goal for id=${req.params.id}`,
  });
});
module.exports = { getPoses, setPoses, updateGoal, deleteGoal };
